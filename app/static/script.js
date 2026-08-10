const index_levels_btn = document.getElementById("index-levels-btn");
const portfolio_performance_btn = document.getElementById("portfolio-performance-btn");
const active_return_btn = document.getElementById("active-return-btn");
const results_section = document.getElementById("results");

async function getData(url) {
  try {
    const response = await fetch(url);
    if (!response.ok) {
      throw new Error(`Response status: ${response.status}`);
    }

    const result = await response.json();
    return result;
  } catch (error) {
    console.error(error.message);
  }
}

function renderTable({ data }) {
  let th = "";
  for (let header of Object.keys(data[0])) {
    th += `<th>${header}</th>`;
  }

  let rows = "";
  for (let row of data) {
    rows += "<tr>";
    for (let value of Object.values(row)) {
      rows += `<td>${value}</td>`;
    }
    rows += "</tr>";
  }

  return `<table><thead><tr>${th}</tr></thead><tbody>${rows}</tbody></table>`;
}

index_levels_btn.addEventListener("click", async () => {
  results_section.innerText = "Loading Index Levels...";

  const url = "/index-levels";
  const data = await getData(url);

  const rendered_data = renderTable(data);

  results_section.innerHTML = rendered_data;
});

portfolio_performance_btn.addEventListener("click", async () => {
  results_section.innerText = "Loading Portfolio Performance...";

  const url = "/portfolio-performance";
  const data = await getData(url);

  const rendered_data = renderTable(data);

  results_section.innerHTML = rendered_data;
});

active_return_btn.addEventListener("click", async () => {
  results_section.innerText = "Loading Active Returns...";

  const url = "/active-return";
  const data = await getData(url);

  const rendered_data = renderTable(data);

  results_section.innerHTML = rendered_data;
});
