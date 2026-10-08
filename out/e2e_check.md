# Check against the city's 911 End-to-End figures

Source: https://data.cityofnewyork.us/resource/t7p9-n9dy.json (NYPD rows, weeks of 2022 to June 2026), fetched with `$where=agency+=+'NYPD'+AND+date+>=+'2021-12-27'+AND+date+<+'2026-07-01'&$limit=50000`.

Minutes. "Ours" counts calls from the public with an arrival between 0 and 24 hours after entry, priority as recorded in the call data (CIP category). End-to-End counts incidents that came through 911 by final incident type. Weekly medians are averaged weighted by incidents.

| Priority | Year | E2E incidents | Our calls | Dispatch, E2E mean | ours | Travel, E2E mean | ours | Wait, E2E mean | ours | Dispatch, E2E median | ours | Travel, E2E median | ours |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Critical | 2022 | 59,831 | 62,525 | 1.9 | 2.2 | 4.4 | 5.2 | 6.4 | 7.4 | 1.0 | 1.0 | 3.0 | 3.1 |
| Critical | 2023 | 59,884 | 62,845 | 2.3 | 2.6 | 4.7 | 5.7 | 6.9 | 8.3 | 1.1 | 1.1 | 3.1 | 3.2 |
| Critical | 2024 | 59,142 | 62,043 | 2.2 | 2.5 | 4.7 | 5.8 | 6.9 | 8.3 | 1.2 | 1.2 | 3.2 | 3.3 |
| Critical | 2025 | 54,598 | 56,914 | 2.2 | 2.6 | 4.7 | 5.9 | 7.0 | 8.5 | 1.1 | 1.1 | 3.1 | 3.3 |
| Critical | 2026 | 26,863 | 27,175 | 2.3 | 2.6 | 4.9 | 6.0 | 7.2 | 8.6 | 1.1 | 1.1 | 3.2 | 3.3 |
| Serious | 2022 | 148,061 | 163,806 | 2.8 | 3.0 | 7.5 | 8.1 | 10.3 | 11.2 | 1.2 | 1.2 | 4.4 | 4.5 |
| Serious | 2023 | 144,128 | 159,103 | 3.4 | 3.7 | 7.9 | 8.7 | 11.2 | 12.4 | 1.3 | 1.3 | 4.6 | 4.6 |
| Serious | 2024 | 139,365 | 153,652 | 3.1 | 3.4 | 8.0 | 8.8 | 11.1 | 12.2 | 1.4 | 1.4 | 4.6 | 4.7 |
| Serious | 2025 | 130,122 | 142,186 | 2.9 | 3.1 | 7.4 | 8.3 | 10.3 | 11.4 | 1.3 | 1.2 | 4.3 | 4.4 |
| Serious | 2026 | 62,101 | 65,368 | 2.9 | 3.2 | 7.1 | 8.1 | 10.0 | 11.2 | 1.2 | 1.2 | 4.2 | 4.3 |
| Non Critical | 2022 | 41,237 | 227,685 | 6.4 | 6.7 | 14.3 | 13.8 | 20.8 | 20.6 | 2.1 | 2.0 | 6.8 | 6.3 |
| Non Critical | 2023 | 43,051 | 239,291 | 8.7 | 9.2 | 17.6 | 16.9 | 26.3 | 26.1 | 2.4 | 2.4 | 7.7 | 7.0 |
| Non Critical | 2024 | 43,089 | 246,972 | 7.8 | 8.2 | 18.3 | 18.0 | 26.1 | 26.2 | 2.4 | 2.5 | 8.2 | 7.6 |
| Non Critical | 2025 | 41,889 | 241,066 | 7.8 | 8.7 | 18.4 | 18.7 | 26.2 | 27.4 | 2.1 | 2.2 | 7.8 | 7.6 |
| Non Critical | 2026 | 22,870 | 124,204 | 7.8 | 8.9 | 19.3 | 19.9 | 27.2 | 28.8 | 2.0 | 2.1 | 8.0 | 7.9 |

End-to-End also counts 2.5 minutes on average for the phone segments before a job exists (pickup and call-taker processing). The call data starts its clock after them.
