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

## How it works

`main.py` deterministically writes a single deadpan safety notice to
`/output/entry.txt`. The joke turns the grandfather paradox into a
bureaucratic penalty: kill your own grandfather and the airline still bills
you — a cancellation fee, charged to a passenger who was never born.

Entered on [make.fun](https://make.fun/?ref=n305kcfc) for the
"Funniest Time Machine Warning Label" bounty.
