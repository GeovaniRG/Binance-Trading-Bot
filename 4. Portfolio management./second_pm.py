#// Geovani Rodriguez //#

import ccxt

# Initialize the exchange object
exchange = ccxt.binance()

# Set the ticker symbols for the assets you want to trade
symbols = ['BTC/USDT', 'ETH/USDT', 'LTC/USDT']

# Define your trading strategy
def portfolio_management_strategy(exchange, symbols):
    # Get your current balance
    balance = exchange.fetch_balance()

    # Calculate the total value of your portfolio
    portfolio_value = 0
    for symbol in symbols:
        ticker = exchange.fetch_ticker(symbol)
        current_price = ticker['last']
        balance_free = balance[symbol.split("/")[0]]['free']
        portfolio_value += current_price * balance_free

    # Define the target allocation for each asset
    target_allocation = {'BTC': 0.5, 'ETH': 0.3, 'LTC': 0.2}

    # Calculate the target value for each asset
    target_values = {k: (v * portfolio_value) for k, v in target_allocation.items()}

    # Check if the current allocation deviates from the target allocation
    for symbol in symbols:
        ticker = exchange.fetch_ticker(symbol)
        current_price = ticker['last']
        balance_free = balance[symbol.split("/")[0]]['free']
        current_value = current_price * balance_free
        asset = symbol.split("/")[0]
        target_value = target_values[asset]
        if current_value > target_value:
            # Sell the asset if it's over-allocated
            sell_amount = current_value - target_value
            exchange.create_market_sell_order(symbol, sell_amount/current_price)
            print('Sold', sell_amount/current_price, asset,'at', current_price)
        elif current_value < target_value:
            # Buy the asset if it's under-allocated
            buy_amount = target_value - current_value
            exchange.create_market_buy_order(symbol, buy_amount/current_price)
            print('Bought', buy_amount/current_price, asset,'at', current_price)

# Run the portfolio management strategy on a loop
while True:
    portfolio_management_strategy(exchange, symbols)
