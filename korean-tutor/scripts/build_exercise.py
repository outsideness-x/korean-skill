#!/usr/bin/env python3
"""Build an interactive Korean exercise page from a JSON spec.

Usage:
  python3 build_exercise.py SPEC.json OUT.html              # standalone page to open in a browser
  python3 build_exercise.py SPEC.json OUT.html --fragment   # page body for an Artifact / chat artifact

The spec format is described in interactive.md. In probe mode every key field
(answer, accept, clean, why, hints, card) is stripped before the page is written,
so the key never reaches the learner; keep the full spec in the course folder.
"""
import json
import re
import sys
import unicodedata
from collections import Counter
from pathlib import Path

TEMPLATE = Path(__file__).resolve().parent.parent / "assets" / "exercise.html"
PLACEHOLDER = "/*KT-DATA*/"
TYPES = {"choice", "text", "fix", "order", "listen", "dictation"}
KEY_FIELDS = ("answer", "accept", "clean", "why", "hints", "card")
ITEM_FIELDS = {"id", "type", "context", "prompt", "ko", "options", "chunks", "say", "audio",
               "shuffle", "spacing", "reason", *KEY_FIELDS}
TOP_FIELDS = {"id", "mode", "lang", "title", "intro", "time_limit_min", "page_title", "items"}
TITLES = {"ru": "Корейский тренажёр", "en": "Korean practice"}


def nfc(value):
    if isinstance(value, str):
        return unicodedata.normalize("NFC", value)
    if isinstance(value, list):
        return [nfc(v) for v in value]
    if isinstance(value, dict):
        return {k: nfc(v) for k, v in value.items()}
    return value


def is_str_list(value, min_len=1):
    return isinstance(value, list) and len(value) >= min_len and all(isinstance(v, str) and v.strip() for v in value)


def check_item(q, n, drill, errors, warnings):
    where = f"item {n} ({q.get('id')})"
    t = q.get("type")
    if t not in TYPES:
        errors.append(f"{where}: type must be one of {sorted(TYPES)}")
        return
    for k in set(q) - ITEM_FIELDS:
        warnings.append(f"{where}: unknown field '{k}' is ignored by the page")
    if q.get("spacing", "ignore") not in ("ignore", "strict"):
        errors.append(f"{where}: spacing must be 'ignore' or 'strict'")
    if "hints" in q and not is_str_list(q["hints"]):
        errors.append(f"{where}: hints must be a non-empty list of strings")
    if "card" in q and not (isinstance(q["card"], dict) and set(q["card"]) <= {"front", "back"}):
        errors.append(f"{where}: card must be an object with 'front' and/or 'back'")

    if t in ("choice", "listen"):
        opts = q.get("options")
        if not is_str_list(opts, 2):
            errors.append(f"{where}: options must list at least two strings")
        elif len(set(opts)) != len(opts):
            errors.append(f"{where}: options repeat")
        elif drill and not (isinstance(q.get("answer"), int) and 0 <= q["answer"] < len(opts)):
            errors.append(f"{where}: answer must be the 0-based index of the right option")
    if t in ("listen", "dictation") and not (q.get("say") or q.get("audio")):
        errors.append(f"{where}: needs 'say' (text for speech synthesis) or 'audio' (URL or data URI)")
    if t in ("text", "choice") and not (q.get("ko") or q.get("prompt")):
        errors.append(f"{where}: needs 'ko' or 'prompt'")
    if t in ("text", "choice") and q.get("ko", "").count("___") > 1:
        warnings.append(f"{where}: more than one ___ gap; the flashcard fills only the first")
    if t == "fix" and not q.get("ko"):
        errors.append(f"{where}: fix needs 'ko', the sentence to judge")
    if t == "order":
        chunks = q.get("chunks")
        if not is_str_list(chunks, 2):
            errors.append(f"{where}: chunks must list at least two strings")
        elif drill:
            accept = q.get("accept")
            if not isinstance(accept, list) or not accept:
                errors.append(f"{where}: accept must list at least one correct order")
            else:
                for seq in accept:
                    parts = seq if isinstance(seq, list) else str(seq).split(" ")
                    if Counter(parts) != Counter(chunks):
                        errors.append(f"{where}: accepted order {parts} does not use exactly the chunks")
    if drill and t in ("text", "dictation") and not is_str_list(q.get("accept")):
        errors.append(f"{where}: accept must list at least one correct answer")
    if drill and t == "fix":
        if q.get("clean") is True:
            if q.get("accept"):
                warnings.append(f"{where}: clean item carries 'accept'; it is ignored")
        elif not is_str_list(q.get("accept")):
            errors.append(f"{where}: an error item needs 'accept' with the corrected sentence(s), or clean: true")
        elif any(unicodedata.normalize("NFC", a) == q["ko"] for a in q["accept"]):
            errors.append(f"{where}: 'accept' repeats the original sentence; mark it clean: true instead")
    if drill and not q.get("why"):
        warnings.append(f"{where}: no 'why'; the learner gets a verdict without the trigger")


