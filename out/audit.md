# Data audit: Police response times by neighborhood, New York City

## Rows and events

32,121,521 rows; 31,170,059 events after rows that share an event id are combined (951,462 extra rows, 2.96%). An event entered more than once keeps its earliest entry, earliest dispatch and earliest arrival.

| Source | First | Last | Events |
|---|---|---|---|
| historic | 2022-01-01 | 2025-12-31 | 27,817,506 |
| ytd | 2026-01-01 | 2026-06-30 | 3,352,553 |

## Monthly coverage

Events per month: median 578,766, range 505,730 to 638,135. Months under 60% of the median: none. Share with an arrival time by month: 72.5% to 84.1%.

Public calls are fewest at 5:00 in the stored times, the overnight low in local time, so the times are local.

## Who started each event

The data has no field for whether an event came from a 911 call or from an officer. These rules from the config separate them; everything else counts as a call from the public.

| Origin | Rule | Critical | Serious | Non-critical | Not a crime in progress |
|---|---|---|---|---|---|
| officer | directed patrols, visits and inspections (75 codes) | 0 (0.0%) | 0 (0.0%) | 0 (0.0%) | 11,827,406 (40.9%) |
| officer | officer asks for assistance (13 codes) | 26,626 (7.7%) | 0 (0.0%) | 0 (0.0%) | 0 (0.0%) |
| on_scene | arrival logged in the same second as entry or dispatch | 2,865 (0.8%) | 18,314 (2.6%) | 94,579 (8.1%) | 3,545,133 (12.2%) |
| public | none | 271,502 (78.4%) | 684,115 (97.4%) | 1,079,218 (91.9%) | 13,575,187 (46.9%) |
| sensor | ShotSpotter alert (10S4) | 45,114 (13.0%) | 0 (0.0%) | 0 (0.0%) | 0 (0.0%) |

## Checks by priority: calls from the public

| Check | Critical | Serious | Non-critical | Not a crime in progress |
|---|---|---|---|---|
| Events | 271,502 | 684,115 | 1,079,218 | 13,575,187 |
| No arrival time | 3.89% | 5.96% | 14.61% | 40.52% |
| No dispatch time | 0.00% | 0.00% | 0.00% | 0.00% |
| Arrival before entry | 0.00% | 0.00% | 0.00% | 0.00% |
| Dispatch before entry | 0.00% | 0.00% | 0.00% | 0.00% |
| Arrival before dispatch | 0.00% | 0.00% | 0.00% | 0.00% |
| Wait over 24 hours | 0.00% | 0.00% | 0.00% | 0.00% |
| No location | 0.00% | 0.00% | 0.00% | 0.00% |
| Location outside every neighborhood | 0.02% | 0.03% | 0.02% | 0.10% |
| In a park, airport or other non-residential area | 1.22% | 1.08% | 1.19% | 1.92% |
| Event entered more than once | 4.32% | 2.07% | 0.81% | 6.25% |

## Checks by priority: all events, including officer-initiated

| Check | Critical | Serious | Non-critical | Not a crime in progress |
|---|---|---|---|---|
| Events | 346,107 | 702,429 | 1,173,797 | 28,947,726 |
| No arrival time | 3.91% | 5.81% | 13.43% | 20.18% |
| No dispatch time | 0.00% | 0.00% | 0.00% | 0.00% |
| Arrival before entry | 0.00% | 0.00% | 0.00% | 0.00% |
| Dispatch before entry | 0.00% | 0.00% | 0.00% | 0.00% |
| Arrival before dispatch | 0.00% | 0.00% | 0.00% | 0.00% |
| Wait over 24 hours | 0.00% | 0.00% | 0.00% | 0.00% |
| No location | 0.00% | 0.00% | 0.00% | 0.00% |
| Location outside every neighborhood | 0.04% | 0.03% | 0.02% | 0.08% |
| In a park, airport or other non-residential area | 1.36% | 1.08% | 1.33% | 2.05% |
| Event entered more than once | 10.93% | 2.06% | 0.76% | 3.03% |

## How the checks vary across neighborhoods

Calls from the public in residential neighborhoods, neighborhoods with at least 200 calls of that priority. The 10th and 90th percentiles are across neighborhoods. Full table: `out/audit_by_neighborhood.csv`.

