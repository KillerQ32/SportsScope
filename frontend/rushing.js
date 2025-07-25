// ===================== rushing.js =====================

// Load Rushing Stats Page
function loadStats(type) {
  if (type !== 'rushing') return;

  content.innerHTML = `
    <section class="max-w-4xl mx-auto py-8 px-4 space-y-6">
      <h2 class="text-3xl font-bold text-indigo-700 mb-2">🏈 Search Rushing Stats</h2>

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
          <option value="yards">Min Yards</option>
          <option value="tds">Min TDs</option>
        </select>
        <input id="filterValue" class="border p-2 rounded w-64 mt-2 block" placeholder="Enter value..." />
      </div>

      <button onclick="runRushingSearch()" class="mt-4 bg-blue-600 text-white px-6 py-2 rounded">Search</button>

      <div id="rushResults" class="pt-8 space-y-4"></div>
    </section>
  `;
}

// Run Rushing Search
function runRushingSearch() {
  const mode = document.querySelector('input[name="searchMode"]:checked').value;
  const year = document.getElementById('selectedYear').value.trim();
  const filter = document.getElementById('filterType').value;
  const value = document.getElementById('filterValue').value.trim();
  const results = document.getElementById('rushResults');
  results.innerHTML = '';

  if (mode === 'year' && year === '') {
    results.innerHTML = `<p class="text-red-500 font-semibold">Please enter a year when using 'Search by Year' mode.</p>`;
    return;
  }

  if (!value) {
    results.innerHTML = `<p class="text-red-500">Please enter a filter value.</p>`;
    return;
  }

  if (mode === 'all' && filter === 'name') {
    fetch(`http://localhost:8000/rushing/players?player_name=${value}`)
      .then(res => res.json())
      .then(renderRusherResults);
    return;
  }

  if (mode === 'all') {
    results.innerHTML = `<p class="text-red-500">All years mode only supports name search.</p>`;
    return;
  }

  if (filter === 'name') {
    fetch(`http://localhost:8000/rushing/players?player_name=${value}`)
      .then(res => res.json())
      .then(data => {
        const filtered = data.filter(p => p.season_year == year);
        renderRusherResults(filtered);
      });
  } else if (filter === 'yards') {
    fetch(`http://localhost:8000/rushing/yds?min_yards=${value}`)
      .then(res => res.json())
      .then(data => {
        const filtered = data.filter(p => p.season_year == year);
        renderRusherResults(filtered);
      });
  } else if (filter === 'tds') {
    fetch(`http://localhost:8000/rushing/tds?min_tds=${value}`)
      .then(res => res.json())
      .then(data => {
        const filtered = data.filter(p => p.season_year == year);
        renderRusherResults(filtered);
      });
  }
}

// Render Results
function renderRusherResults(data) {
  const container = document.getElementById("rushResults");
  if (!data || data.length === 0) {
    container.innerHTML = `<p class="text-red-500">No results found.</p>`;
    return;
  }

  data.forEach(player => {
    container.innerHTML += `
      <div class="bg-white shadow p-4 rounded text-sm">
        <h4 class="text-lg font-semibold">${player.player_name}</h4>
        <p><strong>Season:</strong> ${player.season_year}</p>
        <p><strong>Yards:</strong> ${player.rush_yards}</p>
        <p><strong>TDs:</strong> ${player.rush_tds}</p>
        <p><strong>Attempts:</strong> ${player.rush_attempts}</p>
        ${player.longest_rush ? `<p><strong>Longest:</strong> ${player.longest_rush}</p>` : ''}
      </div>
    `;
  });
}
