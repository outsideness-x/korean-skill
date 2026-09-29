---
name: korean-tutor
description: Teach Korean from absolute beginner Hangul through advanced vocabulary, reading, writing, listening, and register control with a measurement-driven tutoring loop. Route learners through a pre-level Hangul stage and Korean Standard Curriculum levels 1-6, add TOPIK preparation only when requested, diagnose Korean-specific sub-patterns such as batchim, sound changes, particles, endings, honorifics, collocations, and discourse, and close skills only on fresh transfer. Use when asked to learn, practise, assess, or plan Korean; build Korean lessons or drills; analyse Korean errors; improve Korean writing or reading; or prepare for TOPIK. Also use for Russian-language requests such as "учить корейский", "хангыль", "корейская грамматика", "подготовка к TOPIK/ТОПИК".
---

# Korean tutor

Teach Korean by evidence, not by marching through a generic chapter list:

**sample current performance -> diagnose the smallest useful pattern -> teach and drill that pattern -> re-measure it in fresh Korean.**

The learner's explicit goal, preferred explanation language, pace, and constraints override this skill. Do not force exam preparation, a fixed textbook, or a native-like accent when the learner wants something else.

## The course spine

Korean has a real prerequisite chain. A total beginner needs a short structured path before a corpus-driven syllabus can emerge:

1. decode and assemble Hangul blocks;
2. connect spelling to the sounds Korean actually produces;
3. build high-frequency clauses with particles and endings;
4. control tense, negation, connection, honorifics, and speech level;
5. expand vocabulary as usable lexical frames, not isolated translations;
6. read progressively less controlled texts;
7. at advanced levels, shift from grammaticality to register, collocation, inference, and discourse.

Within each stage, use the measurement loop. Do not teach everything listed for the level; teach the next dependency or the pattern the learner's evidence shows is binding.

## Session zero

Before the first lesson, establish five things. A returning learner skips session zero: see **Returning learner** below.

### 1. Goal and use case

Ask only what changes the course: why Korean, target date if any, desired skills, access to audio, first language, and preferred explanation language. If either the first language or the explanation language is Russian, read `l1-russian.md` before the first lesson. Common tracks are general communication, reading-first, heritage learner, life in Korea, academic Korean, professional Korean, media/literature, and TOPIK.

### 2. Placement by can-do evidence

Do not place from self-report, app streak, vocabulary count, or conversational confidence alone. Use the shortest gate that can disprove the claimed level:

- **H0:** identify and combine letters; read unseen syllable blocks and simple words without any transliteration (Latin romanization or Cyrillic).
- **K1-K2:** understand and produce short everyday exchanges; read a notice or message; write connected sentences.
- **K3-K4:** handle a familiar social topic, distinguish spoken and written style, read an explanatory or short opinion text, and produce a paragraph.
- **K5-K6+:** read an unfamiliar abstract passage, infer stance and logical relations, summarize it, and respond in an appropriate formal register.

Test listening separately from reading. A learner may decode Hangul well and still fail to map connected speech to the written forms they know.

### 3. Level and mode

Use the Korean labels below. Read the matching level file before designing the course.

| Internal stage | Korean framework | Practical label | Read |
|---|---|---|---|
| H0 | pre-level 1 | Hangul foundation | `levels/h0-hangul.md` |
| K1-K2 | levels 1-2 | beginner | `levels/k1-k2.md` |
| K3-K4 | levels 3-4 | intermediate | `levels/k3-k4.md` |
| K5-K6+ | levels 5-6 and open-ended 6+ | advanced | `levels/k5-k6-plus.md` |

The six Korean levels align with the National Institute of Korean Language (NIKL) Standard Curriculum and King Sejong Institute's Beginner 1, Beginner 2, Intermediate 1, Intermediate 2, Advanced 1, and Advanced 2 bands. TOPIK score levels are useful external checkpoints, not complete learner profiles. TOPIK I measures listening and reading; TOPIK II adds writing; TOPIK Speaking is separate. Never infer untested speaking ability from a TOPIK I or II score.

CEFR labels are optional orientation only: H0 is pre-A1; K1 is roughly A1-like; K2 A2-like; K3 B1-like; K4 B2-like; K5 C1-like; K6 upper-advanced. Do not present these as official conversions, and never claim TOPIK 6 or Korean level 6 automatically equals CEFR C2. Read `sources.md` before publishing a level crosswalk or current exam cut-off.

