import FinanceDataReader as fdr
import mplfinance as mpf
from mplfinance.original_flavor import candlestick_ohlc
import datetime
from dateutil.relativedelta import relativedelta
import yfinance as yf
import matplotlib.dates as mpdates
import matplotlib.pyplot as plt


if __name__ == '__main__':

    name = '005930'
    end_date = datetime.datetime.today()
    start_date = end_date - relativedelta(months=1)
    df = fdr.DataReader(name, start_date, end_date)
    print(df)
    df['Close'].plot()
    # df_show = df.copy()
    # df_show['Date'] = df_show.index
    # df_show['Date'] = df_show['Date'].map(mpdates.date2num)
    # df_show = df_show[['Date', 'Open', 'High', 'Low','Close']]
    
    # fig, ax = plt.subplots()
    # candlestick_ohlc(ax, df_show.values, width=0.6, colordown='b', colorup='r', alpha=1)
    # ax.grid(True)

    # date_format = mpdates.DateFormatter('%M/%d')

    # years = mpdates.YearLocator()
    # ax.xaxis.set_major_locator(month)
    # ax.xaxis.set_major_formatter(date_format)

    # # fig.autofmt_xdate()

    # fig.tight_layout()

    # plt.show()