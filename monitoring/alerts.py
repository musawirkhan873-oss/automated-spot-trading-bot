import time
import requests
import json

class TradingAlerts:
    def __init__(self, threshold, webhook_url):
        self.threshold = threshold
        self.webhook_url = webhook_url

    def check_price(self, current_price):
        if current_price > self.threshold:
            self.send_alert(current_price)

    def send_alert(self, price):
        alert_message = f'Alert! Price has crossed the threshold: {price}'
        requests.post(self.webhook_url, json={'text': alert_message})

if __name__ == '__main__':
    # Example usage
    alert_threshold = 50000  # Set your alert threshold
    webhook_url = 'https://hooks.slack.com/services/YOUR/WEBHOOK/URL'  # Replace with your actual webhook URL
    trading_alerts = TradingAlerts(alert_threshold, webhook_url)

    # Simulate price monitoring
    while True:
        current_price = get_current_market_price()  # Implement this function to fetch market price
        trading_alerts.check_price(current_price)
        time.sleep(60)  # Check every minute