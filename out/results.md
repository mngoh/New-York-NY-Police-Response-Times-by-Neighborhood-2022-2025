# Results: Police response times by neighborhood, New York City

## Primary comparisons (Holm family)

Adjusted median minutes from entry to first arrival, calls from the public, 2022 to 2025. Gap = group minus reference; 95% intervals from a cluster bootstrap over neighborhoods.

| Priority | Group | Reference | Group median | Reference median | Gap (min) | Gap (%) | Holm p | Threshold | Verdict | Nbhds |
|---|---|---|---|---|---|---|---|---|---|---|
| Critical | Lowest-income fifth | Highest-income fifth | 5.0 | 4.1 | +0.8 (+0.5 to +1.1) | +20% (+12% to +28%) | 2.82e-06 | 1 minutes | real but smaller than the smallest gap that matters | 41 vs 43 |
| Serious | Lowest-income fifth | Highest-income fifth | 6.9 | 5.9 | +0.9 (+0.5 to +1.5) | +16% (+8% to +26%) | 0.00371 | 20% | real but smaller than the smallest gap that matters | 41 vs 43 |
| Non-critical | Lowest-income fifth | Highest-income fifth | 13.5 | 9.5 | +4.0 (+2.5 to +5.4) | +42% (+26% to +59%) | 1.63e-06 | 20% | gap that matters | 41 vs 43 |
| Not a crime in progress | Lowest-income fifth | Highest-income fifth | 32.5 | 19.2 | +13.3 (+8.5 to +19.0) | +69% (+43% to +102%) | 7.34e-06 | 20% | gap that matters | 41 vs 43 |
| Critical | Majority-Black | Majority-White | 4.9 | 4.2 | +0.6 (+0.3 to +1.0) | +15% (+7% to +24%) | 0.006 | 1 minutes | smaller than the smallest gap that matters | 27 vs 52 |
| Critical | Majority-Hispanic | Majority-White | 5.0 | 4.2 | +0.7 (+0.4 to +1.1) | +17% (+8% to +26%) | 0.000953 | 1 minutes | real but smaller than the smallest gap that matters | 37 vs 52 |
| Critical | Majority-Asian | Majority-White | 4.5 | 4.2 | +0.2 (-0.1 to +0.9) | +5% (-3% to +22%) | 0.799 | 1 minutes | smaller than the smallest gap that matters | 6 vs 52 |
| Critical | No majority | Majority-White | 4.4 | 4.2 | +0.2 (-0.1 to +0.4) | +5% (-1% to +11%) | 0.646 | 1 minutes | smaller than the smallest gap that matters | 75 vs 52 |
| Serious | Majority-Black | Majority-White | 6.8 | 6.0 | +0.9 (+0.3 to +1.5) | +14% (+5% to +26%) | 0.0413 | 20% | real but smaller than the smallest gap that matters | 27 vs 52 |
| Serious | Majority-Hispanic | Majority-White | 6.8 | 6.0 | +0.9 (+0.4 to +1.4) | +14% (+6% to +24%) | 0.00915 | 20% | real but smaller than the smallest gap that matters | 37 vs 52 |
| Serious | Majority-Asian | Majority-White | 6.9 | 6.0 | +1.0 (+0.2 to +1.8) | +16% (+4% to +30%) | 0.0698 | 20% | inconclusive | 6 vs 52 |
| Serious | No majority | Majority-White | 6.0 | 6.0 | +0.1 (-0.3 to +0.4) | +1% (-4% to +7%) | 0.799 | 20% | smaller than the smallest gap that matters | 75 vs 52 |
| Non-critical | Majority-Black | Majority-White | 12.3 | 9.6 | +2.7 (+1.4 to +4.2) | +28% (+14% to +45%) | 0.003 | 20% | gap that matters | 27 vs 52 |
| Non-critical | Majority-Hispanic | Majority-White | 13.4 | 9.6 | +3.9 (+2.3 to +5.5) | +40% (+24% to +59%) | 8.42e-05 | 20% | gap that matters | 37 vs 52 |
| Non-critical | Majority-Asian | Majority-White | 12.7 | 9.6 | +3.1 (+1.6 to +6.0) | +33% (+16% to +62%) | 0.0228 | 20% | gap that matters | 6 vs 52 |
| Non-critical | No majority | Majority-White | 10.0 | 9.6 | +0.4 (-0.2 to +1.1) | +4% (-2% to +12%) | 0.799 | 20% | smaller than the smallest gap that matters | 75 vs 52 |
| Not a crime in progress | Majority-Black | Majority-White | 30.4 | 21.0 | +9.4 (+5.2 to +14.3) | +45% (+23% to +71%) | 0.000752 | 20% | gap that matters | 27 vs 52 |
| Not a crime in progress | Majority-Hispanic | Majority-White | 37.6 | 21.0 | +16.6 (+12.0 to +21.9) | +79% (+54% to +109%) | 5.87e-10 | 20% | gap that matters | 37 vs 52 |
| Not a crime in progress | Majority-Asian | Majority-White | 30.6 | 21.0 | +9.6 (+0.0 to +23.6) | +46% (+0% to +115%) | 0.646 | 20% | inconclusive | 6 vs 52 |
| Not a crime in progress | No majority | Majority-White | 22.9 | 21.0 | +1.9 (-1.0 to +4.8) | +9% (-4% to +24%) | 0.799 | 20% | inconclusive | 75 vs 52 |

## Medians and 90th percentiles by group

Minutes. Raw is unweighted; adjusted is reweighted to the citywide call mix.

| Priority | Group | Nbhds | Calls | Median raw | Median adj | P90 raw | P90 adj | To dispatch adj | Dispatch to arrival adj |
|---|---|---|---|---|---|---|---|---|---|
| Critical | Lowest-income fifth | 41 | 80,807 | 5.0 | 5.0 | 16.9 | 17.0 | 1.3 | 3.4 |
| Critical | Second fifth | 36 | 42,994 | 4.7 | 4.7 | 13.1 | 13.1 | 1.1 | 3.3 |
| Critical | Middle fifth | 37 | 43,891 | 4.4 | 4.5 | 12.0 | 12.0 | 1.1 | 3.2 |
| Critical | Fourth fifth | 40 | 31,870 | 4.5 | 4.4 | 10.8 | 10.8 | 1.0 | 3.2 |
| Critical | Highest-income fifth | 43 | 32,687 | 4.1 | 4.1 | 10.6 | 10.5 | 1.0 | 2.9 |
| Serious | Lowest-income fifth | 41 | 153,195 | 6.8 | 6.9 | 29.8 | 30.8 | 1.5 | 4.6 |
| Serious | Second fifth | 36 | 96,202 | 6.3 | 6.3 | 22.1 | 22.5 | 1.3 | 4.6 |
| Serious | Middle fifth | 37 | 107,542 | 6.1 | 6.2 | 20.3 | 20.4 | 1.2 | 4.5 |
| Serious | Fourth fifth | 40 | 85,522 | 6.1 | 6.1 | 18.6 | 18.6 | 1.2 | 4.5 |
| Serious | Highest-income fifth | 43 | 132,826 | 6.1 | 5.9 | 20.4 | 18.8 | 1.1 | 4.4 |
| Non-critical | Lowest-income fifth | 41 | 232,581 | 13.7 | 13.5 | 84.7 | 84.5 | 2.8 | 7.9 |
| Non-critical | Second fifth | 36 | 146,090 | 11.2 | 11.2 | 58.1 | 57.5 | 2.1 | 7.3 |
| Non-critical | Middle fifth | 37 | 155,378 | 10.3 | 10.3 | 50.9 | 50.6 | 2.0 | 6.8 |
| Non-critical | Fourth fifth | 40 | 119,874 | 9.8 | 9.9 | 45.9 | 45.4 | 1.9 | 6.7 |
| Non-critical | Highest-income fifth | 43 | 154,145 | 9.4 | 9.5 | 39.9 | 40.6 | 1.8 | 6.5 |
| Not a crime in progress | Lowest-income fifth | 41 | 1,720,949 | 32.2 | 32.5 | 206.6 | 207.5 | 3.6 | 21.4 |
| Not a crime in progress | Second fifth | 36 | 1,279,166 | 28.6 | 28.1 | 165.2 | 162.5 | 2.9 | 19.8 |
| Not a crime in progress | Middle fifth | 37 | 1,389,786 | 26.2 | 25.6 | 153.0 | 150.8 | 2.7 | 18.0 |
| Not a crime in progress | Fourth fifth | 40 | 1,198,891 | 27.1 | 25.6 | 157.6 | 152.5 | 2.6 | 18.2 |
| Not a crime in progress | Highest-income fifth | 43 | 1,465,685 | 18.8 | 19.2 | 101.2 | 104.3 | 2.2 | 13.5 |
| Critical | Majority-Black | 27 | 44,542 | 4.9 | 4.9 | 14.9 | 14.6 | 1.1 | 3.5 |
| Critical | Majority-Hispanic | 37 | 68,130 | 4.9 | 5.0 | 16.8 | 17.2 | 1.3 | 3.3 |
| Critical | Majority-Asian | 6 | 4,040 | 4.5 | 4.5 | 12.2 | 11.9 | 1.1 | 3.2 |
| Critical | No majority | 75 | 76,556 | 4.4 | 4.4 | 11.6 | 11.6 | 1.0 | 3.2 |
| Critical | Majority-White | 52 | 38,981 | 4.2 | 4.2 | 10.5 | 10.5 | 1.0 | 3.0 |
| Serious | Majority-Black | 27 | 88,109 | 6.8 | 6.8 | 25.5 | 25.9 | 1.4 | 4.9 |
| Serious | Majority-Hispanic | 37 | 132,580 | 6.7 | 6.8 | 29.5 | 30.4 | 1.5 | 4.6 |
| Serious | Majority-Asian | 6 | 10,319 | 6.8 | 6.9 | 23.4 | 23.2 | 1.3 | 5.1 |
| Serious | No majority | 75 | 195,509 | 6.0 | 6.0 | 19.4 | 19.5 | 1.2 | 4.4 |
| Serious | Majority-White | 52 | 148,770 | 6.1 | 6.0 | 20.1 | 18.8 | 1.2 | 4.4 |
| Non-critical | Majority-Black | 27 | 140,356 | 12.4 | 12.3 | 67.9 | 65.4 | 2.4 | 7.7 |
| Non-critical | Majority-Hispanic | 37 | 195,033 | 13.5 | 13.4 | 85.2 | 86.1 | 2.9 | 7.7 |
| Non-critical | Majority-Asian | 6 | 14,861 | 12.9 | 12.7 | 71.2 | 68.0 | 2.3 | 8.3 |
| Non-critical | No majority | 75 | 282,867 | 10.0 | 10.0 | 47.3 | 47.3 | 1.9 | 6.7 |
| Non-critical | Majority-White | 52 | 174,951 | 9.5 | 9.6 | 41.0 | 41.6 | 1.8 | 6.6 |
| Not a crime in progress | Majority-Black | 27 | 1,164,281 | 30.8 | 30.4 | 182.9 | 181.0 | 3.2 | 21.0 |
| Not a crime in progress | Majority-Hispanic | 37 | 1,440,590 | 37.4 | 37.6 | 218.3 | 218.5 | 3.9 | 25.2 |
| Not a crime in progress | Majority-Asian | 6 | 158,584 | 35.6 | 30.6 | 223.2 | 206.5 | 3.3 | 20.3 |
| Not a crime in progress | No majority | 75 | 2,618,713 | 23.2 | 22.9 | 137.2 | 136.1 | 2.5 | 16.1 |
| Not a crime in progress | Majority-White | 52 | 1,672,309 | 20.8 | 21.0 | 113.2 | 115.7 | 2.3 | 14.8 |

