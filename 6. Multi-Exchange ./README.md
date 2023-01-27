# 6. Multi-Exchange

Adding functionality to trade on multiple exchanges can be a great way to diversify your trading strategy and potentially increase profits. This can be done by using a library such as ccxt to interact with multiple exchanges using a single API.

In this example This code snippet uses a list of exchange objects initialized using ccxt, and then loops through each exchange object and runs the trading strategy on it. This allows you to trade on multiple exchanges using the same strategy, which can help you diversify your trading and potentially increase profits.

Please note that it's important to consider the different fees and trading limits for each exchange, and also the different trading pairs available.

To trade on multiple exchanges using the code you provided, you would need to create an instance of the exchange object for each exchange you want to trade on, and then modify the trading_strategy function to handle multiple exchange objects. This can be done by iterating through a list of exchange objects and calling the trading_strategy function for each one.

Additionally, you will need to make sure that your account is funded on each exchange and that your API keys are set up correctly.

An example of how you might set this up is by creating a list of exchange objects:

```
exchanges = [ccxt.binance(), ccxt.bitmex()]
```

Then in the while loop, you would iterate through the list and call the trading_strategy function for each exchange:

```
while True:
    for exchange in exchanges:
        trading_strategy(exchange, symbol)
```
You'll also need to adjust the trading_strategy function so it can handle the different type of order that each exchange could have, for example Binance uses create_market_buy_order but Bitmex uses create_market_buy_order so you'll need to use a if or a switch statement to handle different type of order accordingly to the exchange.

Keep in mind that different exchanges might have different limits, fees, order types and different tickers symbols, so you'll need to adjust your strategy accordingly.
