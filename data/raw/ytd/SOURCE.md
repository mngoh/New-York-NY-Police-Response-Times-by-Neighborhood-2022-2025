# Source: NYPD Calls for Service (Year to Date), NYC Open Data n2zq-pubd, 2026 rows only

- Portal page: https://data.cityofnewyork.us/d/n2zq-pubd
- API: `https://data.cityofnewyork.us/resource/n2zq-pubd.csv`, one request series per calendar month
- Filter: `create_date` from 2026-01-01 to 2026-06-30
- Columns: `cad_evnt_id, create_date, incident_date, incident_time, nypd_pct_cd, boro_nm, patrl_boro_nm, geo_cd_x, geo_cd_y, radio_code, typ_desc, cip_jobs, add_ts, disp_ts, arrivd_ts, closng_ts, latitude, longitude` (all kept as text, as served)
- Ordered by `:id`, paged 500,000 rows at a time; each month's rows checked against the portal's `count(*)` for the same filter
- Fetched: 2026-10-08T14:42:47+00:00 to 2026-10-08T14:45:27+00:00 (UTC)
- Rows: 3,445,395 in 6 monthly files, 2026-01 to 2026-06

Every month's exact URL, filter, time and count is in `sources.json` beside this note.
