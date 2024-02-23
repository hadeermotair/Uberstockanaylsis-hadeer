#date all from only one year 
#MODEL BASED ON FIVE DAYS 
import pandas as pd
import yfinance as yf
from statsmodels.tsa.arima.model import ARIMA
from statsmodels.tsa.stattools import adfuller

# Fetch historical market data for Uber
uber = yf.Ticker("UBER")
hist = uber.history(period="1y")  # Fetch data for the past year

# Prepare the DataFrame
df = hist[['Close']]

# Check for stationarity with the Augmented Dickey-Fuller test
adf_result = adfuller(df['Close'])
print('ADF Statistic:', adf_result[0])
print('p-value:', adf_result[1])

# If the p-value is greater than 0.05, we cannot reject the null hypothesis (the series is not stationary),
# and you might need to difference the series. Here's how you can do it:
if adf_result[1] > 0.05:
    print("Series is not stationary. Differencing the series...")
    df['Close'] = df['Close'].diff().dropna()

# Define and fit the ARIMA model with the chosen order
model = ARIMA(df['Close'], order=(1, 1, 1))
model_fit = model.fit()

# Forecast the next 5 days
forecast_result = model_fit.get_forecast(steps=30)
print(forecast_result.summary_frame(alpha=0.05))  # alpha for 95% CI
#mean=The forecasted value for the closing price.
#Close=The index or time point for the forecasted values.
#mean_se: The standard error of the forecasted value. 
#mean_ci_lower: The lower bound of the 95% confidence interval for the forecasted value.
#mean_ci_upper: The upper bound of the 95% confidence interval for the forecasted value. 
#Quantitative Modeling
#BASED ON the The wide range between mean_ci_lower and mean_ci_upper indicates significant uncertainty in the forecasts.
#Will caculate the value of risk


