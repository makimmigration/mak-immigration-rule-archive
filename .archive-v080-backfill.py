import csv
import json
import re
import sys
from pathlib import Path

BASE = Path(sys.argv[1]) if len(sys.argv) > 1 else Path('.')
VERIFIED = '2026-09-13'
EVENTS_PATH = BASE / 'events.json'

with EVENTS_PATH.open('r', encoding='utf-8') as f:
    data = json.load(f)

new_events = [
    {
        'id': 'ca-pgwp-masters-three-year-duration-2024-02-15',
        'jurisdiction': 'Canada',
        'authority': 'Immigration, Refugees and Citizenship Canada',
        'topic_key': 'pgwp-duration-masters',
        'topic': "Post-graduation work permit duration for master's degree graduates",
        'change_type': 'permit_duration_expanded',
        'announcement_date': '2024-02-05',
        'rule_observed_from': '2024-02-15',
        'effective_from': '2024-02-15',
        'effective_to': None,
        'date_basis': "IRCC's February 5, 2024 reform notice states that starting February 15, 2024 a three-year PGWP would be available to eligible graduates of master's degree programs shorter than two years. IRCC's current PGWP duration page states the same February 15, 2024 threshold.",
        'status': 'current_historical_threshold',
        'previous_rule': "For an eligible program of at least eight months but less than two years, PGWP duration was generally limited to up to the length of the study program; a master's degree shorter than two years did not by itself provide a three-year PGWP duration rule.",
        'new_rule': "As of February 15, 2024, an eligible graduate of a master's degree program can qualify for a three-year PGWP even when the master's program was less than two years, provided the program was at least eight months (900 hours for Quebec programs) and the applicant meets the other PGWP eligibility requirements. The special duration rule does not apply to certificate or diploma programs.",
        'transition_rule': "The official sources state the special master's-duration rule starts February 15, 2024. This archive does not infer a different filing-date transition for applications before that threshold where the cited sources do not state one.",
        'supersedes_event_id': None,
        'superseded_by_event_id': None,
        'controlling_source_url': 'https://www.canada.ca/en/immigration-refugees-citizenship/services/study-canada/work/after-graduation/about.html',
        'supporting_source_urls': ['https://www.canada.ca/en/immigration-refugees-citizenship/news/notices/international-student-program-reform-more-information.html'],
        'evidence_status': 'OFFICIAL_VERIFIED',
        'last_verified_at': VERIFIED,
    },
    {
        'id': 'ca-family-owp-students-2024-03-19',
        'jurisdiction': 'Canada',
        'authority': 'Immigration, Refugees and Citizenship Canada',
        'topic_key': 'family-owp-international-students',
        'topic': 'Family open work permits for spouses of international students',
        'change_type': 'eligibility_narrowed',
        'announcement_date': '2024-02-05',
        'rule_observed_from': '2024-03-19',
        'effective_from': '2024-03-19',
        'effective_to': '2025-01-20',
        'date_basis': "IRCC's February 5, 2024 reform notice announced the coming restriction. Official IRCC Question Period records later state that IRCC implemented the restriction on March 19, 2024. The rule state is bounded through January 20, 2025 because IRCC expressly made the successor family-OWP restrictions effective January 21, 2025.",
        'status': 'superseded',
        'previous_rule': 'Before March 19, 2024, family open-work-permit eligibility for spouses and common-law partners of international students was broader and was not limited to the graduate/professional/pilot cohorts identified by the March 19 restriction.',
        'new_rule': "From March 19, 2024, open work permit eligibility under the international-student spouse measure was restricted to spouses and common-law partners of students in master's and doctoral degree programs, certain professional degree programs and select eligible pilot programs.",
        'transition_rule': "IRCC's February 5 notice stated that spouses and common-law partners seeking to extend an existing open work permit would continue to be eligible under the stream once the restriction took effect. On January 21, 2025, a successor rule further narrowed the master's cohort to programs of at least 16 months and set the current specified-program framework.",
        'supersedes_event_id': None,
        'superseded_by_event_id': 'ca-family-owp-students-2025-01-21',
        'controlling_source_url': 'https://search.open.canada.ca/qpnotes/record/cic%2CIRCC-2024-QP-00066',
        'supporting_source_urls': [
            'https://www.canada.ca/en/immigration-refugees-citizenship/news/notices/international-student-program-reform-more-information.html',
            'https://www.canada.ca/en/immigration-refugees-citizenship/news/notices/changes-open-work-permits-family-members-temporary-residents.html',
        ],
        'evidence_status': 'OFFICIAL_VERIFIED',
        'last_verified_at': VERIFIED,
    },
    {
        'id': 'ca-pgwp-port-of-entry-application-ended-2024-06-21',
        'jurisdiction': 'Canada',
        'authority': 'Immigration, Refugees and Citizenship Canada',
        'topic_key': 'pgwp-filing-location',
        'topic': 'PGWP applications at ports of entry',
        'change_type': 'filing_channel_restricted',
        'announcement_date': '2024-06-21',
        'rule_observed_from': '2024-06-21',
        'effective_from': '2024-06-21',
        'effective_to': None,
        'date_basis': "IRCC's June 21, 2024 news release states that foreign nationals can no longer apply for a PGWP at the border, effective immediately. Current IRCC work-permit instructions state that as of June 21, 2024 a PGWP cannot be applied for at a port of entry.",
        'status': 'current',
        'previous_rule': 'Before June 21, 2024, an otherwise eligible foreign national could in some circumstances seek a PGWP at a port of entry, including through the practice commonly called flagpoling.',
        'new_rule': 'As of June 21, 2024, foreign nationals can no longer apply for a post-graduation work permit at a port of entry, whether at an airport, land border or marine border when entering Canada.',
        'transition_rule': 'The restriction took effect immediately on June 21, 2024. It is specific to PGWP filing at ports of entry and is preserved separately from the broader December 23, 2024 termination of work- and study-permit flagpoling.',
        'supersedes_event_id': None,
        'superseded_by_event_id': None,
        'controlling_source_url': 'https://www.canada.ca/en/immigration-refugees-citizenship/services/work-canada/work-permit/apply/poe.html',
        'supporting_source_urls': ['https://www.canada.ca/en/immigration-refugees-citizenship/news/2024/06/canada-improves-fairness-for-applicants-by-ending-post-graduation-work-permit-flagpoling.html'],
        'evidence_status': 'OFFICIAL_VERIFIED',
        'last_verified_at': VERIFIED,
    },
    {
        'id': 'ca-work-study-permit-flagpoling-ended-2024-12-23',
        'jurisdiction': 'Canada',
        'authority': 'Government of Canada / Canada Border Services Agency',
        'topic_key': 'port-of-entry-flagpoling-work-study-permits',
        'topic': 'Work and study permit flagpoling at ports of entry',
        'change_type': 'filing_channel_restricted',
        'announcement_date': '2024-12-23',
        'rule_observed_from': '2024-12-23',
        'effective_from': '2024-12-23',
        'effective_to': None,
        'date_basis': "The Canada Border Services Agency's December 23, 2024 release states that work and study permits would no longer be provided to flagpolers at ports of entry effective December 23, 2024 at 11:59 p.m. Eastern Time.",
        'status': 'current',
        'previous_rule': 'Before the December 23, 2024 cutoff, some temporary residents in Canada could leave and re-enter Canada to request work- or study-permit service at a port of entry if they were otherwise eligible. PGWP applications had already been separately barred from ports of entry on June 21, 2024.',
        'new_rule': 'Effective December 23, 2024 at 11:59 p.m. ET, work and study permits are generally no longer provided at ports of entry to foreign nationals who flagpole. Applications and renewals are to be submitted through IRCC unless a listed exemption applies.',
        'transition_rule': 'CBSA listed limited exemptions, including U.S. citizens and lawful permanent residents; specified professionals and technicians under listed free-trade agreements; certain spouses/common-law partners under specified agreements; qualifying international truck drivers with maintained status after a timely renewal; and people with a pre-existing CBSA permit-processing appointment.',
        'supersedes_event_id': None,
        'superseded_by_event_id': None,
        'controlling_source_url': 'https://www.canada.ca/en/border-services-agency/news/2024/12/ending-flagpoling-for-work-and-study-permits-at-the-border.html',
        'supporting_source_urls': [],
        'evidence_status': 'OFFICIAL_VERIFIED',
        'last_verified_at': VERIFIED,
    },
    {
        'id': 'ca-study-permit-pal-tal-introduction-2024-01-22',
        'jurisdiction': 'Canada',
        'authority': 'Immigration, Refugees and Citizenship Canada',
        'topic_key': 'study-permit-pal-tal',
        'topic': 'Provincial or territorial attestation letter requirement for study permits',
        'change_type': 'filing_requirement_added',
        'announcement_date': '2024-01-22',
        'rule_observed_from': '2024-01-22',
        'effective_from': '2024-01-22',
        'effective_to': None,
        'date_basis': "IRCC's February 5, 2024 clarification states that as of 8:30 a.m. ET on January 22, 2024 most new post-secondary students at the college or undergraduate level had to include a provincial attestation letter. MI75 later expressly identifies the Ministerial Instructions it amended as having taken effect January 22, 2024.",
        'status': 'current_foundation_with_later_scope_changes',
        'previous_rule': 'Before the January 22, 2024 intake-control measure, there was no general federal PAL/TAL requirement requiring most affected study permit applicants to obtain a provincial or territorial allocation attestation before filing.',
        'new_rule': 'From 8:30 a.m. ET on January 22, 2024, most new post-secondary study permit applicants at the college or undergraduate level, and most non-degree graduate-program applicants, had to include a provincial attestation letter from the province or territory where they intended to study unless an exemption applied.',
        'transition_rule': "IRCC stated that applications received before 8:30 a.m. ET on January 22, 2024 and already-approved study permits required no action. Under the 2024 rule state, master's and doctoral degree students, primary and secondary students, in-Canada study/work permit holders including study-permit extensions, in-Canada family members of permit holders, and specified visiting/exchange students were among the exempt cohorts. Later instructions changed the scope.",
        'supersedes_event_id': None,
        'superseded_by_event_id': None,
        'controlling_source_url': 'https://www.canada.ca/en/immigration-refugees-citizenship/news/notices/international-student-program-reform-more-information.html',
        'supporting_source_urls': [
            'https://www.canada.ca/en/immigration-refugees-citizenship/corporate/mandate/policies-operational-instructions-agreements/ministerial-instructions/other-goals/mi75.html',
            'https://www.canada.ca/en/immigration-refugees-citizenship/services/study-canada/study-permit/get-documents/provincial-attestation-letter.html',
        ],
        'evidence_status': 'OFFICIAL_VERIFIED',
        'last_verified_at': VERIFIED,
    },
    {
        'id': 'ca-study-permit-pal-tal-graduate-expansion-2025-01-22',
        'jurisdiction': 'Canada',
        'authority': 'Immigration, Refugees and Citizenship Canada',
        'topic_key': 'study-permit-pal-tal',
        'topic': 'PAL/TAL requirement expanded to graduate students and additional in-Canada applicants',
        'change_type': 'filing_requirement_expanded',
        'announcement_date': '2024-09-18',
        'rule_observed_from': '2025-01-22',
        'effective_from': '2025-01-22',
        'effective_to': None,
        'date_basis': "IRCC announced on September 18, 2024 that master's and doctoral students would be included in the 2025 study-permit cap and would have to submit a PAL/TAL. IRCC's January 24, 2025 allocation notice confirms the requirement extended to master's and doctoral students and most applicants applying from inside Canada; current IRCC instructions identify January 22, 2025 as the operative date for the 2025 PAL/TAL changes. A later January 1, 2026 exemption only superseded the public-DLI master's/doctoral component, so no record-level effective_to date is asserted for the broader 2025 expansion.",
        'status': 'partially_superseded_for_public_graduate_cohort',
        'previous_rule': "Under the 2024 PAL/TAL framework, master's and doctoral degree students and several in-Canada cohorts were exempt from the attestation requirement.",
        'new_rule': "For the 2025 cap year, the PAL/TAL requirement expanded to master's and doctoral degree students and most applicants applying from within Canada. Existing study permit holders applying to extend at the same DLI and same level remained exempt, along with specified other exempt cohorts.",
        'transition_rule': "The change was announced September 18, 2024 for 2025 implementation. A new PAL/TAL was required in most cases when changing schools or levels from January 22, 2025. On January 1, 2026, degree-granting master's and doctoral students at public DLIs became exempt again; that successor only supersedes the public-DLI graduate component, not the PAL/TAL framework as a whole.",
        'supersedes_event_id': None,
        'superseded_by_event_id': 'ca-study-permit-pal-tal-public-graduate-exemption-2026-01-01',
        'controlling_source_url': 'https://www.canada.ca/en/immigration-refugees-citizenship/news/notices/2025-provincial-territorial-allocations-under-international-student-cap.html',
        'supporting_source_urls': [
            'https://www.canada.ca/en/immigration-refugees-citizenship/news/2024/09/strengthening-temporary-residence-programs-for-sustainable-volumes.html',
            'https://www.canada.ca/en/immigration-refugees-citizenship/services/study-canada/extend-study-permit/how-to-apply.html',
        ],
        'evidence_status': 'OFFICIAL_VERIFIED',
        'last_verified_at': VERIFIED,
    },
    {
        'id': 'ca-study-permit-pal-tal-public-graduate-exemption-2026-01-01',
        'jurisdiction': 'Canada',
        'authority': 'Immigration, Refugees and Citizenship Canada',
        'topic_key': 'study-permit-pal-tal',
        'topic': "PAL/TAL exemption for public-DLI master's and doctoral degree students",
        'change_type': 'filing_requirement_exemption_added',
        'announcement_date': '2025-11-25',
        'rule_observed_from': '2026-01-01',
        'effective_from': '2026-01-01',
        'effective_to': None,
        'date_basis': "IRCC's November 25, 2025 notice expressly states that as of January 1, 2026 master's and doctoral level students enrolled at a public DLI will not need a PAL/TAL. Current IRCC PAL/TAL and graduate-student instructions preserve the same January 1, 2026 threshold.",
        'status': 'current',
        'previous_rule': "During the 2025 cap year, master's and doctoral degree students were included among PAL/TAL-required cohorts, subject to the applicable exemptions then in force.",
        'new_rule': "As of January 1, 2026, students applying for a degree-granting master's or doctoral program at a public designated learning institution do not need to submit a PAL/TAL with the study permit application. Other applicants remain subject to the current PAL/TAL framework unless another exemption applies.",
        'transition_rule': "The exemption applies from January 1, 2026 and is limited to degree-granting master's and doctoral programs at public DLIs. It does not create a general graduate-program exemption. Applicants studying in Quebec must still meet Quebec requirements, including CAQ requirements where applicable.",
        'supersedes_event_id': 'ca-study-permit-pal-tal-graduate-expansion-2025-01-22',
        'superseded_by_event_id': None,
        'controlling_source_url': 'https://www.canada.ca/en/immigration-refugees-citizenship/news/notices/2026-provincial-territorial-allocations-under-international-student-cap.html',
        'supporting_source_urls': [
            'https://www.canada.ca/en/immigration-refugees-citizenship/services/study-canada/study-permit/get-documents/provincial-attestation-letter.html',
            'https://www.canada.ca/en/immigration-refugees-citizenship/services/study-canada/graduate-student/how-to-apply.html',
        ],
        'evidence_status': 'OFFICIAL_VERIFIED',
        'last_verified_at': VERIFIED,
    },
]

