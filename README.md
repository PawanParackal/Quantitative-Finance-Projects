# Quantitative Finance Projects 📈

This repository contains institutional-grade quantitative trading strategies and financial analysis tools developed in Python.

## 🛠 Project 1: Nifty 50 Trend Follower
* **Concept:** Moving Average Crossover (20-day vs 50-day).
* **Objective:** Identifying market momentum in the Indian Benchmark Index.
* **Key Learnings:** Data wrangling with `yfinance`, handling time-series data, and visualizing trend signals.

## 🛠 Project 2: RSI Mean Reversion (Reality-Adjusted)
* **Status:** Completed - Research Phase.
* **Objective:** Test if simple RSI signals survive Indian market friction (STT, GST, Fees).
* **Key Realistic Parameters:**
    * **Execution Lag:** 1-Day shift (Signal at Close, Trade at Next Open).
    * **Transaction Costs:** 0.15% (15bps) per trade (Indian STT + Exchange charges).
* **Results:**
    * **Final Return:** -5.46% (Post-cost).
    * **Max Drawdown:** -9.63%.
* **Conclusion:** Standalone RSI signals in the Nifty 50 are not strong enough to overcome transaction costs. This necessitates a pivot to multi-factor models and machine learning filters.
* **Key Tech:** `pandas_ta` for professional-grade indicators and vectorized backtesting logic.
