function loadKickingStats() {
  content.innerHTML = `
    <section class="max-w-4xl mx-auto py-8 px-4 space-y-6">
      <h2 class="text-3xl font-bold text-indigo-700 mb-2">🥾 Search Kicking Stats</h2>

      <!-- Mode Toggle -->
      <div>
        <h3 class="text-xl font-semibold mb-2">Select Search Mode</h3>
        <label class="mr-4">
          <input type="radio" name="searchMode" value="year" checked onchange="handleModeChange()" /> Search by Year
        </label>
        <label>
          <input type="radio" name="searchMode" value="all" onchange="handleModeChange()" /> Return All Years
        </label>
        <div id="yearInputWrapper" class="mt-2">
          <input id="selectedYear" type="number" placeholder="Enter Year (e.g. 2024)" class="border p-2 rounded w-64" />
        </div>
      </div>

      <!-- Filter Type -->
      <div>
        <h3 class="text-xl font-semibold mb-2">Choose Filter</h3>
        <select id="filterType" class="border p-2 rounded w-64">
          <option value="name">Player Name</option>
          <option value="fg_made">Min FGs Made</option>
          <option value="xp_made">Min XPs Made</option>
        </select>
        <input id="filterValue" class="border p-2 rounded w-64 mt-2 block" placeholder="Enter value..." />
      </div>

      <button onclick="runKickingSearch()" class="mt-4 bg-blue-600 text-white px-6 py-2 rounded">Search</button>

      <div id="kickingResults" class="pt-8 space-y-4"></div>
    </section>
  `;
}

function runKickingSearch() {
  const mode = document.querySelector('input[name="searchMode"]:checked').value;
  const year = document.getElementById('selectedYear').value.trim();
  const filter = document.getElementById('filterType').value;
  const value = document.getElementById('filterValue').value.trim();
  const results = document.getElementById('kickingResults');
  results.innerHTML = '';

  if (mode === 'year' && year === '') {
    results.innerHTML = `<p class="text-red-500 font-semibold">Please enter a year when using 'Search by Year' mode.</p>`;
    return;
  }

  if (!value) {
    results.innerHTML = `<p class="text-red-500">Please enter a filter value.</p>`;
    return;
  }

  if ((filter === 'fg_made' || filter === 'xp_made') && isNaN(value)) {
    results.innerHTML = `<p class="text-red-500">Please enter a valid number for ${filter === 'fg_made' ? 'Field Goals' : 'Extra Points'} Made.</p>`;
    return;
  }

  if (mode === 'all' && filter === 'name') {
    fetch(`http://localhost:8000/kicking/players?player_name=${value}`)
      .then(res => res.json())
      .then(renderKickingResults);
    return;
  }

  if (mode === 'all') {
    results.innerHTML = `<p class="text-red-500">All years mode only supports name search.</p>`;
    return;
  }

  if (filter === 'name') {
    fetch(`http://localhost:8000/kicking/players/${year}?player_name=${value}`)
      .then(res => {
        if (!res.ok) throw new Error(`HTTP ${res.status}`);
        return res.json();
      })
      .then(renderKickingResults)
      .catch(err => {
        results.innerHTML = `<p class="text-red-500">Error: ${err.message}</p>`;
      });
  } else if (filter === 'fg_made') {
    fetch(`http://localhost:8000/kicking/fg_made?min_fg_made=${value}`)
      .then(res => res.json())
      .then(data => {
        const filtered = data.filter(p => p.season_year == year);
        renderKickingResults(filtered);
      });
  } else if (filter === 'xp_made') {
    fetch(`http://localhost:8000/kicking/xp_made?min_xp_made=${value}`)
      .then(res => res.json())
      .then(data => {
        const filtered = data.filter(p => p.season_year == year);
        renderKickingResults(filtered);
      });
  }
}

function renderKickingResults(data) {
  const container = document.getElementById("kickingResults");
  container.innerHTML = "";

  if (!Array.isArray(data) || data.length === 0) {
    container.innerHTML = `<p class="text-red-500">No results found.</p>`;
    return;
  }

  data.forEach(player => {
    let card = `
      <div class="bg-white shadow p-4 rounded text-sm mb-4">
        <h4 class="text-lg font-semibold">${player.player_name}</h4>
        <p><strong>Season:</strong> ${player.season_year}</p>
    `;

    if (player.fg_made !== undefined) card += `<p><strong>FG Made:</strong> ${player.fg_made}</p>`;
    if (player.fg_attempts !== undefined) card += `<p><strong>FG Attempts:</strong> ${player.fg_attempts}</p>`;
    if (player.fg_long !== undefined) card += `<p><strong>FG Long:</strong> ${player.fg_long}</p>`;
    if (player.xp_made !== undefined) card += `<p><strong>XP Made:</strong> ${player.xp_made}</p>`;
    if (player.xp_attempts !== undefined) card += `<p><strong>XP Attempts:</strong> ${player.xp_attempts}</p>`;

    card += `</div>`;
    container.innerHTML += card;
  });
}
