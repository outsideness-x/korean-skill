# Learner state and records

Persist evidence outside conversational memory. Without a dated record every session re-teaches from scratch, and nothing can ever close, because closure needs evidence spread across calendar days.

## Where the record lives

### With a file system (Claude Code, the desktop Code tab)

Keep the record in one fixed place, `~/korean-course/` in the user's home directory, whatever folder the session was opened in, so every session finds the same course. File tools need an absolute path: resolve `~` first (`echo $HOME`). Create the folder in session zero if it does not exist, and never start a second one.

If the learner asks for another location, use it and ask them to name it at the start of each session. If a session cannot read or write the folder (a declined permission prompt, a sandbox), say so and use the chat state block below for that session; never start a new course somewhere else.

```
~/korean-course/
  profile.md        learner profile and dated skill profile
  patterns.jsonl    one pattern per line, open or closed
  vocab.jsonl       one lexical record per line
  defects.jsonl     instrument defects, never learner errors
  sessions.md       append-only session summaries, newest last
  rounds/           one file per round: YYYY-MM-DD-NN.md
  exercises/        page specs with keys and built pages: YYYY-MM-DD-NN.json / .html
  snapshots/        raw writing and speech transcripts: YYYY-MM-DD-<genre>.md
```

JSON Lines lets one pattern or word be updated by its `id` or `lemma` without rewriting the rest. Take today's date from the system (`date +%F`), not from the conversation.

### Without a file system (plain chat)

Keep the same fields but hand them to the learner. End every session with one fenced block headed `KOREAN-TUTOR STATE`: the profile line, open patterns with `next_review`, words due in the next two weeks, and the last three session summaries, compact enough to paste. Ask the learner to paste it at the start of the next conversation, or to keep it as a project file where the environment has projects. If no state arrives, say what was lost and run a short re-placement instead of guessing from memory.

## Session procedure

**Start of a session:**

1. Read `profile.md` and the last two entries of `sessions.md`.
2. Collect every pattern and word whose `next_review` is today or earlier.
3. Open with those due items as unannounced cold checks on new surfaces. They are the evidence that closes things.
4. Continue with the next smallest target named in the last session summary.

If more than about eight items are due, check open patterns before words and words before closed maintenance items, most overdue first. Carry the rest to the next session without resetting them.

**After every round** (a session can be interrupted at any point):

1. Write the round file with item-level data.
2. Update every touched pattern and word: counts, `status`, `last_seen`, `step`, `next_review`.
3. Log instrument defects in `defects.jsonl`, never in the learner's counts.

**End of a session:** append the session summary to `sessions.md` and show the learner a short list of what changed in the record.

## Spacing ladder

Every pattern and word carries `step` and `next_review`. The intervals by step are:

| step | 0 | 1 | 2 | 3 | 4 | 5 |
|---|---:|---:|---:|---:|---:|---:|
| days to next review | 1 | 3 | 7 | 14 | 30 | 60 |

| Event at a check | New step | Next review |
|---|---|---|
| introduced, or missed | 0 | today + 1 day |
| fresh success without a hint | step + 1 | today + interval of the new step |
| success only after a hint | unchanged | today + interval of the current step |
| instrument defect | unchanged | unchanged; the check did not happen |

Successes in the session where the item was taught do not move the step, and the step moves at most once per calendar day. A pattern introduced on day 0 and never missed again is checked on days 1, 4, and 11; the day-11 success satisfies the timing part of the closure base rule in `SKILL.md` at every level. After closure the ladder continues as maintenance (14, 30, 60 days); a miss sets the status to `reopened` and the step to 0.

## Learner profile (`profile.md`)

```
learner_id_or_alias
first_language
preferred_explanation_language
goals[]
target_date: optional
tracks[]: general | reading | conversation | heritage | academic | professional | topik
current_band: H0 | K1 | K2 | K3 | K4 | K5 | K6 | K6+
placement_date
placement_evidence[]
constraints: audio, keyboard, time, accessibility
exercise_page: URL of the published exercise page, if any (interactive.md)
```

Keep an alias in shareable reports. Real messages, recordings, and exam scores are private by default.

## Skill profile (`profile.md`)

Never store only one level. Maintain separate, dated estimates for:

