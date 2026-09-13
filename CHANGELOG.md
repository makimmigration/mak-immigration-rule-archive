# Version history

## v0.7.0 — 2026-09-13

Expanded the federal implementation history with five high-value 2024–2026 rule changes covering PGWP curriculum-licensing eligibility, international-student off-campus work, DLI changes, Provincial Nominee Class assessment roles and post-secondary student work placements. No v0.6.0 events were removed.

### Added

- `ca-pgwp-curriculum-licensing-ineligibility-2024-05-15`: records IRCC's March 22, 2024 decision to advance the PGWP ineligibility threshold for applicable public-private curriculum-licensing programs from the previously announced September 1 date to May 15, 2024, using the student's program start date as the transition point.
- `ca-student-off-campus-work-hours-2024-11-08`: records SOR/2024-219's amendment to R186(v)(iii), increasing the regular-session off-campus work maximum from 20 to 24 hours per week effective on registration, November 8, 2024.
- `ca-study-permit-dli-change-rule-2024-11-08`: records new R217.1 and related amendments requiring an in-Canada study permit holder whose permit names a DLI to apply for a new study permit naming a different DLI, together with the narrow R189.1 interim-study conditions.
- `ca-pnp-irpr-role-realignment-2026-03-30`: records SOR/2026-63's replacement of R87(2)-(4), assigning provinces and territories sole responsibility for evaluating economic establishment and intent to reside and preserving federal admissibility/program-integrity functions.
- `ca-postsecondary-coop-work-permit-exemption-2026-04-01`: records IRCC's removal of the separate co-op work-permit requirement for eligible post-secondary student work placements from April 1, 2026, while preserving the permit requirement for secondary-school placements.

### Transition and date controls

- The May 15, 2024 PGWP curriculum-licensing threshold is controlled by IRCC's March 22 notice, which expressly replaced the previously announced September 1 implementation date.
- SOR/2024-219 was registered November 8, 2024 and expressly came into force on registration. The archive separates its 24-hour work rule from the earlier temporary public policy that had expired April 30, 2024.
- The DLI-change record preserves the actual R189.1 exception rather than describing all pending change-of-DLI applications as carrying interim study authorization.
- SOR/2026-63 was registered March 30, 2026. Its Regulatory Impact Analysis Statement expressly applies the new PNP assessment model to both new applications and existing inventory for which an eligibility decision had not yet been rendered.
- The post-secondary co-op event separates the April 1 effective date from IRCC's April 9 public notice and preserves treatment of existing permits and eligible active pending applications.

### Archive scope

- The public structured release now contains 29 selected material events.
- This release materially improves federal 2024–2026 study/work and PNP implementation coverage while retaining the archive rule that a missing entry never proves that no rule existed.

## v0.6.0 — 2026-09-13

Expanded the public archive with a federal 2024 work-permit policy termination and a three-stage Ontario OINP redesign implementation chain. This release is rebased on the complete public v0.5.0 predecessor/supersession dataset; no v0.5.0 events were dropped.

### Added

- `ca-visitor-inland-work-permit-policy-ended-2024-08-28`: records IRCC's immediate August 28, 2024 termination of the temporary public policy that had allowed qualifying visitors to apply for work permits from inside Canada, while preserving processing for applications submitted before termination.
- `on-oinp-redesign-procedure-2026-05-30`: records the O. Reg. 47/26 procedural redesign provisions effective May 30, 2026 and Ontario's protection for applications already received under the prior framework.
- `on-oinp-workforce-priority-regulatory-replacement-2026-06-25`: records the June 25, 2026 O. Reg. 204/26 replacement of the former eight OINP streams with the Ontario Workforce Priority stream, including withdrawal of uninvited former-stream EOIs and preservation of already-submitted invited applications under submission-date rules.
- `on-oinp-workforce-priority-eoi-launch-2026-08-04`: records the separate August 4, 2026 operational launch of the Workforce Priority expression-of-interest portal rather than back-dating portal availability to the June 25 regulatory change.

### Date and transition controls

- The visitor-policy termination uses August 28, 2024 for announcement, observed-from and effective-from because IRCC expressly states the policy ended effective immediately that day.
- The OINP May 30 date is supported by O. Reg. 47/26 and OINP's May 29 implementation notice; the March 16 filing/announcement date is retained separately.
- The OINP June 25 effective date is supported by O. Reg. 204/26 and OINP's June 26 update. Former-stream EOIs that had not produced invitations were withdrawn, while already-submitted invited applications continue under the eligibility rules in force at submission.
- The August 4 portal launch is preserved as a separate operational milestone, not treated as the legal creation date of the Workforce Priority stream.

### Control/public synchronization

- The v0.6.0 control copy incorporates all v0.5.0 public predecessor/successor records before adding this release, preserving the canonical public history and avoiding regression during concurrent archive maintenance.

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
