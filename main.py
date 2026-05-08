import pandas as pd
import matplotlib.pyplot as plt
import yfinance as yf

# 1. データの取得
aapl = yf.Ticker("AAPL")
df = aapl.history(period="1y")

# 2. データの表示（ここが中途半端だとエラーになります）
print(df)

# 3. グラフの描画
df['Close'].plot()
plt.show()