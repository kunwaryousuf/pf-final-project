import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from mplfinance.original_flavor import candlestick_ohlc
import matplotlib.dates as mpdates

# Read CSV file
reads = pd.read_csv('AAPL.csv')

# Reduce decimal values
reads = reads.round(2)

# Convert Date column
reads['Date'] = pd.to_datetime(reads['Date'])

# NumPy Analysis
average_price = np.mean(reads['Close']).round(2)
highest_price = np.max(reads['High']).round(2)
lowest_price = np.min(reads['Low']).round(2)

# Print analysis
print("Average Closing Price:", average_price)
print("Highest Stock Price:", highest_price)
print("Lowest Stock Price:", lowest_price)

# Convert dates into matplotlib format
reads['Date'] = reads['Date'].map(mpdates.date2num)

# Select required columns
data = reads[['Date', 'Open', 'High', 'Low', 'Close']]

# Create graph window
fig, ax = plt.subplots(figsize=(12,6))

# Create candlestick chart
candlestick_ohlc(
    ax,
    data.values,
    width=0.6,
    colorup='green',
    colordown='red'
)

# Format x-axis dates
ax.xaxis_date()

# Add title and labels
plt.title('Apple Stock Candlestick Chart')
plt.xlabel('Date')
plt.ylabel('Stock Price')

# Rotate dates
plt.xticks(rotation=45)

# Show graph
plt.show()