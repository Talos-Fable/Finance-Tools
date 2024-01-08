##########Can find the close price of a stock for a specific date range when given#############
import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.arima.model import ARIMA
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf

stock_symbol = "MSFT"
start_date = "2023-05-01"
end_date = "2023-05-20"

# Get the historical data for the stock
stock_history = yf.Ticker(stock_symbol).history(start=start_date, end=end_date)

# Get the close prices for the specified date range
close_prices = stock_history["Close"]



#This code works
#Can tell you whether a the closing price for a stock was lower or higher in comparison to the previous closing price
stock_symbol = "MSFT"
start_date = "2023-05-01"
end_date = "2023-05-20"

# Get the historical data for the stock
stock_history = yf.Ticker(stock_symbol).history(start=start_date, end=end_date)

# Get the close prices for the specified date range
close_prices = stock_history["Close"]

# Initialize the previous close price
prev_close = None

# Print the close prices for each day, and whether the next day's closing price is higher
for date, close_price in close_prices.items():
    if prev_close is None:
        prev_close = close_price
    else:
        if close_price > prev_close:
            print("Close price for {} on {}: {} (Higher than previous day)".format(stock_symbol, date, close_price))
        else:
            print("Close price for {} on {}: {} (Lower than or equal to previous day)".format(stock_symbol, date, close_price))
        prev_close = close_price


#Create lists to store dates and price changes
dates_higher = []
prices_higher = []
dates_lower = []
prices_lower = []

# Initialize the previous close price
prev_close = None

# Populate lists based on whether the close price is higher or lower than the previous day
for date, close_price in close_prices.items():
    if prev_close is not None:
        if close_price > prev_close:
            dates_higher.append(date)
            prices_higher.append(close_price)
        else:
            dates_lower.append(date)
            prices_lower.append(close_price)
    prev_close = close_price

# Plotting
plt.figure(figsize=(12, 6))
plt.plot(dates_higher, prices_higher, 'g^', label='Higher than previous day', markersize=10)
plt.plot(dates_lower, prices_lower, 'rv', label='Lower than or equal to previous day', markersize=10)
plt.plot(close_prices.index, close_prices, 'b-', label='Closing Prices', alpha=0.5)
plt.title('Closing Prices of {} with Daily Changes Highlighted'.format(stock_symbol))
plt.xlabel('Date')
plt.ylabel('Close Price')
plt.legend()
plt.grid(True)
plt.show()


# ... [earlier parts of your script] ...

# Fit ARIMA model
model = ARIMA(close_prices, order=(5, 1, 0))  # Example parameters, adjust based on your dataset
model_fit = model.fit()

# Forecast future prices
num_days_to_forecast = 5  # Forecasting for 5 days as an example
forecast = model_fit.forecast(steps=num_days_to_forecast)

# Generate future dates for the forecast
# Adjust to exclude the first date and include only business days
forecast_dates = pd.date_range(start=close_prices.index[-1], periods=num_days_to_forecast+1, freq='B')[1:]

# Plot the forecast alongside historical data
plt.figure(figsize=(12, 6))
plt.plot(close_prices.index, close_prices, label='Historical Closing Prices')
plt.plot(forecast_dates, forecast, label='Forecasted Closing Prices', linestyle='--', color='orange')
plt.title('ARIMA Forecast of {} Closing Prices'.format(stock_symbol))
plt.xlabel('Date')
plt.ylabel('Close Price')
plt.legend()
plt.grid(True)
plt.show()