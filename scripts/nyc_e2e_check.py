"""Compare citywide times from the call data with the city's official 911 End-to-End figures (NYC Open Data t7p9-n9dy).

  python scripts/nyc_e2e_check.py      ->  out/e2e_check.md, out/e2e_check.json

The End-to-End data gives, each week, NYPD incidents that came in through 911 by final incident type
(1. Critical, 2. Serious, 3. Non-Critical), with segment times:
  average_dispatch   minutes from job creation to a unit assigned
  average_travel     minutes from a unit assigned to arrival
  median_dispatch, median_travel   the same segments as medians, in seconds
Job creation is the call data's entry time (add_ts), so dispatch plus travel is the call data's entry-to-arrival
wait. End-to-End also times the phone segments before a job exists (pickup, call-taker processing), which the
call data does not have. Weekly medians are averaged weighted by incidents, which approximates a yearly median.
Needs out/citywide_by_year.csv from audit.py.
"""
import json
import pathlib
import urllib.parse
import urllib.request

import pandas as pd

ROOT = pathlib.Path(__file__).resolve().parent.parent
URL = "https://data.cityofnewyork.us/resource/t7p9-n9dy.json"
TYPES = {"1. Critical": "Critical", "2. Serious": "Serious", "3. Non-Critical": "Non Critical"}


def main():
    q = {"$where": "agency = 'NYPD' AND date >= '2021-12-27' AND date < '2026-07-01'", "$limit": 50000}
    url = URL + "?" + urllib.parse.urlencode(q)
    e = pd.DataFrame(json.load(urllib.request.urlopen(urllib.request.Request(url, headers={"User-Agent": "residents-count/1.0"}), timeout=120)))
    for c in ["of_incidents_calculated", "average_dispatch", "average_travel", "median_dispatch", "median_travel",
              "call_to_agency_arrival", "average_pickup", "average_calltaker_processing"]:
        e[c] = pd.to_numeric(e[c], errors="coerce")
    e["date"] = pd.to_datetime(e["date"])
    e["year"] = (e["date"] + pd.Timedelta(days=3)).dt.year  # a week belongs to the year of its Thursday
    e["priority"] = e["final_incident_type"].map(TYPES)
    e = e[e["priority"].notna()]
    w = "of_incidents_calculated"
    rows = []
    for (pr, y), x in e.groupby(["priority", "year"]):
        n = x[w].sum()
        avg = lambda c: (x[c] * x[w]).sum() / n
        rows.append({"priority": pr, "year": y, "e2e_incidents": int(n),
                     "e2e_mean_dispatch": avg("average_dispatch"), "e2e_mean_travel": avg("average_travel"),
                     "e2e_mean_wait": avg("average_dispatch") + avg("average_travel"),
                     "e2e_med_dispatch": avg("median_dispatch") / 60, "e2e_med_travel": avg("median_travel") / 60,
                     "e2e_phone_minutes": avg("average_pickup") + avg("average_calltaker_processing")})
    e2e = pd.DataFrame(rows)
    ours = pd.read_csv(ROOT / "out" / "citywide_by_year.csv")
    m = e2e.merge(ours, on=["priority", "year"], how="inner")
    m["ratio_incidents"] = m["n"] / m["e2e_incidents"]
    m["ratio_mean_wait"] = m["mean_wait"] / m["e2e_mean_wait"]
    m["ratio_mean_dispatch"] = m["mean_dispatch"] / m["e2e_mean_dispatch"]
    m["ratio_mean_travel"] = m["mean_travel"] / m["e2e_mean_travel"]
    m.to_json(ROOT / "out" / "e2e_check.json", orient="records", indent=1)
    cols = ["priority", "year", "e2e_incidents", "n", "e2e_mean_dispatch", "mean_dispatch", "e2e_mean_travel", "mean_travel",
            "e2e_mean_wait", "mean_wait", "e2e_med_dispatch", "med_dispatch", "e2e_med_travel", "med_travel"]
    order = {"Critical": 0, "Serious": 1, "Non Critical": 2}
    m = m.sort_values(["priority", "year"], key=lambda s: s.map(order) if s.name == "priority" else s)
    lines = ["# Check against the city's 911 End-to-End figures", "",
             f"Source: {URL} (NYPD rows, weeks of 2022 to June 2026), fetched with `{urllib.parse.unquote(urllib.parse.urlencode(q))}`.", "",
             "Minutes. \"Ours\" counts calls from the public with an arrival between 0 and 24 hours after entry, "
             "priority as recorded in the call data (CIP category). End-to-End counts incidents that came through 911 "
             "by final incident type. Weekly medians are averaged weighted by incidents.", "",
             "| Priority | Year | E2E incidents | Our calls | Dispatch, E2E mean | ours | Travel, E2E mean | ours | Wait, E2E mean | ours | Dispatch, E2E median | ours | Travel, E2E median | ours |",
             "|---|---|---|---|---|---|---|---|---|---|---|---|---|---|"]
    for r in m.itertuples():
        lines.append(f"| {r.priority} | {r.year} | {r.e2e_incidents:,} | {r.n:,} | {r.e2e_mean_dispatch:.1f} | {r.mean_dispatch:.1f} | "
                     f"{r.e2e_mean_travel:.1f} | {r.mean_travel:.1f} | {r.e2e_mean_wait:.1f} | {r.mean_wait:.1f} | "
                     f"{r.e2e_med_dispatch:.1f} | {r.med_dispatch:.1f} | {r.e2e_med_travel:.1f} | {r.med_travel:.1f} |")
    lines += ["", f"End-to-End also counts {m['e2e_phone_minutes'].mean():.1f} minutes on average for the phone segments before a job exists "
              "(pickup and call-taker processing). The call data starts its clock after them.", ""]
    (ROOT / "out" / "e2e_check.md").write_text("\n".join(lines))
    print("\n".join(lines))


if __name__ == "__main__":
    main()
