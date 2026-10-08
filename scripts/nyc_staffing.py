"""Uniformed officers assigned to each precinct, from NYPD Officer Profile - Members of Service (pmsy-ewrc).

  python scripts/nyc_staffing.py      ->  data/staffing.csv, data/staffing.source.json

The dataset is a snapshot of active uniformed members and the command each is assigned to on its export
date. Only counts by command are requested (server side); no names or other personal fields are downloaded.
A precinct's count here is its precinct command plus its field training unit and other units named for it
(for example "078 PCT PROSPECT PARK DETAIL"). Housing police service areas and transit districts also answer
calls inside precincts and are not counted. This is staffing on one date in 2026, not during 2022 to 2025.
"""
import csv
import datetime as dt
import json
import pathlib
import re
import urllib.parse
import urllib.request

ROOT = pathlib.Path(__file__).resolve().parent.parent
DATASET = "https://data.cityofnewyork.us/resource/pmsy-ewrc.json"
QUERY = {"$select": "command, export_date, count(*) as n", "$group": "command, export_date", "$limit": 5000}
NAMED = {"CENTRAL PARK PRECINCT": 22}


def main():
    url = DATASET + "?" + urllib.parse.urlencode(QUERY)
    rows = json.load(urllib.request.urlopen(urllib.request.Request(url, headers={"User-Agent": "residents-count/1.0"}), timeout=120))
    by, export = {}, set()
    for r in rows:
        cmd, n = r["command"].strip().upper(), int(r["n"])
        export.add(r["export_date"][:10])
        m = re.match(r"^(\d{3}) (PRECINCT|PCT)\b", cmd)
        num = int(m.group(1)) if m else NAMED.get(cmd)
        if num is None:
            continue
        d = by.setdefault(num, {"district": num, "officers": 0, "precinct_command": 0, "commands": []})
        d["officers"] += n
        if cmd.endswith("PRECINCT") or re.match(r"^\d{3} PCT-[^ ]+ [^ ]+ PCT$", cmd):
            d["precinct_command"] += n
        d["commands"].append(f"{cmd} ({n})")
    out = ROOT / "data" / "staffing.csv"
    with out.open("w", newline="") as fh:
        w = csv.DictWriter(fh, ["district", "officers", "precinct_command", "commands"])
        w.writeheader()
        for k in sorted(by):
            w.writerow({**by[k], "commands": "; ".join(sorted(by[k]["commands"]))})
    (ROOT / "data" / "staffing.source.json").write_text(json.dumps({
        "url": url, "dataset": "https://data.cityofnewyork.us/d/pmsy-ewrc", "export_date": sorted(export),
        "fetched_at": dt.datetime.now(dt.timezone.utc).isoformat(timespec="seconds"),
        "precincts": len(by), "officers": sum(d["officers"] for d in by.values()),
        "all_active_uniformed": sum(int(r["n"]) for r in rows)}, indent=1))
    print(f"{len(by)} precincts, {sum(d['officers'] for d in by.values()):,} officers -> {out}")


if __name__ == "__main__":
    main()
