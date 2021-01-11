#%%
import FinanceDataReader as fdr
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt

ticker_list = ['006400', '006405']

df_list = []
for ticker in ticker_list:
    df_list.append(fdr.DataReader(ticker, '2019-01-01', '2021-01-07'))


# date_index = df_list[0].index


series_diff = (df_list[0]['Close'] - df_list[1]['Close']) / df_list[0]['Close'] * 100
plt.plot(series_diff.index, series_diff.values) 