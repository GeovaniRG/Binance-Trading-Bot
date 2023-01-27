# // Geovani Rodriguez //#

import requests
import json

def get_market_sentiment(symbol):
    # Make an API call to a sentiment analysis service
    url = 'https://api.example.com/sentiment?symbol=' + symbol
    response = requests.get(url)
    sentiment = json.loads(response.text)['sentiment']
    return sentiment

def trading_strategy(exchange, symbol):
    # Get the current price of the asset
    ticker = exchange.fetch_ticker(symbol)
    current_price = ticker['last']

    # Get market sentiment
    sentiment = get_market_sentiment(symbol)
    
    # Define your buy and sell thresholds
    buy_threshold = current_price * 0.9
    sell_threshold = current_price * 1.1

    # Get your current balance
    balance = exchange.fetch_balance()
    btc_balance = balance['BTC']['free']

    # Check if the current price is below the buy threshold
    if current_price < buy_threshold and sentiment == "Bullish":
        # Calculate the number of BTC to buy
        btc_to_buy = btc_balance / current_price
        # Place a buy order
        exchange.create_market_buy_order(symbol, btc_to_buy)
        print('Bought', btc_to_buy, 'BTC at', current_price)

    # Check if the current price is above the sell threshold
    if current_price > sell_threshold or sentiment == "Bearish":
        # Place a sell order
        exchange.create_market_sell_order(symbol, btc_balance)
        print('Sold', btc_balance, 'BTC at', current_price)
