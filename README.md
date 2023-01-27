# Binance-trading-bot
Small Python Trading boot
(This it's just for fun)

This script uses the ccxt library to interact with the Binance exchange. It defines a simple trading strategy where it will buy BTC when the price falls below 90% of the current price and sell when the price rises above 110% of the current price. It does this by repeatedly calling the trading_strategy function in a loop.

The script starts by importing the ccxt library, which is a collection of modules for interacting with different cryptocurrency exchanges. In this example, we are using the binance() function from the ccxt library to initialize the exchange object, which will allow us to interact with the Binance exchange.

Next, we set the ticker symbol for the asset we want to trade. In this case, it is 'BTC/USDT', which represents the Bitcoin/Tether trading pair.

The script then defines a function called trading_strategy(exchange, symbol). This function will be called repeatedly by the script in a loop and will contain the logic for the trading strategy.

The first thing the trading_strategy function does is fetch the current price of the asset by calling exchange.fetch_ticker(symbol). This returns an object containing various information about the asset's current state, including the last price it was traded at. We store this price in a variable called current_price.

Next, we define our buy and sell thresholds. In this case, we have set the buy threshold to 90% of the current price and the sell threshold to 110% of the current price. This means that if the current price falls below 90% of its value, the bot will buy, and if the price rises above 110% of its value, the bot will sell.

Then we get our current balance by calling exchange.fetch_balance(), which returns an object containing information about the balance of all assets in our account. We store the balance of BTC in the variable btc_balance.

Then, we check whether the current price is below the buy threshold. If it is, we calculate the number of BTC to buy by dividing our available balance by the current price. We then place a buy order by calling exchange.create_market_buy_order(symbol, btc_to_buy). This will buy the specified number of BTC at the current market price.

Lastly, we check whether the current price is above the sell threshold. If it is, we place a sell order by calling exchange.create_market_sell_order(symbol, btc_balance). This will sell all of our BTC at the current market price.

Lastly, the script runs the trading strategy on a loop by calling the trading_strategy(exchange, symbol) function inside a while(True) loop.

Please note that this is just an example and there are many other factors to consider when building a trading bot. Also, you should always do your own research before doing any trading.

# Improving the code: 
There are several things you could add to this project to make it more robust and potentially more profitable:
1. Risk management: Implementing risk management measures such as stop-loss orders to limit potential losses.
2. Backtesting: Using historical data to test the performance of the trading strategy and make adjustments as needed.
3. Indicator-based strategy: Incorporating technical indicators such as moving averages or relative strength index (RSI) to generate buy and sell signals.
Portfolio management: Diversifying your portfolio by trading multiple assets, rather than just a single one.
4. Market sentiment analysis: Incorporating external data such as news articles or social media sentiment to inform your trading decisions
5. Multi-Exchange: Adding functionality to trade on multiple exchanges.
Incorporating a database to save historical data and make trading decisions based on historical data.

It is important to note that these are just a few examples and depending on your goals and the complexity of your trading strategy, additional features may be needed. It is also crucial to test and validate any changes you make to the trading bot in order to avoid potential losses.
