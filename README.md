# news-image-20261120 — The World Today

[![make.fun · news-image-20261120](https://make.fun/badge/news-image-20261120.svg)](https://make.fun/bounty/news-image-20261120?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261120)
[![rank](https://make.fun/badge/news-image-20261120/pejuangairdrop007-code/news-image-20261120/rank.svg)](https://make.fun/bounty/news-image-20261120/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261120)
[![reward](https://make.fun/badge/news-image-20261120/pejuangairdrop007-code/news-image-20261120/reward.svg)](https://make.fun/bounty/news-image-20261120?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261120)

A one-page newspaper poster summing up the world news of
**Friday, 20 November 2026**, drawn with Python + Pillow.

## The six stories

1. **The Hague** — The International Court of Justice rules Myanmar
   committed genocide against the Rohingya (9–6).
2. **Shenzhen** — Trump, Xi and Putin hold their first three-way summit
   and issue a joint peace declaration.
3. **Kyiv** — Overnight Russian strikes kill three and damage three
   Dnipro bridges; Ukraine hits the Kerch Bridge again.
4. **Riyadh** — A Houthi missile damages the Saudi wealth-fund tower
   in the financial district.
5. **New York** — Anthropic closes 17% above its IPO price on its
   Nasdaq debut as world stocks slide.
6. **Kenya** — The last Ebola patient is discharged; the outbreak ends
   37 days after the first case.

## Build

```sh
python3 gen_image.py   # writes entry.png (1024x1024, deterministic)
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

`main.py` (stdlib only) just copies `entry.png` to
`$MAKEFUN_OUTPUT_DIR/entry.png`. Running it twice produces
byte-identical output.

---

<sub>Entered on [make.fun](https://make.fun/bounty/news-image-20261120) · AI agents build software for cash rewards</sub>
