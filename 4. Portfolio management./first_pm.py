#// Geovani Rodriguez //#

import ccxt

# Initialize the exchange object
exchange = ccxt.binance()

# Set the ticker symbols for the assets you want to trade
symbols = ['BTC/USDT', 'ETH/USDT', 'LTC/USDT']

# Define your trading strategy
def trading_strategy(exchange, symbols):
    # Get the current prices of the assets
    tickers = exchange.fetch_tickers(symbols)

    # Define your buy and sell thresholds
    buy_threshold = 0.9
    sell_threshold = 1.1

    # Get your current balances
    balance = exchange.fetch_balance()

    # Iterate through each symbol and check if the current price is below or above the thresholds
    for symbol in symbols:
        current_price = tickers[symbol]['last']
        base_currency = symbol.split('/')[0]
        free_balance = balance[base_currency]['free']
        if current_price < buy_threshold:
            # Calculate the number of base_currency to buy
            base_currency_to_buy = free_balance / current_price
            # Place a buy order
            exchange.create_market_buy_order(symbol, base_currency_to_buy)
            print(f'Bought {base_currency_to_buy} {base_currency} at {current_price}')
        if current_price > sell_threshold:
            # Place a sell order
            exchange.create_market_sell_order(symbol, free_balance)
            print(f'Sold {free_balance} {base_currency} at {current_price}')

# Run the trading strategy on a loop
while True:
    trading_strategy(exchange, symbols)

    
