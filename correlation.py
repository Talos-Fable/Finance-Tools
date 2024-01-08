################This code finds the correlation coeefcient between 50 stocks. Showing how each stock correlates with the other 50##################
import yfinance as yf
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

stock_symbols = ["ES=F", "NQ=F", "YM=F", "6S=F"]

# retrieve historical data for the stocks
stock_data = {symbol: yf.Ticker(symbol).history() for symbol in stock_symbols}

# calculate the correlation coefficient between the stocks
correlations = []
for i, symbol1 in enumerate(stock_symbols):
    data1 = stock_data[symbol1]
    for j, symbol2 in enumerate(stock_symbols):
        if j>i:
            data2 = stock_data[symbol2]
            correlation = data1["Close"].corr(data2["Close"])
            correlations.append({"stock1": symbol1, "stock2": symbol2, "correlation": correlation})

# print the correlation coefficients between the stocks
for c in correlations:
    print("Correlation between {} and {}: {:.2f}".format(c["stock1"], c["stock2"], c["correlation"]))



# Create a DataFrame to store the correlation coefficients
correlation_df = pd.DataFrame(index=stock_symbols, columns=stock_symbols)

# Populate the DataFrame with the calculated correlations
for c in correlations:
    correlation_df.at[c['stock1'], c['stock2']] = c['correlation']
    correlation_df.at[c['stock2'], c['stock1']] = c['correlation']

# Fill diagonal with 1's (as a stock is perfectly correlated with itself)
np.fill_diagonal(correlation_df.values, 1)

# Convert DataFrame elements to numeric (as they are currently objects)
correlation_df = correlation_df.apply(pd.to_numeric)

# Plotting the heatmap
plt.figure(figsize=(10, 8))
sns.heatmap(correlation_df, annot=True, cmap="coolwarm")
plt.title("Correlation Heatmap between Stocks")
plt.show()