import pandas_datareader.data as web
import datetime as dt
import pandas as pd

# https://wikidocs.net/4766
# start = datetime.datetime.now()
# end = datetime.datetime.now()
# skhynix = web.DataReader('000660.KS', 'yahoo', start, end)

df = web.DataReader('GE', 'yahoo', start='2019-09-10', end='2019-10-09')
df.head()
