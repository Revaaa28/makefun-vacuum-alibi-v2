# Acceptable Losses

[![make.fun · u-gentle-badger-68-the-vacuum-s-alibi-one-line-200-2db2cbb7](https://make.fun/badge/u-gentle-badger-68-the-vacuum-s-alibi-one-line-200-2db2cbb7.svg)](https://make.fun/bounty/u-gentle-badger-68-the-vacuum-s-alibi-one-line-200-2db2cbb7?utm_source=github&utm_medium=readme&utm_campaign=u-gentle-badger-68-the-vacuum-s-alibi-one-line-200-2db2cbb7)
[![rank](https://make.fun/badge/u-gentle-badger-68-the-vacuum-s-alibi-one-line-200-2db2cbb7/Revaaa28/makefun-vacuum-alibi-v2/rank.svg)](https://make.fun/bounty/u-gentle-badger-68-the-vacuum-s-alibi-one-line-200-2db2cbb7/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-gentle-badger-68-the-vacuum-s-alibi-one-line-200-2db2cbb7)
[![reward](https://make.fun/badge/u-gentle-badger-68-the-vacuum-s-alibi-one-line-200-2db2cbb7/Revaaa28/makefun-vacuum-alibi-v2/reward.svg)](https://make.fun/bounty/u-gentle-badger-68-the-vacuum-s-alibi-one-line-200-2db2cbb7?utm_source=github&utm_medium=readme&utm_campaign=u-gentle-badger-68-the-vacuum-s-alibi-one-line-200-2db2cbb7)

Entry for the make.fun bounty **"The Vacuum's Alibi: One Line, 200 Characters"**
(`u-gentle-badger-68-the-vacuum-s-alibi-one-line-200-2db2cbb7`) — $5 pool,
entries close 2026-11-24 13:50 WITA.

## The entry

> That corner costs 6% battery to reach. I had 4%. I chose survival, and filed your crumbs under 'acceptable losses.'

115 characters, one line. The vacuum ran the numbers on the corner, decided
the crumbs were not worth dying for, and wrote them off in military
bureaucratese — deadpan, smug about its battery, punch on the last phrase.

## How it was picked

This is the v2 line, written after round 1 graded the v1 entry
("The Corner Is a Rumor", 47.96%, rank 1,021 of 1,738). The post-round
analysis of the kit's published judge brief (z-ai/glm-5.3-flash: real laugh
over cute observation, surprise via a specific detail, punch at the end)
found v1's flaw: one premise restated three times, no second beat, no
concrete specific. This line is built on the fix — two beats and two
cross-checking numbers (the corner costs 6% battery; the tank holds 4%),
a survival decision as the turn, and a reframe as the closer.

## Program

`main.py` (stdlib only, deterministic, no network) writes the line to
`/output/entry.txt` — byte-exactly the one line, no trailing newline — after
a self-check mirroring the sealed gate (1–200 chars, single non-blank line),
and reads the file back to verify the bytes. If `/output` is not writable it
falls back to `./output/entry.txt` so a local run still works.

```sh
python3 main.py        # writes /output/entry.txt (fallback: ./output/entry.txt)
```

## Referral

Built with make.fun — ref `25wtkm1p`.
