# RSI Trading Strategy Backtest

This project uses a simple RSI ( Relative Strength Index ) trading strat using historical data
from yahoo finance. It buys when the RSI indicates oversold conditions and sells when the RSI
indicates overbought conditions, then logs and shows trades and profits.

<p float="left">
  <img src="https://github.com/user-attachments/assets/3fcb7825-bf15-4767-9ac7-c5c182301027" width="300" />
 <img src="https://github.com/user-attachments/assets/329b5466-537c-47d6-b9fe-b62809250976" width="300" />
  <img src="https://github.com/user-attachments/assets/9567c289-430e-462c-ab81-4e95e6351d9c" width="300" />
</p>


## Requirements

Install deps with:
`pip install pandas yfinance ta matplotlib notebook`

## Useage 

Set the stock ticker, date range, and params in the script then run:
`python3 main.py`

## How it works

- Buy signal: When RSI falls below 40 (oversold), buy 100 shares
- Sell signal: When RSI rises above 70 (overbought), sell all shares
- Trades are executed at the close price
- No transaction costs considered

## Notes
Obviously not financial adivce