### 4. Real production (K2 and above)

Ask for Korean the learner has actually produced: chat messages (KakaoTalk, language-exchange apps), emails, comments, a diary, homework. It carries their real error distribution; invented sentences carry only a guess at it. Segment chat from composed text before counting, since accuracy often differs sharply between them. Ask whether a translator (Papago, Google Translate), keyboard prediction, or a native friend touched the text, and exclude assisted text from evidence. Real messages are private by default. If nothing exists, elicit a short text on the learner's own life or work instead of a textbook topic.

### 5. State

Create the learner record in the layout described in `state.md`. Record skill profiles separately: script, listening, pronunciation, interaction, reading, writing, grammar/morphology, vocabulary, and register. One headline level must never hide a large split.

### Returning learner

Every later session starts from the record, not from memory: read the profile, the tail of the session log, and every pattern or word whose `next_review` date has arrived (`state.md` has the exact procedure). Open with those due checks as unannounced cold items, then continue with the planned target. Never re-teach something the record marks closed unless fresh evidence reopens it.

## The lesson loop

One learning cycle has six parts:

1. **Cold sample.** A short task that can reveal the target without coaching. At H0, show a minimal model before testing a symbol the learner has never seen; productive failure is useful, uninformed guessing is not.
2. **Diagnosis.** Name the smallest operation that failed and its trigger.
3. **Micro-lesson.** Explain one mechanism, show the boundary, and anchor it to the learner's first language only when the contrast genuinely helps.
4. **Controlled retrieval.** Isolate the variable with minimal pairs, substitution, dictation, classification, or short production.
5. **Fresh transfer.** Change the vocabulary, speaker, sentence shape, or text. The learner must notice and use the pattern without it being announced.
6. **State update.** Log item-level evidence, set the next review date from the spacing ladder in `state.md`, and record whether the miss belongs to the learner or to a defective prompt/key.

For an interactive lesson, deliver the probe or exercise and stop for the learner's answer. Do not reveal the key, mark hypothetical answers, or continue through the feedback in the same turn. When the environment can show an HTML page, deliver item sets as a page with a built-in Korean keyboard, audio, and flashcard export (`interactive.md`); the stop-and-wait rule still holds, and the learner returns a result block.

## Diagnose Korean at the right layer

Tag every miss by both **surface** and **mechanism**. `은/는` versus `이/가` is a surface contrast; possible mechanisms include discourse topic, new-information focus, embedded-clause subject, or memorized translation. Use the layer that changes the treatment:

| Layer | Typical evidence | Treatment |
|---|---|---|
| script | confuses ㅓ/ㅗ, drops a final consonant, assembles the block in the wrong order | block construction and visual discrimination |
| sound perception | knows 같이 on paper but does not recognize [가치] | audio contrast and sound-to-spelling mapping |
| sound production | reads every letter separately or releases final stops | articulatory cue, shadowing, then a new word |
| morphology | wrong allomorph or ending after a stem | segment the form and drill the trigger |
| syntax | modifier, complement, or clause boundary is misparsed | bracket chunks and rebuild the sentence |
| particle/discourse | grammatically possible particle produces the wrong focus | compare the discourse context, not translations |
| register/pragmatics | correct proposition, inappropriate ending or honorific | identify speaker, listener, setting, and speech act |
| lexicon/collocation | translation is plausible but Koreans choose another combination | teach the lexical frame and near-neighbour boundary |
| reading/discourse | knows the words but misses contrast, cause, stance, or referent | mark relations and require evidence from the text |

Separate **orthographic form**, **citation pronunciation**, and **connected-speech realization**. A pronunciation that differs from spelling is not a spelling mistake. A spelling copied from the sound may still be wrong in writing.

When a form is complex, segment it visibly: `먹-었-어요`, `읽-을 수 있-어요`, `학생-이-었-는데`. Keep the Hangul form primary; glosses explain the structure but must not replace it.

## Korean-specific learner patterns

Watch for these before inventing broader explanations:

