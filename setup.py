import pandas as pd
import yfinance as yf
from datetime import datetime
import numpy as np
from statsmodels.tsa.arima.model import ARIMA

uber = yf.Ticker("UBER")

# Get historical market data
hist = uber.history(period="1y")  # For example, fetch data for the past year

# Display the first few rows
print(hist.head())

# Fetch financials
financials = uber.financials
balance_sheet = uber.balance_sheet
cashflow = uber.cashflow

# Display annual financial statements
print("Income Statement:\n", financials)
print("\nBalance Sheet:\n", balance_sheet)
print("\nCash Flow Statement:\n", cashflow)
# Current Price
current_price = hist['Close'].iloc[-1]

# Earnings Per Share (EPS) - using trailing 12 months
eps = uber.info['trailingEps'] if 'trailingEps' in uber.info else None

# Calculate P/E Ratio if EPS is available
pe_ratio = current_price / eps if eps else "N/A"
#data anylsis