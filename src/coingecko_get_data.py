import os
import requests
from dotenv import load_dotenv
import json

def load_api_key():
    """Load API key for Alpha Vantage's stock and BTC data retrieval"""
    # Load environment files
    load_dotenv()
    # Access the API key
    api_key = os.getenv("COIN_GECKO_API_KEY")
    # Check if API key is loaded
    if not api_key:
        print("API key not found. Please set COIN_GECKO_API_KEY in your .env file.")
        return None
    return api_key

def get_companies_holding_btc():
    """Return data for publicly traded companies holding Bitcoin."""
    # Make sure API key is working
    api_key = load_api_key()
    if not api_key:
        return None  # Exit if API key is not loaded
    
    # Define the endpoint and parameters
    url = "https://api.coingecko.com/api/v3/companies/public_treasury/bitcoin"
    params = {
        "x_cg_demo_api_key": api_key
        }

    # Make the API request
    response = requests.get(url, params=params)

    # Check the status code
    if response.status_code != 200:
        print(f"Error: {response.status_code}")
        return None

    # Convert to JSON
    data = response.json()
    # Store JSON data in a file
    filename = 'data/for_analysis/companies_with_btc.json'
    # Check if filename exists and print message
    if os.path.exists(filename):
        print(f"File: '{filename}' already exists.. Updating file.")
    else:
        print(f"Saving '{filename}' as new file.")
    # Save the file
    with open(filename, "w") as json_file:
        json.dump(data, json_file, indent=4) 
    # Print success message
    print(f"Data successfully saved to '{filename}'!")
    