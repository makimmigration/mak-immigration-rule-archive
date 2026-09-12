# Version history

## v0.5.0 — 2026-09-13

Added three archived predecessor public policies and converted three previously descriptive replacement statements into explicit machine-readable supersession chains.

### Added

- `ca-quebec-pstq-work-permit-public-policy-2026-03-13`: archived the March 12-signed / March 13-effective Quebec PSTQ employer-specific work-permit public policy that preceded the June 5 replacement.
- `ca-fmcsp-study-permit-policy-2025-09-18`: archived the September 18, 2025 FMCSP study-permit public policy, including its annual processing caps and treatment of pending applications under the August 2024 predecessor.
- `ca-fmcsp-pr-policy-2025-09-18`: archived the September 18, 2025 FMCSP permanent-residence/open-work-permit public policy.

### Supersession chains

- Quebec PSTQ: `ca-quebec-pstq-work-permit-public-policy-2026-03-13` -> `ca-quebec-pstq-work-permit-public-policy-2026-06-05`.
- FMCSP study: `ca-fmcsp-study-permit-policy-2025-09-18` -> `ca-fmcsp-study-permit-policy-2026-06-25`.
- FMCSP PR/OWP: `ca-fmcsp-pr-policy-2025-09-18` -> `ca-fmcsp-pr-owp-policy-2026-06-25`.

### Source-quality control

The archived 2025 FMCSP PR policy prints `November 31, 2031` as its nominal expiry. Because that is not a valid calendar date, this archive does not silently normalize it. The event records the source anomaly and uses the verified June 25, 2026 successor to bound the predecessor's historical active state through June 24, 2026.

## v0.4.0 — 2026-09-13

Expanded the archive with five additional official-source public-policy records and historical transition states.

### Added

- `ca-worker-study-exemption-2023-06-27`: preserved IRCC's 2023 worker-study public policy as an expired historical rule state. The policy took effect June 27, 2023, required the relevant work-permit application or renewal to have been received on or before June 7, 2023, and expired June 27, 2026.
- `ca-construction-apprentice-study-exemption-2025-02-26`: added the current construction-trade apprentice study-without-study-permit measure. IRCC states it started February 26, 2025 and remains open through February 26, 2027; applicants must have a valid work permit, an eligible construction occupation and a registered apprenticeship agreement.
- `ca-quebec-pstq-work-permit-public-policy-2026-06-05`: added the signed Quebec PSTQ prospective-permanent-residence work-permit public policy, including the principal-worker cohorts, spouse/common-law-partner facilitation and the explicit replacement of the March 12, 2026 predecessor.
- `ca-fmcsp-study-permit-policy-2026-06-25`: added the updated Francophone Minority Communities Student Pilot study-permit public policy. The archive preserves the June 25, 2026 effective date, Part A's August 25, 2027 expiry, Parts B/C linkage to the November 30, 2032 companion-policy expiry, and the two annual 2,970-application Part A caps.
- `ca-fmcsp-pr-owp-policy-2026-06-25`: added the updated FMCSP permanent-residence/open-work-permit public policy, including the qualifying graduate framework, pending-PR open-work-permit facilitation, accompanying-family facilitation and November 30, 2032 expiry.

### Transition controls

- The expired 2023 worker-study measure is not falsely treated as the same mechanism as the different September 2026 short-study policy. Their eligibility structures and dates differ.
- The Quebec June 5 policy states that it revokes and replaces a March 12, 2026 predecessor and applies to pending applications under that predecessor.
- The FMCSP June 25 study and PR/OWP policies each expressly revoke and replace September 18, 2025 predecessors.
- The FMCSP study policy has part-specific expiry dates, so the record-level `effective_to` remains null and the exact expiry architecture is preserved in the date and transition fields.

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

## v0.2.0 — 2026-09-11

Expanded verified coverage to Saskatchewan SINP.

### Added

- Added `sk-sinp-capped-sector-final-intake-2026-09-14`: current SINP Processing Statistics and OASIS pages state that September 14–15 is the final 2026 capped-sector intake, with nomination spaces previously allocated for later intakes moved into September.
- Recorded sector windows and limits: Trucking 150 and Retail 175 at 9:30 a.m. September 14; Accommodation 50 at 1:30 p.m. September 14; Food Services 175 at 1:30 p.m. September 15.
- Preserved filing constraints: active intake window only, six months or less remaining on a valid work permit, first-come first-served, with OASIS indicating out-of-window EPAs or cases with more than six months remaining will be closed and returned.

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

- Added `ca-work-permit-short-study-2026-09-04`: IRCC's temporary public policy for valid work permit holders to study in a course or program lasting six months or less without a study permit. The signed policy was dated 2026-08-05, came into effect 2026-09-04, was publicly announced/observed on 2026-09-09, and expires 2027-12-31 unless revoked earlier.

### Coverage warning

v0.1.0 is a seed archive, not a complete historical reconstruction. Missing results must not be interpreted to mean that no rule existed.
