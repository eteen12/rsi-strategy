import pandas as pd
import yfinance as yf
import numpy as np
import ta
import matplotlib.pyplot as plt

end_date = '2025-06-27'
start_date = pd.to_datetime(end_date)-pd.DateOffset(365)

stock = "LHA.DE"

df = yf.download(tickers=stock, start=start_date, end=end_date, auto_adjust=True).stack(future_stack=True)

df.index.names = ['date','ticker']
df.columns = df.columns.str.lower()

def rsi_calc(x, window=14):
    return ta.momentum.RSIIndicator(close=x, window=window).rsi()

df['rsi'] = df.groupby(level='ticker')['close'].transform(lambda x: rsi_calc(x, window=14))

shares_to_buy = 100
position = 0
buy_price = 0
total_profit = 0
trades = []

for (date, ticker), row in df.iterrows():
    rsi = row['rsi']
    close = row['close']

    if pd.isna(rsi):
        continue

    if position == 0 and rsi <= 40:
        buy_price = close
        position = 1
        trades.append((date, 'BUY', close))
        print(f"Buy on {date.date()} at {close:.2f}")

    elif position == 1 and rsi >= 70:
        sell_price = close 
        profit = (sell_price - buy_price) * shares_to_buy
        total_profit += profit
        position = 0
        trades.append((date, 'SELL', close, profit))
        print(f"Sell on {date.date()} at {close:.2f} Profit: ${profit:.2f}")

print(f"\nTotal Profit: ${total_profit:.2f}")
