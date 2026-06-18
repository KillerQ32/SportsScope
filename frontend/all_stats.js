const STAT_CATEGORY_CONFIG = {
  passing: {
    title: "Passing",
    metrics: [
      { key: "pass_yards", label: "Pass Yards", color: "#2563eb" },
      { key: "pass_tds", label: "Pass TDs", color: "#16a34a" },
      { key: "pass_ints", label: "Interceptions", color: "#dc2626" }
    ],
    columns: [
      { key: "season_year", label: "Season" },
      { key: "team_name", label: "Team" },
      { key: "pass_completed", label: "Completions" },
      { key: "pass_attempts", label: "Attempts" },
      { key: "pass_yards", label: "Yards" },
      { key: "pass_tds", label: "TDs" },
      { key: "pass_ints", label: "INTs" },
      { key: "pass_long", label: "Long" }
    ]
  },
  rushing: {
    title: "Rushing",
    metrics: [
      { key: "rush_yards", label: "Rush Yards", color: "#7c3aed" },
      { key: "rush_tds", label: "Rush TDs", color: "#16a34a" },
      { key: "rush_attempts", label: "Attempts", color: "#ea580c" }
    ],
    columns: [
      { key: "season_year", label: "Season" },
      { key: "team_name", label: "Team" },
      { key: "rush_attempts", label: "Attempts" },
      { key: "rush_yards", label: "Yards" },
      { key: "rush_tds", label: "TDs" },
      { key: "longest_rush", label: "Long" }
    ]
  },
  receiving: {
    title: "Receiving",
    metrics: [
      { key: "rec_yards", label: "Receiving Yards", color: "#0891b2" },
      { key: "rec_tds", label: "Receiving TDs", color: "#16a34a" },
      { key: "receptions", label: "Receptions", color: "#d97706" },
      { key: "targets", label: "Targets", color: "#4f46e5" }
    ],
    columns: [
      { key: "season_year", label: "Season" },
      { key: "team_name", label: "Team" },
      { key: "targets", label: "Targets" },
      { key: "receptions", label: "Receptions" },
      { key: "rec_yards", label: "Yards" },
      { key: "rec_tds", label: "TDs" },
      { key: "rec_long", label: "Long" }
    ]
  },
  kicking: {
    title: "Kicking",
    metrics: [
      { key: "fg_made", label: "FG Made", color: "#2563eb" },
      { key: "fg_attempts", label: "FG Attempts", color: "#9333ea" },
      { key: "xp_made", label: "XP Made", color: "#16a34a" }
    ],
    columns: [
      { key: "season_year", label: "Season" },
      { key: "team_name", label: "Team" },
      { key: "fg_made", label: "FG Made" },
      { key: "fg_attempts", label: "FG Att" },
      { key: "fg_long", label: "FG Long" },
      { key: "xp_made", label: "XP Made" },
      { key: "xp_attempts", label: "XP Att" }
    ]
  }
};

function renderPlayerStatsDashboard(stats, playerName) {
  const container = document.getElementById("statResults");
  const categories = getAvailableCategories(stats);

  if (categories.length === 0) {
    container.innerHTML = `<p class="text-red-500 font-semibold">No stats found for "${escapeHtml(playerName)}"</p>`;
    return;
  }

  container.innerHTML = `
    <section class="space-y-6">
      ${renderPlayerSummary(stats, playerName, categories)}
      ${categories.map(([category, rows]) => renderStatCategory(category, rows)).join("")}
    </section>
  `;
}

function getAvailableCategories(stats) {
  return Object.keys(STAT_CATEGORY_CONFIG)
    .map(category => [category, Array.isArray(stats?.[category]) ? stats[category] : []])
    .filter(([, rows]) => rows.length > 0);
}

function renderPlayerSummary(stats, playerName, categories) {
  const seasons = getAllSeasons(stats);
  const rowCount = categories.reduce((total, [, rows]) => total + rows.length, 0);
  const seasonText = seasons.length ? seasons.join(", ") : "No seasons";
  const latestSeason = seasons.length ? Math.max(...seasons) : "-";

  return `
    <div class="bg-white shadow p-5 rounded">
      <div class="flex flex-col gap-2 sm:flex-row sm:items-end sm:justify-between">
        <div>
          <p class="text-sm uppercase tracking-wide text-gray-500">All-year stat profile</p>
          <h2 class="text-3xl font-bold text-gray-900">${escapeHtml(playerName)}</h2>
        </div>
        <p class="text-sm text-gray-600">Latest season: <strong>${escapeHtml(latestSeason)}</strong></p>
      </div>

      <div class="grid gap-3 sm:grid-cols-3 mt-5">
        <div class="border rounded p-3">
          <p class="text-xs uppercase text-gray-500">Seasons</p>
          <p class="text-lg font-semibold">${escapeHtml(seasonText)}</p>
        </div>
        <div class="border rounded p-3">
          <p class="text-xs uppercase text-gray-500">Stat groups</p>
          <p class="text-lg font-semibold">${categories.length}</p>
        </div>
        <div class="border rounded p-3">
          <p class="text-xs uppercase text-gray-500">Rows returned</p>
          <p class="text-lg font-semibold">${formatNumber(rowCount)}</p>
        </div>
      </div>
    </div>
  `;
}

