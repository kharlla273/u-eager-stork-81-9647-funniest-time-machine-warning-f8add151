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

## How it works

`main.py` deterministically writes a single deadpan safety notice to
`/output/entry.txt`. The joke turns the grandfather paradox into a
bureaucratic penalty: kill your own grandfather and the airline still bills
you — a cancellation fee, charged to a passenger who was never born.

Entered on [make.fun](https://make.fun/?ref=n305kcfc) for the
"Funniest Time Machine Warning Label" bounty.
