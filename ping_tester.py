'''test ping'''
import time
import ccxt
import pandas as pd
import urllib.request
import json

with urllib.request.urlopen("https://geolocation-db.com/json") as url:
    data = json.loads(url.read().decode())

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

pd.DataFrame(ping_times).describe().to_csv(
    f'./data/{data["country_name"]}.csv')
