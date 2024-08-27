import os
import requests
from dotenv import load_dotenv
import json

# Load environment files
load_dotenv()

# Access the API key
api_key = os.getenv("ALPHA_VANTAGE_API_KEY")

# Check if API key is loaded
if not api_key:
    print("API key not found. Please set ALPHA_VANTAGE_API_KEY in your .env file.")

# Define function to fetch monthly data
def fetch_stock_data(symbol):
    """Return historical monthly stock data for a publicly traded company."""
    url = "https://www.alphavantage.co/query"
    params = {
        "function" : "TIME_SERIES_MONTHLY",
        "symbol" : symbol,
        "apikey" : api_key
        }
    # Make the API request
    response = requests.get(url, params=params)
    # Check status code
    if response.status_code == 200:
        # Convert to JSON
        data = response.json()
        if "Monthly Time Series" in data:
            # Store JSON data in a file
            filename = f"data/stock_data/{symbol}.json"
            # Check if filename exists and print message
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
    else:
        # Print if error with connection to API
        print(f"Error: {response.status_code}")
        return None

monthly = fetch_stock_data("aapl")