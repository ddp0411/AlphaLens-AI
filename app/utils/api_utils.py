import requests

def get_market_news():
    url = "https://financialmodelingprep.com/api/v3/stock_news?limit=5"
    return requests.get(url).json()
