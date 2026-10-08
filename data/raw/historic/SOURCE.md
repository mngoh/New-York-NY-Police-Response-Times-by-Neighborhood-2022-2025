# Source: NYPD Calls for Service (Historic), NYC Open Data d6zx-ckhd

- Portal page: https://data.cityofnewyork.us/d/d6zx-ckhd
- API: `https://data.cityofnewyork.us/resource/d6zx-ckhd.csv`, one request series per calendar month
- Filter: `create_date` from 2022-01-01 to 2025-12-31
- Columns: `cad_evnt_id, create_date, incident_date, incident_time, nypd_pct_cd, boro_nm, patrl_boro_nm, geo_cd_x, geo_cd_y, radio_code, typ_desc, cip_jobs, add_ts, disp_ts, arrivd_ts, closng_ts, latitude, longitude` (all kept as text, as served)
- Ordered by `:id`, paged 500,000 rows at a time; each month's rows checked against the portal's `count(*)` for the same filter
- Fetched: 2026-10-08T14:46:24+00:00 to 2026-10-08T15:12:42+00:00 (UTC)
- Rows: 28,676,126 in 48 monthly files, 2022-01 to 2025-12

Every month's exact URL, filter, time and count is in `sources.json` beside this note.
