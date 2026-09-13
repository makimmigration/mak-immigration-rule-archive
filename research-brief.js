(() => {
  const esc = s => String(s ?? '').replace(/[&<>\"]/g, c => ({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c]));
  const dateOf = e => e.effective_from || e.rule_observed_from || e.announcement_date || '';
  const statusClass = s => String(s || '').includes('superseded') || String(s || '').includes('expired') ? 'old' : '';
  const sourceLinks = e => {
    let out = `<a href="${esc(e.controlling_source_url)}" target="_blank" rel="noopener">Controlling official source</a>`;
    (e.supporting_source_urls || []).forEach((u,i) => out += ` · <a href="${esc(u)}" target="_blank" rel="noopener">Official supporting source ${i+1}</a>`);
    return out;
  };
  function renderEvent(e) {
    return `<article class="event" id="${esc(e.id)}">
      <div class="meta"><span class="pill">${esc(e.jurisdiction)}</span><span class="pill ${statusClass(e.status)}">${esc(e.status)}</span><span class="pill">${esc(e.change_type)}</span></div>
      <h2>${esc(e.topic)}</h2>
      <p class="date"><strong>${esc(dateOf(e) || 'No separate date stated')}</strong>${e.effective_from ? ' · effective date' : ' · observed/announcement basis'} · verified ${esc(e.last_verified_at)}</p>
      <div class="grid"><div class="block"><strong>Rule/change recorded</strong>${esc(e.new_rule)}</div><div class="block"><strong>Transition / historical context</strong>${esc(e.transition_rule)}</div></div>
      <details><summary>Previous rule / archive coverage</summary><p>${esc(e.previous_rule)}</p><p class="small">Date basis: ${esc(e.date_basis)}</p></details>
      <div class="sources">${sourceLinks(e)}</div>
      <div class="perma"><a href="event.html?id=${encodeURIComponent(e.id)}">Stable archive event permalink</a> · <code>${esc(e.id)}</code></div>
    </article>`;
  }
  async function run() {
    const cfg = window.BRIEF_CONFIG || {};
    const root = document.getElementById('events');
    try {
      const j = await (await fetch('events.json', {cache:'no-store'})).json();
      const keys = new Set(cfg.topicKeys || []);
      const rows = (j.events || []).filter(e => keys.has(e.topic_key)).sort((a,b) => dateOf(a).localeCompare(dateOf(b)) || a.id.localeCompare(b.id));
      document.getElementById('count').textContent = `${rows.length} verified archive event${rows.length === 1 ? '' : 's'} in this brief.`;
      root.innerHTML = rows.map(renderEvent).join('');
    } catch (err) {
      root.innerHTML = '<p class="notice">Archive data could not be loaded.</p>';
    }
  }
  run();
})();
