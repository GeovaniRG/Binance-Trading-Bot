#// Geovani Rodriguez //#

import talib
import numpy as np

# Get historical data for the asset
historical_data = exchange.fetch_ohlcv(symbol)

# Extract the close prices from the historical data
close_prices = [x[4] for x in historical_data]

# Calculate the SMA of the close prices
sma = talib.SMA(np.array(close_prices), timeperiod=14)

# Calculate the RSI of the close prices
rsi = talib.RSI(np.array(close_prices), timeperiod=14)

# Define your trading strategy
def trading_strategy(exchange, symbol, sma, rsi):
    # Get the current price of the asset
    ticker = exchange.fetch_ticker(symbol)
    current_price = ticker['last']

    # Define your buy and sell thresholds based on the SMA and RSI
    buy_threshold = sma[-1] * 0.9
    sell_threshold = sma[-1] * 1.1

    # Get your current balance
    balance = exchange.fetch_balance()
    btc_balance = balance['BTC']['free']

    # Check if the current price is below the buy threshold and RSI is below 30
    if current_price < buy_threshold and rsi[-1] < 30:
        # Calculate the number of BTC to buy
        btc_to_buy = btc_balance / current_price
        # Place a buy order
        exchange.create_market_buy_order(symbol, btc_to_buy)
        print('Bought', btc_to_buy, 'BTC at', current_price)

    # Check if the current price is above the sell threshold and RSI is above 70
    if current_price > sell_threshold and rsi[-1] > 70:
        # Place a sell order
        exchange.create_market_sell_order(symbol, btc_balance)
        print('Sold', btc_balance, 'BTC at', current_price)

# You would then call the trading_strategy function with sma and rsi as arguments.

trading_strategy(exchange, symbol, sma, rsi)