existing = {e['id']: e for e in data['events']}
for event in new_events:
    if event['id'] not in existing:
        data['events'].append(event)
        existing[event['id']] = event

successor = existing.get('ca-family-owp-students-2025-01-21')
if successor is None:
    raise SystemExit('Missing existing family OWP successor event')
successor['supersedes_event_id'] = 'ca-family-owp-students-2024-03-19'
successor['previous_rule'] = "From March 19, 2024 through January 20, 2025, family OWP eligibility for spouses and common-law partners of international students was already limited to master's/doctoral degree students, certain professional degree programs and select eligible pilots. The January 21, 2025 rule further narrowed the master's cohort to programs of at least 16 months and established the successor specified-program framework."
successor['last_verified_at'] = VERIFIED

data['archive']['version'] = '0.8.0'
data['archive']['released'] = '2026-09-13'
data['archive']['coverage'] = 'Selected material federal IRCC, IRPR and CBSA rule/policy changes plus verified Ontario OINP, Saskatchewan SINP, Manitoba and Quebec history, including PGWP duration and filing rules, PAL/TAL study-permit transitions, family open work permits, international-student work/study rules, PNP federal-provincial assessment roles, and preserved predecessor/successor transition chains.'
data['archive']['last_verified_at'] = '2026-09-13T07:01:36+05:00'

