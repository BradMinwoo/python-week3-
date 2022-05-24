#pip install -U finance-datareader
import FinanceDataReader as fdr
import matplotlib.pyplot as plt
import pandas as pd
import mpl_finance
#pip install mpl_finance

#한국거래소 상장종목
print(fdr.__version__)
df_krx = fdr.StockListing('KRX')
KOSPI = df_krx[df_krx['Market'].str.contains('KOSPI')]
print(KOSPI.columns)
print(KOSPI)
df_samsung = fdr.DataReader('005930','2015')
print(df_samsung)
print(df_samsung.describe())

df_apple = fdr.DataReader('GOOG','2022-01-01','2022-05-24')
print(df_apple)

# write = pd.ExcelFile('apple.xlsx', engine='xlsxwriter')
# df_apple.to_excel(write, sheet_name='Sheet1')
# write.close()

fig = plt.figure(figsize=(12,8))
ax  = fig.add_subplot(111)

# mpl_finance.candlestick2_ohlc(ax, df_apple['Open'], df_apple['High']
#                               ,df_apple['Low'], df_apple['Close']
#                               ,width=0.5, colorup='r',colordown='b')

df_apple['Colse']
plt.show()