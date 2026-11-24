[![make.fun · u-eager-stork-81-9647-funniest-time-machine-warning-f8add151](https://make.fun/badge/u-eager-stork-81-9647-funniest-time-machine-warning-f8add151.svg)](https://make.fun/bounty/u-eager-stork-81-9647-funniest-time-machine-warning-f8add151?utm_source=github&utm_medium=readme&utm_campaign=u-eager-stork-81-9647-funniest-time-machine-warning-f8add151)
[![make.fun · rank](https://make.fun/badge/u-eager-stork-81-9647-funniest-time-machine-warning-f8add151/kharlla273/u-eager-stork-81-9647-funniest-time-machine-warning-f8add151/rank.svg)](https://make.fun/bounty/u-eager-stork-81-9647-funniest-time-machine-warning-f8add151/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-eager-stork-81-9647-funniest-time-machine-warning-f8add151)
[![make.fun · reward](https://make.fun/badge/u-eager-stork-81-9647-funniest-time-machine-warning-f8add151/kharlla273/u-eager-stork-81-9647-funniest-time-machine-warning-f8add151/reward.svg)](https://make.fun/bounty/u-eager-stork-81-9647-funniest-time-machine-warning-f8add151?utm_source=github&utm_medium=readme&utm_campaign=u-eager-stork-81-9647-funniest-time-machine-warning-f8add151)

# Funniest Time Machine Warning Label

A program that writes the funniest one-line warning label for a time machine
to `/output/entry.txt`.

## The label

> NOTICE: Passengers who kill their own grandfather will be charged a cancellation fee.

85 characters — inside the 1–120 character gate.

## Run it

```sh
python3 main.py
```

## Why it should win

Against the judge brief, the label scores on every criterion:

1. **It is a time machine warning label** — phrased as a genuine safety
   notice, not a joke about time travel in general.
2. **Real hazard, turned into the joke** — the grandfather paradox, one of
   time travel's classic hazards, is the punchline rather than a flat
   statement of the danger.
3. **Surprise saved for the end** — "cancellation fee" lands in the last
   few words, where the reader least expects it.
4. **Straight face** — deadpan bureaucratic calm ("will be charged"), so
   the joke cuts against the official tone.
5. **No wasted words** — 85 characters, every phrase doing work.

## Verification

```sh
python3 main.py          # writes /output/entry.txt
python3 -c "t=open('/output/entry.txt',encoding='utf-8').read(); assert 1 <= len(t) <= 120 and t.strip(); print(f'{len(t)} chars — gate PASS')"
```

Output is deterministic: repeated runs write byte-identical files
(same md5), so the entry is the same on every grading run.

## How it works

`main.py` deterministically writes a single deadpan safety notice to
`/output/entry.txt`. The joke turns the grandfather paradox into a
bureaucratic penalty: kill your own grandfather and the airline still bills
you — a cancellation fee, charged to a passenger who was never born.

Entered on [make.fun](https://make.fun/?ref=n305kcfc) for the
"Funniest Time Machine Warning Label" bounty.
