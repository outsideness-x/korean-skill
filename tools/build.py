#!/usr/bin/env python3
"""Validate the korean-tutor skill source and pack it into korean-tutor.skill.

Usage (from the repository root):  python3 tools/build.py
"""
import json
import re
import shutil
import subprocess
import sys
import tempfile
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SKILL = ROOT / "korean-tutor"
OUT = ROOT / "korean-tutor.skill"
# Files of the learner's course folder (state.md), not of the package.
RECORD_FILES = {"profile.md", "sessions.md"}


def validate() -> list[str]:
    errors = []
    text = (SKILL / "SKILL.md").read_text(encoding="utf-8")
    m = re.match(r"^---\n(.*?)\n---\n", text, re.S)
    if not m:
        return ["SKILL.md: missing YAML frontmatter"]
    fields = dict(re.findall(r"^(\w+): (.*)$", m.group(1), re.M))
    name, desc = fields.get("name", ""), fields.get("description", "")
    if name != SKILL.name:
        errors.append(f"frontmatter name {name!r} != folder name {SKILL.name!r}")
    if not re.fullmatch(r"[a-z0-9-]{1,64}", name):
        errors.append(f"name {name!r} must be lowercase letters, digits and hyphens")
    if not desc or len(desc) > 1024:
        errors.append(f"description must be 1-1024 chars, has {len(desc)}")
    if "<" in desc or ">" in desc:
        errors.append("description must not contain angle brackets")

    # Every `file.md` / `dir/file.md` mentioned in any page must exist in the package.
    for page in sorted(SKILL.rglob("*.md")):
        for ref in set(re.findall(r"`([\w./-]+\.md)`", page.read_text(encoding="utf-8"))):
            if ref not in RECORD_FILES and not (SKILL / ref).is_file():
                errors.append(f"{page.relative_to(SKILL)}: broken reference `{ref}`")
    return errors


def smoke() -> list[str]:
    """Build the example spec as a drill and as a probe; the probe page must carry no keys."""
    errors = []
    script, example = SKILL / "scripts" / "build_exercise.py", SKILL / "assets" / "example-drill.json"
    with tempfile.TemporaryDirectory() as tmp:
        spec = json.loads(example.read_text(encoding="utf-8"))
        spec["mode"] = "probe"
        probe = Path(tmp, "probe.json")
        probe.write_text(json.dumps(spec, ensure_ascii=False), encoding="utf-8")
        for src, out in ((example, "drill.html"), (probe, "probe.html")):
            r = subprocess.run([sys.executable, str(script), str(src), str(Path(tmp, out))],
                               capture_output=True, text=True)
            if r.returncode:
                return [f"example {out} does not build: {r.stderr.strip()}"]
        page = Path(tmp, "probe.html").read_text(encoding="utf-8")
        data = re.search(r'id="kt-data">(.*?)</script>', page, re.S).group(1)
        leaked = {k for q in json.loads(data)["items"] for k in q} & {"answer", "accept", "clean", "why", "hints", "card"}
        if leaked:
            errors.append(f"probe page leaks key fields: {sorted(leaked)}")
        if shutil.which("node"):
            js = re.search(r"<script>\n(.*?)</script>", page, re.S).group(1)
            Path(tmp, "page.js").write_text(js, encoding="utf-8")
            r = subprocess.run(["node", "--check", str(Path(tmp, "page.js"))], capture_output=True, text=True)
            if r.returncode:
                errors.append(f"page script does not parse: {r.stderr.strip()}")
    return errors


def pack() -> int:
    entries = sorted([SKILL, *SKILL.rglob("*")])
    files = [p for p in entries if p.is_file() and p.name != ".DS_Store"]
    with zipfile.ZipFile(OUT, "w", zipfile.ZIP_DEFLATED) as z:
        for p in entries:
            if p.is_dir():  # explicit folder entries, as importers expect korean-tutor/ on top
                z.write(p, p.relative_to(ROOT).as_posix() + "/")
            elif p in files:
                z.write(p, p.relative_to(ROOT).as_posix())
    return len(files)


if __name__ == "__main__":
    errors = validate() or smoke()
    if errors:
        print("\n".join(f"error: {e}" for e in errors), file=sys.stderr)
        sys.exit(1)
    print(f"ok: packed {pack()} files into {OUT.name}")
