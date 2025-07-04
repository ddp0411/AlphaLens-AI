from langchain.tools import tool
import yfinance as yf
from alpha_vantage.timeseries import TimeSeries
from app.config import Config

@tool
def fetch_stock_data(symbol: str) -> dict:
    """Fetch real-time stock data using yfinance and Alpha Vantage."""
    ts = TimeSeries(key=Config.ALPHA_VANTAGE_API_KEY, output_format='json')
    try:
        alpha_data, _ = ts.get_quote_endpoint(symbol)
    except:
        alpha_data = {}

    try:
        yf_data = yf.Ticker(symbol).info
    except:
        yf_data = {}

    return {
        "symbol": symbol,
        "alpha_vantage": alpha_data,
        "yfinance": yf_data
    }
