import os
import requests
from dotenv import load_dotenv
import json

# Load environment variables from .env file
load_dotenv()

# Access the API key
api_key = os.getenv("COIN_GECKO_API_KEY")

# Check if API key is loaded.
if not api_key:
    print("API key not found. Please set COIN_GECKO_API_KEY in your .env file.")

# Define the endpoint and parameters
url = "https://api.coingecko.com/api/v3/companies/public_treasury/bitcoin"
params = {
    "x_cg_demo_api_key": api_key
    }

# Make the API request
response = requests.get(url, params=params)

# Check status code
if response.status_code == 200:
    # Convert to JSON
    data = response.json()
    # Store JSON data in a file
    filename = 'data/companies_with_btc.json'
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
else:
    # Print if error to connection with API
    print(f"Error: {response.status_code} - {response.text}")
