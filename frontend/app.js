const content = document.getElementById('content');

// homepage
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
        <button onclick="loadPlayerTrends()" class="bg-blue-600 hover:bg-blue-700 text-white px-6 py-3 rounded-md transition">
          Player Trends
        </button>
        <button onclick="loadRushingStats()" class="bg-indigo-600 hover:bg-indigo-700 text-white px-6 py-3 rounded-md transition">
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
        <label for="searchInput" class="block text-lg font-semibold mb-2">Search player trends:</label>
        <div class="flex justify-center gap-2">
          <input id="searchInput" type="text" placeholder="e.g., Jalen Hurts" class="border p-2 rounded w-64" onkeydown="if (event.key === 'Enter') getAllStatsFromInput()" />
          <button onclick="getAllStatsFromInput()" class="bg-blue-600 text-white px-4 py-2 rounded">
            View Trends
          </button>
        </div>
        <div id="statResults" class="mt-6 text-left"></div>
      </div>
    </section>
  `;
}

function loadPlayerTrends() {
  content.innerHTML = `
    <section class="max-w-6xl mx-auto py-8 px-4 space-y-6">
      <div class="bg-white shadow p-5 rounded">
        <h2 class="text-3xl font-bold text-indigo-700 mb-4">Player Trends</h2>
        <div class="flex flex-col sm:flex-row gap-3">
          <input id="searchInput" type="text" placeholder="e.g., Jalen Hurts" class="border p-3 rounded flex-1" onkeydown="if (event.key === 'Enter') getAllStatsFromInput()" />
          <button onclick="getAllStatsFromInput()" class="bg-blue-600 hover:bg-blue-700 text-white px-6 py-3 rounded">
            View All Years
          </button>
        </div>
      </div>

      <div id="statResults" class="space-y-6"></div>
    </section>
  `;
}

// homepage search bar functionality
function getAllStatsFromInput() {
  const name = document.getElementById('searchInput').value.trim();
  if (!name) return;
  getAllStats(name);
}

function getAllStats(playerName) {
  const results = document.getElementById('statResults');
  results.innerHTML = `<p class="text-gray-600">Loading ${playerName}...</p>`;

  fetch(`http://localhost:8000/all/stats?player_name=${encodeURIComponent(playerName)}`)
    .then(res => {
      if (!res.ok) throw new Error(`HTTP ${res.status}`);
      return res.json();
    })
    .then(stats => {
      renderPlayerStatsDashboard(stats, playerName);
    })
    .catch(err => {
      console.error("Fetch error:", err);
      results.innerHTML = `<p class="text-red-500">Error loading stats. Make sure the FastAPI backend is running on port 8000.</p>`;
    });
}

// shared utility for stats search bar (rush, passing, etc)
function handleModeChange() {
  const mode = document.querySelector('input[name="searchMode"]:checked').value;
  const yearWrapper = document.getElementById('yearInputWrapper');
  if (mode === 'year') {
    yearWrapper.classList.remove('hidden');
  } else {
    yearWrapper.classList.add('hidden');
  }
}

// for searching game later
function loadGuessGame() {
  content.innerHTML = `<h2 class="text-2xl font-bold text-center mt-10">Guess That Player Game (Coming Soon)</h2>`;
}

function loadTeams() {
  content.innerHTML = `<h2 class="text-2xl font-bold text-center mt-10">Teams Page (Coming Soon)</h2>`;
}

// ✅ LOAD HOME SCREEN ON FIRST VISIT
document.addEventListener('DOMContentLoaded', loadHome);
