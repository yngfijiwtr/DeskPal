import time
import yfinance as yf
import requests

def get_sp500_price():
  max_retries = 3
  retries = 0
  while retries < max_retries:
    try:
      sp500_ticker = "^GSPC"  # Ticker symbol for S&P 500 index
      sp500_data = yf.Ticker(sp500_ticker)
      sp500_price = sp500_data.history(period='1d')['Close'].iloc[0]
      return sp500_price
    except IndexError:
      print("Error: no data available for the specified period.")
      print("Retrying in 5 seconds...")
      retries += 1
      time.sleep(5)
    except Exception as e:
      print("Error fetching S&P500 Price: ", e)
      print("Retrying in 5 seconds...")
      retries += 1
      time.sleep(5)
  print("Max retries exceeded. Unable to fetch S&P500 price.")
  return 0
def get_dow_jones_price():
  max_retries = 3
  retries = 0
  while retries < max_retries:
    try:
      dow_jones_ticker = "^DJI"  # Ticker symbol for Dow Jones Industrial Average
      dow_jones_data = yf.Ticker(dow_jones_ticker)
      dow_jones_price = dow_jones_data.history(period='1d')['Close'].iloc[0]
      return dow_jones_price
    except IndexError:
      print("Error: no data available for the specified period.")
      print("Retrying in 5 seconds...")
      retries += 1
      time.sleep(5)
    except Exception as e:
      print("Error fetching DOW JONES Price: ", e)
      print("Retrying in 5 seconds...")
      retries += 1
      time.sleep(5)
  print("Max retries exceeded. Unable to fetch DOW JONES price.")
  return 0
def get_nasdaq_price():
  max_retries = 3
  retries = 0
  while retries < max_retries:
    try:
      nasdaq_ticker = "^IXIC"  # Ticker symbol for NASDAQ Composite index
      nasdaq_data = yf.Ticker(nasdaq_ticker)
      nasdaq_price = nasdaq_data.history(period='1d')['Close'].iloc[0]
      return nasdaq_price
    except IndexError:
      print("Error: no data available for the specified period.")
      print("Retrying in 5 seconds...")
      retries += 1
      time.sleep(5)
    except Exception as e:
      print("Error fetching NASDAQ Price: ", e)
      print("Retrying in 5 seconds...")
      retries += 1
      time.sleep(5)
  print("Max retries exceeded. Unable to fetch NASDAQ price.")
  return 0
def get_bitcoin_price():
  url = 'https://api.coingecko.com/api/v3/simple/price'
  params = {
    'ids': 'bitcoin',
    'vs_currencies': 'usd'
  }
  try:
    response = requests.get(url, params=params)
    response.raise_for_status()  # Raise an exception for HTTP errors
    data = response.json()
    bitcoin_price = data['bitcoin']['usd']
    return bitcoin_price
  except requests.RequestException as e:
    print("Error fetching Bitcoin price:", e)
    return None
