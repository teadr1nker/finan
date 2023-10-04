#!/usr/bin/python3
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

figure, axis = plt.subplots(2, 3)


def analyse(path, i=0):
    df = pd.read_csv(path, delimiter=',')

    # SMA
    axis[i, 0].plot(df['Close'])

    sma50 = df['Close'].rolling(window=50).mean()
    sma200 = df['Close'].rolling(window=200).mean()
    axis[i, 0].plot(sma50)
    axis[i, 0].plot(sma200)
    axis[i, 0].legend([path, '50', '200'])
    axis[i, 0].set_title(f'SMA {path}')
    axis[i, 0].set_ylabel('Price')

    # Profit std
    sigma = np.std(df['Close'].diff(1), ddof=1)
    print(f'sigma {path}: {sigma}')

    # Bollinger lines
    upper  = df['Close'].rolling(window=50).mean() + df['Close'].rolling(window=50).std() * 2
    bottom = df['Close'].rolling(window=50).mean() - df['Close'].rolling(window=50).std() * 2

    axis[i, 1].plot(df['Close'])
    axis[i, 1].plot(bottom)
    axis[i, 1].plot(upper)
    axis[i, 1].legend([path, 'bottom', 'upper'])
    axis[i, 1].set_title(f'Bollinger bands {path}')
    axis[i, 1].set_ylabel('Price')

    # RSI
    profit = df['Close'].diff(1)
    gain = profit.clip(lower=0)
    loss = profit.clip(upper=0).abs()

    avgGain = gain.rolling(window=50).mean()
    avgLoss = loss.rolling(window=50).mean()

    rs = avgGain / avgLoss
    RSI = 100 - (100 / (1.0 + rs))

    axis[i, 2].plot(df['Close'] / df['Close'].max() * 100)
    axis[i, 2].plot(RSI, color='r')
    axis[i, 2].plot(np.ones(len(df)) * 30)
    axis[i, 2].plot(np.ones(len(df)) * 50)
    axis[i, 2].plot(np.ones(len(df)) * 70)
    axis[i, 2].set_title(f'RSI {path}')
    axis[i, 2].legend([path, 'RSI', '30 line', '50 line', '70 line'])


analyse('AMD3Y.csv')
analyse('NVDA3Y.csv', 1)
plt.show()