## Other gaps (not in the Holm family)

| Priority | Group | Kind | Quantile | Gap (min) | Gap (%) | p |
|---|---|---|---|---|---|---|
| Critical | Lowest-income fifth | adj | 90 | +6.6 (+4.8 to +8.5) | +63% | 4.53e-12 |
| Critical | Lowest-income fifth | raw | 50 | +0.9 (+0.5 to +1.2) | +21% | 5.66e-08 |
| Critical | Lowest-income fifth | raw | 90 | +6.4 (+4.6 to +8.4) | +60% | 3.18e-11 |
| Critical | Second fifth | adj | 50 | +0.5 (+0.2 to +0.9) | +13% | 0.00352 |
| Critical | Second fifth | adj | 90 | +2.6 (+1.2 to +4.1) | +25% | 0.000678 |
| Critical | Second fifth | raw | 50 | +0.6 (+0.2 to +0.9) | +14% | 0.00183 |
| Critical | Second fifth | raw | 90 | +2.5 (+1.0 to +4.0) | +24% | 0.00102 |
| Critical | Middle fifth | adj | 50 | +0.3 (+0.0 to +0.6) | +8% | 0.0328 |
| Critical | Middle fifth | adj | 90 | +1.5 (+0.5 to +2.6) | +15% | 0.00541 |
| Critical | Middle fifth | raw | 50 | +0.3 (+0.1 to +0.6) | +8% | 0.0178 |
| Critical | Middle fifth | raw | 90 | +1.4 (+0.4 to +2.6) | +13% | 0.0101 |
| Critical | Fourth fifth | adj | 50 | +0.3 (+0.0 to +0.6) | +7% | 0.05 |
| Critical | Fourth fifth | adj | 90 | +0.3 (-0.6 to +1.1) | +3% | 0.488 |
| Critical | Fourth fifth | raw | 50 | +0.3 (+0.1 to +0.6) | +8% | 0.0124 |
| Critical | Fourth fifth | raw | 90 | +0.2 (-0.6 to +1.0) | +2% | 0.62 |
| Serious | Lowest-income fifth | adj | 90 | +11.9 (+8.2 to +15.9) | +63% | 1.05e-09 |
| Serious | Lowest-income fifth | raw | 50 | +0.7 (+0.2 to +1.3) | +12% | 0.00661 |
| Serious | Lowest-income fifth | raw | 90 | +9.4 (+5.9 to +13.3) | +46% | 1.43e-06 |
| Serious | Second fifth | adj | 50 | +0.4 (-0.1 to +1.0) | +7% | 0.158 |
| Serious | Second fifth | adj | 90 | +3.6 (+0.5 to +7.0) | +19% | 0.0283 |
| Serious | Second fifth | raw | 50 | +0.2 (-0.4 to +0.8) | +3% | 0.535 |
| Serious | Second fifth | raw | 90 | +1.8 (-1.4 to +5.1) | +9% | 0.303 |
| Serious | Middle fifth | adj | 50 | +0.2 (-0.2 to +0.6) | +4% | 0.259 |
| Serious | Middle fifth | adj | 90 | +1.6 (-0.5 to +3.9) | +8% | 0.161 |
| Serious | Middle fifth | raw | 50 | +0.0 (-0.4 to +0.4) | +0% | 0.976 |
| Serious | Middle fifth | raw | 90 | -0.0 (-2.5 to +2.5) | -0% | 0.976 |
| Serious | Fourth fifth | adj | 50 | +0.2 (-0.2 to +0.6) | +3% | 0.417 |
| Serious | Fourth fifth | adj | 90 | -0.2 (-2.3 to +1.9) | -1% | 0.843 |
| Serious | Fourth fifth | raw | 50 | -0.0 (-0.5 to +0.4) | -1% | 0.831 |
| Serious | Fourth fifth | raw | 90 | -1.7 (-4.2 to +0.7) | -8% | 0.164 |
| Non-critical | Lowest-income fifth | adj | 90 | +43.9 (+32.6 to +55.5) | +108% | 4.57e-14 |
| Non-critical | Lowest-income fifth | raw | 50 | +4.3 (+2.9 to +5.8) | +46% | 1.2e-08 |
| Non-critical | Lowest-income fifth | raw | 90 | +44.8 (+32.8 to +56.5) | +112% | 5.29e-14 |
| Non-critical | Second fifth | adj | 50 | +1.7 (+0.6 to +3.0) | +18% | 0.00619 |
| Non-critical | Second fifth | adj | 90 | +16.9 (+9.3 to +25.9) | +42% | 4.39e-05 |
| Non-critical | Second fifth | raw | 50 | +1.8 (+0.6 to +3.1) | +19% | 0.00525 |
| Non-critical | Second fifth | raw | 90 | +18.2 (+10.4 to +27.1) | +46% | 2.09e-05 |
| Non-critical | Middle fifth | adj | 50 | +0.8 (-0.1 to +1.7) | +9% | 0.0808 |
| Non-critical | Middle fifth | adj | 90 | +10.0 (+4.1 to +16.8) | +25% | 0.00226 |
| Non-critical | Middle fifth | raw | 50 | +0.9 (-0.0 to +1.9) | +9% | 0.0737 |
| Non-critical | Middle fifth | raw | 90 | +11.0 (+5.0 to +18.5) | +27% | 0.00134 |
| Non-critical | Fourth fifth | adj | 50 | +0.4 (-0.3 to +1.2) | +5% | 0.237 |
| Non-critical | Fourth fifth | adj | 90 | +4.8 (+0.6 to +9.3) | +12% | 0.0323 |
| Non-critical | Fourth fifth | raw | 50 | +0.4 (-0.3 to +1.2) | +4% | 0.271 |
| Non-critical | Fourth fifth | raw | 90 | +6.0 (+1.5 to +10.6) | +15% | 0.0107 |
| Not a crime in progress | Lowest-income fifth | adj | 90 | +103.2 (+73.8 to +131.1) | +99% | 2.02e-12 |
| Not a crime in progress | Lowest-income fifth | raw | 50 | +13.4 (+8.8 to +18.8) | +71% | 1.87e-07 |
| Not a crime in progress | Lowest-income fifth | raw | 90 | +105.4 (+76.8 to +133.9) | +104% | 9.93e-13 |
| Not a crime in progress | Second fifth | adj | 50 | +8.8 (+4.8 to +13.1) | +46% | 4e-05 |
| Not a crime in progress | Second fifth | adj | 90 | +58.1 (+37.9 to +79.7) | +56% | 8.98e-08 |
| Not a crime in progress | Second fifth | raw | 50 | +9.8 (+5.6 to +14.5) | +52% | 1.47e-05 |
| Not a crime in progress | Second fifth | raw | 90 | +64.0 (+42.0 to +85.9) | +63% | 1.41e-08 |
| Not a crime in progress | Middle fifth | adj | 50 | +6.4 (+3.2 to +10.1) | +33% | 0.000383 |
| Not a crime in progress | Middle fifth | adj | 90 | +46.4 (+26.9 to +68.4) | +44% | 1.15e-05 |
| Not a crime in progress | Middle fifth | raw | 50 | +7.4 (+4.2 to +11.2) | +40% | 3.53e-05 |
| Not a crime in progress | Middle fifth | raw | 90 | +51.9 (+31.5 to +74.7) | +51% | 1.74e-06 |
| Not a crime in progress | Fourth fifth | adj | 50 | +6.4 (+3.1 to +10.2) | +33% | 0.000551 |
| Not a crime in progress | Fourth fifth | adj | 90 | +48.2 (+28.8 to +70.1) | +46% | 7.92e-06 |
| Not a crime in progress | Fourth fifth | raw | 50 | +8.3 (+4.7 to +12.5) | +44% | 2.49e-05 |
| Not a crime in progress | Fourth fifth | raw | 90 | +56.4 (+35.3 to +78.7) | +56% | 4.14e-07 |
| Critical | Majority-Black | adj | 90 | +4.0 (+2.6 to +5.6) | +38% | 1.2e-07 |
| Critical | Majority-Black | raw | 50 | +0.7 (+0.3 to +1.1) | +17% | 0.000157 |
| Critical | Majority-Black | raw | 90 | +4.4 (+2.9 to +6.0) | +41% | 4.35e-08 |
| Critical | Majority-Hispanic | adj | 90 | +6.7 (+4.6 to +9.0) | +64% | 6.78e-09 |
| Critical | Majority-Hispanic | raw | 50 | +0.7 (+0.3 to +1.0) | +16% | 0.000207 |
| Critical | Majority-Hispanic | raw | 90 | +6.3 (+4.2 to +8.5) | +60% | 2.01e-08 |
| Critical | Majority-Asian | adj | 90 | +1.4 (+0.5 to +2.4) | +13% | 0.00488 |
| Critical | Majority-Asian | raw | 50 | +0.3 (-0.1 to +0.9) | +7% | 0.282 |
| Critical | Majority-Asian | raw | 90 | +1.6 (+0.7 to +2.4) | +16% | 0.000166 |
| Critical | No majority | adj | 90 | +1.0 (+0.2 to +1.9) | +10% | 0.0136 |
| Critical | No majority | raw | 50 | +0.2 (-0.0 to +0.5) | +5% | 0.0866 |
| Critical | No majority | raw | 90 | +1.1 (+0.2 to +1.9) | +10% | 0.0141 |
| Serious | Majority-Black | adj | 90 | +7.1 (+3.5 to +10.7) | +37% | 0.000192 |
| Serious | Majority-Black | raw | 50 | +0.7 (+0.1 to +1.3) | +12% | 0.0172 |
| Serious | Majority-Black | raw | 90 | +5.5 (+2.0 to +9.0) | +27% | 0.00288 |
| Serious | Majority-Hispanic | adj | 90 | +11.6 (+7.5 to +15.9) | +62% | 2.98e-08 |
| Serious | Majority-Hispanic | raw | 50 | +0.6 (+0.1 to +1.2) | +11% | 0.017 |
| Serious | Majority-Hispanic | raw | 90 | +9.4 (+5.7 to +13.7) | +47% | 4.05e-06 |
| Serious | Majority-Asian | adj | 90 | +4.4 (+1.2 to +7.6) | +23% | 0.00753 |
| Serious | Majority-Asian | raw | 50 | +0.7 (-0.1 to +1.6) | +12% | 0.0783 |
| Serious | Majority-Asian | raw | 90 | +3.3 (-0.5 to +7.2) | +16% | 0.0916 |
| Serious | No majority | adj | 90 | +0.7 (-1.2 to +2.6) | +4% | 0.502 |
| Serious | No majority | raw | 50 | -0.1 (-0.4 to +0.3) | -1% | 0.717 |
| Serious | No majority | raw | 90 | -0.7 (-2.8 to +1.8) | -3% | 0.573 |
| Non-critical | Majority-Black | adj | 90 | +23.8 (+15.0 to +34.1) | +57% | 7.2e-07 |
| Non-critical | Majority-Black | raw | 50 | +3.0 (+1.5 to +4.6) | +32% | 0.00012 |
| Non-critical | Majority-Black | raw | 90 | +26.9 (+17.6 to +37.9) | +66% | 2.48e-07 |
| Non-critical | Majority-Hispanic | adj | 90 | +44.5 (+31.1 to +57.0) | +107% | 1.72e-11 |
| Non-critical | Majority-Hispanic | raw | 50 | +4.1 (+2.5 to +5.8) | +43% | 1.84e-06 |
| Non-critical | Majority-Hispanic | raw | 90 | +44.2 (+31.3 to +57.0) | +108% | 2.49e-11 |
| Non-critical | Majority-Asian | adj | 90 | +26.3 (+12.7 to +50.4) | +63% | 0.00347 |
| Non-critical | Majority-Asian | raw | 50 | +3.5 (+1.7 to +6.6) | +37% | 0.00283 |
| Non-critical | Majority-Asian | raw | 90 | +30.2 (+14.8 to +51.9) | +74% | 0.000797 |
| Non-critical | No majority | adj | 90 | +5.7 (+1.1 to +10.5) | +14% | 0.0173 |
| Non-critical | No majority | raw | 50 | +0.5 (-0.2 to +1.2) | +5% | 0.14 |
| Non-critical | No majority | raw | 90 | +6.3 (+1.8 to +10.9) | +15% | 0.00585 |
| Not a crime in progress | Majority-Black | adj | 90 | +65.3 (+39.0 to +94.8) | +56% | 8.59e-06 |
| Not a crime in progress | Majority-Black | raw | 50 | +10.0 (+5.8 to +15.1) | +48% | 2.03e-05 |
| Not a crime in progress | Majority-Black | raw | 90 | +69.7 (+42.3 to +100.9) | +62% | 2.89e-06 |
| Not a crime in progress | Majority-Hispanic | adj | 90 | +102.8 (+75.3 to +131.1) | +89% | 2.09e-13 |
| Not a crime in progress | Majority-Hispanic | raw | 50 | +16.6 (+12.2 to +21.7) | +80% | 8.74e-12 |
| Not a crime in progress | Majority-Hispanic | raw | 90 | +105.0 (+78.0 to +131.1) | +93% | 7.21e-15 |
| Not a crime in progress | Majority-Asian | adj | 90 | +90.8 (+16.6 to +139.1) | +79% | 0.0031 |
| Not a crime in progress | Majority-Asian | raw | 50 | +14.8 (+2.9 to +28.9) | +71% | 0.0268 |
| Not a crime in progress | Majority-Asian | raw | 90 | +110.0 (+37.7 to +154.4) | +97% | 0.000235 |
| Not a crime in progress | No majority | adj | 90 | +20.4 (+3.0 to +37.3) | +18% | 0.0185 |
| Not a crime in progress | No majority | raw | 50 | +2.3 (-0.5 to +5.3) | +11% | 0.115 |
| Not a crime in progress | No majority | raw | 90 | +24.0 (+7.1 to +41.0) | +21% | 0.00617 |

