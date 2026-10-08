# Plan: police response times by neighborhood, New York City, 2022 to 2025

Written 2026-10-08, after the data audit and before any comparison of response times between groups of neighborhoods. It is committed to git before the analysis runs. Any change made after that commit is listed under "Changes after the plan was committed", with its reason.

Ticket: mngoh/Residents-Count#1, "Police response times by neighborhood".

## Question

Do 911 calls wait longer for police to arrive in some New York neighborhoods than in others, at the same call priority?

## Data

| What | Source | Window |
|---|---|---|
| Calls | NYPD Calls for Service (Historic), NYC Open Data `d6zx-ckhd` | 2022-01-01 to 2025-12-31, by `create_date` |
| Holdout | NYPD Calls for Service (Year to Date), NYC Open Data `n2zq-pubd`, its 2026 rows only (it overlaps 2025) | 2026-01-01 to 2026-06-30 |
| Neighborhoods | 2020 Neighborhood Tabulation Areas, NYC Planning, `9nt8-h7nd` | current |
| Residents | American Community Survey 2020 to 2024 five-year estimates, by census tract (Census Reporter), summed to neighborhoods with NYC Planning's tract-to-NTA field (`63ge-mke6`) | 2020 to 2024 |
| Precincts | Police precinct polygons, `y76i-bdw7` | current |
| Station houses | NYPD's precinct list (address of each station house), geocoded with NYC Planning's GeoSearch | 2026-10-08 |
| Staffing | NYPD Officer Profile, Members of Service, `pmsy-ewrc`: uniformed members by assigned command (counts only) | snapshot of 2026-10-04 |
| Check | NYC 911 End-to-End Data, `t7p9-n9dy` | 2022 to June 2026 |

Fields, confirmed against NYPD's data dictionary (`NYPD_CallsForService_DataDictionary.xlsx`, attached to both call datasets):
`add_ts` is when the call was added to the system (the job was entered), `disp_ts` when it was dispatched to a responding unit, `arrivd_ts` when the responding unit arrived ("not all calls will have an arrival time"), `closng_ts` when the call was marked closed. `cip_jobs` is the crime-in-progress category (Critical, Serious, Non Critical, or Non CIP for everything else). `radio_code` is the call type and `typ_desc` its description. `nypd_pct_cd` is the precinct. `latitude` and `longitude` are the midblock of the street segment.

Raw files, one per month, are in `data/raw/<source>/`, each source with `SOURCE.md` and `sources.json` (URL, query, time, row count).

## What the audit found (out/audit.md)