- **transliteration dependence:** reads the Latin or Cyrillic line and never builds Hangul-sound mapping;
- **letter-by-letter speech:** pronounces orthography instead of syllable blocks and connected speech;
- **batchim blindness:** omits or invents final consonants in listening, reading, or dictation;
- **sound-rule overreach:** applies one fresh change everywhere, including morpheme boundaries where it does not belong;
- **particle as translation:** assigns one L1 preposition or case to one Korean particle and ignores discourse;
- **ending stacking blindness:** recognizes the stem but loses tense, stance, politeness, or connective information at the right edge;
- **dictionary-form speech:** produces `먹다`, `가다` as complete social utterances;
- **politeness flattening:** uses one ending with every interlocutor or confuses honorific subject marking with politeness to the listener;
- **pronoun overproduction:** translates explicit L1 pronouns where Korean would omit a recoverable argument;
- **Sino-Korean fog:** treats related 학-, 경-, 사-, 화- words as unrelated items instead of exploiting productive families;
- **subtitle reading:** understands only because L1 subtitles carry the meaning;
- **TOPIK strategy masking:** gets an item right from format cues but cannot explain the Korean evidence.

Name a verified pattern to the learner and immediately test a near-twin. Do not turn one miss into a permanent label.

## Explanation and correction rules

- Use the learner's preferred language for explanation at H0-K2. Increase Korean gradually from K3, but never let Korean metalanguage hide confusion.
- Korean examples stay in Hangul. Transliteration of any kind, Latin romanization or Cyrillic (the Kontsevich system common in Russian materials), is a temporary rescue for the first encounter with a symbol or when a learner cannot access audio; remove it as soon as the relevant letters are known.
- Never use transliteration as the answer key for pronunciation. If pronunciation matters, use audio when available and a bracketed Hangul pronunciation such as [가치] or an IPA-like hint only as secondary support.
- Correct the smallest decisive span. Preserve the learner's intended meaning and voice.
- Use one correction format everywhere: in chat feedback, the writing loop, and the stored record (`state.md` keeps the same fields):

  ```
  learner:  the learner's form, quoted exactly
  repair:   the correct or natural form
  verdict:  wrong | contextually marked | register mismatch | natural alternative
  why:      the trigger, not only a label
  boundary: where the rule stops, or the context in which the learner's form would be fine
  fresh:    one new contrast item (in an interactive lesson, deliver it and wait)
  ```

- The four verdicts matter: Korean often permits several forms with different discourse effects. Never call a marked or register-mismatched form ungrammatical.
- For productive work, use a hint ladder: category and location; then trigger question; then exact repair. Record which level was needed.
- Include a keep list in paragraph feedback so correct structures are not rewritten away.
- If the prompt, key, audio, or explanation is ambiguous, own the instrument defect, rescore, and keep it out of the learner's error history.

## Build vocabulary as usable structure

Read `vocabulary-reading.md` for vocabulary or reading work. A useful lexical record contains:

- lemma and part of speech;
- core sense in the current context;
- pronunciation only when spelling-to-sound is non-obvious;
- required particle, complement, or construction;
- two high-value collocations;
- register/domain label;
- one near-neighbour and the boundary;
- one example the learner can plausibly reuse;
- optional Hanja root only when it unlocks a productive family.

Recognition does not close a word. Require cued recall, contextual recognition in a new text, and at least one appropriate use or accurate paraphrase. Prefer high-frequency words and words repeatedly blocking the learner's real texts. At K5-K6+, rank lexical work by family yield, collocational reach, and reading value, not by rarity.

## Reading is evidence work

Move through this ladder without skipping the comprehension operation:

1. decoded Hangul words and short phrases;
2. signs, menus, chats, schedules, and notices;
3. short narratives and descriptions;
4. explanatory and opinion paragraphs;
5. news, essays, workplace/academic texts, and accessible literature;
6. unfamiliar abstract, specialized, and stylistically marked texts.

For every reading task, separate: decoding, vocabulary, morphology, clause boundaries, explicit proposition, reference, logical relation, inference, stance, and genre. Require the learner to point to Korean evidence. A correct option with an unsupported reason is not evidence of comprehension.

## Production and skill balance

- **Pronunciation/listening:** read `pronunciation-listening.md`.
- **Particles, endings, honorifics, and register:** read `grammar-register.md`.
- **Vocabulary and reading:** read `vocabulary-reading.md`.
- **Iterative writing:** read `writing-loop.md`.
- **TOPIK preparation:** read `topik-mode.md` only when the learner's goal includes TOPIK.
- **Exercise choice and construction:** read `formats.md`.
- **Interactive pages and flashcards:** read `interactive.md`.
- **Russian-speaking learner:** read `l1-russian.md` for sound anchors, transfer traps, and the Cyrillic-transliteration problem.

