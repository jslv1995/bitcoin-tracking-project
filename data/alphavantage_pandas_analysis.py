import pandas as pd
import os

def process_stock_data(symbol):
    """Produce a JSON used to analyze historical stock prices"""
    try:
        file_path = f"data/for_analysis/{symbol}_price_history.json"
        # The goal is to analyze 2017 to now.. So actual starting date will be 12/30/2016
        start_date = "2016-12-30"
        save_path = f"data/for_analysis/{symbol}_processed.json"
        
        # Load JSON data
        stock_data = pd.read_json(file_path)
        
        # Sort the data
        stock_data = stock_data.sort_index()
        
        # Extract monthly closing prices
        sorted_stock_prices = stock_data.loc['4. close']
        
        # Reorganize with date and monthly_closing_price columns
        closing_prices = sorted_stock_prices.reset_index().rename(columns={'index': 'date', '4. close': 'monthly_closing_price'})
        
        # Filter from start date to now
        filtered_stock_prices = closing_prices[closing_prices['date'] >= start_date]
        
        # Save the DataFrame as a JSON file in a format that can be easily loaded by pandas
        filtered_stock_prices.to_json(save_path, orient='records', date_format='iso', indent=4)
        
        print(f"Data successfully saved to {save_path}!")
    
    except FileNotFoundError:
        print(f"File for symbol '{symbol}' not found. Please ensure it is in 'data/stock_data'.")
    except KeyError:
        print(f"Expected data not found in the file for symbol '{symbol}'.")
    except Exception:
        print(f"An error occurred: {Exception}")

## This can be run to process the files in data/for_analysis
# symbols_to_review = ['MSTR', 'SPY']
# for symbol in symbols_to_review:
#     process_stock_data(symbol)
#     print(f"{symbol} done!")