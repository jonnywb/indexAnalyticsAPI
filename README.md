# Index Analytics Dashboard

A small Flask dashboard that calculates and displays benchmark index levels, portfolio performance, and active return using sample financial data.

This project was built as a junior developer practice project to demonstrate Python, pandas, Flask, pytest, JavaScript, and Chart.js in a finance-style analytics workflow. It focuses on taking simple constituent, price, and portfolio data, turning that data into useful calculations, and presenting the results in both table and graph form.

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
