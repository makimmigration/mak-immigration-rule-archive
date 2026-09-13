# MAK Canadian Immigration Rule Change Archive

Version: 0.8.0  
Seed release: 2026-09-11  
Public site: https://makimmigration.github.io/mak-immigration-rule-archive/

## Purpose

This archive is designed to answer a narrow historical question accurately: **what did an official Canadian immigration source say was the applicable rule or policy state on a given date?**

It is a research and reference archive maintained by MAK Canadian Immigration Services. It is not legal advice and it is not a substitute for checking the current controlling government source for a live client matter.

## Source standard

Only current or preserved official government sources are used as controlling evidence for rule entries. Source priority is:

1. legislation, regulations, Ministerial Instructions or other controlling legal instruments;
2. official IRCC / Government of Canada program-delivery, eligibility, policy or notice pages;
3. official provincial or territorial immigration-program pages and notices;
4. official archived/superseded government material when needed to reconstruct a historical state.

A third-party article may help discover a change but cannot become the controlling source in this archive.

## Preservation rule

History is never silently overwritten.

When a later rule supersedes an archived rule:

- the older event remains in the archive;
- its `effective_to` is filled only when a defensible end date exists;
- its `superseded_by_event_id` points to the newer event where the relationship is fully archived;
- the newer event uses `supersedes_event_id` to point back where the relationship is clear;
- both records keep their own controlling official source and verification date.

If an official source later corrects itself, contains an internal anomaly, or clarifies a date, the archive records that explicitly rather than silently normalizing the source.

## Date discipline

Three date concepts are kept separate:

- `announcement_date`: when an official announcement or notice was published, if known;
- `rule_observed_from`: earliest date on which the archive has verified the stated rule from the cited official evidence;
- `effective_from`: legal/program effective date **only when an official source explicitly supports it or the controlling instrument establishes it**.

If an official page announces a change but gives no separate effective date, `effective_from` stays `null`. The archive does not convert a publication date into a legal coming-into-force date.

`effective_to` is used only when the end of that rule state can be supported. Where one public policy contains parts with different expiry dates, the archive may leave the record-level `effective_to` null and explain the part-specific dates in `date_basis` and `transition_rule`.

## Event fields

Each event can include:

- `id`
- `jurisdiction`
- `authority`
- `topic_key`
- `topic`
- `change_type`
- `announcement_date`
- `rule_observed_from`
- `effective_from`
- `effective_to`
- `date_basis`
- `status`
- `previous_rule`
- `new_rule`
- `transition_rule`
- `supersedes_event_id`
- `superseded_by_event_id`
- `controlling_source_url`
- `supporting_source_urls`
- `evidence_status`
- `last_verified_at`

## Interpretation

A result means the archive contains a verified record for that topic/date. A missing result **does not mean no rule existed**. It means this release does not yet contain enough verified historical evidence to answer that date/topic safely.

Current official government sources always control if they conflict with this archive.

## Coverage of v0.8.0

The v0.8.0 release contains **36 selected material events**. It preserves all v0.7.0 records and adds a reconstructed 2024–2026 federal implementation chain for study permits, PGWP filing/duration, family open work permits and border filing practice, including:

- the January 22, 2024 introduction of the PAL/TAL study-permit filing requirement and its original exemptions/transition rule;
- the February 15, 2024 three-year PGWP duration rule for eligible master's degree graduates even where the master's program is shorter than two years;
- the March 19, 2024 restriction of international-student spouse/common-law-partner open work permits, now explicitly linked to the January 21, 2025 successor;
- the June 21, 2024 end of PGWP applications at ports of entry;
- the December 23, 2024 broader end of work- and study-permit flagpoling, with CBSA's listed exemptions preserved;
- the January 22, 2025 expansion of PAL/TAL requirements to master's/doctoral students and most in-Canada applicants, with the later public-DLI graduate exemption treated as a partial supersession rather than an inferred end to the whole 2025 framework;
- the January 1, 2026 PAL/TAL exemption for degree-granting master's and doctoral programs at public DLIs;
- the May 15, 2024 PGWP ineligibility threshold for applicable public-private curriculum-licensing programs;
- SOR/2024-219's November 8, 2024 increase of eligible international-student off-campus work from 20 to 24 hours per week and its post-secondary DLI-change filing rule;
- SOR/2026-63's March 30, 2026 realignment of Provincial Nominee Class assessment roles;
- the April 1, 2026 removal of the separate co-op work-permit requirement for eligible post-secondary student work placements;
- the expired 2023 worker-study public policy and the distinct September 2026 short-study policy;
- the Quebec PSTQ and FMCSP predecessor/successor public-policy chains;
- IRCC's August 28, 2024 termination of the visitor in-Canada work-permit temporary public policy; and
- the Ontario OINP redesign implementation milestones of May 30, June 25 and August 4, 2026.

The archived 2025 FMCSP PR policy displays the impossible calendar date `November 31, 2031` as its nominal expiry. The archive does **not** silently convert that to another date. Instead, the record notes the source anomaly and bounds the historical active state by the verified June 25, 2026 successor that expressly revoked and replaced it.

The archive is **not a complete history of Canadian immigration law or policy**. Federal coverage is implementation-first but still selective, and Saskatchewan, Manitoba, Quebec and Ontario program coverage remains selective rather than a complete provincial historical reconstruction. Additional federal and provincial historical backfill is added only where dates, source state and transitions can be supported from official sources.

## Machine-readable and research access

- `events.json` is the canonical public structured release.
- `events.csv` is a flat export for analysts, journalists and spreadsheet users; it includes `supporting_source_urls` as a JSON-array cell so secondary official-source chains remain machine-readable.
- `research-briefs.html` provides 12 topic-focused citation entry points derived from the canonical events, including PGWP, family work permits, PAL/TAL, flagpoling/filing channels, Ontario PNP redesign, Quebec PSTQ measures, the Francophone Minority Communities Student Pilot, study-without-study-permit measures, international-student work rules, broader international-student changes, PNP 2026 and Express Entry.
- `research-briefs.csv` maps every brief to its included event IDs and stable event permalinks.
- `researcher-kit.html` provides one-page access to canonical data, research briefs, citation views, methodology and reuse controls.
- `release.json` exposes a machine-readable map of the public release and derived views.
- `CHANGELOG.md` records archive-version changes.

Research briefs are derived views only. They add no new legal proposition and never replace the current controlling government source.

## Change acceptance gate

A new archive event must have:

1. a material rule, eligibility, evidence, filing, status/work-permit, processing-instruction or officer-guidance change;
2. an official controlling source;
3. a defensible date basis;
4. a clear topic key;
5. explicit treatment of transition/supersession where applicable;
6. a verification date.

No entry is created from rumours, social posts, commentary, press coverage, unofficial summaries or an inferred effective date.

## Citation / reuse

Users may cite the archive as a MAK-curated research reference, but the underlying rule should also be attributed to the controlling government authority. Government source material remains subject to the applicable Crown / Government of Canada or provincial terms. MAK-authored summaries are not a substitute for the source text.

Suggested reference:

> MAK Canadian Immigration Services, Immigration Data Observatory. *Canadian Immigration Rule Change Archive*, version 0.8.0, 2026-09-13. Individual entries cite the controlling official government source.