function renderStatCategory(category, rows) {
  const config = STAT_CATEGORY_CONFIG[category];
  const sortedRows = [...rows].sort(sortBySeasonThenTeam);
  const aggregatedRows = aggregateRowsBySeason(sortedRows, config.metrics.map(metric => metric.key));
  const chartMetrics = config.metrics.filter(metric =>
    aggregatedRows.some(row => Number.isFinite(parseStatNumber(row[metric.key])))
  );

  return `
    <article class="bg-white shadow p-5 rounded space-y-5">
      <div class="flex flex-col gap-1 sm:flex-row sm:items-end sm:justify-between">
        <div>
          <h3 class="text-2xl font-bold text-indigo-700">${config.title} Trends</h3>
          <p class="text-sm text-gray-600">${formatNumber(aggregatedRows.length)} season${aggregatedRows.length === 1 ? "" : "s"} found</p>
        </div>
      </div>

      ${chartMetrics.length ? `
        <div class="grid gap-4 lg:grid-cols-2">
          ${chartMetrics.map(metric => renderTrendChart(aggregatedRows, metric)).join("")}
        </div>
      ` : `<p class="text-sm text-gray-500">No numeric trend fields found for this stat group.</p>`}

      ${renderStatsTable(sortedRows, config.columns)}
    </article>
  `;
}

function renderTrendChart(rows, metric) {
  const points = rows
    .map(row => ({
      year: Number(row.season_year),
      value: parseStatNumber(row[metric.key])
    }))
    .filter(point => Number.isFinite(point.year) && Number.isFinite(point.value))
    .sort((a, b) => a.year - b.year);

  if (points.length === 0) return "";

  const width = 640;
  const height = 260;
  const margin = { top: 28, right: 24, bottom: 42, left: 64 };
  const chartWidth = width - margin.left - margin.right;
  const chartHeight = height - margin.top - margin.bottom;
  const maxValue = Math.max(...points.map(point => point.value), 1);
  const yMax = maxValue === 0 ? 1 : maxValue * 1.15;
  const latest = points[points.length - 1];

  const coordinates = points.map((point, index) => {
    const x = points.length === 1
      ? margin.left + chartWidth / 2
      : margin.left + (index / (points.length - 1)) * chartWidth;
    const y = margin.top + chartHeight - (point.value / yMax) * chartHeight;
    return { ...point, x, y };
  });

  const polyline = coordinates.map(point => `${point.x},${point.y}`).join(" ");
  const yTicks = [0, 1, 2, 3, 4].map(index => {
    const value = yMax - (index / 4) * yMax;
    const y = margin.top + (index / 4) * chartHeight;
    return `
      <g>
        <line x1="${margin.left}" y1="${y}" x2="${width - margin.right}" y2="${y}" stroke="#e5e7eb" stroke-width="1" />
        <text x="${margin.left - 10}" y="${y + 4}" text-anchor="end" font-size="12" fill="#6b7280">${formatCompactNumber(value)}</text>
      </g>
    `;
  }).join("");

  return `
    <div class="border rounded bg-gray-50 p-4">
      <div class="flex items-center justify-between gap-3 mb-2">
        <h4 class="font-semibold text-gray-800">${escapeHtml(metric.label)}</h4>
        <span class="text-sm text-gray-600">${latest.year}: <strong>${formatNumber(latest.value)}</strong></span>
      </div>

      <svg class="w-full h-auto" viewBox="0 0 ${width} ${height}" role="img" aria-label="${escapeHtml(metric.label)} trend chart">
        <rect x="0" y="0" width="${width}" height="${height}" rx="8" fill="#f9fafb"></rect>
        ${yTicks}
        <line x1="${margin.left}" y1="${height - margin.bottom}" x2="${width - margin.right}" y2="${height - margin.bottom}" stroke="#9ca3af" stroke-width="1.5" />
        <line x1="${margin.left}" y1="${margin.top}" x2="${margin.left}" y2="${height - margin.bottom}" stroke="#9ca3af" stroke-width="1.5" />
        <polyline fill="none" stroke="${metric.color}" stroke-width="4" stroke-linecap="round" stroke-linejoin="round" points="${polyline}" />
        ${coordinates.map(point => `
          <g>
            <circle cx="${point.x}" cy="${point.y}" r="5" fill="${metric.color}">
              <title>${point.year}: ${formatNumber(point.value)}</title>
            </circle>
            <text x="${point.x}" y="${point.y - 10}" text-anchor="middle" font-size="12" fill="#374151">${formatCompactNumber(point.value)}</text>
            <text x="${point.x}" y="${height - 18}" text-anchor="middle" font-size="12" fill="#374151">${point.year}</text>
          </g>
        `).join("")}
      </svg>
    </div>
  `;
}

