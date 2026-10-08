# Police response times by neighborhood: New York, NY, 2022 to 2025

Do 911 calls wait longer for police to arrive in some New York neighborhoods than in others, at the same call priority?

NYPD calls for service from NYC Open Data, 2022 to 2025, with January to June 2026 held out as a check, compared across the city's residential neighborhoods (2020 Neighborhood Tabulation Areas) grouped by income and by racial and ethnic makeup. The plan, committed before the comparison ran, is in [PLAN.md](PLAN.md).

<!-- results:start -->
Results will appear here after the analysis runs.
<!-- results:end -->

## Rebuild

The code is the response-time module of [disparity-kit](https://github.com/mngoh/disparity-kit) (`kit/response/`), driven by this folder's `response.json`. The same steps run for another city with that city's config.

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
out/                   audit, results, tables
index.html             the findings page
```