| Priority | Check | Neighborhoods | Lowest | 10th pct | Median | 90th pct | Highest |
|---|---|---|---|---|---|---|---|
| Critical | No arrival time | 194 | 0.2% | 1.3% | 2.5% | 4.6% | 42.7% |
| Critical | Wait over 24 hours | 194 | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| Critical | Arrival before entry | 194 | 0.0% | 0.0% | 0.0% | 0.0% | 0.2% |
| Critical | Event entered more than once | 194 | 1.8% | 3.1% | 4.3% | 5.8% | 7.3% |
| Critical | Not from the public (all events) | 194 | 2.0% | 5.3% | 17.4% | 33.8% | 49.8% |
| Critical | Unit on scene at entry (all events) | 194 | 0.0% | 0.1% | 0.5% | 1.4% | 3.1% |
| Serious | No arrival time | 197 | 1.6% | 2.5% | 4.3% | 8.0% | 27.5% |
| Serious | Wait over 24 hours | 197 | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| Serious | Arrival before entry | 197 | 0.0% | 0.0% | 0.0% | 0.0% | 0.1% |
| Serious | Event entered more than once | 197 | 1.0% | 1.4% | 2.2% | 3.2% | 8.6% |
| Serious | Not from the public (all events) | 197 | 0.1% | 0.5% | 1.4% | 3.8% | 11.0% |
| Serious | Unit on scene at entry (all events) | 197 | 0.1% | 0.5% | 1.4% | 3.8% | 11.0% |
| Non-critical | No arrival time | 197 | 4.5% | 6.5% | 10.3% | 20.5% | 30.7% |
| Non-critical | Wait over 24 hours | 197 | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| Non-critical | Arrival before entry | 197 | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| Non-critical | Event entered more than once | 197 | 0.2% | 0.5% | 0.8% | 1.3% | 3.2% |
| Non-critical | Not from the public (all events) | 197 | 0.0% | 0.1% | 2.4% | 13.7% | 32.3% |
| Non-critical | Unit on scene at entry (all events) | 197 | 0.0% | 0.1% | 2.4% | 13.7% | 32.3% |
| Not a crime in progress | No arrival time | 197 | 26.2% | 31.2% | 38.5% | 47.3% | 57.8% |
| Not a crime in progress | Wait over 24 hours | 197 | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| Not a crime in progress | Arrival before entry | 197 | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| Not a crime in progress | Event entered more than once | 197 | 3.1% | 4.7% | 6.1% | 7.6% | 12.6% |
| Not a crime in progress | Not from the public (all events) | 197 | 20.0% | 29.9% | 48.4% | 62.9% | 77.1% |
| Not a crime in progress | Unit on scene at entry (all events) | 197 | 4.8% | 7.7% | 11.7% | 16.1% | 23.9% |

### Critical: neighborhoods with the highest and lowest share of calls with no arrival time

| Neighborhood | Calls | No arrival |
|---|---|---|
| Upper West Side-Manhattan Valley | 1,824 | 42.7% |
| Fordham Heights | 3,309 | 23.0% |
| Ocean Hill | 3,247 | 21.6% |
| Financial District-Battery Park City | 1,105 | 7.6% |
| Bushwick (East) | 2,534 | 6.5% |
| Mount Hope | 3,866 | 6.3% |
| Sunset Park (East)-Borough Park (West) | 730 | 6.2% |
| Dyker Heights | 590 | 6.1% |
| Prospect Lefferts Gardens-Wingate | 1,841 | 6.1% |
| Mount Eden-Claremont (West) | 3,734 | 5.6% |
| East Flushing | 400 | 0.2% |
| Middle Village | 333 | 0.6% |
| Annadale-Huguenot-Prince's Bay-Woodrow | 383 | 0.8% |
| Maspeth | 625 | 0.8% |
| Bensonhurst | 1,165 | 0.9% |
| Oakland Gardens-Hollis Hills | 220 | 0.9% |
| Glen Oaks-Floral Park-New Hyde Park | 214 | 0.9% |
| Bath Beach | 314 | 1.0% |
| Whitestone-Beechhurst | 381 | 1.0% |
| Ozone Park (North) | 649 | 1.1% |

### Serious: neighborhoods with the highest and lowest share of calls with no arrival time

