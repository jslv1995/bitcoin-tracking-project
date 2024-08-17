import os
import requests
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Access the API key
api_key = os.getenv("CRYPTO_COMPARE_API_KEY")

# Define endpoint and variables
url = "https://min-api.cryptocompare.com/data/price"
parameters = {
    "fsym" : "BTC", # Symbol of the cryptocurrency (Bitcoin)
    "tsyms" : "USD", # Symbol of what we are converting to (Dollars)
    "api_key" : api_key,
    }

# Make the request to CryptoCompare API
response = requests.get(url, params=parameters)

# Print results or error
if response.status_code == 200:
    data = response.json()
    print(data) # Output the JSON data
else:
    print(f"Error: {response.status_code} - {response.text}")
