# Interactive exercises and flashcards

When the environment can show an HTML page, deliver item sets as a page built from `assets/exercise.html` by `scripts/build_exercise.py`. The page delivers items, records answers, time per item, hints, and audio replays, and hands back a result block. It does not diagnose: the mechanism, the verdict on unlisted answers, and the state update stay with the tutor.

## When to use a page

Use a page for:

- listening and dictation: the page speaks Korean through the browser's speech synthesis;
- H0, and any learner without Korean input set up: the page has an on-screen keyboard in the standard two-set layout (두벌식) and shows each typed block in 원고지-style cells, so block structure and spacing are visible;
- sets of 5-12 closed items (choice, gap, find-and-fix, word order);
- timed probes (`time_limit_min`).

Stay in plain text for one to three items, the writing loop, open discussion, items that are mostly reasoning, or when the learner prefers chat.

## Two modes

| Mode | Lesson-loop step | On the page |
|---|---|---|
| `probe` | cold sample, fresh transfer, due delayed checks | no checking, no hints, no keys: the builder strips `answer`, `accept`, `clean`, `why`, `hints`, and `card` before writing the page |
| `drill` | controlled retrieval | a Check button per item, then verdict, answer, explanation, and flashcard; opened hints are logged |

Due checks and transfer tasks always use `probe`: feedback during them would destroy the evidence they exist to collect.

## Workflow

1. **Write the spec with keys** (format below). With a file system, save it as `~/korean-course/exercises/<id>.json`, where `<id>` is `YYYY-MM-DD-NN` and matches the round file.
2. **Build the page.** `<skill-dir>` is this skill's folder:

   ```
   python3 <skill-dir>/scripts/build_exercise.py ~/korean-course/exercises/<id>.json ~/korean-course/exercises/<id>.html
   ```

   Add `--fragment` when the page will be published as an artifact. Fix every error and read every warning.
3. **Show the page** with what the environment offers:
   - **Artifact tool** (Claude Code, desktop Code tab): build with `--fragment` to one stable path, `~/korean-course/exercises/page.html`, and publish it. Record the URL in `profile.md` as `exercise_page` and republish each new round to that same URL, so the learner keeps one link. Republishing reloads an open page, so publish the next round only after the previous result has arrived.
   - **Files but no Artifact tool:** open the standalone page in the learner's browser (`open` on macOS, `xdg-open` on Linux, `start` on Windows).
   - **Chat with artifacts:** create an HTML artifact from the `--fragment` output. The template is about 50 KB, so in chat prefer text for short sets.
4. **Stop and wait.** The learner finishes, presses Copy, and pastes the `KT-RESULT` block into the chat.
5. **Grade and log** as described under **The result block**.

## Spec

```json
{
  "id": "2026-09-29-01",
  "mode": "drill",
  "lang": "ru",
  "title": "에 и 에서: где и куда",
  "intro": "optional one-paragraph introduction",
  "time_limit_min": 10,
  "items": [ ... ]
}
```

`lang` sets the interface language (`ru` or `en`). `time_limit_min` is optional; at zero the page finishes itself. `assets/example-drill.json` is a complete drill using all six item types.

| Field | Item types | Meaning |
|---|---|---|
| `id` | all | unique; the result block reports it |
| `type` | all | `choice`, `text`, `fix`, `order`, `listen`, `dictation` |
| `context` | all | the situation: speaker, listener, setting, medium |
| `prompt` | all | the instruction |
| `ko` | choice, text, fix | the Korean exhibit; `___` marks one gap; for `fix`, the sentence to judge |
| `options`, `answer` | choice, listen | Korean options; `answer` is the 0-based index of the right one |
| `accept` | text, dictation, fix, order | every defensible answer; for `order`, a list of chunk lists |
| `clean` | fix | `true` when the sentence has no error |
| `chunks` | order | the pieces to arrange; the page shuffles them |
| `say` or `audio` | listen, dictation | text for speech synthesis, or a recording as a URL or data URI |
| `spacing` | text, dictation, fix | `ignore` (default) or `strict` when 띄어쓰기 is the target |
| `shuffle` | choice, listen | `false` keeps the option order, for example on a scale |
| `reason` | all | adds a "why?" field; the learner's text appears in the result |
| `hints` | all, drill | L1 and L2 of the hint ladder; each opened hint is logged |
| `why` | all, drill | trigger and boundary, shown after checking |
| `card` | all, drill | `{"front": ..., "back": ...}` for the flashcard export |

