# Geovani Rodriguez

import ccxt

# Initialize the exchange object
exchange = ccxt.binance()

# Set the ticker symbol for the asset you want to trade
symbol = 'BTC/USDT'

# Define your trading strategy
def trading_strategy(exchange, symbol):
    # Get the current price of the asset
    ticker = exchange.fetch_ticker(symbol)
    current_price = ticker['last']

    # Define your buy and sell thresholds
    buy_threshold = current_price * 0.9
    sell_threshold = current_price * 1.1

    # Get your current balance
    balance = exchange.fetch_balance()
    btc_balance = balance['BTC']['free']

    # Check if the current price is below the buy threshold
    if current_price < buy_threshold:
        # Calculate the number of BTC to buy
        btc_to_buy = btc_balance / current_price
        # Place a buy order
        exchange.create_market_buy_order(symbol, btc_to_buy)
        print('Bought', btc_to_buy, 'BTC at', current_price)

    # Check if the current price is above the sell threshold
    if current_price > sell_threshold:
        # Place a sell order
        exchange.create_market_sell_order(symbol, btc_balance)
        print('Sold', btc_balance, 'BTC at', current_price)

# Run the trading strategy on a loop
while True:
    trading_strategy(exchange, symbol)
