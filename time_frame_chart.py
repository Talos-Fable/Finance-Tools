#####################Create a chart for a specifc time frame ##########################

import yfinance as yf
import matplotlib.pyplot as plt

def fetch_stock_data(symbol, start_date, end_date):
    """ Fetch stock data for a specific symbol between two dates. """
    stock_data = yf.download(symbol, start=start_date, end=end_date)
    return stock_data

def print_stock_chart(stock_data, symbol):
    """ Print a line chart of the stock's closing prices. """
    stock_data['Close'].plot(title=f"{symbol} Stock Price")
    plt.xlabel("Date")
    plt.ylabel("Close Price")
    plt.show()

def main():
    symbol = input("Enter the stock symbol (e.g., AAPL): ")
    start_date = input("Enter start date (YYYY-MM-DD): ")
    end_date = input("Enter end date (YYYY-MM-DD): ")

    # Fetching the stock data
    data = fetch_stock_data(symbol, start_date, end_date)

    # Printing the stock chart
    if not data.empty:
        print_stock_chart(data, symbol)
    else:
        print("No data available for the given symbol and date range.")

if __name__ == "__main__":
    main()