ids = [e['id'] for e in data['events']]
if len(ids) != len(set(ids)):
    raise SystemExit('Duplicate event ID detected')
if len(ids) != 36:
    raise SystemExit(f'Expected 36 events after v0.8.0 backfill, found {len(ids)}')
by_id = {e['id']: e for e in data['events']}
for e in data['events']:
    for key in ('supersedes_event_id', 'superseded_by_event_id'):
        if e.get(key) and e[key] not in by_id:
            raise SystemExit(f'Broken {key} on {e["id"]}: {e[key]}')

EVENTS_PATH.write_text(json.dumps(data, ensure_ascii=False, separators=(',', ':')) + '\n', encoding='utf-8')

fields = [
    'id','jurisdiction','authority','topic_key','topic','change_type','announcement_date','rule_observed_from','effective_from','effective_to','date_basis','status','previous_rule','new_rule','transition_rule','supersedes_event_id','superseded_by_event_id','controlling_source_url','supporting_source_urls','evidence_status','last_verified_at'
]
with (BASE / 'events.csv').open('w', encoding='utf-8', newline='') as f:
    w = csv.DictWriter(f, fieldnames=fields, extrasaction='ignore')
    w.writeheader()
    for e in data['events']:
        row = dict(e)
        row['supporting_source_urls'] = json.dumps(e.get('supporting_source_urls', []), ensure_ascii=False, separators=(',', ':'))
        w.writerow(row)

