import datetime as dt
import matplotlib.pyplot as plt
from matplotlib import style
import mplfinance
from mplfinance.original_flavor import candlestick_ohlc
import matplotlib.dates as mdates
import pandas as pd
import pandas_datareader.data as web

style.use('ggplot')

#video 1:
# start = dt.datetime(2010,1,1)
# end = dt.datetime(2020,12,31)
df = pd.read_csv('tsla to csv', parse_dates =True, index_col=0)
# df = web.DataReader('TSLA','yahoo', start, end)
# df.to_csv('tsla to csv')

#video 2:

# print(df[['Open', 'High']].head())
# df['Adj Close'].plot()
# plt.show()

#video 3:
df['100ma'] = df['Adj Close'].rolling(window=100, min_periods=0).mean()
# df.dropna(inplace=True)
# print(df.head())

ax1 = plt.subplot2grid((6,1),(0,0),rowspan=5, colspan=1)
ax2 = plt.subplot2grid((6,1),(5,0),rowspan=1, colspan=1, sharex=ax1)
# ax1.plot(df.index, df['Adj Close'])
# ax1.plot(df.index, df['100ma'])
# ax2.bar(df.index, df['Adj Close'])
# plt.show()

# #video 4: candle graph

df_ohlc = df['Adj Close'].resample('10D').ohlc() #ohlc: open high low close
df_volume = df['Volume'].resample('10D').sum()

df_ohlc.reset_index(inplace=True)
df_ohlc['Date'] = df_ohlc['Date'].map((mdates.date2num))
print(df_ohlc.head())
ax1.xaxis_date()
candlestick_ohlc(ax1, df_ohlc.values, width=2, colorup='g')
ax2.fill_between(df_volume.index.map(mdates.date2num), df_volume.values, 0)
plt.show()

