function loadPassingStats() {
  content.innerHTML = `
    <section class="max-w-4xl mx-auto py-8 px-4 space-y-6">
      <h2 class="text-3xl font-bold text-indigo-700 mb-2">📤 Search Passing Stats</h2>

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

      <button onclick="runPassingSearch()" class="mt-4 bg-blue-600 text-white px-6 py-2 rounded">Search</button>

      <div id="passingResults" class="pt-8 space-y-4"></div>
    </section>
  `;
}

function runPassingSearch() {
  const mode = document.querySelector('input[name="searchMode"]:checked').value;
  const year = document.getElementById('selectedYear').value.trim();
  const filter = document.getElementById('filterType').value;
  const value = document.getElementById('filterValue').value.trim();
  const results = document.getElementById('passingResults');
  results.innerHTML = '';

  if (mode === 'year' && year === '') {
    results.innerHTML = `<p class="text-red-500 font-semibold">Please enter a year when using 'Search by Year' mode.</p>`;
    return;
  }

  if (!value) {
    results.innerHTML = `<p class="text-red-500">Please enter a filter value.</p>`;
    return;
  }

  if ((filter === 'yards' || filter === 'tds') && isNaN(value)) {
    results.innerHTML = `<p class="text-red-500">Please enter a valid number for ${filter === 'yards' ? 'Yards' : 'Touchdowns'}.</p>`;
    return;
  }

  if (mode === 'all' && filter === 'name') {
    fetch(`http://localhost:8000/passing/players?player_name=${value}`)
      .then(res => res.json())
      .then(renderPassingResults);
    return;
  }

  if (mode === 'all') {
    results.innerHTML = `<p class="text-red-500">All years mode only supports name search.</p>`;
    return;
  }

  if (filter === 'name') {
    fetch(`http://localhost:8000/passing/players/${year}?player_name=${value}`)
      .then(res => {
        if (!res.ok) throw new Error(`HTTP ${res.status}`);
        return res.json();
      })
      .then(renderPassingResults)
      .catch(err => {
        results.innerHTML = `<p class="text-red-500">Error: ${err.message}</p>`;
      });
  } else if (filter === 'yards') {
    fetch(`http://localhost:8000/passing/yds?min_yards=${value}`)
      .then(res => res.json())
      .then(data => {
        const filtered = data.filter(p => p.season_year == year);
        renderPassingResults(filtered);
      });
  } else if (filter === 'tds') {
    fetch(`http://localhost:8000/passing/tds?min_tds=${value}`)
      .then(res => res.json())
      .then(data => {
        const filtered = data.filter(p => p.season_year == year);
        renderPassingResults(filtered);
      });
  }
}

function renderPassingResults(data) {
  const container = document.getElementById("passingResults");
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

    if (player.pass_yards !== undefined) card += `<p><strong>Yards:</strong> ${player.pass_yards}</p>`;
    if (player.pass_tds !== undefined) card += `<p><strong>TDs:</strong> ${player.pass_tds}</p>`;
    if (player.pass_completed !== undefined) card += `<p><strong>Completions:</strong> ${player.pass_completed}</p>`;
    if (player.pass_attempts !== undefined) card += `<p><strong>Attempts:</strong> ${player.pass_attempts}</p>`;
    if (player.pass_ints !== undefined) card += `<p><strong>INTs:</strong> ${player.pass_ints}</p>`;
    if (player.pass_long !== undefined) card += `<p><strong>Longest Pass:</strong> ${player.pass_long}</p>`;

    card += `</div>`;
    container.innerHTML += card;
  });
}