| Neighborhood | Calls | No arrival |
|---|---|---|
| Upper West Side-Manhattan Valley | 5,822 | 27.5% |
| Fordham Heights | 4,014 | 15.8% |
| Midtown-Times Square | 18,353 | 13.3% |
| Harlem (South) | 7,900 | 12.1% |
| East Midtown-Turtle Bay | 5,050 | 11.2% |
| Hell's Kitchen | 7,814 | 10.8% |
| Murray Hill-Kips Bay | 4,691 | 10.6% |
| Spring Creek-Starrett City | 2,409 | 10.5% |
| Bellerose | 922 | 10.3% |
| Ocean Hill | 5,668 | 9.9% |
| Great Kills-Eltingville | 962 | 1.6% |
| Grasmere-Arrochar-South Beach-Dongan Hills | 1,791 | 1.8% |
| Middle Village | 1,079 | 1.9% |
| Mariner's Harbor-Arlington-Graniteville | 2,122 | 2.0% |
| Oakland Gardens-Hollis Hills | 447 | 2.0% |
| Laurelton | 1,072 | 2.1% |
| Canarsie | 4,620 | 2.1% |
| West New Brighton-Silver Lake-Grymes Hill | 1,622 | 2.2% |
| Maspeth | 1,699 | 2.3% |
| Hollis | 1,212 | 2.3% |

### Non-critical: neighborhoods with the highest and lowest share of calls with no arrival time

| Neighborhood | Calls | No arrival |
|---|---|---|
| Midtown-Times Square | 24,108 | 30.7% |
| Fordham Heights | 9,520 | 27.0% |
| Stuyvesant Town-Peter Cooper Village | 1,107 | 26.6% |
| Hell's Kitchen | 14,363 | 25.6% |
| East Midtown-Turtle Bay | 6,141 | 24.8% |
| Mount Eden-Claremont (West) | 9,834 | 24.0% |
| Concourse-Concourse Village | 14,352 | 23.9% |
| Melrose | 13,618 | 23.8% |
| Midtown South-Flatiron-Union Square | 15,033 | 23.5% |
| Mott Haven-Port Morris | 13,472 | 23.4% |
| Oakwood-Richmondtown | 883 | 4.5% |
| Middle Village | 1,390 | 4.5% |
| Kew Gardens | 1,606 | 4.7% |
| Canarsie | 8,127 | 5.4% |
| South Richmond Hill | 2,376 | 5.5% |
| New Dorp-Midland Beach | 1,959 | 5.6% |
| Rockaway Beach-Arverne-Edgemere | 5,703 | 5.6% |
| Ozone Park (North) | 2,135 | 5.7% |
| Arden Heights-Rossville | 745 | 5.8% |
| Great Kills-Eltingville | 1,866 | 5.9% |

### Not a crime in progress: neighborhoods with the highest and lowest share of calls with no arrival time

| Neighborhood | Calls | No arrival |
|---|---|---|
| Hell's Kitchen | 145,935 | 57.8% |
| Mount Eden-Claremont (West) | 108,176 | 57.2% |
| Midtown-Times Square | 309,329 | 56.6% |
| East Midtown-Turtle Bay | 84,243 | 56.2% |
| Highbridge | 64,201 | 53.8% |
| Claremont Village-Claremont (East) | 61,042 | 53.2% |
| Concourse-Concourse Village | 153,284 | 52.9% |
| Murray Hill-Kips Bay | 99,471 | 52.9% |
| University Heights (South)-Morris Heights | 109,290 | 52.4% |
| Mott Haven-Port Morris | 163,902 | 52.0% |
| Canarsie | 102,788 | 26.2% |
| Rockaway Beach-Arverne-Edgemere | 67,699 | 26.4% |
| Breezy Point-Belle Harbor-Rockaway Park-Broad Channel | 27,809 | 27.2% |
| Ozone Park | 27,004 | 27.9% |
| South Ozone Park | 98,951 | 28.3% |
| South Richmond Hill | 26,490 | 28.4% |
| Woodhaven | 35,963 | 28.5% |
| Hamilton Heights-Sugar Hill | 82,491 | 28.5% |
| Astoria (East)-Woodside (North) | 56,729 | 28.5% |
| Forest Hills | 87,139 | 28.7% |

## Single locations with many calls and no arrival

Calls from the public at one location (one street segment) with 50 or more calls that have no arrival time, in the three smallest priority categories. Named by neighborhood only.

| Priority | Neighborhood | Calls | No arrival | Closed within 2 minutes, no arrival |
|---|---|---|---|---|
| Serious | Upper West Side-Manhattan Valley | 1,122 | 1062 | 71.6% |
| Critical | Upper West Side-Manhattan Valley | 694 | 629 | 70.3% |
| Non-critical | Midtown-Times Square | 1,478 | 599 | 2.0% |
| Non-critical | East Harlem (North) | 830 | 310 | 3.1% |
| Non-critical | East Village | 602 | 296 | 3.2% |
| Non-critical | Morningside Heights | 941 | 275 | 0.7% |
| Serious | Upper West Side (Central) | 1,766 | 271 | 0.2% |
| Non-critical | Fordham Heights | 1,002 | 266 | 0.2% |
| Non-critical | Harlem (South) | 1,015 | 253 | 1.0% |
| Non-critical | Harlem (North) | 722 | 252 | 0.7% |
| Non-critical | SoHo-Little Italy-Hudson Square | 587 | 249 | 0.9% |
| Non-critical | Midtown-Times Square | 712 | 242 | 0.6% |
| Critical | Ocean Hill | 285 | 237 | 58.9% |
| Non-critical | Morrisania | 709 | 237 | 0.1% |
| Non-critical | Melrose | 642 | 229 | 3.4% |

