import datetime as dt
import matplotlib.pyplot as plt
from matplotlib import style
import matplotlib.dates as mdates
from mpl_finance import candlestick_ohlc
import pandas_datareader.data as web
from company_identifier import find_ticker as ft
from urllib.request import urlopen
import json
from PIL import Image


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
    plt.savefig('graph.jpeg')

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
    plt.savefig('candlestick.jpeg')


#Code for getting stock indicator icon

#Downloads json file from API
def get_jsonparsed_data(url):
    response = urlopen(url)
    data = response.read().decode("utf-8")
    return json.loads(data)

#Decides what indicator to use
def stock_indicator(companyName):
    ticker = ft(companyName)
    url = "https://financialmodelingprep.com/api/company/profile/{}?datatype=json".format(ticker)
    x = get_jsonparsed_data(url)
    y = x[ticker]['ChangesPerc']
    s = y[1]
    s1 = y[1:7]
    if s == '+':
        indicator_image("green")
        return ticker + ": " + s1 + " " + "green"
    else:
        indicator_image("red")
        return ticker + ": " + s1 + " " + "red"


# Returns the right image for the stock indicator
def indicator_image(color):
    imageUp = Image.open("StockUp.jpg")
    imageDown = Image.open("StockDown.jpg")
    if color == "green":
        return imageUp
    else:
        return imageDown