coverage = """## Coverage of v0.8.0

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
"""

readme_path = BASE / 'README.md'
readme = readme_path.read_text(encoding='utf-8')
readme = re.sub(r'^Version: [0-9.]+\s*$', 'Version: 0.8.0  ', readme, count=1, flags=re.M)
match = re.search(r'^## Coverage of v[0-9.]+\n', readme, flags=re.M)
if not match:
    raise SystemExit('README coverage heading not found')
next_heading = re.search(r'^## ', readme[match.end():], flags=re.M)
end = match.end() + next_heading.start() if next_heading else len(readme)
readme = readme[:match.start()] + coverage + '\n' + readme[end:]
readme = readme.replace('*Canadian Immigration Rule Change Archive*, version 0.7.0,', '*Canadian Immigration Rule Change Archive*, version 0.8.0,')
old_csv_bullet = '- `events.csv` is a flat export for analysts, journalists and spreadsheet users.'
new_csv_bullet = '- `events.csv` is a flat export for analysts, journalists and spreadsheet users; it includes `supporting_source_urls` as a JSON-array cell so secondary official-source chains remain machine-readable.'
if old_csv_bullet in readme:
    readme = readme.replace(old_csv_bullet, new_csv_bullet)
readme_path.write_text(readme, encoding='utf-8')

