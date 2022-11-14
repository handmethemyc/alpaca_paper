import requests
from alpaca.trading.requests import MarketOrderRequest
from alpaca.trading.enums import OrderSide, TimeInForce
from alpaca.trading import TradingClient
from secret_keys import API_KEY, SECRET_KEY

api_url = 'https://paper-api.alpaca.markets'

trading_client = TradingClient(API_KEY, SECRET_KEY, paper=True)

account = trading_client.get_account()
positions = trading_client.get_all_positions()

for position in positions:
    print(f'{position.side} {position.qty} {position.symbol} {position.market_value}')

market_order = MarketOrderRequest(
    symbol="TSLA",
    qty=200,
    side=OrderSide.SELL,
    time_in_force=TimeInForce.GTC 
)
