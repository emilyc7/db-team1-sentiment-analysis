from company_identifier import find_ticker as ft
import pandas_datareader.data as web
import datetime as dt
import json
import pandas as pd
import numpy as np
import csv


def stock_to_JSON(compname):
    # sets the start and end date for ticker data
    # print('This is: ' + compname)
    start = dt.datetime(2019, 1, 1)
    end = dt.datetime.now()

    # uses find_ticker from company_identifier
    tickName = ft(compname)

    # Gets the stock data from Yahoo API
    df = web.DataReader(tickName, "yahoo", start, end)
    df = df.loc[:, ["Close"]]
    indexNamesArr = df.index.values
    dates = list(indexNamesArr)
    arr = df.to_numpy()
    price = list()
    for elt in arr:
        elt = elt[0]
        price.append(elt)
    datesStr = list()
    for date in dates:
        date = str(date)[:10]
        datesStr.append(date)
    # d = df.to_dict(orient='split')
    return datesStr, price

    def myconverter(o):
        if isinstance(o, dt.datetime):
            return o.__str__()
    j = json.dumps(d, default=myconverter)
    print(j)
    return j

stock_to_JSON('Apple')

