# Police response times by neighborhood: New York, NY, 2022 to 2025

Do 911 calls wait longer for police to arrive in some New York neighborhoods than in others, at the same call priority?

NYPD calls for service from NYC Open Data, 2022 to 2025, with January to June 2026 held out as a check, compared across the city's residential neighborhoods (2020 Neighborhood Tabulation Areas) grouped by income and by racial and ethnic makeup. The plan, committed before the comparison ran, is in [PLAN.md](PLAN.md).

<!-- results:start -->
**New York's most urgent 911 calls wait under a minute longer for police in lower-income, majority-Black and majority-Hispanic neighborhoods than in the highest-income and majority-White ones. Less urgent calls wait 28% to 79% longer. Inside the same precinct, the gaps disappear.**

Critical calls: an adjusted median of 5.0 minutes in the lowest-income fifth of neighborhoods and 4.1 in the highest; 4.9 in majority-Black, 5.0 in majority-Hispanic and 4.2 in majority-White neighborhoods. Gaps of 0.6 to 0.8 minutes, under the 1-minute bar (intervals reach about 1.1). Serious calls: about 0.9 minutes, under the 20% bar.

Less urgent calls: 42%, 28% and 40% longer for non-critical crimes in progress (lowest-income, majority-Black, majority-Hispanic); 69%, 45% and 79% for calls not about a crime in progress. All above the 20% bar.

Call type, hour, precinct workload, distance to the station house and officers per call barely move the gaps. Inside the same precinct they disappear, which locates them between precincts without explaining them. The majority-Black gaps were smaller in 2026; the others held.

Adjusted median minutes from the call being entered to the first officer arriving, calls from the public, 2022 to 2025. Gap with a 95% interval; p is Holm-adjusted across the 20 planned comparisons.

| Priority | Neighborhoods | Median (min) | Gap (min) | Gap | Holm p | Result |
|---|---|---|---|---|---|---|
| Critical | Lowest-income fifth vs highest-income fifth | 5.0 vs 4.1 | +0.8 (+0.5 to +1.1) | +20% | 2.8e-06 | real but smaller than the smallest gap that matters |
| Serious | Lowest-income fifth vs highest-income fifth | 6.9 vs 5.9 | +0.9 (+0.5 to +1.5) | +16% | 0.0037 | real but smaller than the smallest gap that matters |
| Non-critical | Lowest-income fifth vs highest-income fifth | 13.5 vs 9.5 | +4.0 (+2.5 to +5.4) | +42% | 1.6e-06 | gap that matters |
| Not a crime in progress | Lowest-income fifth vs highest-income fifth | 32.5 vs 19.2 | +13.3 (+8.5 to +19.0) | +69% | 7.3e-06 | gap that matters |
| Critical | Majority-Black vs majority-White | 4.9 vs 4.2 | +0.6 (+0.3 to +1.0) | +15% | 0.006 | smaller than the smallest gap that matters |
| Critical | Majority-Hispanic vs majority-White | 5.0 vs 4.2 | +0.7 (+0.4 to +1.1) | +17% | 0.00095 | real but smaller than the smallest gap that matters |
| Critical | Majority-Asian * vs majority-White | 4.5 vs 4.2 | +0.2 (-0.1 to +0.9) | +5% | 0.8 | smaller than the smallest gap that matters |
| Critical | No majority vs majority-White | 4.4 vs 4.2 | +0.2 (-0.1 to +0.4) | +5% | 0.65 | smaller than the smallest gap that matters |
| Serious | Majority-Black vs majority-White | 6.8 vs 6.0 | +0.9 (+0.3 to +1.5) | +14% | 0.041 | real but smaller than the smallest gap that matters |
| Serious | Majority-Hispanic vs majority-White | 6.8 vs 6.0 | +0.9 (+0.4 to +1.4) | +14% | 0.0092 | real but smaller than the smallest gap that matters |
| Serious | Majority-Asian * vs majority-White | 6.9 vs 6.0 | +1.0 (+0.2 to +1.8) | +16% | 0.07 | inconclusive |
| Serious | No majority vs majority-White | 6.0 vs 6.0 | +0.1 (-0.3 to +0.4) | +1% | 0.8 | smaller than the smallest gap that matters |
| Non-critical | Majority-Black vs majority-White | 12.3 vs 9.6 | +2.7 (+1.4 to +4.2) | +28% | 0.003 | gap that matters |
| Non-critical | Majority-Hispanic vs majority-White | 13.4 vs 9.6 | +3.9 (+2.3 to +5.5) | +40% | 8.4e-05 | gap that matters |
| Non-critical | Majority-Asian * vs majority-White | 12.7 vs 9.6 | +3.1 (+1.6 to +6.0) | +33% | 0.023 | gap that matters |
| Non-critical | No majority vs majority-White | 10.0 vs 9.6 | +0.4 (-0.2 to +1.1) | +4% | 0.8 | smaller than the smallest gap that matters |
| Not a crime in progress | Majority-Black vs majority-White | 30.4 vs 21.0 | +9.4 (+5.2 to +14.3) | +45% | 0.00075 | gap that matters |
| Not a crime in progress | Majority-Hispanic vs majority-White | 37.6 vs 21.0 | +16.6 (+12.0 to +21.9) | +79% | 5.9e-10 | gap that matters |
| Not a crime in progress | Majority-Asian * vs majority-White | 30.6 vs 21.0 | +9.6 (+0.0 to +23.6) | +46% | 0.65 | inconclusive |
| Not a crime in progress | No majority vs majority-White | 22.9 vs 21.0 | +1.9 (-1.0 to +4.8) | +9% | 0.8 | inconclusive |

