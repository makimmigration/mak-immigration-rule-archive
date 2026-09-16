# Permanent-Resident Admissions with Prior PGWP Holder Status: Descriptive Tables, 2015–2025

Version: 1.0  
Published: 2026-09-16  
Publisher: MAK Canadian Immigration Services · Immigration Data Observatory  
Evidence basis: IRCC Open Data workbook `EN_ODP-TR_to_PR-PGWP_PT_immcat.xlsx`, source line `IRCC, June 30, 2026`  

## Purpose

This data note provides citation-ready descriptive tables for permanent-resident admissions involving people with **prior Post-graduate Work Permit Holder status**. It is designed for researchers, journalists and policy analysts who need a bounded, reproducible summary of the public IRCC series without turning admissions counts into transition probabilities.

This is **not** a cohort conversion-rate study, an approval-rate report, or a causal evaluation of immigration policy. The source does not provide the denominator or individual-level linkage required to estimate the probability that a PGWP holder becomes a permanent resident.

## Controlling source and reproducibility identity

IRCC source workbook:  
https://www.ircc.canada.ca/opendata-donneesouvertes/data/EN_ODP-TR_to_PR-PGWP_PT_immcat.xlsx

Source workbook SHA-256:  
`01aba963e8453635e6e4389e3b839def143152d5bbc67be6fe2fdf842dec5a5f`

MAK Observatory normalized source file:  
`normalized/IRCC_TR_TO_PR_PGWP-01aba963e8453635.csv`

Public Release 2 build provenance:
- GitHub Actions run `34348424967`
- artifact `10102678399`
- artifact digest `sha256:914ab2f505a0aedea5d4da0f08f53beb0a7dcc54010824c521b8035ee9770a80`

The workbook states that small values are shown as `--` for privacy protection, other values are rounded to the nearest multiple of 5, totals may therefore not add exactly, and the data are preliminary estimates subject to change.

## National annual totals

These figures use the workbook's own national **Total** row. They are not reconstructed by summing province/category cells.

| Year | PR admissions with prior PGWP holder status |
|---|---:|
| 2015 | 10,215 |
| 2016 | 10,995 |
| 2017 | 18,765 |
| 2018 | 24,535 |
| 2019 | 27,515 |
| 2020 | 19,395 |
| 2021 | 88,430 |
| 2022 | 52,735 |
| 2023 | 67,875 |
| 2024 | 61,475 |
| 2025 | 49,985 |

The same workbook reports **24,865** for January–June 2026. That is a partial-year observation and must not be compared with the full-year values above as though it were a complete 2026 total.

## Published-visible program mix

The figures below sum the **published annual province/territory category cells** for selected immigration categories. Where one or more source cells are `--`, the visible sum is a **published-visible minimum**, not an exact national category total. Suppressed cells are never replaced with zero.

| Year | Canadian Experience | Provincial Nominee Program total | TR-to-PR Pathway total | Economic total |
|---|---:|---:|---:|---:|
| 2019 | 11,115 + suppressed cells | 10,750 + suppressed cells | 0 | 25,715 + suppressed cells |
| 2020 | 9,145 + suppressed cells | 6,445 | 0 | 18,210 + suppressed cells |
| 2021 | 52,970 + suppressed cells | 8,100 | 17,050 + suppressed cells | 85,335 |
| 2022 | 8,640 + suppressed cells | 8,755 | 22,725 + suppressed cells | 49,670 + suppressed cells |
| 2023 | 17,110 + suppressed cells | 20,730 | 17,240 + suppressed cells | 62,935 + suppressed cells |
| 2024 | 20,080 + suppressed cells | 26,175 | 1,045 | 57,270 + suppressed cells |
| 2025 | 18,345 | 17,305 | 30 + suppressed cells | 47,550 |

This table can describe changes in the **published composition of admissions**. It cannot establish why the mix changed, how many applicants were refused, or an individual's chance of transitioning to permanent residence.

## 2025 province/territory of intended destination

These are the source workbook's annual province/territory totals for 2025. `Province/Territory of Intended Destination` must not be relabelled as current residence or long-term settlement location.

| Intended destination | 2025 total |
|---|---:|
| Ontario | 23,125 |
| Quebec | 9,335 |
| British Columbia | 7,510 |
| Alberta | 2,900 |
| Manitoba | 1,815 |
| New Brunswick | 1,610 |
| Nova Scotia | 1,490 |
| Saskatchewan | 1,190 |
| Newfoundland and Labrador | 475 |
| Prince Edward Island | 360 |
| Northwest Territories | 95 |
| Yukon | 75 |
| Nunavut | 5 |
| **Canada total** | **49,985** |

The listed province/territory totals sum to the source national 2025 total of 49,985.

## Interpretation safeguards

When reusing this note:

1. Use the workbook's own national Total row for annual national totals where available.
2. Never replace `--` with zero.
3. Never impute suppressed values without a separately disclosed and professionally reviewed methodology that preserves disclosure controls.
4. Do not add the separate `prior study permit` and `prior PGWP` datasets as though they were mutually exclusive populations; overlap has not been ruled out here.
5. Do not describe these admissions as `PGWP holders who became PR at a rate of X%`; this source does not supply the cohort denominator or individual-level transition linkage required for a conversion rate.
6. Do not describe category movements as approval rates, success rates, processing times, applicant demand, or causal policy effects.
7. Preserve the source concept **prior Post-graduate Work Permit Holder status** when precision matters.
8. Treat January–June 2026 separately from full calendar years.
9. Recheck the current IRCC source before using this historical snapshot for a time-sensitive claim.

## Machine-readable companion

Long-form CSV: [`pgwp-pr-admissions-descriptive-tables-2015-2025-v1.0.csv`](pgwp-pr-admissions-descriptive-tables-2015-2025-v1.0.csv)

Human-readable web view: [`pgwp-pr-admissions-descriptive-tables-2015-2025-v1.0.html`](pgwp-pr-admissions-descriptive-tables-2015-2025-v1.0.html)

The CSV keeps source-table type, period, geography, metric, value, suppression status and interpretation note separate so downstream users do not have to infer whether a number is an exact source total or a published-visible minimum.

## Suggested citation

MAK Canadian Immigration Services, Immigration Data Observatory. *Permanent-Resident Admissions with Prior PGWP Holder Status: Descriptive Tables, 2015–2025*. Version 1.0, September 16, 2026. Derived from IRCC Open Data workbook `EN_ODP-TR_to_PR-PGWP_PT_immcat.xlsx` (source line: IRCC, June 30, 2026).

## Reuse boundary

This is a descriptive data note, not legal advice and not a journal manuscript. IRCC's source workbook remains the controlling source for the underlying administrative data. The note is intentionally non-causal and does not estimate individual immigration outcomes.