## Districts

95.9% of located events fall inside the polygon of the district the event is coded to. Full table: `out/audit_by_district.csv`.

Districts that first appear after the start of the data: None from 2022-04-10 (13 events); 116 from 2024-12-18 (70,920 events).

## Citywide times by year (calls from the public)

Minutes. Medians and means over calls with an arrival between 0 and 24 hours after entry.

| priority | year | n | arrived | med_wait | mean_wait | p90_wait | med_dispatch | mean_dispatch | med_travel | mean_travel |
|---|---|---|---|---|---|---|---|---|---|---|
| Critical | 2022 | 62,525 | 96.1% | 4.4 | 7.4 | 12.2 | 1.0 | 2.2 | 3.1 | 5.2 |
| Critical | 2023 | 62,845 | 95.9% | 4.6 | 8.3 | 13.7 | 1.1 | 2.6 | 3.2 | 5.7 |
| Critical | 2024 | 62,043 | 96.3% | 4.7 | 8.3 | 13.9 | 1.2 | 2.5 | 3.3 | 5.8 |
| Critical | 2025 | 56,914 | 96.5% | 4.7 | 8.5 | 13.8 | 1.1 | 2.6 | 3.3 | 5.9 |
| Critical | 2026 | 27,175 | 95.3% | 4.7 | 8.6 | 13.8 | 1.1 | 2.6 | 3.3 | 6.0 |
| Not a crime in progress | 2022 | 2,876,836 | 61.2% | 23.9 | 53.2 | 139.6 | 3.3 | 10.6 | 16.2 | 42.5 |
| Not a crime in progress | 2023 | 2,959,354 | 60.3% | 26.2 | 61.0 | 162.7 | 3.5 | 12.8 | 17.8 | 48.2 |
| Not a crime in progress | 2024 | 3,022,632 | 60.4% | 27.7 | 62.5 | 167.0 | 3.2 | 10.8 | 19.7 | 51.7 |
| Not a crime in progress | 2025 | 3,104,232 | 58.9% | 26.1 | 61.7 | 163.0 | 2.9 | 11.6 | 18.4 | 50.1 |
| Not a crime in progress | 2026 | 1,612,133 | 54.4% | 25.9 | 62.0 | 165.7 | 2.8 | 11.9 | 18.2 | 50.1 |
| Non-critical | 2022 | 227,685 | 86.2% | 9.6 | 20.6 | 46.4 | 2.0 | 6.7 | 6.3 | 13.8 |
| Non-critical | 2023 | 239,291 | 85.1% | 11.1 | 26.1 | 61.5 | 2.4 | 9.2 | 7.0 | 16.9 |
| Non-critical | 2024 | 246,972 | 85.3% | 11.9 | 26.2 | 61.7 | 2.5 | 8.2 | 7.6 | 18.0 |
| Non-critical | 2025 | 241,066 | 85.8% | 11.4 | 27.4 | 63.0 | 2.2 | 8.7 | 7.6 | 18.7 |
| Non-critical | 2026 | 124,204 | 83.8% | 11.7 | 28.8 | 67.2 | 2.1 | 8.9 | 7.9 | 19.9 |
| Serious | 2022 | 163,806 | 93.3% | 6.1 | 11.2 | 21.4 | 1.2 | 3.0 | 4.5 | 8.1 |
| Serious | 2023 | 159,103 | 93.6% | 6.5 | 12.4 | 24.1 | 1.3 | 3.7 | 4.6 | 8.7 |
| Serious | 2024 | 153,652 | 94.1% | 6.6 | 12.2 | 23.8 | 1.4 | 3.4 | 4.7 | 8.8 |
| Serious | 2025 | 142,186 | 95.1% | 6.1 | 11.4 | 21.2 | 1.2 | 3.1 | 4.4 | 8.3 |
| Serious | 2026 | 65,368 | 94.6% | 5.9 | 11.2 | 20.6 | 1.2 | 3.2 | 4.3 | 8.1 |
