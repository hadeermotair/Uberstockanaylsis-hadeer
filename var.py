import pandas as pd
import numpy as np
import yfinance as yf
from statsmodels.tsa.arima.model import ARIMA
from statsmodels.tsa.stattools import adfuller

# Fetch historical market data for Uber
#uber = yf.Ticker("UBER")
hist = yf.download("UBER", period = '1y')


# Prepare the DataFrame
df = hist[['Adj Close']]

# Check for stationarity with the Augmented Dickey-Fuller test
adf_result = adfuller(df['Adj Close'])
if adf_result[1] > 0.05:
    # If the series is not stationary, difference it
    df['Adj Close'] = df['Adj Close'].diff().dropna()

# Fit the ARIMA model
model = ARIMA(df['Adj Close'], order=(1, 1, 1))
model_fit = model.fit()

# Forecast the next 5 days
forecast_result = model_fit.forecast(steps=30)
print (forecast_result)

#forecasted_prices = pd.Series(forecast_result)
#forecast_returns = forecasted_prices.pct_change().dropna()

# Assuming forecast_result are forecasted prices
# Convert these forecasts into returns
forecasted_prices = pd.Series(forecast_result, index=range(len(df['Adj Close']), len(df['Adj Close']) + 5))
forecast_returns = forecasted_prices.pct_change().dropna()

# Proceed with VaR calculation
confidence_level = 0.05
var_95 = np.percentile(forecast_returns, 100 * confidence_level)
var_95_abs = abs(var_95)

print(f"The 95% Value at Risk (VaR) based on forecasted returns is: {var_95_abs*100:.2f}%")




