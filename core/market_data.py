import requests
import pandas as pd
import talib

class MarketData:
    def __init__(self, symbol):
        self.symbol = symbol
        self.base_url = 'https://api.example.com/v1/'  # Replace with a real API endpoint

    def get_real_time_data(self):
        response = requests.get(f'{self.base_url}ticker/{self.symbol}')
        return response.json()

    def get_historical_data(self, period='1d'):  # Can adjust period
        response = requests.get(f'{self.base_url}historical/{self.symbol}?period={period}')
        return pd.DataFrame(response.json())

    def calculate_indicator(self, data, indicator_name):
        if indicator_name == 'SMA':
            return talib.SMA(data)  # Simple Moving Average
        elif indicator_name == 'EMA':
            return talib.EMA(data)  # Exponential Moving Average
        # Add more indicators as needed
        return None

# Example usage:
# market_data = MarketData('AAPL')
# print(market_data.get_real_time_data())
# historical_data = market_data.get_historical_data('7d')
# sma = market_data.calculate_indicator(historical_data['close'], 'SMA')
