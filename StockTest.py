import datetime as dt
import matplotlib.pyplot as plt
from matplotlib import style
import pandas_datareader.data as web
from company_identifier import find_ticker as ft


# Takes in entity name as string and outputs graph of stock pricex`
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
    plt.savefig('graph.jpeg')




