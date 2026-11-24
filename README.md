# THE DAILY GLOBE — 24 November 2026

[![make.fun · news-image-20261124](https://make.fun/badge/news-image-20261124.svg)](https://make.fun/bounty/news-image-20261124?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261124)
[![rank](https://make.fun/badge/news-image-20261124/Yetu89/news-image-20261124/rank.svg)](https://make.fun/bounty/news-image-20261124/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261124)
[![reward](https://make.fun/badge/news-image-20261124/Yetu89/news-image-20261124/reward.svg)](https://make.fun/bounty/news-image-20261124?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261124)

One image that sums up the world news of Tuesday, 24 November 2026:
Nvidia reinstates Jensen Huang as CEO and shares soar 31.5% in a day,
Rep. Jimmy Gomez quits after a House ethics report, Ukraine sinks the
Russian corvette Merkury off Libya, Russian strikes kill 11 in the Kyiv
region, 24 die in an Indonesian candy-factory fire, the World Chess
Championship opens in Geneva, and New Zealand bat out a draw after
India's 720 — plus COP31's no-deal ending, India's Nepal package,
Huawei's Mate X8 launch, and Monday's market close.

## How it is made

`tools/stories.json` holds the day's stories, briefs and market figures.
`tools/build_image.py` (Pillow plus the standard library) draws the
1024x1024 newspaper front page and writes `entry.png`. `main.py`
(standard library only) copies `entry.png` to `/output/entry.png`
(or `$OUTPUT_DIR/entry.png`).

```sh
python3 tools/build_image.py
python3 main.py
```

The build is deterministic: running `build_image.py` twice produces
byte-identical output, and `main.py` copies the same file every run.

## License

MIT. See `LICENSE`.