- **Rows.** 32,121,521 rows: 28,676,126 for 2022 to 2025 and 3,445,395 for January to June 2026. Every month's rows matched the portal's own count. Combining the 951,462 rows (3.0%) that repeat an event id leaves 31,170,059 events (27,817,506 in 2022 to 2025). Repeated rows keep the event's location and call type and differ in entry, dispatch or arrival times.
- **Coverage.** No month is thin: 505,730 to 638,135 events a month. Calls are fewest at 5 a.m. in the stored times, the overnight low, so the times are local.
- **Officer-initiated events can be separated only by rule** (the data has no field for it). Of all events: 11,827,406 directed patrols, visits and inspections (75 codes, 40.9% of "Non CIP" events); 26,626 officer requests for assistance (13 codes, 7.7% of Critical); 45,114 ShotSpotter alerts (13.0% of Critical); and 3,660,891 events whose arrival was logged in the same second as the entry or the dispatch. That leaves 15,610,022 calls from the public. The share of Critical events that are not calls from the public ranges from 5% to 34% across neighborhoods (10th to 90th percentile), mostly ShotSpotter alerts, which come from some neighborhoods far more than others.
- **No arrival time**, calls from the public: Critical 3.9%, Serious 6.0%, Non-critical 14.6%, Not a crime in progress 40.5%. It clusters by neighborhood (10th to 90th percentile across neighborhoods): Critical 1.3% to 4.6%, Serious 2.5% to 8.0%, Non-critical 6.5% to 20.5%, Not a crime in progress 31.2% to 47.3%. The highest shares are in Midtown Manhattan and neighborhoods of the South and West Bronx (Hell's Kitchen 57.8% and Mount Eden-Claremont (West) 57.2% for calls not about a crime in progress); the lowest in Canarsie, the Rockaways and southern Queens (about 26% to 28%). This is a finding in itself and is compared across groups below.
- **One location** (one street segment) on the Upper West Side produced 694 Critical and 1,122 Serious calls from the public, about 70% of them closed within two minutes with no arrival. It accounts for most of the high no-arrival shares in Upper West Side-Manhattan Valley (42.7% of Critical calls, 27.5% of Serious). Ocean Hill has a similar location (285 Critical calls, 237 with no arrival). The data does not say why. The location is named here by neighborhood only.
- **Implausible times are rare.** Among calls from the public, 179 arrivals are logged before the entry, 150 dispatches before the entry, 160 arrivals before the dispatch, and 56 waits are over 24 hours: all under 0.01% in every priority. No event lacks a dispatch time.
- **Location.** Every published event has coordinates; events NYPD could not place may be left out before publication, which the data cannot show. 0.02% to 0.10% fall outside every neighborhood (shorelines) and 1.1% to 1.9% in parks, airports and other non-residential areas.
- **Precincts.** 95.9% of events fall inside the current polygon of the precinct they are coded to. The 116th Precinct first appears on 2024-12-18 (70,920 events), formed from part of the 105th. The analysis uses the precinct each call was coded to at the time, and that precinct's station house.

## Calls in the analysis

1. **One row per event.** Rows sharing `cad_evnt_id` are one event, with the earliest entry, earliest dispatch and earliest arrival (the first unit to arrive).
2. **Calls from the public.** The data has no field saying whether an event came from a 911 call or from an officer. These rules, applied in order, remove events that did not start with someone calling:
   - ShotSpotter alerts (`10S4`): a sensor, not a caller.
   - Codes starting `75`: directed patrols, visibility patrols, station inspections, train runs and community visits.
   - Codes starting `13`: an officer asking for assistance.
   - An arrival logged in the same second as the entry or the dispatch: the unit was already there (on view, or flagged down).
3. **Located in a residential neighborhood**: one of the 197 residential NTAs. Calls in parks, airports, cemeteries and other non-residential areas are left out.
4. **The wait** is measured for calls with an arrival between 0 and 24 hours after entry. Calls with no arrival are a separate outcome (below).

## Priority

Each of NYPD's four categories is analyzed separately and never pooled: Critical, Serious, Non-critical (the three crime-in-progress levels) and Not a crime in progress (Non CIP).

## Measure

- **Median minutes from the call being entered (`add_ts`) to the first arrival (`arrivd_ts`)**, and the **90th percentile**.
- Its two parts: entry to dispatch, and dispatch to arrival.
- The clock starts when the call taker enters the job. The phone time before that (pickup and call-taker processing, about 2.5 minutes on average in the End-to-End data) is not in the call data.

## Groups of neighborhoods

Set from Census data only, before any call outcome was compared (`out/neighborhoods.json`). Each call takes the group of the neighborhood it was located in.

**Income.** Neighborhoods ranked by median household income (interpolated from the summed ACS income brackets) and cut into five groups that each hold about a fifth of residents:

| Fifth | Neighborhoods | Residents | Median household income |
|---|---|---|---|
| Lowest | 41 | 1,708,998 | $28,470 to $55,341 |
| Second | 36 | 1,686,435 | $55,669 to $73,563 |
| Middle | 37 | 1,678,878 | $73,805 to $85,739 |
| Fourth | 40 | 1,702,532 | $85,891 to $107,044 |
| Highest | 43 | 1,698,911 | $108,826 to $200,000 or more |

**Racial and ethnic makeup.** The group that is more than half of a neighborhood's residents; otherwise "no majority". Hispanic is any race; Black, White and Asian are non-Hispanic.

| Makeup | Neighborhoods | Residents |
|---|---|---|
| Majority-Black | 27 | 1,312,600 |
| Majority-Hispanic | 37 | 1,584,848 |
| Majority-Asian | 6 | 224,852 |
| No majority | 75 | 3,080,801 |
| Majority-White | 52 | 2,272,653 |

The majority-Asian group has 6 neighborhoods. Its comparisons are computed and reported, but are not headlined: with fewer than 10 neighborhoods a group's result can turn on one or two places.

## Primary comparisons (one family, Holm-corrected)

For each of the four priorities:

- the lowest-income fifth against the highest-income fifth;
- majority-Black, majority-Hispanic, majority-Asian and no-majority neighborhoods, each against majority-White neighborhoods.

That is 5 comparisons x 4 priorities = **20 tests**.

## Controls in the primary estimate

Within each priority, each group's calls are reweighted (raking) so that their mix matches the citywide mix of calls of that priority on:

- **call type**: radio code (codes with fewer than 200 calls of that priority in 2022 to 2025 pooled as "other");
- **hour of the week**: hour of the day by day of the week, 168 cells;
- **precinct busyness**: calls from the public entered in the same precinct in the same clock hour, in five bands (fifths of all calls).

The adjusted median and 90th percentile are weighted quantiles. Weights are capped at 20 times a group's average.

## Tests

- **Statistic**: the difference in adjusted median minutes, group minus reference.
- **Uncertainty**: cluster bootstrap over neighborhoods, 2,000 resamples, neighborhoods resampled within each group (calls in one neighborhood are not independent). 95% intervals from the percentiles.
- **p-value**: two-sided, from the bootstrap standard error.
- **Multiple comparisons**: Holm-Bonferroni across the 20 primary tests, at 0.05.

## Smallest gap that matters (proposed, to be confirmed before running)

- **Critical**: 2 minutes in adjusted median.
- **Serious, Non-critical, Not a crime in progress**: 20% of the reference group's adjusted median.

Each primary result is classed, in either direction:

| Result | Rule |
|---|---|
| A gap that matters | Holm p under 0.05 and the gap at least the smallest gap that matters |
| Smaller than the smallest gap that matters | the whole 95% interval inside plus or minus that bound |
| Real but smaller than the smallest gap that matters | Holm p under 0.05, the gap under the bound, interval not wholly inside it |
| Inconclusive | anything else |

"Smaller than the smallest gap that matters" is a finding, not an absence of one, and gets the same prominence as a gap that matters.

## Explanations to test (secondary, not in the Holm family)

For each primary comparison and priority, a regression of log minutes with errors clustered by neighborhood, reported as the percent difference in typical minutes after each step:

1. no controls;
2. call type;
3. and hour of the week;
4. and precinct busyness (the primary estimate's controls);
5. and straight-line distance from the call to its precinct's station house (log km);
6. and officers assigned to the precinct per 1,000 calls from the public a year (2026 snapshot, precinct level);
7. the primary's controls within the same precinct (precinct fixed effects).

Priority is handled by analyzing each category separately. A gap that shrinks after a control has been located (for example in farther-flung precincts), not explained away.

Also secondary: the two parts of the wait (entry to dispatch, dispatch to arrival) by the primary method; the 90th percentile; and the share of calls with no arrival time by group, with bootstrap intervals, both as recorded and leaving out calls closed within two minutes with no arrival (which may be duplicates or cancellations, as at the Upper West Side location; the data does not say).

## Replication

- **2022-23 against 2024-25**: the primary estimate in each half, weights raked within each half.
- **2026 holdout** (January to June 2026, the Year to Date dataset): the same.
- Groups stay fixed (ACS 2020 to 2024) in every period.
- A gap that matters **replicates** if it has the same direction in both halves and in 2026 and each period's 95% interval excludes zero. A result whose direction flips in any period is not headlined.

## Sensitivity checks (secondary)

1. Every event, including officer-initiated, on-scene and ShotSpotter events.
2. Without transit and limited-access-highway call types (other bureaus respond, and those locations are not neighborhoods).
3. Precinct busyness measured against the precinct's own average hour instead of in absolute calls.
4. Calls with no arrival counted as waiting until the event was closed (an upper bound).
5. Continuous measures: percent difference per 10 points of a neighborhood's Black, Hispanic or Asian share, and per $25,000 lower median income, with the primary's controls.

## Validation before trusting finer results

Citywide times from the call data were compared with the city's 911 End-to-End figures (`out/e2e_check.md`) before this plan was written:

| | Critical, End-to-End | Critical, call data | Serious, End-to-End | Serious, call data |
|---|---|---|---|---|
| Median, entry to dispatch, 2022 to 2025 | 1.0 to 1.2 min | 1.0 to 1.2 min | 1.2 to 1.4 min | 1.2 to 1.4 min |
| Median, dispatch to arrival | 3.0 to 3.2 min | 3.1 to 3.3 min | 4.3 to 4.6 min | 4.4 to 4.7 min |
| Calls a year | 54,598 to 59,884 | 56,914 to 62,845 | 130,122 to 148,061 | 142,186 to 163,806 |

Medians agree within 0.2 minutes every year; the call data has 4% to 11% more calls, as expected from counting by the CIP category rather than by final incident type. Means in the call data run 0.9 to 1.5 minutes higher; End-to-End may trim long cases, which its documentation does not say. End-to-End's "Non-Critical" type is defined differently (about 42,000 incidents a year against 240,000 Non-critical calls here), but its medians also agree within 0.7 minutes.

## What it cannot show

- **Why.** Recorded times reflect deployment, other work units were handling, and dispatch decisions, none of which the data shows.
- **Where calls come from and how they are classified.** Neighborhoods differ in which calls are made and how call takers code them; the controls hold the code fixed but not the judgment behind it.
- **How the system records time.** The clock starts at job entry, not at the ring; officers mark their own arrival; some calls get none.
- **Calls never made**, and calls closed without an arrival.
- **People.** Groups describe neighborhoods by residents' makeup and income, not who called.
- **Staffing during the window.** The staffing figure is one date in 2026 and counts officers assigned to a precinct, not officers on patrol in a given hour.

## Reporting rules

Neutral voice. Neighborhoods are described by their makeup ("majority-Black neighborhoods"), never as statements about people. Results that favor the NYPD get the same prominence as results that don't. No causes are claimed. Every text that compares neighborhoods by racial makeup goes through `/racial-discrimination-check` before it is shown to anyone.

## Changes after the plan was committed

None yet.