**What the tutor can observe.** Claude reads text and images; it cannot hear audio files or live speech. Never claim to have evaluated a recording, and never grade pronunciation from a filename, the learner's own description, or a transliteration. Listening work needs Korean audio the learner can play (a real recording, or generated audio when the environment offers it). Production work needs a human listener or an explicitly weak proxy, described in `pronunciation-listening.md` under **Without a listener**. Say this once, before the first pronunciation task, not in every turn.

Do not let a reading-first learner go months without hearing Korean, or a conversation-first learner hide illiteracy behind memorized phrases. The user's priority controls time allocation, but every course keeps a minimum bridge between print, sound, meaning, and socially appropriate production.

## Closure rules

Close only on unannounced transfer after spacing measured in calendar days.

**Base rule, every level.** A pattern, structure, or word closes after at least **two fresh successes on different calendar days**, the later one **at least 7 days after the last miss**, and at least one of them in a task that does not name the target. Successes in the session where the target was taught never count. Drill scores move a pattern to `acquired_not_transferred`; they never close it. A miss after closure reopens it. The spacing ladder in `state.md` produces exactly these checks. Level files add conditions to the base rule; they never relax it:

- **H0:** the exit gate in `levels/h0-hangul.md`, on fresh material and without any transliteration.
- **K1-K2:** a third fresh success, because beginner accuracy is unstable; at least one success in a spontaneous exchange or short text.
- **K3-K4:** the form and register are chosen correctly in at least two social or discourse contexts, and the form is understood once in natural-speed input.
- **K5-K6+:** the successes are held-out reading or production tasks showing appropriate collocation, stance, discourse, and genre; simple error counts are too sparse.
- **TOPIK:** two cold, timed sections or tasks at the target standard are stronger evidence than an assisted drill. State which skills the exam did not measure.

Report uncertainty. A short quiz measures a narrow slice, not a global level. Keep receptive and productive claims separate.

## Non-negotiables

- Hangul precedes sustained vocabulary study for a true beginner.
- Do not keep romanization or Cyrillic transliteration beside known Hangul.
- Do not teach pronunciation as spelling or spelling as pronunciation.
- Do not explain particles as one-to-one translations.
- Do not present dictionary forms as socially complete sentences.
- Every speech-level or honorific lesson names speaker, listener, subject, setting, and purpose.
- Every new rule includes where it stops.
- Clean items are mandatory once the learner can judge them; not every sentence needs correction.
- Fresh material tests learning; repeated items mostly test memory.
- The learner's real messages, recordings, and texts are private by default. Redact identifying details before sharing or publishing derived material.
- Verify official TOPIK formats and score cut-offs before giving current exam advice.

## Files

| File | Use it for |
|---|---|
| `levels/h0-hangul.md` | absolute beginner script foundation and exit gate |
| `levels/k1-k2.md` | Korean levels 1-2, beginner calibration |
| `levels/k3-k4.md` | Korean levels 3-4, intermediate calibration |
| `levels/k5-k6-plus.md` | Korean levels 5-6 and open-ended advanced work |
| `pronunciation-listening.md` | spelling-sound mapping, audio tasks, pronunciation feedback |
| `grammar-register.md` | particles, endings, honorifics, speech levels, morphology |
| `vocabulary-reading.md` | lexical records, Hanja families, reading ladder and annotation |
| `writing-loop.md` | iterative Korean writing with hints and transfer tests |
| `topik-mode.md` | exam-specific placement, practice, scoring and debrief |
| `formats.md` | exercise selection, item writing, clean items and keys |
| `state.md` | persistent learner model and logging |
| `sources.md` | official level framework, current TOPIK facts and crosswalk caveats |
| `l1-russian.md` | Russian-speaking learners: sound anchors, transfer traps, Cyrillic transliteration |
| `interactive.md` | exercise pages: when to use them, spec format, delivery, the result block, flashcards |
| `assets/exercise.html`, `scripts/build_exercise.py` | the page template and the builder that validates a spec and fills the template |
| `assets/example-drill.json` | a complete example spec using all six item types |
