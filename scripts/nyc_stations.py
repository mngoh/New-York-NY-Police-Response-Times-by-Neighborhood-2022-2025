"""Precinct station houses: the NYPD's precinct list (name, borough, address), geocoded with NYC Planning's GeoSearch.

  python scripts/nyc_stations.py      ->  data/stations.csv, data/stations.source.json

Columns: district (precinct number as in the calls' nypd_pct_cd), name, borough, address, lat, lon, match.
Central Park is precinct 22; Midtown South and Midtown North are 14 and 18.
"""
import csv
import datetime as dt
import html
import json
import pathlib
import re
import urllib.parse
import urllib.request

ROOT = pathlib.Path(__file__).resolve().parent.parent
LIST = "https://www.nyc.gov/site/nypd/bureaus/patrol/precincts-landing.page"
GEOSEARCH = "https://geosearch.planninglabs.nyc/v2/search"
SPECIAL = {"Central Park Precinct": 22, "Midtown South Precinct": 14, "Midtown North Precinct": 18}
UA = "Mozilla/5.0 (residents-count research)"
# GeoSearch misses these two; coordinates from NYC Planning's Facilities Database (ji82-xba5).
# geo.py checks that every station house falls inside its own precinct's polygon.
OVERRIDE = {7: (40.716522, -73.983915, "FacDB ji82-xba5: 19 1/2 Pitt Street"),
            22: (40.782493, -73.965548, "FacDB ji82-xba5: Central Park Precinct, 86th Street transverse")}


def get(url):
    with urllib.request.urlopen(urllib.request.Request(url, headers={"User-Agent": UA}), timeout=60) as r:
        return r.read().decode("utf-8", "replace")


def main():
    page = get(LIST)
    rows, boro = [], None
    for m in re.finditer(r'<th class="subhead"[^>]*>([^<]+)</th>|<td data-label="Precinct"><a[^>]*>([^<]+)</a></td>\s*'
                         r'<td[^>]*>[^<]*</td>\s*<td data-label="Address">([^<]+)</td>', page):
        if m.group(1):
            boro = html.unescape(m.group(1)).strip()
            continue
        name, addr = html.unescape(m.group(2)).strip(), html.unescape(m.group(3)).strip()
        num = SPECIAL.get(name) or int(re.match(r"(\d+)", name).group(1))
        rows.append({"district": num, "name": name, "borough": boro, "address": addr})
    for r in rows:
        if r["district"] in OVERRIDE:
            r["lat"], r["lon"], r["match"] = OVERRIDE[r["district"]]
            continue
        q = urllib.parse.urlencode({"text": f"{r['address']}, {r['borough']}, NY", "size": 1})
        feats = json.loads(get(f"{GEOSEARCH}?{q}"))["features"]
        if feats:
            f = feats[0]
            r["lon"], r["lat"] = f["geometry"]["coordinates"]
            r["match"] = f["properties"].get("label", "")
        else:
            r["lat"] = r["lon"] = None
            r["match"] = "NOT FOUND"
    out = ROOT / "data" / "stations.csv"
    with out.open("w", newline="") as fh:
        w = csv.DictWriter(fh, ["district", "name", "borough", "address", "lat", "lon", "match"])
        w.writeheader()
        w.writerows(sorted(rows, key=lambda r: r["district"]))
    (ROOT / "data" / "stations.source.json").write_text(json.dumps({
        "list": LIST, "geocoder": GEOSEARCH, "fetched_at": dt.datetime.now(dt.timezone.utc).isoformat(timespec="seconds"),
        "rows": len(rows)}, indent=1))
    print(f"{len(rows)} station houses -> {out}")
    for r in rows:
        num = re.match(r"[\d-]+", r["address"])
        if r["match"] == "NOT FOUND" or (num and not r["match"].startswith(num.group(0).split("-")[0]) and r["district"] not in OVERRIDE):
            print("CHECK:", r)


if __name__ == "__main__":
    main()
