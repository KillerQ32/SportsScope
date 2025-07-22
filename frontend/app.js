const content = document.getElementById('content');

function loadHome() {
  content.innerHTML = `
    <h2 class="text-2xl font-bold mb-4">Top Players</h2>
    <div id="players" class="grid grid-cols-1 md:grid-cols-2 gap-4"></div>
  `;

  fetch('http://localhost:8000/players/') // or your actual backend URL
    .then(res => res.json())
    .then(players => {
      const playersDiv = document.getElementById('players');
      players.forEach(p => {
        playersDiv.innerHTML += `
          <div class="bg-white p-4 rounded shadow">
            <h3 class="text-lg font-semibold">${p.player_name}</h3>
            <p class="text-sm text-gray-600">${p.position}</p>
          </div>
        `;
      });
    });
}


function loadStats(type) {
  content.innerHTML = `
    <h2 class="text-2xl font-bold capitalize mb-4">${type} Stats</h2>
    <table class="w-full bg-white shadow rounded">
      <thead class="bg-gray-200">
        <tr class="text-left text-sm">
          <th class="p-2">Player</th>
          <th class="p-2">Team</th>
          <th class="p-2">Yards</th>
          <th class="p-2">TDs</th>
        </tr>
      </thead>
      <tbody id="statBody"></tbody>
    </table>
  `;

  fetch(`http://localhost:8000/${type}`) // endpoint like /rushing, /passing...
    .then(res => res.json())
    .then(stats => {
      const tbody = document.getElementById('statBody');
      stats.forEach(s => {
        tbody.innerHTML += `
          <tr class="border-t text-sm">
            <td class="p-2">${s.name}</td>
            <td class="p-2">${s.team}</td>
            <td class="p-2">${s.yards}</td>
            <td class="p-2">${s.tds}</td>
          </tr>
        `;
      });
    });
}

function loadTeams() {
  content.innerHTML = `
    <h2 class="text-2xl font-bold mb-4">Teams</h2>
    <div id="teams" class="grid grid-cols-2 md:grid-cols-4 gap-4"></div>
  `;

  fetch('http://localhost:8000/teams')
    .then(res => res.json())
    .then(teams => {
      const teamsDiv = document.getElementById('teams');
      teams.forEach(t => {
        teamsDiv.innerHTML += `
          <div class="bg-white p-4 rounded shadow text-center">
            <h3 class="text-lg font-bold">${t.name}</h3>
            <p>${t.city}</p>
          </div>
        `;
      });
    });
}

// Load home on page load
document.addEventListener('DOMContentLoaded', loadHome);