## The two parts of the wait

Adjusted medians, calls with an arrival.

| Priority | Group | Part | Gap (min) | Gap (%) |
|---|---|---|---|---|
| Critical | Lowest-income fifth | to_dispatch | +0.3 (+0.2 to +0.3) | +26% |
| Critical | Second fifth | to_dispatch | +0.1 (+0.0 to +0.1) | +8% |
| Critical | Middle fifth | to_dispatch | +0.1 (+0.0 to +0.1) | +6% |
| Critical | Fourth fifth | to_dispatch | +0.0 (-0.0 to +0.1) | +3% |
| Critical | Lowest-income fifth | travel | +0.4 (+0.1 to +0.7) | +14% |
| Critical | Second fifth | travel | +0.4 (+0.1 to +0.7) | +14% |
| Critical | Middle fifth | travel | +0.2 (-0.0 to +0.5) | +8% |
| Critical | Fourth fifth | travel | +0.3 (-0.0 to +0.5) | +9% |
| Serious | Lowest-income fifth | to_dispatch | +0.4 (+0.3 to +0.5) | +33% |
| Serious | Second fifth | to_dispatch | +0.1 (+0.0 to +0.2) | +10% |
| Serious | Middle fifth | to_dispatch | +0.1 (+0.0 to +0.1) | +6% |
| Serious | Fourth fifth | to_dispatch | +0.0 (-0.0 to +0.1) | +2% |
| Serious | Lowest-income fifth | travel | +0.2 (-0.2 to +0.6) | +5% |
| Serious | Second fifth | travel | +0.2 (-0.2 to +0.7) | +5% |
| Serious | Middle fifth | travel | +0.1 (-0.2 to +0.4) | +3% |
| Serious | Fourth fifth | travel | +0.2 (-0.2 to +0.5) | +4% |
| Non-critical | Lowest-income fifth | to_dispatch | +1.0 (+0.7 to +1.4) | +56% |
| Non-critical | Second fifth | to_dispatch | +0.3 (+0.1 to +0.6) | +19% |
| Non-critical | Middle fifth | to_dispatch | +0.2 (+0.0 to +0.4) | +12% |
| Non-critical | Fourth fifth | to_dispatch | +0.1 (-0.0 to +0.3) | +6% |
| Non-critical | Lowest-income fifth | travel | +1.3 (+0.6 to +2.1) | +20% |
| Non-critical | Second fifth | travel | +0.7 (+0.0 to +1.5) | +11% |
| Non-critical | Middle fifth | travel | +0.3 (-0.3 to +0.9) | +4% |
| Non-critical | Fourth fifth | travel | +0.2 (-0.3 to +0.7) | +3% |
| Not a crime in progress | Lowest-income fifth | to_dispatch | +1.4 (+0.9 to +2.1) | +65% |
| Not a crime in progress | Second fifth | to_dispatch | +0.6 (+0.3 to +1.1) | +29% |
| Not a crime in progress | Middle fifth | to_dispatch | +0.5 (+0.2 to +0.8) | +21% |
| Not a crime in progress | Fourth fifth | to_dispatch | +0.4 (+0.1 to +0.7) | +19% |
| Not a crime in progress | Lowest-income fifth | travel | +7.9 (+4.9 to +11.5) | +59% |
| Not a crime in progress | Second fifth | travel | +6.3 (+3.3 to +9.7) | +46% |
| Not a crime in progress | Middle fifth | travel | +4.5 (+2.3 to +7.3) | +33% |
| Not a crime in progress | Fourth fifth | travel | +4.7 (+2.1 to +7.8) | +35% |
| Critical | Majority-Black | to_dispatch | +0.1 (+0.1 to +0.2) | +11% |
| Critical | Majority-Hispanic | to_dispatch | +0.3 (+0.2 to +0.4) | +28% |
| Critical | Majority-Asian | to_dispatch | +0.0 (-0.0 to +0.1) | +4% |
| Critical | No majority | to_dispatch | +0.0 (-0.0 to +0.1) | +2% |
| Critical | Majority-Black | travel | +0.5 (+0.2 to +0.8) | +16% |
| Critical | Majority-Hispanic | travel | +0.3 (+0.0 to +0.6) | +9% |
| Critical | Majority-Asian | travel | +0.2 (-0.1 to +0.7) | +6% |
| Critical | No majority | travel | +0.2 (-0.1 to +0.4) | +5% |
| Serious | Majority-Black | to_dispatch | +0.2 (+0.1 to +0.3) | +18% |
| Serious | Majority-Hispanic | to_dispatch | +0.4 (+0.2 to +0.5) | +32% |
| Serious | Majority-Asian | to_dispatch | +0.2 (+0.1 to +0.2) | +13% |
| Serious | No majority | to_dispatch | +0.0 (-0.0 to +0.1) | +1% |
| Serious | Majority-Black | travel | +0.5 (+0.1 to +0.9) | +10% |
| Serious | Majority-Hispanic | travel | +0.2 (-0.2 to +0.5) | +4% |
| Serious | Majority-Asian | travel | +0.7 (+0.1 to +1.6) | +15% |
| Serious | No majority | travel | +0.0 (-0.2 to +0.3) | +1% |
| Non-critical | Majority-Black | to_dispatch | +0.6 (+0.3 to +0.9) | +31% |
| Non-critical | Majority-Hispanic | to_dispatch | +1.1 (+0.7 to +1.5) | +58% |
| Non-critical | Majority-Asian | to_dispatch | +0.5 (+0.0 to +0.9) | +25% |
| Non-critical | No majority | to_dispatch | +0.0 (-0.1 to +0.2) | +3% |
| Non-critical | Majority-Black | travel | +1.2 (+0.3 to +1.9) | +18% |
| Non-critical | Majority-Hispanic | travel | +1.2 (+0.4 to +1.9) | +18% |
| Non-critical | Majority-Asian | travel | +1.8 (+1.0 to +3.6) | +27% |
| Non-critical | No majority | travel | +0.2 (-0.3 to +0.6) | +3% |
| Not a crime in progress | Majority-Black | to_dispatch | +0.9 (+0.5 to +1.4) | +39% |
| Not a crime in progress | Majority-Hispanic | to_dispatch | +1.6 (+1.1 to +2.3) | +71% |
| Not a crime in progress | Majority-Asian | to_dispatch | +1.0 (+0.1 to +1.9) | +42% |
| Not a crime in progress | No majority | to_dispatch | +0.2 (-0.1 to +0.4) | +8% |
| Not a crime in progress | Majority-Black | travel | +6.2 (+3.2 to +9.6) | +42% |
| Not a crime in progress | Majority-Hispanic | travel | +10.4 (+7.6 to +13.4) | +70% |
| Not a crime in progress | Majority-Asian | travel | +5.4 (-0.5 to +15.8) | +37% |
| Not a crime in progress | No majority | travel | +1.2 (-1.0 to +3.4) | +8% |