\* Fewer than 10 neighborhoods: reported, not headlined.

What narrows the gaps (percent difference in typical minutes, the plan's controls, across the city and inside the same precinct):

| Neighborhoods | Priority | Across the city | Same precinct |
|---|---|---|---|
| Lowest-income fifth | Critical | +27% | -8% (-14% to -2%) |
| Lowest-income fifth | Serious | +23% | -10% (-16% to -3%) |
| Lowest-income fifth | Non-critical | +50% | -7% (-14% to -1%) |
| Lowest-income fifth | Not a crime in progress | +61% | -11% (-18% to -4%) |
| Majority-Black | Critical | +20% | -3% (-8% to +2%) |
| Majority-Black | Serious | +19% | -2% (-7% to +3%) |
| Majority-Black | Non-critical | +32% | -2% (-7% to +3%) |
| Majority-Black | Not a crime in progress | +42% | -5% (-11% to +1%) |
| Majority-Hispanic | Critical | +25% | -6% (-11% to -1%) |
| Majority-Hispanic | Serious | +21% | -10% (-15% to -4%) |
| Majority-Hispanic | Non-critical | +47% | -8% (-13% to -2%) |
| Majority-Hispanic | Not a crime in progress | +64% | -7% (-16% to +2%) |
| No majority | Critical | +6% | -5% (-9% to -0%) |
| No majority | Serious | +1% | -7% (-11% to -3%) |
| No majority | Non-critical | +6% | -6% (-10% to -2%) |
| No majority | Not a crime in progress | +10% | -9% (-13% to -5%) |

Limits:

- **This shows what, not why.** The data shows differences in recorded times between groups of neighborhoods. It does not show why: how units were deployed, what else they were handling, or how dispatchers chose.
- **Where calls come from.** Times depend on which calls are made, from where, and how call takers classify them. Neighborhoods differ in all three; holding the call type fixed does not hold fixed the judgment behind it.
- **How the system records time.** The clock starts when the call taker enters the job, not when the phone rings, and stops when a unit is marked as arrived. Officers mark their own arrival, and some calls never get an arrival time.
- **Neighborhoods, not people.** Groups describe neighborhoods by their residents' income and makeup (Census estimates). The data says nothing about who made a call.
- **Calls from the public are separated by rule.** The data has no field for whether an event started with a call. 15,560,037 events were left out: directed patrols and visits (75 codes), officers asking for assistance (13 codes), ShotSpotter alerts, and events with an arrival logged in the same second as the entry or dispatch.
- **Calls with no arrival.** Calls with no recorded arrival are left out of the waits. For calls not about a crime in progress their share is highest in both the lowest-income fifth (45%) and the highest-income fifth (42%), and in majority-Hispanic (45%) and majority-White (43%) neighborhoods, against 37% in majority-Black neighborhoods. Counting them as waiting until the event was closed widens the gaps for less urgent calls.
- **Staffing is a 2026 snapshot.** Officers per call counts uniformed officers assigned to each precinct on 2026-10-04, after the window, not officers on patrol in a given hour. It is the only public precinct staffing figure found.
- **Distance is a straight line.** Distance runs from the call to its precinct's station house. Patrol cars are usually out on patrol, not at the station.
- **A small group.** Only 6 neighborhoods are majority-Asian. Their results are in the tables but not in the headline.
- **Precinct lines changed.** The 116th Precinct was formed from part of the 105th in December 2024. Each call keeps the precinct it was coded to at the time.
<!-- results:end -->

## Rebuild

The code is the response-time module of [disparity-kit](https://github.com/mngoh/disparity-kit) (`kit/response/`), run with this folder's `response.json`. The same steps run for another city with that city's config.

```bash
K=~/.claude/disparity-kit
$K/.venv/bin/python $K/kit/response/fetch.py response.json       # monthly API pulls, data/raw/
python3 scripts/nyc_stations.py                                   # station houses, data/stations.csv
python3 scripts/nyc_staffing.py                                   # officers by precinct, data/staffing.csv
$K/.venv/bin/python $K/kit/response/prepare.py response.json      # data/calls.parquet
$K/.venv/bin/python $K/kit/response/geo.py response.json          # neighborhoods, Census, call locations
$K/.venv/bin/python $K/kit/response/audit.py response.json        # out/audit.md
$K/.venv/bin/python scripts/nyc_e2e_check.py                      # out/e2e_check.md
$K/.venv/bin/python $K/kit/response/analyze.py response.json      # out/results.json
$K/.venv/bin/python $K/kit/response/report.py response.json       # out/results.md
$K/.venv/bin/python $K/kit/response/page.py response.json         # index.html and the block above
```

disparity-kit's `/disparity-tests` and `/replicate-check` are built for per-resident rates, so their scripts were not run here; their design (an adjustment ladder, pairwise comparisons, replication in a later period) is carried into `kit/response/analyze.py`, and `kit/response/bias_scan.py` reuses the kit's writeup rules for `/racial-discrimination-check`.

Raw monthly files and the call table are not in the repository (about 1.5 GB); `fetch.py` downloads them again, and each source's `SOURCE.md` records the exact queries, times and row counts.

## Layout

```
response.json          the city's config: sources, field names, who-started-it rules, neighborhoods, groups, tests
PLAN.md                the analysis plan, committed before the comparison ran
data/raw/<source>/     SOURCE.md and sources.json for each download (parquet files not committed)
data/neighborhoods.csv neighborhoods with residents, income, makeup and groups
data/stations.csv      precinct station houses
data/staffing.csv      uniformed officers by precinct command (2026 snapshot)
scripts/               New York specific: station houses, staffing, the End-to-End check
out/audit.md           the data audit; out/e2e_check.md, the check against NYC's 911 End-to-End figures
out/results.md         every result table; out/results.json, the numbers behind the page
out/by_neighborhood.csv, out/by_precinct.csv   raw medians, 90th percentiles and no-arrival shares by neighborhood and precinct
out/bias_review.md     the racial-discrimination check and its judgment pass
index.html             the findings page
```
