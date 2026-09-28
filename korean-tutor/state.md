# Learner state and records

Persist evidence outside conversational memory. Use the storage format that fits the environment; the required information matters more than JSON versus Markdown.

## Learner profile

Record:

```
learner_id_or_alias
preferred_explanation_language
goals[]
target_date: optional
tracks[]: general | reading | conversation | heritage | academic | professional | topik
current_band: H0 | K1 | K2 | K3 | K4 | K5 | K6 | K6+
placement_date
placement_evidence[]
constraints: audio, keyboard, time, accessibility
```

Keep an alias in shareable reports. Real messages, recordings, and exam scores are private by default.

## Skill profile

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

Every estimate carries the evidence slice: task type, length/items, support, timing, and whether the material was fresh.

## Pattern record

Use one row per smallest actionable pattern:

```json
{
  "id": "particles.topic-vs-focus.new-subject",
  "layer": "particle_discourse",
  "status": "open",
  "correct": 4,
  "wrong": 3,
  "clean_false_positive": 1,
  "last_seen": "2026-09-23",
  "evidence": ["round-004:item-3", "writing-002:s2"],
  "hypothesis": "uses one-to-one L1 translation instead of discourse context",
  "counter_evidence": [],
  "next_check": "newly introduced subject vs established contrast topic",
  "next_review": "2026-09-27"
}
```

Do not merge `batchim omission in dictation` with `batchim release in speaking`; they require different treatment. Do not split so finely that the row has only one unexplained miss.

## Vocabulary record

Track dimensions separately:

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
  "last_seen": "2026-09-23",
  "next_review": "2026-09-26",
  "sources": ["reading-007:p2"]
}
```

Seeing a word in the answer key updates exposure, not recall.

## Round record

Store item-level data:

```
round_id, date, level_slice, mode, targets, fresh_or_repeated
item_id, prompt/source, learner_answer, accepted_answers, verdict
learner_reason, hint_level, pattern_ids, instrument_defect
```

Store audio/text provenance and enough context to revisit a diagnosis. Preserve the learner's wording; aggregated totals cannot reconstruct a mechanism later.

## Production snapshot

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

If automatic transcription or grammar correction sits in the path, record it. Corrected transcripts are not raw pronunciation or grammar evidence.

## Module status

Use:

- `unseen`;
- `introduced`;
- `acquired_not_transferred`;
- `transferred_once`;
- `closed`;
- `reopened`.

Attach the closure rule and a calendar review date. Drill scores may move a pattern to `acquired_not_transferred`; only fresh production or comprehension can close it.

## Instrument defects

Keep tutor/test defects beside learner evidence but never count them as learner errors:

```
item_id, date, defect_type, description, resolution, affected_scores
```

Useful defect types include insufficient context, multiple defensible answers, unnatural Korean, audio artifact, normalization bug, wrong key, and outdated exam fact.

## Session summary

End each completed session with:

- what was sampled;
- what is now verified;
- what remains a hypothesis;
- one to three keep items;
- the next smallest target;
- delayed review date;
- homework only if the learner wants it.

Use dates, not "round 3" alone. Spacing is measured in calendar time.
