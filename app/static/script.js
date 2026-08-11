const indexLevelsBtn = document.getElementById("index-levels-btn");
const portfolioPerformanceBtn = document.getElementById("portfolio-performance-btn");
const activeReturnBtn = document.getElementById("active-return-btn");
const resultsSection = document.getElementById("results__inner");

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

function renderTable(data) {
  let th = "";
  for (const header of Object.keys(data[0])) {
    th += `<th>${header}</th>`;
  }

  let rows = "";
  for (const row of data) {
    rows += "<tr>";
    for (const value of Object.values(row)) {
      rows += `<td>${value}</td>`;
    }
    rows += "</tr>";
  }

  return `<table><thead><tr>${th}</tr></thead><tbody>${rows}</tbody></table>`;
}

async function loadTable(url, loadingMessage, errorLabel) {
  resultsSection.innerText = loadingMessage;

  const result = await getData(url);

  if (result.status === "ok") {
    resultsSection.innerHTML = renderTable(result.data);
  } else {
    resultsSection.innerHTML = `
      <p>Error loading ${errorLabel}</p>
      <p>${result.message}</p>
    `;
  }
}

indexLevelsBtn.addEventListener("click", () => {
  loadTable("/index-levels", "Loading Index Levels...", "Index Levels");
});

portfolioPerformanceBtn.addEventListener("click", () => {
  loadTable("/portfolio-performance", "Loading Portfolio Performance...", "Portfolio Performance");
});

activeReturnBtn.addEventListener("click", () => {
  loadTable("/active-return", "Loading Active Return...", "Active Return");
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