- Hangul decoding and spelling;
- sound perception;
- pronunciation/intelligibility;
- listening comprehension;
- interaction/speaking;
- grammar/morphology;
- vocabulary recognition and recall;
- reading;
- writing;
- register/pragmatics;
- TOPIK section performance when relevant.

Every estimate carries the evidence slice: task type, length/items, support, timing, and whether the material was fresh. Mark a skill `not measured` rather than inferring it from another skill; pronunciation stays `not measured` when no one has listened to the learner.

## Pattern record (`patterns.jsonl`)

One line per smallest actionable pattern (shown expanded here):

```json
{
  "id": "particles.topic-vs-focus.new-subject",
  "layer": "particle_discourse",
  "status": "acquired_not_transferred",
  "correct": 4,
  "wrong": 3,
  "clean_false_positive": 1,
  "step": 1,
  "last_miss": "2026-09-23",
  "last_seen": "2026-09-24",
  "next_review": "2026-09-27",
  "evidence": ["2026-09-23-01:item-3", "snapshots/2026-09-24-message.md:s2"],
  "hypothesis": "uses one-to-one L1 translation instead of discourse context",
  "counter_evidence": [],
  "next_check": "newly introduced subject vs established contrast topic"
}
```

Do not merge `batchim omission in dictation` with `batchim release in speaking`; they require different treatment. Do not split so finely that the row has only one unexplained miss.

## Correction record (inside round files)

Every correction is stored with the same fields the learner sees (the format in `SKILL.md`), plus the context needed to revisit the diagnosis:

```
learner, repair, verdict, why, boundary, fresh
context: speaker / listener / subject / setting / purpose
segmentation: only when it explains the error, e.g. 먹-었-어요
pattern_id
```

If the learner's form is possible in a different context, the `boundary` field names that context.

## Vocabulary record (`vocab.jsonl`)

Track recognition, recall, and use separately (shown expanded):

```json
{
  "lemma": "영향",
  "sense": "influence/effect",
  "frame": "N에 영향을 미치다 / N의 영향을 받다",
  "collocations": ["큰 영향", "긍정적인 영향"],
  "register": "neutral-written",
  "family": ["영향력"],
  "recognition": "learning",
  "recall": "open",
  "use": "open",
  "step": 0,
  "last_seen": "2026-09-23",
  "next_review": "2026-09-24",
  "sources": ["reading-007:p2"]
}
```

Seeing a word in the answer key updates exposure, not recall.

## Round record (`rounds/`)

Store item-level data:

```
round_id, date, level_slice, mode, targets, fresh_or_repeated
item_id, prompt/source, learner_answer, accepted_answers, verdict
learner_reason, hint_level, pattern_ids, instrument_defect
```

Store audio/text provenance and enough context to revisit a diagnosis. Preserve the learner's wording; aggregated totals cannot reconstruct a mechanism later. For a round delivered as a page, paste the learner's `KT-RESULT` block into the round file verbatim, next to the spec id, before interpreting it.

## Production snapshot (`snapshots/`)

For speech or writing:

```
snapshot_id, date, prompt, genre, audience, time/support conditions
raw_text_or_transcript
word_or_eojeol_count
annotations[]
keep[]
open_patterns[]
new_patterns[]
```

If automatic transcription, a translator, keyboard prediction, or grammar correction sits in the path, record it. Corrected transcripts are not raw pronunciation or grammar evidence.

## Module status

Use:

- `unseen`;
- `introduced`;
- `acquired_not_transferred`;
- `transferred_once`;
- `closed`;
- `reopened`.

Attach the closure rule and a calendar review date. Drill scores may move a pattern to `acquired_not_transferred`; only fresh production or comprehension can close it.

## Instrument defects (`defects.jsonl`)

Keep tutor/test defects beside learner evidence but never count them as learner errors:

```
item_id, date, defect_type, description, resolution, affected_scores
```

Useful defect types include insufficient context, multiple defensible answers, unnatural Korean, audio artifact, normalization bug, wrong key, and outdated exam fact.

## Session summary (`sessions.md`)

End each completed session with:

- date;
- what was sampled;
- what is now verified;
- what remains a hypothesis;
- one to three keep items;
- the next smallest target;
- the earliest `next_review` date in the record;
- homework only if the learner wants it.

Use dates, not "round 3" alone. Spacing is measured in calendar time.
