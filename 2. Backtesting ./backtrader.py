# // Geovani Rodriguez //# 

import backtrader as bt

# Create a subclass of the Backtrader Strategy class
class MyStrategy(bt.Strategy):
    params = (('sma_period', 20),)

    def __init__(self):
        self.sma = bt.indicators.SimpleMovingAverage(self.data.close, period=self.params.sma_period)

    def next(self):
        if self.data.close[0] > self.sma[0]:
            self.buy()
        elif self.data.close[0] < self.sma[0]:
            self.sell()

# Create a Backtrader cerebro instance
cerebro = bt.Cerebro()

# Add your strategy to cerebro
cerebro.addstrategy(MyStrategy)

# Add the historical data to cerebro
data = bt.feeds.YahooFinanceData(dataname='AAPL', fromdate=datetime(2020, 1, 1), todate=datetime(2020, 12, 31))
cerebro.adddata(data)

# Add analyzers
cerebro.addanalyzer(bt.analyzers.Returns)
cerebro.addanalyzer(bt.analyzers.SQN)

# Run the backtest
results = cerebro.run()

# Print the returns and SQN of the strategy
print("Returns:", results[0].analyzers.returns.get_analysis())
print("SQN:", results[0].analyzers.sqn.get_analysis())


