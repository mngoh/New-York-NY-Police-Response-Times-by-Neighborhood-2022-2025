# Racial discrimination review: response times

This screen finds candidates; every flag needs to be read in context before acting.

## Data

- **note: neighborhoods, not people.** Makeup groups come from Census estimates of residents (self-identified), so there is no officer-recorded race and no race-coding bound. The data says nothing about who made each call; the writeup must not imply that callers of a race waited longer.
- **FLAG: small group.** Asian: 6 neighborhoods, 224,852 residents. Do not headline its comparisons.
- **note: size moves by period.** income Non Critical 1: 2022-23 +3.2, 2024-25 +4.8, 2026 holdout +6.3.
- **FLAG: direction changes by period.** makeup Critical Asian: 2022-23 +0.2 min, 2024-25 +0.2 min, 2026 holdout -0.3 min (pooled +0.2). Do not headline.
- **FLAG: direction changes by period.** makeup Critical No majority: 2022-23 +0.2 min, 2024-25 +0.2 min, 2026 holdout -0.0 min (pooled +0.2). Do not headline.
- **FLAG: direction changes by period.** makeup Serious No majority: 2022-23 +0.1 min, 2024-25 +0.1 min, 2026 holdout -0.1 min (pooled +0.1). Do not headline.
- **note: size moves by period.** makeup Non Critical Black: 2022-23 +2.7, 2024-25 +2.6, 2026 holdout +1.2.
- **note: size moves by period.** makeup Non Critical Hispanic: 2022-23 +3.0, 2024-25 +4.9, 2026 holdout +7.0.
- **note: size moves by period.** makeup Non Critical Asian: 2022-23 +3.6, 2024-25 +2.6, 2026 holdout +0.3.
- **note: size moves by period.** makeup Non CIP Black: 2022-23 +10.4, 2024-25 +8.4, 2026 holdout +5.4.
- **FLAG: missing arrivals differ by group.** income, Non Critical: 10.4% (4) to 17.4% (1). The waits leave these calls out; state the difference beside the waits and report the upper-bound check.
- **FLAG: missing arrivals differ by group.** income, Non CIP: 34.6% (3) to 45.0% (1). The waits leave these calls out; state the difference beside the waits and report the upper-bound check.
- **FLAG: missing arrivals differ by group.** makeup, Non Critical: 11.4% (Asian) to 17.1% (White). The waits leave these calls out; state the difference beside the waits and report the upper-bound check.
- **FLAG: missing arrivals differ by group.** makeup, Non CIP: 34.0% (Asian) to 44.8% (Hispanic). The waits leave these calls out; state the difference beside the waits and report the upper-bound check.
- **note: controls are not neutral.** Call types, precinct busyness and precinct boundaries reflect where calls come from, how they are coded, and how police are deployed, which are shaped by segregation. A gap that narrows after them has been located, not explained away.

## Writeup

Files: `index.html`, `README.md`, `PLAN.md`

### index.html
- **review: Absolute or proof language** (`never`): "The clock starts when the call taker enters the job, not when the phone rings, and stops when a unit is marked as arrived. Officers mark their own arrival, and some calls never get an arrival time."  
  Overstates certainty. Use 'the data shows' and keep the caveats attached.

### README.md
- **review: Absolute or proof language** (`never`): "- **How the system records time.** The clock starts when the call taker enters the job, not when the phone rings, and stops when a unit is marked as arrived. Officers mark their own arrival, and some calls never get an a..."  
  Overstates certainty. Use 'the data shows' and keep the caveats attached.

### PLAN.md
- **review: Causal claim** (`causes`): "Neutral voice. Neighborhoods are described by their makeup ("majority-Black neighborhoods"), never as statements about people. Results that favor the NYPD get the same prominence as results that don't. No causes are clai..."  
  The data shows rates, not causes. Keep causal words only in sentences that say a cause is not measured.
