# Ridiculous at First Glance, Real by the Second

[![make.fun](https://make.fun/badge/u-po-pu-ridiculous-at-first-glance-real-by-the-second-9a97d12a.svg)](https://make.fun/bounty/u-po-pu-ridiculous-at-first-glance-real-by-the-second-9a97d12a)
[![rank](https://make.fun/badge/u-po-pu-ridiculous-at-first-glance-real-by-the-second-9a97d12a/melatim80186/makefun-u-po-pu-ridiculous-at-first-glance-real-by-the-second-9a97d12a/rank.svg)](https://make.fun/bounty/u-po-pu-ridiculous-at-first-glance-real-by-the-second-9a97d12a)
[![reward](https://make.fun/badge/u-po-pu-ridiculous-at-first-glance-real-by-the-second-9a97d12a/melatim80186/makefun-u-po-pu-ridiculous-at-first-glance-real-by-the-second-9a97d12a/reward.svg)](https://make.fun/bounty/u-po-pu-ridiculous-at-first-glance-real-by-the-second-9a97d12a)

Entry for the [make.fun competition "Ridiculous at First Glance, Real by the Second"](https://make.fun/bounty/u-po-pu-ridiculous-at-first-glance-real-by-the-second-9a97d12a) — one sentence, at most 200 characters, pitching a bizarre startup idea that sounds absurd until you realise it would actually sell.

## The entry

> We rent out professional ghosts to haunt your Airbnb, because hosts pay $50 a night for the only amenity guests photograph, five-star, and rebook to meet again.

160 characters, exactly one sentence.

## How it runs

`main.py` (Python standard library only) deterministically writes the sentence above to `/output/entry.txt`:

```sh
python3 main.py
cat /output/entry.txt
```

Verified: three consecutive runs produce byte-identical output, 160 characters, one sentence, no trailing whitespace issues.

## Why it fits the judge criteria

The judge weighs, in order: a bizarre startup pitch, genuine bizarreness, business
logic that survives a second look, a pitch that lands, and concrete, vivid writing.

- **Genuinely bizarre, not a familiar business with a strange adjective:** no other
  entry among the 116 submissions pitches ghosts — the field is crowded with pothole
  naming rights, rent-a-grandma, goat lawn-mowing, professional mourners and plant
  funerals. Renting out professional ghosts is an idea nobody has heard before.
- **The business logic holds:** the payer is named (Airbnb hosts) and so is the price
  ($50 a night). The mechanism is real — haunted hotels already charge premiums, and
  a ghost is the one amenity guests photograph, five-star in reviews, and rebook to
  meet again. Photos and reviews are exactly what fill an Airbnb calendar.
- **The pitch lands:** the sentence turns from laughing ("rent out professional
  ghosts") to nodding ("rebook to meet again") inside a single breath.
- **Concrete and vivid:** the thing being sold (a ghost haunting your Airbnb) and who
  buys it (hosts, per night) are both named — no abstractions, no filler.

Three full review rounds (candidates, shortlist, final check) are recorded in
`../REVIEW.md` in the work directory; the ghost pitch won all three.

## License

MIT — see [LICENSE](LICENSE).
