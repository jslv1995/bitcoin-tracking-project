import os
import requests
from dotenv import load_dotenv
import json

from alphavantage_get_data import load_api_key, get_stock_data
from coingecko_get_data import load_api_key, get_companies_holding_btc

get_companies_holding_btc()

symbols_for_analysis = ["MSTR", "SPY"]

for symbol in symbols_for_analysis:
    get_stock_data(symbol)
