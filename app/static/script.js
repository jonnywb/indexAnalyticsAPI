const indexLevelsBtn = document.getElementById("index-levels-btn");
const portfolioPerformanceBtn = document.getElementById("portfolio-performance-btn");
const activeReturnBtn = document.getElementById("active-return-btn");
const resultsSection = document.getElementById("results__inner");
const graphBtn = document.getElementById("graph-btn");
const tableBtn = document.getElementById("table-btn");

/* ====== Data Display ===== */
let currMetricKey = "index_level";
let currURL = "/index-levels";
let currLoadingMessage = "Loading Index Levels...";
let currTitle = "Index Levels";

async function getData(url) {
  try {
    const response = await fetch(url);

    if (!response.ok) {
      throw new Error(`Response status: ${response.status}`);
    }

    const result = await response.json();
    return { status: "ok", data: result.data };
  } catch (error) {
    console.error(error.message);
    return { status: "error", message: error.message };
  }
}

function renderTable(data, title) {
  if (data.length === 0) {
    return "No data to display";
  }

  let th = "";
  for (const header of Object.keys(data[0])) {
    th += `<th>${header}</th>`;
  }

  let rows = "";
  for (const row of data) {
    rows += "<tr>";
    for (const value of Object.values(row)) {
      rows += `<td>${value ?? "-"}</td>`;
    }
    rows += "</tr>";
  }

  return `<div><h2>${title}</h2></div><table><thead><tr>${th}</tr></thead><tbody>${rows}</tbody></table>`;
}

function renderGraph(data, metricKey) {
  const datesArr = [];
  const yValues = [];
  for (const row of data) {
    datesArr.push(row["date"]);
    yValues.push(row[metricKey]);
  }

  return { canvas: `<canvas id="index-chart"></canvas>`, datesArr, yValues };
}

function createCanvas(canvas, datesArr, yValues, title) {
  resultsSection.innerHTML = canvas;
  const chartCanvas = document.getElementById("index-chart");
  const ctx = chartCanvas.getContext("2d");
  return new Chart(ctx, {
    type: "line",
    data: {
      labels: datesArr,
      datasets: [
        {
          label: title,
          data: yValues,
        },
      ],
    },
  });
}

async function loadResults(url, loadingMessage, title) {
  resultsSection.innerText = loadingMessage;

  const result = await getData(url);

  if (result.status === "ok") {
    if (view === "table") {
      resultsSection.innerHTML = renderTable(result.data, title);
    } else {
      const { canvas, datesArr, yValues } = renderGraph(result.data, currMetricKey);
      createCanvas(canvas, datesArr, yValues, title);
    }
  } else {
    resultsSection.innerHTML = `
      <p>Error loading ${title}</p>
      <p>${result.message}</p>
    `;
  }
}

indexLevelsBtn.addEventListener("click", () => {
  currMetricKey = "index_level";
  currURL = "/index-levels";
  currLoadingMessage = "Loading Index Levels...";
  currTitle = "Index Levels";
  loadResults(currURL, currLoadingMessage, currTitle);

  indexLevelsBtn.classList.add("active");
  portfolioPerformanceBtn.classList.remove("active");
  activeReturnBtn.classList.remove("active");
});

portfolioPerformanceBtn.addEventListener("click", () => {
  currMetricKey = "position_value";
  currURL = "/portfolio-performance";
  currLoadingMessage = "Loading Portfolio Performance...";
  currTitle = "Portfolio Performance";
  loadResults(currURL, currLoadingMessage, currTitle);

  portfolioPerformanceBtn.classList.add("active");
  indexLevelsBtn.classList.remove("active");
  activeReturnBtn.classList.remove("active");
});

activeReturnBtn.addEventListener("click", () => {
  currMetricKey = "active_return";
  currURL = "/active-return";
  currLoadingMessage = "Loading Active Return...";
  currTitle = "Active Return";
  loadResults(currURL, currLoadingMessage, currTitle);

  activeReturnBtn.classList.add("active");
  indexLevelsBtn.classList.remove("active");
  portfolioPerformanceBtn.classList.remove("active");
});

/* ====== Display View ======= */

let view = "table";

graphBtn.addEventListener("click", () => {
  view = "graph";
  loadResults(currURL, currLoadingMessage, currTitle);

  graphBtn.classList.add("active");
  tableBtn.classList.remove("active");
});

tableBtn.addEventListener("click", () => {
  view = "table";
  loadResults(currURL, currLoadingMessage, currTitle);

  tableBtn.classList.add("active");
  graphBtn.classList.remove("active");
});

// ===== THEME TOGGLE =====
const toggle = document.querySelector("[data-theme-toggle]");
const root = document.documentElement;
let theme = matchMedia("(prefers-color-scheme: dark)").matches ? "dark" : "light";
root.setAttribute("data-theme", theme);
updateToggleIcon();

if (toggle) {
  toggle.addEventListener("click", () => {
    theme = theme === "dark" ? "light" : "dark";
    root.setAttribute("data-theme", theme);
    toggle.setAttribute("aria-label", "Switch to " + (theme === "dark" ? "light" : "dark") + " mode");
    updateToggleIcon();
  });
}

function updateToggleIcon() {
  if (!toggle) return;
  toggle.innerHTML =
    theme === "dark"
      ? '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="5"/><path d="M12 1v2M12 21v2M4.22 4.22l1.42 1.42M18.36 18.36l1.42 1.42M1 12h2M21 12h2M4.22 19.78l1.42-1.42M18.36 5.64l1.42-1.42"/></svg>'
      : '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 12.79A9 9 0 1 1 11.21 3 7 7 0 0 0 21 12.79z"/></svg>';
}
