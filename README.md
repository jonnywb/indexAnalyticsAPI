# Index Analytics Dashboard

A Flask-based analytics dashboard that calculates and displays benchmark index levels, portfolio performance, and active return using sample financial data.

This project was built as a portfolio project to practise financial analytics and data presentation using Python, pandas, Flask, pytest, JavaScript, and Chart.js. It focuses on taking simple constituent, price, and portfolio data, turning that data into useful calculations, and presenting the results in both table and graph form.

## Features

- Calculate market capitalisation and index weights for benchmark constituents
- Build a simple market-cap-weighted index level over time
- Calculate daily portfolio value from holdings and prices
- Calculate portfolio return over time
- Calculate active return versus the benchmark
- Validate price data and test core calculations with pytest
- View results in either table or graph mode
- Toggle between light and dark theme

## Tech stack

- Python
- Flask
- pandas
- pytest
- HTML
- CSS
- JavaScript
- Chart.js

## Project structure

```text
app/
  services/
  routes.py
data/
tests/
static/
templates/
run.py
README.md
```

## Data used

The project uses sample financial datasets stored locally as CSV files.

These include:

- benchmark constituent data
- historical price data
- sample portfolio holdings

The data is intentionally simple and is designed to support calculation logic, validation, and dashboard presentation rather than model real market behaviour in full detail.

## Calculations included

### 1. Market capitalisation

For each constituent:

```text
market_cap = shares_outstanding × close_price
```

### 2. Index weight

For each constituent on a given date:

```text
weight = constituent_market_cap / total_market_cap
```

### 3. Portfolio value

For each holding:

```text
position_value = units_held × close_price
```

Daily portfolio value is then calculated by summing all position values for each date.

### 4. Portfolio return

Portfolio return is calculated from the daily total portfolio value series.

### 5. Active return

```text
active_return = portfolio_return - benchmark_return
```

In this project, the benchmark return is the daily return of the calculated index.

## Running the project

### 1. Create and activate a virtual environment

```bash
python -m venv venv
source venv/bin/activate
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the Flask app

```bash
python run.py
```

Then open the local Flask URL shown in the terminal.

## Running tests

Run the test suite with:

```bash
python -m pytest
```

Current test coverage includes:

- market-cap weights summing to 1
- duplicate price validation
- portfolio value calculation on a known date
- active return calculation on a known date

## What this project demonstrates

This project is designed to show:

- working with tabular financial-style data in pandas
- joining datasets and creating derived columns
- grouping and aggregating time-series data
- validating input data
- testing calculation logic
- exposing results through Flask routes
- rendering data in a small frontend dashboard
- formatting financial values for presentation

## Possible future improvements

- Add summary cards for latest index level, portfolio value, and active return
- Improve chart styling and annotations
- Add CSV export for calculated results
- Expand validation rules for missing data and date mismatches
- Deploy the project publicly for portfolio use
