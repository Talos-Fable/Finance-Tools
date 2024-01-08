

################ Find the closing price for a specifc day #################################
import yfinance as yf
import pandas as pd

def fetch_closing_prices(symbol, dates):
    """ Fetches closing prices for a stock symbol on specified dates. """
    data = yf.download(symbol, start=min(dates), end=max(dates) + pd.DateOffset(1))
    closing_prices = data['Close'][data.index.isin(dates)]
    return closing_prices

def main():
    symbol = input("Enter the stock symbol (e.g., AAPL): ")
    dates_input = input("Enter dates separated by commas (YYYY-MM-DD): ")
    dates = [pd.to_datetime(date.strip()) for date in dates_input.split(',')]

    # Fetching closing prices
    closing_prices = fetch_closing_prices(symbol, dates)

    if not closing_prices.empty:
        print("\nClosing Prices:")
        for date, price in closing_prices.items():
            print(f"{date.date()}: {price}")
    else:
        print("No data available for the given dates.")

if __name__ == "__main__":
    main()