changelog_path = BASE / 'CHANGELOG.md'
changelog = changelog_path.read_text(encoding='utf-8')
entry = """## v0.8.0 — 2026-09-13

Expanded the implementation-first federal history from 29 to 36 events. No v0.7.0 event was removed. This release reconstructs several high-value 2024–2026 transition chains from official IRCC, CBSA and Ministerial Instruction evidence and improves the flat CSV export.

### Added

- `ca-study-permit-pal-tal-introduction-2024-01-22`: reconstructs the January 22, 2024 introduction of the PAL/TAL study-permit filing requirement, including the 8:30 a.m. ET intake boundary and original exemption cohorts.
- `ca-pgwp-masters-three-year-duration-2024-02-15`: records the February 15, 2024 special three-year PGWP duration rule for eligible master's degree graduates whose programs are shorter than two years.
- `ca-family-owp-students-2024-03-19`: reconstructs the March 19, 2024 restriction of international-student spouse/common-law-partner open work permit eligibility and links it to the January 21, 2025 successor.
- `ca-pgwp-port-of-entry-application-ended-2024-06-21`: records the immediate June 21, 2024 end of PGWP applications at ports of entry.
- `ca-work-study-permit-flagpoling-ended-2024-12-23`: records the broader December 23, 2024 at 11:59 p.m. ET end of work- and study-permit flagpoling and preserves CBSA's listed exceptions.
- `ca-study-permit-pal-tal-graduate-expansion-2025-01-22`: records the 2025 expansion of PAL/TAL requirements to master's/doctoral students and most in-Canada applicants.
- `ca-study-permit-pal-tal-public-graduate-exemption-2026-01-01`: records the January 1, 2026 PAL/TAL exemption for degree-granting master's and doctoral programs at public DLIs.

### Supersession and transition reconstruction

- Updated `ca-family-owp-students-2025-01-21` so its predecessor is no longer described generically: it now links back to the reconstructed March 19, 2024 rule state and explains the additional January 21, 2025 narrowing.
- The January 22, 2025 PAL/TAL expansion has no record-level `effective_to` date because the January 1, 2026 change only superseded the public-DLI master's/doctoral component. The broader 2025 framework is therefore marked as partially superseded rather than silently ended.
- Historical filing-channel changes are kept distinct: PGWP port-of-entry filing ended June 21, 2024; the wider work/study flagpoling restriction followed December 23, 2024.

### Machine-readable release

- `events.csv` now exports `supporting_source_urls` in addition to each event's controlling source, keeping the CSV source chain aligned with `events.json`.
- Archive metadata, README coverage, interface version and CITATION metadata were advanced together to v0.8.0.

"""
if '## v0.8.0 — 2026-09-13' not in changelog:
    changelog = changelog.replace('# Version history\n\n', '# Version history\n\n' + entry, 1)