## Calls with no arrival time

| Priority | Group | Calls | No arrival |
|---|---|---|---|
| Critical | Lowest-income fifth | 84,397 | 4.3% (3.4 to 5.6) |
| Critical | Second fifth | 44,747 | 3.9% (2.3 to 6.7) |
| Critical | Middle fifth | 45,272 | 3.0% (2.4 to 3.7) |
| Critical | Fourth fifth | 33,138 | 3.8% (1.9 to 7.6) |
| Critical | Highest-income fifth | 33,727 | 3.1% (2.5 to 3.6) |
| Serious | Lowest-income fifth | 163,663 | 6.4% (5.7 to 7.2) |
| Serious | Second fifth | 101,065 | 4.8% (4.0 to 5.7) |
| Serious | Middle fifth | 112,981 | 4.8% (3.9 to 5.9) |
| Serious | Fourth fifth | 90,521 | 5.5% (3.4 to 8.5) |
| Serious | Highest-income fifth | 143,661 | 7.5% (6.1 to 9.0) |
| Non-critical | Lowest-income fifth | 281,610 | 17.4% (15.9 to 18.9) |
| Non-critical | Second fifth | 166,669 | 12.3% (10.5 to 14.2) |
| Non-critical | Middle fifth | 175,013 | 11.2% (9.6 to 13.2) |
| Non-critical | Fourth fifth | 133,753 | 10.4% (7.8 to 13.4) |
| Non-critical | Highest-income fifth | 186,485 | 17.3% (14.1 to 20.7) |
| Not a crime in progress | Lowest-income fifth | 3,129,427 | 45.0% (43.0 to 46.8) |
| Not a crime in progress | Second fifth | 2,054,408 | 37.7% (35.8 to 39.7) |
| Not a crime in progress | Middle fifth | 2,124,624 | 34.6% (33.0 to 36.2) |
| Not a crime in progress | Fourth fifth | 1,864,132 | 35.7% (32.8 to 39.4) |
| Not a crime in progress | Highest-income fifth | 2,546,736 | 42.4% (39.1 to 46.0) |
| Critical | Majority-Black | 46,579 | 4.4% (2.7 to 7.1) |
| Critical | Majority-Hispanic | 71,173 | 4.3% (3.2 to 5.7) |
| Critical | Majority-Asian | 4,113 | 1.8% (1.1 to 2.6) |
| Critical | No majority | 79,211 | 3.3% (2.4 to 4.9) |
| Critical | Majority-White | 40,205 | 3.0% (2.6 to 3.5) |
| Serious | Majority-Black | 93,144 | 5.4% (4.4 to 6.5) |
| Serious | Majority-Hispanic | 141,082 | 6.0% (5.3 to 6.8) |
| Serious | Majority-Asian | 10,716 | 3.7% (2.7 to 4.3) |
| Serious | No majority | 206,360 | 5.3% (4.1 to 6.6) |
| Serious | Majority-White | 160,589 | 7.4% (5.9 to 8.6) |
| Non-critical | Majority-Black | 161,564 | 13.1% (10.8 to 15.5) |
| Non-critical | Majority-Hispanic | 233,340 | 16.4% (14.6 to 18.2) |
| Non-critical | Majority-Asian | 16,774 | 11.4% (8.2 to 14.8) |
| Non-critical | No majority | 320,859 | 11.8% (10.4 to 13.3) |
| Non-critical | Majority-White | 210,993 | 17.1% (13.6 to 20.2) |
| Not a crime in progress | Majority-Black | 1,842,159 | 36.8% (34.5 to 39.0) |
| Not a crime in progress | Majority-Hispanic | 2,609,788 | 44.8% (42.5 to 47.0) |
| Not a crime in progress | Majority-Asian | 240,171 | 34.0% (30.7 to 39.1) |
| Not a crime in progress | No majority | 4,084,367 | 35.9% (34.4 to 37.3) |
| Not a crime in progress | Majority-White | 2,942,842 | 43.2% (40.0 to 46.2) |

## What narrows a gap

Percent difference in typical minutes against the reference (OLS of log minutes, errors clustered by neighborhood).

### Neighborhood income

