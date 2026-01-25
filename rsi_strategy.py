import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

data = yf.download('^NSEI', start='2023-01-01', end='2026-01-20')

# Flatten the MultiIndex columns
data.columns = data.columns.get_level_values(0)
# FOR Precise mathematical function in RSI (Wilder's Smoothing function)
import pandas_ta as ta
data.ta.rsi(length=14, append=True)

data.rename(columns={'RSI_14': 'RSI'}, inplace=True)
data.dropna(inplace=True)

# # Calculate RSI (maths way of rolling average)
# change = data['Close'].diff()
# gain = change.mask(change<0, 0)
# loss = -change.mask(change>0, 0)

# avg_gain = gain.rolling(window=14).mean()
# avg_loss = loss.rolling(window=14).mean()

# rs = avg_gain / avg_loss
# data['RSI'] = 100 - (100 / (1 + rs))

# Simple Strategy : Buy when RSI < 30, Sell when RSI > 70
data['Signal'] = 0
data.loc[data['RSI']<30, 'Signal'] = 1
data.loc[data['RSI']>70,'Signal'] = -1

# Visualize
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 8), sharex=True)

ax1.plot(data['Close'], label='Nifty 50 Price', color='black')
ax1.set_title('Nifty_50_Price & RSI Signals')
ax1.legend()

ax2.axhline(70, color='red', linestyle='--')
ax2.axhline(30, color='green', linestyle='--')
ax2.plot(data['RSI'], label='RSI', color='purple')
ax2.set_title('RSI Indicator')
ax2.legend()

plt.show()

# BACKTESTING---------------------------------

# Market Daily returns
data['Market_Returns'] = data['Close'].pct_change()

# Strategy Return
data['Strategy_Returns'] = data['Signal'].shift(1) * data['Market_Returns']

# Cumulative Returns (The growth of 1 Rupee)
data['Cumulative_Market'] = (1 + data['Market_Returns']).cumprod()
data['Cumulative_Strategy'] = (1 + data['Strategy_Returns']).cumprod()

final_return = data['Cumulative_Strategy'].iloc[-1]
print(f"Total Strategy Return: {(final_return - 1) * 100:.2f}%")

# Maxixmum Drawdown {Risk Measure}
data['Peak'] = data['Cumulative_Strategy'].cummax()
data['Drawdown'] = (data['Cumulative_Strategy'] - data['Peak']) / data['Peak']
max_drawdown = data['Drawdown'].min()
print(f"Maximum Drawdown: {max_drawdown * 100:.2f}%")