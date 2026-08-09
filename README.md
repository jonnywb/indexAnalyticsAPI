## What it does

This is a small Flask API for simple index and portfolio analytics.

It loads sample constituent, price, and portfolio data, then calculates index levels, portfolio performance, and active return.

## Endpoints

- `/index-levels` returns daily market cap, index level, and benchmark daily return
- `/portfolio-performance` returns daily portfolio value and portfolio return
- `/active-return` returns portfolio return, benchmark return, and active return

## Running locally

Create and activate a virtual environment, install the requirements, then run the Flask app.

## Tests

Run `python -m pytest` from the project root to run the test suite.
