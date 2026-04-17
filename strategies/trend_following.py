# Trend Following Strategy Using Moving Averages

class MovingAverage:
    def __init__(self, period):
        self.period = period
        self.prices = []

    def add_price(self, price):
        self.prices.append(price)
        if len(self.prices) > self.period:
            self.prices.pop(0)

    def get_average(self):
        if len(self.prices) < self.period:
            return None  # Not enough data
        return sum(self.prices) / self.period


class TrendFollowingStrategy:
    def __init__(self, short_window, long_window):
        self.short_ma = MovingAverage(short_window)
        self.long_ma = MovingAverage(long_window)

    def signal(self, price):
        # Add the current price to both moving averages
        self.short_ma.add_price(price)
        self.long_ma.add_price(price)

        # Calculate both moving averages
        short_average = self.short_ma.get_average()
        long_average = self.long_ma.get_average()

        # Generate signal
        if short_average is None or long_average is None:
            return None  # Not enough data to generate a signal
        if short_average > long_average:
            return 'buy'
        elif short_average < long_average:
            return 'sell'
        else:
            return 'hold'


# Example usage
if __name__ == '__main__':
    strategy = TrendFollowingStrategy(short_window=15, long_window=50)
    
    # Simulated price data
    prices = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 
              16, 17, 18, 19, 20, 21, 22, 23, 24, 25]
    
    for price in prices:
        action = strategy.signal(price)
        if action:
            print(f'Price: {price}, Action: {action}')