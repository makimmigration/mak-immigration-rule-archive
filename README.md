# MAK Canadian Immigration Rule Change Archive

Version: 0.1.0  
Seed release: 2026-09-11

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
- its `superseded_by_event_id` points to the newer event;
- the newer event uses `supersedes_event_id` to point back where the relationship is clear;
- both records keep their own controlling official source and verification date.

If an official source later corrects itself or clarifies a date, the archive records that as a versioned correction rather than pretending the earlier archive entry never existed.

## Date discipline

Three date concepts are kept separate:

- `announcement_date`: when an official announcement or notice was published, if known;
- `rule_observed_from`: earliest date on which the archive has verified the stated rule from the cited official evidence;
- `effective_from`: legal/program effective date **only when an official source explicitly supports it or the controlling instrument establishes it**.

If an official page announces a change but gives no separate effective date, `effective_from` stays `null`. The archive does not convert a publication date into a legal coming-into-force date.

`effective_to` is used only when the end of that rule state can be supported. Open-ended rules remain `null` until supersession or expiry is verified.

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

## Coverage of v0.1.0

The seed release contains selected material federal IRCC events from November 2024 through June 2026, including PGWP eligibility and field-of-study changes, family open-work-permit changes, Express Entry arranged-employment CRS changes, 2026 category-based selection changes, and selected 2026 targeted work-permit measures.

The seed release is **not a complete history of Canadian immigration law or policy**. Ontario and Saskatchewan monitoring are enabled for future verified material entries; additional federal and provincial historical backfill will be added only where dates and supersession can be supported from official sources.

## Machine-readable access

- `events.json` is the canonical public structured release.
- `events.csv` is a flat export for analysts, journalists and spreadsheet users.
- `CHANGELOG.md` records archive-version changes.

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

> MAK Canadian Immigration Services, Immigration Data Observatory. *Canadian Immigration Rule Change Archive*, version 0.1.0, 2026-09-11. Individual entries cite the controlling official government source.