changelog_path.write_text(changelog, encoding='utf-8')

index_path = BASE / 'index.html'
index = index_path.read_text(encoding='utf-8').replace('v0.7.0', 'v0.8.0').replace('0.7.0', '0.8.0')
index_path.write_text(index, encoding='utf-8')

cff_path = BASE / 'CITATION.cff'
cff = cff_path.read_text(encoding='utf-8')
cff = re.sub(r'^version: ".*"$', 'version: "0.8.0"', cff, count=1, flags=re.M)
cff = re.sub(r'^date-released: .*$', 'date-released: 2026-09-13', cff, count=1, flags=re.M)
cff_path.write_text(cff, encoding='utf-8')

with EVENTS_PATH.open('r', encoding='utf-8') as f:
    check = json.load(f)
assert check['archive']['version'] == '0.8.0'
assert len(check['events']) == 36
for eid in [e['id'] for e in new_events]:
    assert eid in {e['id'] for e in check['events']}
with (BASE / 'events.csv').open('r', encoding='utf-8', newline='') as f:
    rows = list(csv.DictReader(f))
assert len(rows) == 36
assert 'supporting_source_urls' in rows[0]
assert '36 selected material events' in readme_path.read_text(encoding='utf-8')
assert '## v0.8.0 — 2026-09-13' in changelog_path.read_text(encoding='utf-8')
assert 'version: "0.8.0"' in cff_path.read_text(encoding='utf-8')
print(f'archive v0.8.0 ready at {BASE}: {len(check["events"])} events')
