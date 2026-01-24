import pandas as pd
import matplotlib.pyplot as plt
import yfinance as yf

# Load Nifty_50 data
data = yf.download('^NSEI', start='2023-01-01', end='2026-01-20')

# Calculate Moving Averages
data['MA20'] = data['Close'].rolling(window=20).mean()
data['MA50'] = data['Close'].rolling(window=50).mean()

# Simple Strategy : Buy MA20 > MA50
data['Signal'] = 0
data.loc[data['MA20'] > data['MA50'], 'Signal'] = 1

# Visualize
plt.figure(figsize=(12,6))
plt.plot(data['Close'], label='Nifty 50 Price', alpha=0.5)
plt.plot(data['MA20'], label='20-Day MA', color='blue')
plt.plot(data['MA50'], label='50-Day MA', color='red')
plt.title('Nifty 50 Quant Analysis - Moving Average Crossover')
plt.legend()
plt.show()
# print(data.tail())