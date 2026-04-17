import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

class MeanReversionStrategy:
    def __init__(self, data, lookback_period=20, entry_threshold=1.0, exit_threshold=0.0):
        self.data = data
        self.lookback_period = lookback_period
        self.entry_threshold = entry_threshold
        self.exit_threshold = exit_threshold
        self.signals = None
        self.positions = None

    def calculate_indicators(self):
        self.data['Rolling Mean'] = self.data['Close'].rolling(window=self.lookback_period).mean()
        self.data['Rolling Std'] = self.data['Close'].rolling(window=self.lookback_period).std()
        self.data['Z-Score'] = (self.data['Close'] - self.data['Rolling Mean']) / self.data['Rolling Std']

    def generate_signals(self):
        self.calculate_indicators()
        self.data['Signal'] = 0
        self.data.loc[self.data['Z-Score'] < -self.entry_threshold, 'Signal'] = 1  # Buy signal
        self.data.loc[self.data['Z-Score'] > self.entry_threshold, 'Signal'] = -1  # Sell signal
        self.signals = self.data[['Close', 'Z-Score', 'Signal']]

    def backtest(self):
        self.generate_signals()
        self.data['Position'] = self.signals['Signal'].shift()  # Shift signals for backtesting
        self.data['Strategy Returns'] = self.data['Position'] * self.data['Close'].pct_change()
        self.data['Cumulative Strategy Returns'] = (1 + self.data['Strategy Returns']).cumprod()
        self.data['Cumulative Market Returns'] = (1 + self.data['Close'].pct_change()).cumprod()

    def plot_results(self):
        self.backtest()
        plt.figure(figsize=(14, 7))
        plt.plot(self.data['Cumulative Strategy Returns'], label='Strategy Returns')
        plt.plot(self.data['Cumulative Market Returns'], label='Market Returns')
        plt.title('Mean Reversion Strategy vs. Market Returns')
        plt.legend()
        plt.show()

# Example usage:
# data = pd.read_csv('your_data.csv')  # Make sure your data contains 'Close' price.
# strategy = MeanReversionStrategy(data)
# strategy.plot_results()