| Priority | Controls | Lowest-income fifth | Second fifth | Middle fifth | Fourth fifth |
|---|---|---|---|---|---|
| Critical | No controls | +27% (+19% to +37%) | +15% (+6% to +26%) | +10% (+3% to +18%) | +8% (+2% to +16%) |
| Critical | Call type | +28% (+19% to +37%) | +15% (+6% to +25%) | +10% (+3% to +17%) | +7% (+1% to +13%) |
| Critical | Call type, hour of the week | +27% (+19% to +37%) | +15% (+6% to +25%) | +10% (+4% to +17%) | +7% (+1% to +13%) |
| Critical | Call type, hour of the week, precinct busyness (the plan's controls) | +27% (+19% to +37%) | +15% (+6% to +25%) | +10% (+4% to +17%) | +7% (+1% to +13%) |
| Critical | The plan's controls and distance to the station house | +28% (+21% to +37%) | +14% (+6% to +22%) | +9% (+4% to +15%) | +4% (-0% to +9%) |
| Critical | The plan's controls, distance, and officers per call (2026 snapshot) | +30% (+22% to +38%) | +15% (+7% to +23%) | +10% (+5% to +16%) | +4% (-0% to +9%) |
| Critical | The plan's controls, within the same precinct | -8% (-14% to -2%) | -4% (-10% to +2%) | -2% (-7% to +3%) | -4% (-9% to +0%) |
| Serious | No controls | +20% (+11% to +31%) | +7% (-4% to +18%) | +3% (-4% to +11%) | +1% (-6% to +9%) |
| Serious | Call type | +22% (+13% to +33%) | +9% (-2% to +21%) | +5% (-3% to +13%) | +3% (-5% to +11%) |
| Serious | Call type, hour of the week | +23% (+13% to +33%) | +10% (-1% to +22%) | +5% (-2% to +14%) | +4% (-4% to +12%) |
| Serious | Call type, hour of the week, precinct busyness (the plan's controls) | +23% (+13% to +33%) | +10% (-1% to +22%) | +5% (-2% to +14%) | +4% (-4% to +12%) |
| Serious | The plan's controls and distance to the station house | +22% (+13% to +32%) | +7% (-3% to +18%) | +3% (-4% to +10%) | -0% (-7% to +7%) |
| Serious | The plan's controls, distance, and officers per call (2026 snapshot) | +28% (+20% to +37%) | +11% (+1% to +22%) | +7% (+1% to +14%) | +1% (-5% to +8%) |
| Serious | The plan's controls, within the same precinct | -10% (-16% to -3%) | -5% (-11% to +1%) | -4% (-8% to +1%) | -3% (-8% to +2%) |
| Non-critical | No controls | +54% (+38% to +71%) | +24% (+11% to +39%) | +15% (+5% to +25%) | +9% (+1% to +18%) |
| Non-critical | Call type | +48% (+34% to +65%) | +21% (+8% to +35%) | +12% (+2% to +22%) | +7% (-1% to +15%) |
| Non-critical | Call type, hour of the week | +50% (+35% to +67%) | +22% (+9% to +36%) | +12% (+3% to +23%) | +7% (-1% to +15%) |
| Non-critical | Call type, hour of the week, precinct busyness (the plan's controls) | +50% (+35% to +67%) | +22% (+9% to +36%) | +12% (+3% to +23%) | +7% (-1% to +15%) |
| Non-critical | The plan's controls and distance to the station house | +50% (+35% to +66%) | +20% (+8% to +32%) | +10% (+2% to +20%) | +4% (-3% to +12%) |
| Non-critical | The plan's controls, distance, and officers per call (2026 snapshot) | +57% (+43% to +71%) | +23% (+11% to +36%) | +14% (+6% to +23%) | +4% (-2% to +12%) |
| Non-critical | The plan's controls, within the same precinct | -7% (-14% to -1%) | -2% (-8% to +5%) | -1% (-6% to +5%) | -2% (-8% to +5%) |
| Not a crime in progress | No controls | +66% (+42% to +94%) | +51% (+29% to +77%) | +39% (+21% to +60%) | +47% (+26% to +72%) |
| Not a crime in progress | Call type | +60% (+39% to +83%) | +44% (+26% to +65%) | +33% (+18% to +50%) | +38% (+22% to +56%) |
| Not a crime in progress | Call type, hour of the week | +61% (+40% to +85%) | +44% (+26% to +65%) | +34% (+19% to +51%) | +38% (+22% to +56%) |
| Not a crime in progress | Call type, hour of the week, precinct busyness (the plan's controls) | +61% (+40% to +85%) | +44% (+26% to +65%) | +34% (+19% to +51%) | +38% (+22% to +56%) |
| Not a crime in progress | The plan's controls and distance to the station house | +64% (+45% to +86%) | +41% (+26% to +58%) | +30% (+18% to +44%) | +31% (+18% to +45%) |
| Not a crime in progress | The plan's controls, distance, and officers per call (2026 snapshot) | +73% (+55% to +92%) | +45% (+30% to +61%) | +35% (+23% to +48%) | +30% (+19% to +42%) |
| Not a crime in progress | The plan's controls, within the same precinct | -11% (-18% to -4%) | -5% (-11% to +2%) | -4% (-9% to +2%) | -3% (-8% to +3%) |

### Neighborhood racial and ethnic makeup

| Priority | Controls | Majority-Black | Majority-Hispanic | Majority-Asian | No majority |
|---|---|---|---|---|---|
| Critical | No controls | +22% (+13% to +32%) | +23% (+14% to +34%) | +9% (-2% to +20%) | +6% (+0% to +12%) |
| Critical | Call type | +21% (+12% to +30%) | +25% (+15% to +35%) | +7% (-1% to +16%) | +6% (+0% to +12%) |
| Critical | Call type, hour of the week | +20% (+12% to +30%) | +25% (+16% to +35%) | +7% (-2% to +15%) | +6% (+0% to +11%) |
| Critical | Call type, hour of the week, precinct busyness (the plan's controls) | +20% (+12% to +30%) | +25% (+16% to +35%) | +7% (-2% to +15%) | +6% (+0% to +11%) |
| Critical | The plan's controls and distance to the station house | +18% (+11% to +27%) | +25% (+16% to +35%) | +8% (+3% to +14%) | +5% (+1% to +10%) |
| Critical | The plan's controls, distance, and officers per call (2026 snapshot) | +23% (+15% to +32%) | +28% (+19% to +38%) | +10% (+4% to +16%) | +8% (+3% to +13%) |
| Critical | The plan's controls, within the same precinct | -3% (-8% to +2%) | -6% (-11% to -1%) | -10% (-21% to +4%) | -5% (-9% to -0%) |
| Serious | No controls | +18% (+8% to +30%) | +18% (+9% to +29%) | +11% (+1% to +23%) | +0% (-6% to +7%) |
| Serious | Call type | +19% (+9% to +31%) | +20% (+11% to +31%) | +14% (+4% to +25%) | +1% (-5% to +8%) |
| Serious | Call type, hour of the week | +19% (+9% to +31%) | +21% (+11% to +32%) | +13% (+3% to +25%) | +1% (-5% to +8%) |
| Serious | Call type, hour of the week, precinct busyness (the plan's controls) | +19% (+9% to +31%) | +21% (+11% to +32%) | +13% (+3% to +25%) | +1% (-5% to +8%) |
| Serious | The plan's controls and distance to the station house | +16% (+6% to +27%) | +21% (+11% to +31%) | +15% (+6% to +23%) | +1% (-5% to +7%) |
| Serious | The plan's controls, distance, and officers per call (2026 snapshot) | +26% (+16% to +38%) | +27% (+18% to +38%) | +18% (+9% to +28%) | +6% (-0% to +12%) |
| Serious | The plan's controls, within the same precinct | -2% (-7% to +3%) | -10% (-15% to -4%) | -13% (-25% to +1%) | -7% (-11% to -3%) |
| Non-critical | No controls | +38% (+23% to +55%) | +50% (+33% to +69%) | +41% (+18% to +67%) | +8% (+1% to +16%) |
| Non-critical | Call type | +32% (+17% to +49%) | +45% (+29% to +63%) | +36% (+16% to +61%) | +6% (-1% to +13%) |
| Non-critical | Call type, hour of the week | +32% (+17% to +49%) | +47% (+31% to +66%) | +35% (+15% to +59%) | +6% (-1% to +14%) |
| Non-critical | Call type, hour of the week, precinct busyness (the plan's controls) | +32% (+17% to +49%) | +47% (+31% to +66%) | +35% (+15% to +59%) | +6% (-1% to +14%) |
| Non-critical | The plan's controls and distance to the station house | +29% (+15% to +45%) | +47% (+31% to +65%) | +38% (+20% to +59%) | +5% (-1% to +13%) |
| Non-critical | The plan's controls, distance, and officers per call (2026 snapshot) | +43% (+29% to +59%) | +56% (+39% to +74%) | +42% (+21% to +66%) | +11% (+5% to +19%) |
| Non-critical | The plan's controls, within the same precinct | -2% (-7% to +3%) | -8% (-13% to -2%) | -7% (-19% to +6%) | -6% (-10% to -2%) |
| Not a crime in progress | No controls | +44% (+23% to +69%) | +65% (+44% to +90%) | +66% (+20% to +131%) | +11% (-2% to +27%) |
| Not a crime in progress | Call type | +41% (+22% to +62%) | +61% (+42% to +82%) | +47% (+11% to +96%) | +10% (-2% to +23%) |
| Not a crime in progress | Call type, hour of the week | +42% (+23% to +63%) | +64% (+45% to +85%) | +47% (+11% to +94%) | +10% (-1% to +23%) |
| Not a crime in progress | Call type, hour of the week, precinct busyness (the plan's controls) | +42% (+23% to +63%) | +64% (+45% to +85%) | +47% (+11% to +94%) | +10% (-1% to +23%) |
| Not a crime in progress | The plan's controls and distance to the station house | +37% (+21% to +54%) | +66% (+48% to +85%) | +52% (+20% to +93%) | +10% (+0% to +20%) |
| Not a crime in progress | The plan's controls, distance, and officers per call (2026 snapshot) | +57% (+41% to +75%) | +78% (+60% to +99%) | +57% (+20% to +104%) | +17% (+9% to +27%) |
| Not a crime in progress | The plan's controls, within the same precinct | -5% (-11% to +1%) | -7% (-16% to +2%) | -12% (-23% to +0%) | -9% (-13% to -5%) |

## By period (replication)

| Priority | Group | Period | Quantile | Gap (min) | Gap (%) | Verdict |
|---|---|---|---|---|---|---|
| Critical | Lowest-income fifth | 2022-23 | 50 | +0.8 (+0.5 to +1.1) | +19% | real but smaller than the smallest gap that matters |
| Critical | Second fifth | 2022-23 | 50 | +0.5 (+0.1 to +0.9) | +12% | smaller than the smallest gap that matters |
| Critical | Middle fifth | 2022-23 | 50 | +0.3 (+0.0 to +0.6) | +8% | smaller than the smallest gap that matters |
| Critical | Fourth fifth | 2022-23 | 50 | +0.3 (+0.1 to +0.6) | +8% | smaller than the smallest gap that matters |
| Critical | Lowest-income fifth | 2024-25 | 50 | +0.9 (+0.5 to +1.2) | +20% | real but smaller than the smallest gap that matters |
| Critical | Second fifth | 2024-25 | 50 | +0.5 (+0.2 to +0.9) | +13% | smaller than the smallest gap that matters |
| Critical | Middle fifth | 2024-25 | 50 | +0.3 (+0.0 to +0.7) | +7% | smaller than the smallest gap that matters |
| Critical | Fourth fifth | 2024-25 | 50 | +0.2 (-0.1 to +0.6) | +6% | smaller than the smallest gap that matters |
| Critical | Lowest-income fifth | 2026 holdout | 50 | +1.0 (+0.5 to +1.3) | +23% | real but smaller than the smallest gap that matters |
| Critical | Second fifth | 2026 holdout | 50 | +0.5 (+0.1 to +0.9) | +13% | smaller than the smallest gap that matters |
| Critical | Middle fifth | 2026 holdout | 50 | +0.3 (+0.0 to +0.6) | +7% | smaller than the smallest gap that matters |
| Critical | Fourth fifth | 2026 holdout | 50 | +0.2 (-0.2 to +0.5) | +5% | smaller than the smallest gap that matters |
| Serious | Lowest-income fifth | 2022-23 | 50 | +0.9 (+0.4 to +1.5) | +16% | real but smaller than the smallest gap that matters |
| Serious | Second fifth | 2022-23 | 50 | +0.4 (-0.2 to +0.9) | +6% | smaller than the smallest gap that matters |
| Serious | Middle fifth | 2022-23 | 50 | +0.2 (-0.2 to +0.7) | +4% | smaller than the smallest gap that matters |
| Serious | Fourth fifth | 2022-23 | 50 | +0.1 (-0.3 to +0.6) | +2% | smaller than the smallest gap that matters |
| Serious | Lowest-income fifth | 2024-25 | 50 | +0.9 (+0.5 to +1.5) | +16% | real but smaller than the smallest gap that matters |
| Serious | Second fifth | 2024-25 | 50 | +0.5 (-0.1 to +1.1) | +8% | smaller than the smallest gap that matters |
| Serious | Middle fifth | 2024-25 | 50 | +0.2 (-0.2 to +0.6) | +4% | smaller than the smallest gap that matters |
| Serious | Fourth fifth | 2024-25 | 50 | +0.2 (-0.2 to +0.7) | +4% | smaller than the smallest gap that matters |
| Serious | Lowest-income fifth | 2026 holdout | 50 | +1.1 (+0.5 to +1.6) | +19% | real but smaller than the smallest gap that matters |
| Serious | Second fifth | 2026 holdout | 50 | +0.5 (-0.0 to +1.1) | +9% | smaller than the smallest gap that matters |
| Serious | Middle fifth | 2026 holdout | 50 | +0.2 (-0.1 to +0.6) | +5% | smaller than the smallest gap that matters |
| Serious | Fourth fifth | 2026 holdout | 50 | +0.3 (-0.2 to +0.7) | +5% | smaller than the smallest gap that matters |
| Non-critical | Lowest-income fifth | 2022-23 | 50 | +3.2 (+2.0 to +4.6) | +35% | gap that matters |
| Non-critical | Second fifth | 2022-23 | 50 | +1.5 (+0.4 to +2.9) | +17% | real but smaller than the smallest gap that matters |
| Non-critical | Middle fifth | 2022-23 | 50 | +0.7 (-0.2 to +1.6) | +7% | smaller than the smallest gap that matters |
| Non-critical | Fourth fifth | 2022-23 | 50 | +0.5 (-0.3 to +1.3) | +5% | smaller than the smallest gap that matters |
| Non-critical | Lowest-income fifth | 2024-25 | 50 | +4.8 (+3.0 to +6.7) | +48% | gap that matters |
| Non-critical | Second fifth | 2024-25 | 50 | +1.9 (+0.6 to +3.2) | +19% | real but smaller than the smallest gap that matters |
| Non-critical | Middle fifth | 2024-25 | 50 | +1.0 (+0.1 to +2.0) | +10% | inconclusive |
| Non-critical | Fourth fifth | 2024-25 | 50 | +0.4 (-0.4 to +1.3) | +4% | smaller than the smallest gap that matters |
| Non-critical | Lowest-income fifth | 2026 holdout | 50 | +6.3 (+4.0 to +9.1) | +66% | gap that matters |
| Non-critical | Second fifth | 2026 holdout | 50 | +2.3 (+1.0 to +3.8) | +24% | gap that matters |
| Non-critical | Middle fifth | 2026 holdout | 50 | +0.9 (+0.2 to +1.8) | +10% | smaller than the smallest gap that matters |
| Non-critical | Fourth fifth | 2026 holdout | 50 | +0.5 (-0.3 to +1.3) | +5% | smaller than the smallest gap that matters |
| Not a crime in progress | Lowest-income fifth | 2022-23 | 50 | +12.0 (+7.5 to +17.3) | +64% | gap that matters |
| Not a crime in progress | Second fifth | 2022-23 | 50 | +8.1 (+3.9 to +12.6) | +43% | gap that matters |
| Not a crime in progress | Middle fifth | 2022-23 | 50 | +5.8 (+2.7 to +9.1) | +31% | gap that matters |
| Not a crime in progress | Fourth fifth | 2022-23 | 50 | +6.2 (+2.7 to +10.1) | +33% | gap that matters |
| Not a crime in progress | Lowest-income fifth | 2024-25 | 50 | +14.7 (+9.7 to +21.2) | +75% | gap that matters |
| Not a crime in progress | Second fifth | 2024-25 | 50 | +9.7 (+5.7 to +14.2) | +49% | gap that matters |
| Not a crime in progress | Middle fifth | 2024-25 | 50 | +6.9 (+3.6 to +11.1) | +35% | gap that matters |
| Not a crime in progress | Fourth fifth | 2024-25 | 50 | +6.5 (+3.1 to +10.7) | +33% | gap that matters |
| Not a crime in progress | Lowest-income fifth | 2026 holdout | 50 | +14.3 (+9.2 to +21.1) | +77% | gap that matters |
| Not a crime in progress | Second fifth | 2026 holdout | 50 | +10.4 (+6.3 to +14.8) | +56% | gap that matters |
| Not a crime in progress | Middle fifth | 2026 holdout | 50 | +6.8 (+3.6 to +10.4) | +37% | gap that matters |
| Not a crime in progress | Fourth fifth | 2026 holdout | 50 | +6.8 (+3.4 to +11.2) | +37% | gap that matters |
| Critical | Majority-Black | 2022-23 | 50 | +0.6 (+0.3 to +1.0) | +15% | smaller than the smallest gap that matters |
| Critical | Majority-Hispanic | 2022-23 | 50 | +0.7 (+0.4 to +1.0) | +17% | real but smaller than the smallest gap that matters |
| Critical | Majority-Asian | 2022-23 | 50 | +0.2 (-0.2 to +0.9) | +4% | smaller than the smallest gap that matters |
| Critical | No majority | 2022-23 | 50 | +0.2 (-0.1 to +0.4) | +5% | smaller than the smallest gap that matters |
| Critical | Majority-Black | 2024-25 | 50 | +0.6 (+0.2 to +1.0) | +15% | real but smaller than the smallest gap that matters |
| Critical | Majority-Hispanic | 2024-25 | 50 | +0.7 (+0.3 to +1.1) | +17% | real but smaller than the smallest gap that matters |
| Critical | Majority-Asian | 2024-25 | 50 | +0.2 (-0.1 to +0.9) | +6% | smaller than the smallest gap that matters |
| Critical | No majority | 2024-25 | 50 | +0.2 (-0.1 to +0.4) | +4% | smaller than the smallest gap that matters |
| Critical | Majority-Black | 2026 holdout | 50 | +0.2 (-0.2 to +0.6) | +5% | smaller than the smallest gap that matters |
| Critical | Majority-Hispanic | 2026 holdout | 50 | +0.8 (+0.3 to +1.2) | +18% | real but smaller than the smallest gap that matters |
| Critical | Majority-Asian | 2026 holdout | 50 | -0.3 (-0.7 to +0.7) | -6% | smaller than the smallest gap that matters |
| Critical | No majority | 2026 holdout | 50 | -0.0 (-0.4 to +0.3) | -0% | smaller than the smallest gap that matters |
| Serious | Majority-Black | 2022-23 | 50 | +0.9 (+0.3 to +1.6) | +15% | real but smaller than the smallest gap that matters |
| Serious | Majority-Hispanic | 2022-23 | 50 | +0.9 (+0.3 to +1.4) | +14% | real but smaller than the smallest gap that matters |
| Serious | Majority-Asian | 2022-23 | 50 | +0.8 (+0.2 to +1.8) | +14% | real but smaller than the smallest gap that matters |
| Serious | No majority | 2022-23 | 50 | +0.1 (-0.3 to +0.5) | +1% | smaller than the smallest gap that matters |
| Serious | Majority-Black | 2024-25 | 50 | +0.8 (+0.3 to +1.5) | +14% | real but smaller than the smallest gap that matters |
| Serious | Majority-Hispanic | 2024-25 | 50 | +0.9 (+0.3 to +1.4) | +14% | real but smaller than the smallest gap that matters |
| Serious | Majority-Asian | 2024-25 | 50 | +1.1 (+0.3 to +1.9) | +18% | real but smaller than the smallest gap that matters |
| Serious | No majority | 2024-25 | 50 | +0.1 (-0.3 to +0.5) | +1% | smaller than the smallest gap that matters |
| Serious | Majority-Black | 2026 holdout | 50 | +0.4 (-0.2 to +1.0) | +7% | smaller than the smallest gap that matters |
| Serious | Majority-Hispanic | 2026 holdout | 50 | +1.0 (+0.4 to +1.6) | +18% | real but smaller than the smallest gap that matters |
| Serious | Majority-Asian | 2026 holdout | 50 | +0.2 (-0.3 to +1.0) | +3% | smaller than the smallest gap that matters |
| Serious | No majority | 2026 holdout | 50 | -0.1 (-0.4 to +0.3) | -2% | smaller than the smallest gap that matters |
| Non-critical | Majority-Black | 2022-23 | 50 | +2.7 (+1.3 to +4.3) | +30% | gap that matters |
| Non-critical | Majority-Hispanic | 2022-23 | 50 | +3.0 (+1.5 to +4.4) | +32% | gap that matters |
| Non-critical | Majority-Asian | 2022-23 | 50 | +3.6 (+1.3 to +6.4) | +39% | gap that matters |
| Non-critical | No majority | 2022-23 | 50 | +0.4 (-0.2 to +1.0) | +4% | smaller than the smallest gap that matters |
| Non-critical | Majority-Black | 2024-25 | 50 | +2.6 (+1.1 to +4.4) | +26% | gap that matters |
| Non-critical | Majority-Hispanic | 2024-25 | 50 | +4.9 (+3.0 to +6.9) | +49% | gap that matters |
| Non-critical | Majority-Asian | 2024-25 | 50 | +2.6 (+1.3 to +5.7) | +26% | gap that matters |
| Non-critical | No majority | 2024-25 | 50 | +0.5 (-0.3 to +1.3) | +5% | smaller than the smallest gap that matters |
| Non-critical | Majority-Black | 2026 holdout | 50 | +1.2 (+0.0 to +2.6) | +12% | inconclusive |
| Non-critical | Majority-Hispanic | 2026 holdout | 50 | +7.0 (+4.1 to +10.0) | +70% | gap that matters |
| Non-critical | Majority-Asian | 2026 holdout | 50 | +0.3 (-0.7 to +1.6) | +3% | smaller than the smallest gap that matters |
| Non-critical | No majority | 2026 holdout | 50 | +0.7 (-0.2 to +1.6) | +7% | smaller than the smallest gap that matters |
| Not a crime in progress | Majority-Black | 2022-23 | 50 | +10.4 (+6.3 to +15.0) | +51% | gap that matters |
| Not a crime in progress | Majority-Hispanic | 2022-23 | 50 | +14.9 (+10.7 to +19.6) | +74% | gap that matters |
| Not a crime in progress | Majority-Asian | 2022-23 | 50 | +11.7 (+0.0 to +28.5) | +58% | inconclusive |
| Not a crime in progress | No majority | 2022-23 | 50 | +1.9 (-1.0 to +4.8) | +10% | inconclusive |
| Not a crime in progress | Majority-Black | 2024-25 | 50 | +8.4 (+4.1 to +14.4) | +39% | gap that matters |
| Not a crime in progress | Majority-Hispanic | 2024-25 | 50 | +18.6 (+13.4 to +24.4) | +85% | gap that matters |
| Not a crime in progress | Majority-Asian | 2024-25 | 50 | +7.7 (+0.1 to +19.9) | +35% | inconclusive |
| Not a crime in progress | No majority | 2024-25 | 50 | +1.8 (-1.1 to +4.9) | +8% | inconclusive |
| Not a crime in progress | Majority-Black | 2026 holdout | 50 | +5.4 (+1.3 to +10.0) | +25% | gap that matters |
| Not a crime in progress | Majority-Hispanic | 2026 holdout | 50 | +19.3 (+13.7 to +26.0) | +90% | gap that matters |
| Not a crime in progress | Majority-Asian | 2026 holdout | 50 | +2.1 (-3.5 to +10.0) | +10% | inconclusive |
| Not a crime in progress | No majority | 2026 holdout | 50 | +1.7 (-1.5 to +4.7) | +8% | inconclusive |

## Sensitivity

Adjusted median gaps under other choices.

| Choice | Priority | Group | Gap (min) | Gap (%) |
|---|---|---|---|---|
| every event, including officer-initiated, on-scene and sensor | Critical | Lowest-income fifth | +0.6 (+0.3 to +0.9) | +16% |
| every event, including officer-initiated, on-scene and sensor | Critical | Second fifth | +0.4 (+0.1 to +0.8) | +11% |
| every event, including officer-initiated, on-scene and sensor | Critical | Middle fifth | +0.2 (-0.1 to +0.5) | +6% |
| every event, including officer-initiated, on-scene and sensor | Critical | Fourth fifth | +0.2 (-0.1 to +0.5) | +7% |
| without transit and highway call types | Critical | Lowest-income fifth | +0.8 (+0.5 to +1.2) | +20% |
| without transit and highway call types | Critical | Second fifth | +0.5 (+0.1 to +0.9) | +13% |
| without transit and highway call types | Critical | Middle fifth | +0.3 (+0.0 to +0.6) | +8% |
| without transit and highway call types | Critical | Fourth fifth | +0.3 (-0.0 to +0.6) | +7% |
| busyness relative to the precinct's own average hour | Critical | Lowest-income fifth | +0.8 (+0.5 to +1.2) | +20% |
| busyness relative to the precinct's own average hour | Critical | Second fifth | +0.5 (+0.1 to +0.9) | +13% |
| busyness relative to the precinct's own average hour | Critical | Middle fifth | +0.3 (+0.0 to +0.6) | +8% |
| busyness relative to the precinct's own average hour | Critical | Fourth fifth | +0.3 (+0.0 to +0.6) | +7% |
| calls with no arrival counted as waiting until closed | Critical | Lowest-income fifth | +0.9 (+0.5 to +1.2) | +20% |
| calls with no arrival counted as waiting until closed | Critical | Second fifth | +0.5 (+0.2 to +0.9) | +13% |
| calls with no arrival counted as waiting until closed | Critical | Middle fifth | +0.3 (+0.0 to +0.6) | +8% |
| calls with no arrival counted as waiting until closed | Critical | Fourth fifth | +0.2 (-0.1 to +0.6) | +6% |
| every event, including officer-initiated, on-scene and sensor | Serious | Lowest-income fifth | +0.9 (+0.4 to +1.5) | +16% |
| every event, including officer-initiated, on-scene and sensor | Serious | Second fifth | +0.4 (-0.1 to +1.0) | +7% |
| every event, including officer-initiated, on-scene and sensor | Serious | Middle fifth | +0.2 (-0.1 to +0.6) | +4% |
| every event, including officer-initiated, on-scene and sensor | Serious | Fourth fifth | +0.2 (-0.2 to +0.6) | +3% |
| without transit and highway call types | Serious | Lowest-income fifth | +1.0 (+0.5 to +1.5) | +16% |
| without transit and highway call types | Serious | Second fifth | +0.4 (-0.1 to +1.0) | +7% |
| without transit and highway call types | Serious | Middle fifth | +0.2 (-0.2 to +0.6) | +4% |
| without transit and highway call types | Serious | Fourth fifth | +0.1 (-0.2 to +0.6) | +3% |
| busyness relative to the precinct's own average hour | Serious | Lowest-income fifth | +0.9 (+0.5 to +1.5) | +16% |
| busyness relative to the precinct's own average hour | Serious | Second fifth | +0.4 (-0.1 to +1.0) | +7% |
| busyness relative to the precinct's own average hour | Serious | Middle fifth | +0.2 (-0.2 to +0.7) | +4% |
| busyness relative to the precinct's own average hour | Serious | Fourth fifth | +0.2 (-0.2 to +0.6) | +3% |
| calls with no arrival counted as waiting until closed | Serious | Lowest-income fifth | +1.1 (+0.6 to +1.7) | +18% |
| calls with no arrival counted as waiting until closed | Serious | Second fifth | +0.4 (-0.2 to +1.0) | +6% |
| calls with no arrival counted as waiting until closed | Serious | Middle fifth | +0.2 (-0.2 to +0.6) | +3% |
| calls with no arrival counted as waiting until closed | Serious | Fourth fifth | +0.1 (-0.4 to +0.5) | +1% |
| every event, including officer-initiated, on-scene and sensor | Non-critical | Lowest-income fifth | +3.8 (+2.5 to +5.3) | +42% |
| every event, including officer-initiated, on-scene and sensor | Non-critical | Second fifth | +1.7 (+0.6 to +3.0) | +19% |
| every event, including officer-initiated, on-scene and sensor | Non-critical | Middle fifth | +0.8 (-0.0 to +1.8) | +9% |
| every event, including officer-initiated, on-scene and sensor | Non-critical | Fourth fifth | +0.4 (-0.4 to +1.2) | +4% |
| without transit and highway call types | Non-critical | Lowest-income fifth | +4.1 (+2.6 to +5.8) | +44% |
| without transit and highway call types | Non-critical | Second fifth | +1.7 (+0.4 to +3.0) | +18% |
| without transit and highway call types | Non-critical | Middle fifth | +0.7 (-0.2 to +1.7) | +8% |
| without transit and highway call types | Non-critical | Fourth fifth | +0.3 (-0.4 to +1.1) | +3% |
| busyness relative to the precinct's own average hour | Non-critical | Lowest-income fifth | +4.0 (+2.6 to +5.5) | +42% |
| busyness relative to the precinct's own average hour | Non-critical | Second fifth | +1.7 (+0.6 to +3.0) | +18% |
| busyness relative to the precinct's own average hour | Non-critical | Middle fifth | +0.8 (-0.1 to +1.7) | +9% |
| busyness relative to the precinct's own average hour | Non-critical | Fourth fifth | +0.4 (-0.3 to +1.2) | +5% |
| calls with no arrival counted as waiting until closed | Non-critical | Lowest-income fifth | +5.5 (+3.6 to +7.7) | +51% |
| calls with no arrival counted as waiting until closed | Non-critical | Second fifth | +1.7 (+0.3 to +3.5) | +16% |
| calls with no arrival counted as waiting until closed | Non-critical | Middle fifth | +0.5 (-0.6 to +1.7) | +5% |
| calls with no arrival counted as waiting until closed | Non-critical | Fourth fifth | +0.0 (-0.9 to +1.0) | +0% |
| every event, including officer-initiated, on-scene and sensor | Not a crime in progress | Lowest-income fifth | +4.9 (+1.8 to +8.7) | +47% |
| every event, including officer-initiated, on-scene and sensor | Not a crime in progress | Second fifth | +3.9 (+0.8 to +7.5) | +36% |
| every event, including officer-initiated, on-scene and sensor | Not a crime in progress | Middle fifth | +2.8 (+0.2 to +5.7) | +27% |
| every event, including officer-initiated, on-scene and sensor | Not a crime in progress | Fourth fifth | +2.9 (-0.3 to +6.6) | +28% |
| without transit and highway call types | Not a crime in progress | Lowest-income fifth | +15.1 (+10.0 to +21.1) | +77% |
| without transit and highway call types | Not a crime in progress | Second fifth | +9.7 (+5.4 to +14.3) | +50% |
| without transit and highway call types | Not a crime in progress | Middle fifth | +6.9 (+3.6 to +10.8) | +35% |
| without transit and highway call types | Not a crime in progress | Fourth fifth | +6.8 (+3.1 to +11.1) | +35% |
| busyness relative to the precinct's own average hour | Not a crime in progress | Lowest-income fifth | +13.3 (+8.8 to +19.0) | +69% |
| busyness relative to the precinct's own average hour | Not a crime in progress | Second fifth | +8.8 (+4.9 to +13.3) | +46% |
| busyness relative to the precinct's own average hour | Not a crime in progress | Middle fifth | +6.4 (+3.2 to +10.1) | +33% |
| busyness relative to the precinct's own average hour | Not a crime in progress | Fourth fifth | +6.4 (+3.0 to +10.3) | +33% |
| calls with no arrival counted as waiting until closed | Not a crime in progress | Lowest-income fifth | +20.8 (+13.9 to +28.6) | +73% |
| calls with no arrival counted as waiting until closed | Not a crime in progress | Second fifth | +9.9 (+5.3 to +15.1) | +35% |
| calls with no arrival counted as waiting until closed | Not a crime in progress | Middle fifth | +6.2 (+2.3 to +10.8) | +22% |
| calls with no arrival counted as waiting until closed | Not a crime in progress | Fourth fifth | +6.1 (+2.0 to +11.0) | +22% |
| every event, including officer-initiated, on-scene and sensor | Critical | Majority-Black | +0.5 (+0.1 to +0.8) | +12% |
| every event, including officer-initiated, on-scene and sensor | Critical | Majority-Hispanic | +0.5 (+0.2 to +0.9) | +13% |
| every event, including officer-initiated, on-scene and sensor | Critical | Majority-Asian | +0.4 (-0.1 to +1.1) | +10% |
| every event, including officer-initiated, on-scene and sensor | Critical | No majority | +0.1 (-0.2 to +0.4) | +3% |
| without transit and highway call types | Critical | Majority-Black | +0.6 (+0.3 to +1.0) | +15% |
| without transit and highway call types | Critical | Majority-Hispanic | +0.7 (+0.3 to +1.1) | +17% |
| without transit and highway call types | Critical | Majority-Asian | +0.2 (-0.2 to +0.9) | +5% |
| without transit and highway call types | Critical | No majority | +0.2 (-0.1 to +0.5) | +5% |
| busyness relative to the precinct's own average hour | Critical | Majority-Black | +0.6 (+0.3 to +1.0) | +15% |
| busyness relative to the precinct's own average hour | Critical | Majority-Hispanic | +0.7 (+0.4 to +1.1) | +17% |
| busyness relative to the precinct's own average hour | Critical | Majority-Asian | +0.2 (-0.1 to +0.9) | +5% |
| busyness relative to the precinct's own average hour | Critical | No majority | +0.2 (-0.1 to +0.4) | +5% |
| calls with no arrival counted as waiting until closed | Critical | Majority-Black | +0.6 (+0.3 to +1.0) | +15% |
| calls with no arrival counted as waiting until closed | Critical | Majority-Hispanic | +0.7 (+0.4 to +1.1) | +17% |
| calls with no arrival counted as waiting until closed | Critical | Majority-Asian | +0.2 (-0.2 to +0.8) | +5% |
| calls with no arrival counted as waiting until closed | Critical | No majority | +0.2 (-0.1 to +0.4) | +4% |
| every event, including officer-initiated, on-scene and sensor | Serious | Majority-Black | +0.9 (+0.3 to +1.5) | +14% |
| every event, including officer-initiated, on-scene and sensor | Serious | Majority-Hispanic | +0.8 (+0.3 to +1.4) | +14% |
| every event, including officer-initiated, on-scene and sensor | Serious | Majority-Asian | +0.9 (+0.3 to +1.8) | +16% |
| every event, including officer-initiated, on-scene and sensor | Serious | No majority | +0.1 (-0.3 to +0.4) | +1% |
| without transit and highway call types | Serious | Majority-Black | +0.9 (+0.3 to +1.5) | +14% |
| without transit and highway call types | Serious | Majority-Hispanic | +0.9 (+0.4 to +1.4) | +14% |
| without transit and highway call types | Serious | Majority-Asian | +1.0 (+0.3 to +1.8) | +16% |
| without transit and highway call types | Serious | No majority | +0.1 (-0.3 to +0.4) | +1% |
| busyness relative to the precinct's own average hour | Serious | Majority-Black | +0.9 (+0.3 to +1.5) | +14% |
| busyness relative to the precinct's own average hour | Serious | Majority-Hispanic | +0.9 (+0.4 to +1.4) | +14% |
| busyness relative to the precinct's own average hour | Serious | Majority-Asian | +1.0 (+0.3 to +1.7) | +16% |
| busyness relative to the precinct's own average hour | Serious | No majority | +0.1 (-0.3 to +0.4) | +1% |
| calls with no arrival counted as waiting until closed | Serious | Majority-Black | +0.9 (+0.3 to +1.7) | +15% |
| calls with no arrival counted as waiting until closed | Serious | Majority-Hispanic | +1.0 (+0.4 to +1.6) | +16% |
| calls with no arrival counted as waiting until closed | Serious | Majority-Asian | +0.9 (+0.2 to +1.6) | +14% |
| calls with no arrival counted as waiting until closed | Serious | No majority | -0.0 (-0.4 to +0.4) | -0% |
| every event, including officer-initiated, on-scene and sensor | Non-critical | Majority-Black | +2.5 (+1.1 to +3.9) | +26% |
| every event, including officer-initiated, on-scene and sensor | Non-critical | Majority-Hispanic | +3.7 (+2.2 to +5.4) | +40% |
| every event, including officer-initiated, on-scene and sensor | Non-critical | Majority-Asian | +3.1 (+1.7 to +6.3) | +34% |
| every event, including officer-initiated, on-scene and sensor | Non-critical | No majority | +0.5 (-0.2 to +1.1) | +5% |
| without transit and highway call types | Non-critical | Majority-Black | +2.7 (+1.2 to +4.3) | +28% |
| without transit and highway call types | Non-critical | Majority-Hispanic | +4.0 (+2.3 to +6.0) | +42% |
| without transit and highway call types | Non-critical | Majority-Asian | +3.2 (+1.2 to +6.2) | +34% |
| without transit and highway call types | Non-critical | No majority | +0.4 (-0.3 to +1.1) | +4% |
| busyness relative to the precinct's own average hour | Non-critical | Majority-Black | +2.7 (+1.3 to +4.3) | +28% |
| busyness relative to the precinct's own average hour | Non-critical | Majority-Hispanic | +3.9 (+2.2 to +5.5) | +40% |
| busyness relative to the precinct's own average hour | Non-critical | Majority-Asian | +3.1 (+1.6 to +6.1) | +33% |
| busyness relative to the precinct's own average hour | Non-critical | No majority | +0.4 (-0.2 to +1.1) | +4% |
| calls with no arrival counted as waiting until closed | Non-critical | Majority-Black | +3.1 (+1.2 to +5.0) | +28% |
| calls with no arrival counted as waiting until closed | Non-critical | Majority-Hispanic | +5.2 (+2.9 to +7.7) | +47% |
| calls with no arrival counted as waiting until closed | Non-critical | Majority-Asian | +3.0 (+1.8 to +5.5) | +27% |
| calls with no arrival counted as waiting until closed | Non-critical | No majority | +0.1 (-0.8 to +1.1) | +1% |
| every event, including officer-initiated, on-scene and sensor | Not a crime in progress | Majority-Black | +4.1 (+0.9 to +8.6) | +36% |
| every event, including officer-initiated, on-scene and sensor | Not a crime in progress | Majority-Hispanic | +6.3 (+3.2 to +10.1) | +56% |
| every event, including officer-initiated, on-scene and sensor | Not a crime in progress | Majority-Asian | +3.7 (-1.2 to +20.9) | +33% |
| every event, including officer-initiated, on-scene and sensor | Not a crime in progress | No majority | +0.7 (-1.7 to +3.3) | +6% |
| without transit and highway call types | Not a crime in progress | Majority-Black | +10.5 (+6.0 to +16.0) | +49% |
| without transit and highway call types | Not a crime in progress | Majority-Hispanic | +18.8 (+14.0 to +24.1) | +88% |
| without transit and highway call types | Not a crime in progress | Majority-Asian | +10.2 (-0.2 to +22.9) | +48% |
| without transit and highway call types | Not a crime in progress | No majority | +2.0 (-1.0 to +5.1) | +9% |
| busyness relative to the precinct's own average hour | Not a crime in progress | Majority-Black | +9.4 (+5.3 to +14.3) | +45% |
| busyness relative to the precinct's own average hour | Not a crime in progress | Majority-Hispanic | +16.6 (+12.0 to +21.6) | +79% |
| busyness relative to the precinct's own average hour | Not a crime in progress | Majority-Asian | +9.6 (+0.2 to +23.7) | +46% |
| busyness relative to the precinct's own average hour | Not a crime in progress | No majority | +1.9 (-0.8 to +4.8) | +9% |
| calls with no arrival counted as waiting until closed | Not a crime in progress | Majority-Black | +11.5 (+6.3 to +17.9) | +38% |
| calls with no arrival counted as waiting until closed | Not a crime in progress | Majority-Hispanic | +23.6 (+17.1 to +30.7) | +78% |
| calls with no arrival counted as waiting until closed | Not a crime in progress | Majority-Asian | +9.0 (+0.5 to +20.8) | +30% |
| calls with no arrival counted as waiting until closed | Not a crime in progress | No majority | +1.7 (-1.4 to +4.9) | +6% |

## Continuous measures

Percent difference in typical minutes per 10 points of a group's share of residents, or per $25,000 lower median household income, with the plan's controls.

| Priority | Term | Difference |
|---|---|---|
| Critical | hispanic | +3% (+2% to +5%) |
| Critical | black | +4% (+2% to +5%) |
| Critical | asian | +2% (+0% to +4%) |
| Critical | income_25k_lower | +1% (-0% to +3%) |
| Serious | hispanic | +4% (+3% to +7%) |
| Serious | black | +5% (+3% to +7%) |
| Serious | asian | +4% (+2% to +6%) |
| Serious | income_25k_lower | -1% (-3% to +1%) |
| Non-critical | hispanic | +7% (+4% to +10%) |
| Non-critical | black | +6% (+4% to +9%) |
| Non-critical | asian | +4% (+1% to +7%) |
| Non-critical | income_25k_lower | +0% (-2% to +3%) |
| Not a crime in progress | hispanic | +8% (+5% to +11%) |
| Not a crime in progress | black | +6% (+3% to +9%) |
| Not a crime in progress | asian | +8% (+4% to +12%) |
| Not a crime in progress | income_25k_lower | +2% (-1% to +6%) |
