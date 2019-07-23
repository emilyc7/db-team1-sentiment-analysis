from company_identifier import find_ticker as ft
import pandas_datareader.data as web
import datetime as dt
import json
import csv

def stock_to_JSON(compname):
    # sets the start and end date for ticker data
    start = dt.datetime(2019, 1, 1)
    end = dt.datetime.now()

    # uses find_ticker from company_identifier
    tickName = ft(compname)

    # Gets the stock data from Yahoo API
    df = web.DataReader(tickName, "yahoo", start, end)
    d = df.to_dict(orient='split')

    def myconverter(o):
        if isinstance(o, dt.datetime):
            return o.__str__()
    j = json.dumps(d, default=myconverter)
    return j


