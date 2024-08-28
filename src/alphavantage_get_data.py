import os
import requests
from dotenv import load_dotenv
import json

def load_api_key():
    """Load API key for Alpha Vantage's stock and BTC data retrieval"""
    # Load environment files
    load_dotenv()
    # Access the API key
    api_key = os.getenv("ALPHA_VANTAGE_API_KEY")
    # Check if API key is loaded
    if not api_key:
        print("API key not found. Please set ALPHA_VANTAGE_API_KEY in your .env file.")
        return None
    return api_key

def get_stock_data(symbol):
    """Return historical monthly stock data for a publicly traded company."""
    # Make sure API key is working
    api_key = load_api_key()
    if not api_key:
        return None  # Exit if API key is not loaded

    # Define URL and params
    url = "https://www.alphavantage.co/query"
    params = {
        "function" : "TIME_SERIES_MONTHLY",
        "symbol" : symbol,
        "apikey" : api_key
        }
    
    # Make the API request
    response = requests.get(url, params=params)

    # Check the status code
    if response.status_code != 200:
        print(f"Error: {response.status_code}")
        return None

    # Convert to JSON
    data = response.json()

    if "Monthly Time Series" in data:
        # Store JSON data in a file
        filename = f"data/stock_data/{symbol}.json"
        # Check if file exists and print status message
        if os.path.exists(filename):
            print(f"File: '{filename}' already exists.. Updating file.")
        else:
            print(f"Saving '{filename}' as new file.")
        # Save the file
        with open(filename, "w") as json_file:
            json.dump(data["Monthly Time Series"], json_file, indent=4)
        # Print success message
        print(f"Data successfully saved to '{filename}'!")
        return data["Monthly Time Series"]
    else:
        # Print if error with symbol
        print(f"No data found for symbol: {symbol}")
        return None

def get_btc_data():
    """Return historical monthly data for Bitcoin."""
    # Make sure API key is working
    api_key = load_api_key()
    if not api_key:
        return None  # Exit if API key is not loaded

    # Retrieve BTC data
    url = "https://www.alphavantage.co/query"
    params = {
        "function" : "DIGITAL_CURRENCY_MONTHLY",
        "symbol" : "BTC",
        "market" : "USD",
        "apikey" : api_key
        }
    
    # Make the API request
    response = requests.get(url, params=params)

    # Check the status code
    if response.status_code != 200:
        # Print if error with connection to API
        print(f"Error: {response.status_code}")
        return None

    # Convert to JSON
    data = response.json()
    filename = "data/crypto_data/BTC_price_history.json"

    # Check if file exists and print status message
    if os.path.exists(filename):
        print(f"File: '{filename}' already exists.. Updating file.")
    else:
        print(f"Saving '{filename}' as new file.")

    # Save the file
    with open(filename, "w") as json_file:
        json.dump(data, json_file, indent=4)
    print(f"Data successfully saved to '{filename}'!")
    return data  
