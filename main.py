import json
from array import array

import ccxt
from datetime import datetime

binance = ccxt.binance()

markets = binance.load_markets()

formatted_tickers = []

for symbol in markets:
    market = markets[symbol]

    if market['type'] != 'future' and market['type'] != 'swap':
        continue

    ticker = binance.fetch_ticker(symbol)

    clean_symbol = symbol.replace('/', '').replace(':USDT', '')

    if 'USDT' in clean_symbol:
        market_type = 'PERP'
        combined_symbol = clean_symbol + market_type

        formatted_data = f"BINANCE:{combined_symbol}"

        formatted_tickers.append(formatted_data)

date = datetime.today().strftime('%Y-%m-%d')
file_name = date + ".txt"
with open(file_name, 'w') as file:
    for ticker in formatted_tickers:
        file.write(ticker + "\n")

print("Data Write finished successfully")