In the metalanguage fields (`context`, `prompt`, `why`, `hints`, `card`), wrap Korean in backticks so it renders and copies as Korean: "`있다` — просто находиться где-то".

## Authoring rules

Everything in `formats.md` applies, context sufficiency and clean items included. In addition:

- **Make `accept` generous.** The page normalizes to NFC, collapses whitespace, strips final punctuation, and ignores spaces unless `spacing` is `strict`. It does nothing else. A correct answer missing from `accept` is an instrument defect: rescore it, log it, and extend the spec.
- **Clean `fix` items** have "no error" as their right answer. Never tell the learner how many there are.
- **Options must not leak the answer** by length, form, or position; the page shuffles by a seed, so position is stable across reloads and carries no information.
- **The `say` text is in the page source** in both modes. That is acceptable: reading the source is a deliberate act.
- **Synthetic audio is one voice** (on macOS the best Korean voice is Yuna). It is good enough for drills and probes. A perception pattern closes only after a second voice or a real recording, as `pronunciation-listening.md` requires. The result header records the voice.
- **No Korean voice in the browser:** the learner presses the "no audio" button, the item comes back as `NOAUDIO` / `noaudio`, and it is an instrument defect, never a miss.

## The result block

```
KT-RESULT id=2026-09-29-01 mode=drill items=8 time=4m12s voice=Yuna keyboard=onscreen
1 | choice | 에서 | miss | 38s
3 | text | 에 | ok | hint=1 | 12s | why: цель движения
4 | fix | CLEAN | ok | 6s
7 | listen | 학교에서 와요. | ok | plays=2 | 9s
```

Each line: item id, type, the learner's answer (`—` unanswered, `CLEAN` for "no error", `NOAUDIO`), in drill mode the page's verdict (`ok`, `miss`, `unchecked`, `noaudio`), then `hint=N`, `plays=N`, seconds spent on the item, and the learner's reason after `why:`.

- **Probe:** grade every line yourself against the stored spec.
- **Drill:** `ok` and `miss` are string matches against `accept`, not a diagnosis. Re-read every miss and every free-text answer; a correct answer outside `accept` is rescored and logged as a defect. Then diagnose by mechanism as `SKILL.md` describes.
- `hint=N` is the `hint_level` of the round record. Seconds and replays are evidence: retrieval latency matters at K1-K2, and replay count shows what listening needed.
- Write the round file under the spec's id and update patterns and words as `state.md` describes.

## Flashcards

Every piece of material on the page has a copy button: the situation, the instruction, the Korean sentence, the options, the chunks, the hints, the answer, the explanation, and the audio transcript once the item is answered. In drill mode each checked item also offers "copy flashcard", and the result screen exports all cards as TSV: front, a tab, back, one card per line. Anki (File → Import, separator Tab) and Quizlet (Import, Tab between term and definition) accept it.

The default card is the Korean item on the front and the full correct sentence plus the explanation on the back. Add `card` with a translation when that default would make a poor card. A probe page has no keys, so it exports no cards: after grading a probe, offer the learner the same TSV, built from the stored spec.

## Maintaining the template

Each behaviour below fixes an observed failure; keep them when editing `assets/exercise.html`:

- the items stay hidden until Start; Finish and Start over use two-click arming, because the viewer blocks `confirm()`;
- answers are saved in `localStorage` under the exercise id, every access in `try/catch`, and the page works without storage;
- Enter pressed while the Korean IME is composing (`isComposing`, keyCode 229) is ignored;
- answers are compared after NFC normalization;
- copying falls back from the Clipboard API to `execCommand`, then to selecting the text;
- form controls declare their own colours; no external scripts; fonts come from Google Fonts with system fallbacks;
- voices load asynchronously, so nothing re-renders before the page is fully wired.

After an edit, build `assets/example-drill.json` in both modes and click through it once before using the template with a learner.
