'''test ping'''
import time
import ccxt
import pandas as pd
ping_times = {}

exchange_ids = ['ascendex', 'gateio', 'binance', 'kucoin', 'ftx', 'cryptocom']

for exchange_id in exchange_ids:
    exchange: ccxt.Exchange = getattr(ccxt, exchange_id)()
    exchange.load_markets()
    ping_times[exchange_id] = []
    for _ in range(10):
        start_time = time.time()
        exchange.fetch_ticker('BTC/USDT')
        ping_times[exchange_id].append(time.time() - start_time)

print(pd.DataFrame(ping_times).describe())
