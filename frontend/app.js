const content = document.getElementById('content');

// ✅ LANDING PAGE
function loadHome() {
  content.innerHTML = `
    <section class="text-center max-w-3xl mx-auto py-12 px-4">
      <h1 class="text-4xl font-bold mb-4 text-indigo-700">Welcome to SportsScope 🏈</h1>

      <p class="text-gray-700 text-lg mb-6">
        SportsScope is your interactive dashboard for exploring NFL stats. Whether you're a casual fan or a data nerd,
        this app helps you dive deep into player performance, team stats, and fun challenges that test your football knowledge.
      </p>

      <div class="text-left mb-8 space-y-3">
        <h2 class="text-xl font-semibold text-gray-800">🔍 What can you do here?</h2>
        <ul class="list-disc list-inside text-gray-600 space-y-1">
          <li>📊 Track player stats over time and by season</li>
          <li>🕵️ Play <strong>Guess That Player</strong> — guess the player based on stats, year, and position (no names!)</li>
          <li>📂 Browse stats by type: Rushing, Passing, Kicking, Receiving</li>
          <li>🏟️ Explore team performance and rosters</li>
        </ul>
      </div>

      <div class="flex justify-center gap-4 flex-wrap mb-12">
        <button onclick="loadStats('rushing')" class="bg-indigo-600 hover:bg-indigo-700 text-white px-6 py-3 rounded-md transition">
          Browse Rushing Stats
        </button>
        <button onclick="loadGuessGame()" class="bg-yellow-500 hover:bg-yellow-600 text-white px-6 py-3 rounded-md transition">
          Try Guess the Player
        </button>
        <button onclick="loadTeams()" class="bg-gray-800 hover:bg-gray-900 text-white px-6 py-3 rounded-md transition">
          View Teams
        </button>
      </div>

      <hr class="my-10 border-t">

      <div class="mt-8">
        <label for="searchInput" class="block text-lg font-semibold mb-2">Search for a specific player:</label>
        <div class="flex justify-center gap-2">
          <input id="searchInput" type="text" placeholder="e.g., Jalen Hurts" class="border p-2 rounded w-64" />
          <button onclick="getAllStatsFromInput()" class="bg-blue-600 text-white px-4 py-2 rounded">
            Search Stats
          </button>
        </div>
        <div id="statResults" class="mt-6 text-left"></div>
      </div>
    </section>
  `;
}

// ✅ SEARCH STATS BY NAME
function getAllStatsFromInput() {
  const name = document.getElementById('searchInput').value;
  if (!name) return;
  getAllStats(name);
}

function getAllStats(playerName) {
  fetch(`http://localhost:8000/all/stats?player_name=${playerName}`)
    .then(res => res.json())
    .then(stats => {
      const results = document.getElementById('statResults');
      results.innerHTML = '';

      for (const [statType, entries] of Object.entries(stats)) {
        if (entries.length === 0) continue;
        results.innerHTML += `
          <div class="bg-white shadow-md p-4 rounded mb-4">
            <h2 class="text-xl font-semibold mb-2 capitalize">${statType} Stats</h2>
            ${entries.map(stat => `
              <div class="border-t pt-2 text-sm">
                ${Object.entries(stat).map(([key, val]) => `
                  <p><strong>${key}:</strong> ${val}</p>
                `).join('')}
              </div>
            `).join('')}
          </div>
        `;
      }

      if (results.innerHTML.trim() === '') {
        results.innerHTML = `<p class="text-red-500 font-semibold">No stats found for "${playerName}"</p>`;
      }
    })
    .catch(err => {
      console.error("Fetch error:", err);
      document.getElementById('statResults').innerHTML = `<p class="text-red-500">Error loading stats.</p>`;
    });
}

// ✅ STUB PAGES (PLACEHOLDER FOR NOW)
function loadStats(type) {
  if (type !== 'rushing') {
    content.innerHTML = `<h2 class="text-2xl font-bold text-center mt-10">${type.toUpperCase()} Stats Page (Coming Soon)</h2>`;
    return;
  }

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

      <!-- Results -->
      <div id="rushResults" class="pt-8 space-y-4"></div>
    </section>
  `;
}

function fetchTopRushers() {
  fetch("http://localhost:8000/rushing/players/2024?player_name=a")
    .then(res => res.json())
    .then(data => {
      // Sort by rush_yards, take top 3
      const top3 = data.sort((a, b) => b.rush_yards - a.rush_yards).slice(0, 3);
      const container = document.getElementById('topRushers');

      top3.forEach(player => {
        container.innerHTML += `
          <div class="bg-white shadow p-4 rounded text-sm">
            <h4 class="text-lg font-semibold">${player.player_name}</h4>
            <p><strong>Position:</strong> ${player.position}</p>
            <p><strong>Yards:</strong> ${player.rush_yards}</p>
            <p><strong>TDs:</strong> ${player.rush_tds}</p>
            <p><strong>Longest Run:</strong> ${player.longest_rush}</p>
          </div>
        `;
      });
    });
}


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

  // All years (only name search supported)
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

  // Search by year
  if (filter === 'name') {
    fetch(`http://localhost:8000/rushing/players/${year}?player_name=${value}`)
      .then(res => res.json())
      .then(renderRusherResults);
  } else if (filter === 'yards') {
    fetch(`http://localhost:8000/rushing/yds?min_yards=${value}`)
      .then(res => res.json())
      .then(data => {
        const filtered = data.filter(p => p.season_year == year); // apply year filter manually
        renderRusherResults(filtered)
      });
  } else if (filter === 'tds') {
    fetch(`http://localhost:8000/rushing/tds?min_tds=${value}`)
      .then(res => res.json())
      .then(data => {
        const filtered = data.filter(p => p.season_year == year); // filter manually
        renderRusherResults(filtered);
      });
  }
}


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


function handleModeChange() {
  const mode = document.querySelector('input[name="searchMode"]:checked').value;
  const yearWrapper = document.getElementById('yearInputWrapper');
  if (mode === 'year') {
    yearWrapper.classList.remove('hidden');
  } else {
    yearWrapper.classList.add('hidden');
  }
}

function loadGuessGame() {
  content.innerHTML = `<h2 class="text-2xl font-bold text-center mt-10">Guess That Player Game (Coming Soon)</h2>`;
}

function loadTeams() {
  content.innerHTML = `<h2 class="text-2xl font-bold text-center mt-10">Teams Page (Coming Soon)</h2>`;
}

// ✅ LOAD HOME SCREEN ON FIRST VISIT
document.addEventListener('DOMContentLoaded', loadHome);