function renderStatsTable(rows, columns) {
  const activeColumns = columns.filter(column =>
    rows.some(row => row[column.key] !== undefined && row[column.key] !== null)
  );

  if (activeColumns.length === 0) return "";

  return `
    <div class="overflow-x-auto border rounded">
      <table class="min-w-full text-sm">
        <thead class="bg-gray-100 text-gray-700">
          <tr>
            ${activeColumns.map(column => `<th class="text-left px-3 py-2 font-semibold">${escapeHtml(column.label)}</th>`).join("")}
          </tr>
        </thead>
        <tbody class="divide-y divide-gray-200">
          ${rows.map(row => `
            <tr>
              ${activeColumns.map(column => `<td class="px-3 py-2 whitespace-nowrap">${formatCell(row[column.key])}</td>`).join("")}
            </tr>
          `).join("")}
        </tbody>
      </table>
    </div>
  `;
}

function aggregateRowsBySeason(rows, metricKeys) {
  const bySeason = new Map();

  rows.forEach(row => {
    const season = Number(row.season_year);
    if (!Number.isFinite(season)) return;

    if (!bySeason.has(season)) {
      bySeason.set(season, { season_year: season, teams: new Set() });
    }

    const bucket = bySeason.get(season);
    if (row.team_name) bucket.teams.add(row.team_name);

    metricKeys.forEach(key => {
      const value = parseStatNumber(row[key]);
      if (Number.isFinite(value)) {
        bucket[key] = (bucket[key] || 0) + value;
      }
    });
  });

  return [...bySeason.values()]
    .map(row => ({
      ...row,
      teams: [...row.teams].join(", ")
    }))
    .sort((a, b) => a.season_year - b.season_year);
}

function getAllSeasons(stats) {
  const seasons = new Set();

  Object.values(stats || {}).forEach(rows => {
    if (!Array.isArray(rows)) return;
    rows.forEach(row => {
      const season = Number(row.season_year);
      if (Number.isFinite(season)) seasons.add(season);
    });
  });

  return [...seasons].sort((a, b) => a - b);
}

function sortBySeasonThenTeam(a, b) {
  const seasonA = Number(a.season_year) || 0;
  const seasonB = Number(b.season_year) || 0;
  if (seasonA !== seasonB) return seasonA - seasonB;
  return String(a.team_name || "").localeCompare(String(b.team_name || ""));
}

function parseStatNumber(value) {
  if (value === null || value === undefined || value === "") return null;
  const parsed = Number(String(value).replace(/,/g, ""));
  return Number.isFinite(parsed) ? parsed : null;
}

function formatCell(value) {
  if (value === null || value === undefined || value === "") return "-";
  const numericValue = parseStatNumber(value);
  if (Number.isFinite(numericValue) && String(value).trim() !== "") {
    return formatNumber(numericValue);
  }
  return escapeHtml(value);
}

function formatNumber(value) {
  const numericValue = Number(value);
  if (!Number.isFinite(numericValue)) return escapeHtml(value);
  return numericValue.toLocaleString();
}

function formatCompactNumber(value) {
  const numericValue = Number(value);
  if (!Number.isFinite(numericValue)) return "-";
  if (Math.abs(numericValue) >= 1000) {
    return `${(numericValue / 1000).toFixed(numericValue >= 10000 ? 0 : 1)}k`;
  }
  return `${Math.round(numericValue)}`;
}

function escapeHtml(value) {
  return String(value)
    .replace(/&/g, "&amp;")
    .replace(/</g, "&lt;")
    .replace(/>/g, "&gt;")
    .replace(/"/g, "&quot;")
    .replace(/'/g, "&#039;");
}
