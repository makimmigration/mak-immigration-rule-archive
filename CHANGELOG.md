# Version history

## v0.3.0 — 2026-09-13

Expanded verified public-policy coverage with the Manitoba Workforce Transition Bridge.

### Added

- Added `ca-manitoba-workforce-transition-bridge-2026-07-06`, controlled by IRCC's signed A25.2 Manitoba Workforce Transition Bridge public policy.
- Recorded the legal effective date as July 6, 2026 because the policy states it comes into effect on the date signed and is dated July 6, 2026.
- Recorded the policy expiry as December 31, 2027 unless revoked earlier.
- Preserved the defined cohort and evidence controls: Manitoba support letter issued on or before December 31, 2025, MPNP EOI placement on or before December 31, 2025, and a letter of employment from the current employer.
- Preserved the distinct restoration/work-authorization situations in the policy rather than reducing them to a generic 'all Manitoba workers qualify' rule.
- Added IRCC's operational support-letter page as supporting evidence, including the current statement that the resulting open work permit may be issued for up to two years and that the measure is not for applicants already nominated by a province or territory.

### Date treatment

- `announcement_date` is left `null`: the signed policy and later Canada.ca publication pages establish the policy/effective dates, but this archive does not infer a separate announcement date.
- `rule_observed_from` is 2026-07-06 because the signed policy itself establishes the rule from that date.
- `effective_from` is 2026-07-06.
- `effective_to` is 2027-12-31.
- No unsupported supersession relationship is asserted with the archived 2024 prospective-PNP public policy; the 2026 policy expressly builds on an earlier measure but defines a new Manitoba-specific cohort and conditions.

## v0.2.0 — 2026-09-11

Expanded verified coverage to Saskatchewan SINP.

### Added

- Added `sk-sinp-capped-sector-final-intake-2026-09-14`: current SINP Processing Statistics and OASIS pages state that September 14–15 is the final 2026 capped-sector intake, with nomination spaces previously allocated for later intakes moved into September.
- Recorded sector windows and limits: Trucking 150 and Retail 175 at 9:30 a.m. September 14; Accommodation 50 at 1:30 p.m. September 14; Food Services 175 at 1:30 p.m. September 15.
- Preserved filing constraints: active intake window only, six months or less remaining on a valid work permit, first-come first-served, with OASIS indicating out-of-window EPAs or cases with more than six months remaining will be closed and returned.

### Date treatment

- `announcement_date` remains `null` because the current official pages do not state when this schedule revision was first published.
- `rule_observed_from` is 2026-09-11, the date this archive verified the current official rule state.
- `effective_from` remains `null`; September 14–15 are operational intake dates, not asserted by the archive as a separate change-effective date.
- No supersession link is created because the prior intake schedule is not independently archived with a defensible end date.

## v0.1.0 — 2026-09-11

First public seed release of the MAK Canadian Immigration Rule Change Archive.

### Added

- Search-by-date and topic interface.
- Canonical machine-readable `events.json` archive.
- Flat `events.csv` export.
- Explicit announcement / observed / effective date separation.
- Explicit `effective_to`, `supersedes_event_id` and `superseded_by_event_id` preservation model.
- Controlling and supporting official-source fields.
- Transition-rule and previous-rule context fields.
- Methodology and historical-preservation policy.

### Seed events

1. PGWP eligibility changes for applications on or after 2024-11-01.
2. Family OWP restriction for spouses of international students effective 2025-01-21.
3. Family OWP restriction for spouses of foreign workers effective 2025-01-21.
4. Removal of Express Entry arranged-employment CRS points effective 2025-03-25.
5. PGWP field-of-study list update effective 2025-06-25.
6. Restoration of removed PGWP fields on 2025-07-04.
7. Official 2026 Express Entry category-based selection update published 2026-02-18, with no separate effective date asserted by this archive.
8. Targeted SIP spouse OWP eligibility from 2026-03-23.
9. Selected Quebec PSTQ spouse/common-law OWP measure from 2026-06-05 through 2026-12-31.

### Material update — 2026-09-11

- Added `ca-work-permit-short-study-2026-09-04`: IRCC's temporary public policy for valid work permit holders to study in a course or program lasting six months or less without a study permit. The signed policy was dated 2026-08-05, came into effect 2026-09-04, was publicly announced/observed on 2026-09-09, and expires 2027-12-31 unless revoked earlier. The controlling source is IRCC's signed temporary public policy under A25.2 exempting the R188(1)(c) completion-within-authorized-stay requirement for eligible permit holders.

### Coverage warning

v0.1.0 is a seed archive, not a complete historical reconstruction. Missing results must not be interpreted to mean that no rule existed.
