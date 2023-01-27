#// Geovani Rodriguez //#

import ccxt
import talib
import pandas as pd
import numpy as np
from datetime import datetime
from sqlalchemy import create_engine

# Initialize the exchange object
exchange = ccxt.binance()

# Set the ticker symbol for the asset you want to trade
symbol = 'BTC/USDT'

# Connect to the database
engine = create_engine('sqlite:///trading_data.db')

# Define your trading strategy
def trading_strategy(exchange, symbol):
    # Get historical data for the asset
    historical_data = exchange.fetch_ohlcv(symbol)
    df = pd.DataFrame(historical_data, columns=['timestamp', 'open', 'high', 'low', 'close', 'volume'])
    df['timestamp'] = pd.to_datetime(df['timestamp'], unit='ms')
    df.set_index('timestamp', inplace=True)
    # Add technical indicators
    df['sma50'] = talib.SMA(df['close'], timeperiod=50)
    df['rsi'] = talib.RSI(df['close'], timeperiod=14)

    # Get the current price of the asset
    ticker = exchange.fetch_ticker(symbol)
    current_price = ticker['last']

    # Define your buy and sell thresholds
    buy_threshold = current_price * 0.9
    sell_threshold = current_price * 1.1
    # Define stop loss and take profit thresholds
    stop_loss_threshold = current_price * 0.8
    take_profit_threshold = current_price * 1.2

    # Get your current balance
    balance = exchange.fetch_balance()
    btc_balance = balance['BTC']['free']
    usdt_balance = balance['USDT']['free']

    # Check if the current price is below the buy threshold and the RSI is below 30
    if current_price < buy_threshold and df.iloc[-1]['rsi'] < 30:
        # Calculate the amount of USDT to spend
        usdt_to_spend = usdt_balance * 0.1
        # Calculate the number of BTC to buy
        btc_to_buy = usdt_to_spend / current_price
        # Place a buy order
        exchange.create_market_buy_order(symbol, btc_to_buy)
        print('Bought', btc_to_buy, 'BTC at', current_price)

    # Check if the current price is above the sell threshold and the SMA50 is above the current price
    if current_price > sell_threshold and df.iloc[-1]['sma50'] > current_price:
        # Place a sell order
        exchange.create_market_sell_order(symbol, btc_balance)
        print('Sold', btc_balance, 'BTC at', current_price)
        
        # Check if the current price is below the stop loss threshold
    if current_price < stop_loss_threshold:
        # Place a sell order to minimize losses
        exchange.create_market_sell_order(symbol, btc_balance)
        print('Stop loss triggered, sold', btc_balance, 'BTC at', current_price)
        
    # Check if the current price is above the take profit threshold
    if current_price > take_profit_threshold:
        # Place a sell order to take profits
        exchange.create_market_sell_order(symbol, btc_balance)
        print('Take profit triggered, sold', btc_balance, 'BTC at', current_price)
