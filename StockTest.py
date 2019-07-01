import datetime as dt
import matplotlib.pyplot as plt
from matplotlib import style
import matplotlib.dates as mdates
from mpl_finance import candlestick_ohlc
import pandas_datareader.data as web
from company_identifier import find_ticker as ft
import numpy as np


# Takes in entity name as string and outputs graph of stock price as jpeg file
def stockGraph(compName):
    style.use('ggplot')
    # Sets the start and end date for stock data you need
    start = dt.datetime(2019, 1, 1)
    end = dt.datetime.now()

    # uses find_ticker from company_identifier
    tickName = ft(compName)

    # Gets the stock data from Yahoo API
    df = web.DataReader(tickName, "yahoo", start, end)

    # formats the data better
    df.reset_index(inplace=True)
    df.set_index("Date", inplace=True)

    df['Adj Close'].plot()
    plt.ylabel('Close price(USD)')
    plt.title(compName)
    plt.show()

    # Code to output data as candlestick graph

    # configuring data to work with candlestick graph format
    df_ohlc = df['Adj Close'].resample('10D').ohlc()
    df_volume = df['Volume'].resample('10D').sum()
    df_ohlc = df_ohlc.reset_index()
    df_ohlc['Date'] = df_ohlc['Date'].map(mdates.date2num)

    # Setting up the figure
    ax1 = plt.subplot2grid((6, 1), (0, 0), rowspan=5, colspan=1)
    ax1.xaxis_date()
    candlestick_ohlc(ax1, df_ohlc.values, width=2, colorup='green', colordown='red')
    ax1.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m'))
    plt.title(compName)
    plt.show()


# just to test
stockGraph("Apple")