- **review: Absolute or proof language** (`never`): "Each of NYPD's four categories is analyzed separately and never pooled: Critical, Serious, Non-critical (the three crime-in-progress levels) and Not a crime in progress (Non CIP)."  
  Overstates certainty. Use 'the data shows' and keep the caveats attached.
- **review: Absolute or proof language** (`never`): "- **Calls never made**, and calls closed without an arrival."  
  Overstates certainty. Use 'the data shows' and keep the caveats attached.
- **review: Absolute or proof language** (`never`): "Neutral voice. Neighborhoods are described by their makeup ("majority-Black neighborhoods"), never as statements about people. Results that favor the NYPD get the same prominence as results that don't. No causes are clai..."  
  Overstates certainty. Use 'the data shows' and keep the caveats attached.
- **review: Explained-away language** (`accounts for most`): "- **One location** (one street segment) on the Upper West Side produced 694 Critical and 1,122 Serious calls from the public, about 70% of them closed within two minutes with no arrival. It accounts for most of the high ..."  
  Controls like neighborhood and income are themselves shaped by segregation and discrimination. 'Explained by location' does not mean 'not related to race'.
- **review: Explained-away language** (`explained away`): "Priority is handled by analyzing each category separately. A gap that shrinks after a control has been located (for example in farther-flung precincts), not explained away."  
  Controls like neighborhood and income are themselves shaped by segregation and discrimination. 'Explained by location' does not mean 'not related to race'.

### Required statements

- present: says it does not show why
- present: says groups describe neighborhoods, not callers
- present: names where calls come from and how they are classified
- present: names how the system records time
- present: names calls with no arrival

## Reviewer questions (answer in prose)

- Does any sentence turn a neighborhood difference into a statement about people of a race?
- Would the framing read the same if the groups were swapped?
- Do results that favor the police get the same prominence as those that don't?
- Is the headline comparison stable across periods and not the smallest group?
- Are deployment, staffing and dispatch choices named as unmeasured, without being asserted as the cause?
## Judgment (2026-10-08)

Data flags:
- Small group: the 6 majority-Asian neighborhoods are in the tables, marked, and out of the headline and answer.
- Direction changes: only in gaps of 0.3 minutes or less (majority-Asian and no-majority, Critical and Serious), none headlined.
- Size moves: the majority-Black gaps were smaller in 2026 (calls not about a crime in progress 51% in 2022-23, 25% in 2026; non-critical 12%, under the bar). The answer says so. The lowest-income and majority-Hispanic gaps for non-critical calls grew; the answer says so.
- Missing arrivals: the no-arrival share is highest in both the lowest- and highest-income fifths and in majority-Hispanic and majority-White neighborhoods, lower in majority-Black ones. The caveat now states this, and the upper-bound check (no-arrival calls counted as waiting until closed) widens every less-urgent gap, so leaving them out does not create the gaps.
- Controls: the within-precinct result is written as locating the gaps between precincts, "not explaining them".

Writeup flags: "never" (some calls never get an arrival time; categories never pooled), "driven by" (removed from the README), "accounts for most" (one location and missing arrivals in one neighborhood) and "explained away" (the plan's own rule) are factual or rule text. "Neighborhoods waited" was changed to "calls from those neighborhoods waited".

Reviewer questions:
- Statements about people: none. Every comparison is of calls located in neighborhoods grouped by Census makeup; the limits say the data says nothing about who made a call.
- Swapped groups: the framing is symmetric; gaps are reported in both directions, and "no majority" neighborhoods, which show little difference, get the same treatment.
- Results that favor the police: the headline leads with the Critical result (under the bar) and ends with the within-precinct result; both are in the answer before the less urgent gaps' explanations.
- Stability: the headline range (28% to 79%) comes from the 2022 to 2025 estimates; the majority-Black end shrank in 2026, which the answer reports.
- Unmeasured explanations: deployment, other work and dispatch choices are named as not shown; nothing is asserted as the cause.

Rerun 2026-10-08 after shortening the page and the Residents Count article: no writeup flags beyond factual "never"; the data flags are unchanged and still covered (the no-arrival table and caveat on the page, the "Every call" item in the article).