def build(spec):
    errors, warnings = [], []
    for k in set(spec) - TOP_FIELDS:
        warnings.append(f"unknown top-level field '{k}' is ignored")
    if not re.fullmatch(r"[\w.-]{1,64}", str(spec.get("id", ""))):
        errors.append("id must be 1-64 letters, digits, '.', '_' or '-' (use YYYY-MM-DD-NN)")
    mode = spec.get("mode")
    if mode not in ("probe", "drill"):
        errors.append("mode must be 'probe' or 'drill'")
    if spec.get("lang", "ru") not in TITLES:
        errors.append(f"lang must be one of {sorted(TITLES)}")
    items = spec.get("items")
    if not isinstance(items, list) or not items:
        errors.append("items must be a non-empty list")
        return None, errors, warnings, {}
    ids = [str(q.get("id", i + 1)) for i, q in enumerate(items)]
    for dup in {i for i in ids if ids.count(i) > 1}:
        errors.append(f"item id '{dup}' is used twice")
    for i, q in enumerate(items):
        q["id"] = ids[i]
        check_item(q, i + 1, mode == "drill", errors, warnings)

    clean = sum(1 for q in items if q.get("clean") is True)
    stripped = 0
    if mode == "probe":
        for q in items:
            if any(k in q for k in KEY_FIELDS):
                stripped += 1
            for k in KEY_FIELDS:
                q.pop(k, None)
    stats = {
        "types": Counter(q["type"] for q in items),
        "clean": clean,
        "audio": sum(1 for q in items if q["type"] in ("listen", "dictation")),
        "stripped": stripped,
    }
    return spec, errors, warnings, stats


def render(spec, fragment):
    page = TEMPLATE.read_text(encoding="utf-8")
    if page.count(PLACEHOLDER) != 1:
        sys.exit(f"error: template must contain {PLACEHOLDER} exactly once")
    data = json.dumps(spec, ensure_ascii=False).replace("</", "<\\/")
    page = page.replace(PLACEHOLDER, data)
    lang = spec.get("lang", "ru")
    title = spec.get("page_title") or TITLES[lang]
    page = re.sub(r"<title>.*?</title>", lambda m: f"<title>{title}</title>", page, count=1)
    if fragment:
        return page
    head, body = page.split("\n", 1)  # the template's first line is its <title>
    return (f'<!doctype html>\n<html lang="{lang}">\n<head>\n<meta charset="utf-8">\n'
            f'<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">\n'
            f"{head}\n</head>\n<body>\n{body}</body>\n</html>\n")


def main(argv):
    args = [a for a in argv if not a.startswith("--")]
    if len(args) != 2:
        sys.exit(__doc__)
    spec_path, out_path = Path(args[0]), Path(args[1])
    spec = nfc(json.loads(spec_path.read_text(encoding="utf-8")))
    spec, errors, warnings, stats = build(spec)
    for w in warnings:
        print(f"warning: {w}", file=sys.stderr)
    if errors:
        print("\n".join(f"error: {e}" for e in errors), file=sys.stderr)
        sys.exit(1)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(render(spec, "--fragment" in argv), encoding="utf-8")
    types = ", ".join(f"{t} {n}" for t, n in sorted(stats["types"].items()))
    extra = f"; keys stripped from {stats['stripped']} items" if stats["stripped"] else ""
    print(f"ok: {spec['mode']}, {len(spec['items'])} items ({types}); clean {stats['clean']}, "
          f"audio {stats['audio']}{extra} -> {out_path}")


if __name__ == "__main__":
    main(sys.argv[1:])
