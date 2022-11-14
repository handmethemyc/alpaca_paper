from secret_keys import API_KEY, SECRET_KEY
import requests
import alpaca_trade_api as api

symbol='APPL, TSLA'
API_URL = 'https://data.sandbox.alpaca.markets/v2/GET/v2/stocks/{symbol}/trades'

trades = requests.get(API_KEY)