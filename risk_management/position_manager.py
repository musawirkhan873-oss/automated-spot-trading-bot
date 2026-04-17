class PositionManager:
    def __init__(self, account_balance, risk_per_trade):
        self.account_balance = account_balance
        self.risk_per_trade = risk_per_trade

    def calculate_position_size(self, entry_price, stop_loss_price):
        risk_per_share = entry_price - stop_loss_price
        position_size = self.account_balance * self.risk_per_trade / risk_per_share
        return position_size

    def update_account_balance(self, amount):
        self.account_balance += amount

# Example usage:
if __name__ == '__main__':
    manager = PositionManager(account_balance=10000, risk_per_trade=0.02)
    size = manager.calculate_position_size(entry_price=100, stop_loss_price=95)
    print(f"Position Size: {size}")