import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from mplfinance.original_flavor import candlestick_ohlc
import matplotlib.dates as mpdates
reads = pd.read_csv('AAPL.csv')
reads = reads.round(2)
reads['Date'] = pd.to_datetime(reads['Date'])
average_price = np.mean(reads['Close']).round(2)
highest_price = np.max(reads['High']).round(2)
lowest_price = np.min(reads['Low']).round(2)
print("Average Closing Price:", average_price)
print("Highest Stock Price:", highest_price)
print("Lowest Stock Price:", lowest_price)
reads['Date'] = reads['Date'].map(mpdates.date2num)
data = reads[['Date', 'Open', 'High', 'Low', 'Close']]
fig, ax = plt.subplots(figsize=(12,6))
candlestick_ohlc(
    ax,
    data.values,
    width=0.6,
    colorup='green',
    colordown='red'
)
plt.text(
    0.02,
    0.95,
    f'Average: {average_price}\nHighest: {highest_price}\nLowest: {lowest_price}',
    transform=ax.transAxes,
    fontsize=10,
    verticalalignment='top'
)

ax.xaxis_date()
plt.title('Apple Stock Candlestick Chart')
plt.xlabel('Date')
plt.ylabel('Stock Price')
plt.xticks(rotation=45)
plt.show()