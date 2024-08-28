## Bitcoin and Stock Market Analysis Project

# Overview
This project focuses on analyzing the stock performance of MicroStrategy Inc. (MSTR), the largest public company in America holding Bitcoin (BTC) as an asset. The analysis aims to explore the relationship between MicroStrategy's stock performance and Bitcoin's price over time, particularly before and after the company began purchasing Bitcoin in August 2020.

The project utilizes data from the CoinGecko API to retrieve information about MicroStrategy's Bitcoin holdings and from the Alpha Vantage API to obtain historical stock and Bitcoin price data.

## Project Goals:
- Data Retrieval:
    - Completed: Established connections to the CoinGecko API to fetch data on MicroStrategy's Bitcoin holdings, ensuring accurate and up-to-date information.
    - Completed: Successfully connected to the Alpha Vantage API to retrieve monthly historical stock data for MicroStrategy, as well as Bitcoin price data, demonstrating the ability to interact with multiple APIs and handle API keys securely.

- Data Processing and Analysis:
    - Completed: Utilized pandas to clean, process, and merge data retrieved from both APIs, ensuring that the data is in a usable format for further analysis. This included handling JSON responses, converting them into DataFrames, and performing operations like filtering, sorting, and merging data sets.
    - In Development: Beginning the analysis phase, focusing on MicroStrategy's stock performance from 2017 to the present. The aim is to identify any significant trends or correlations between Bitcoin holdings and stock price movements, particularly before and after August 2020.

- Data Visualization (in development):
    - In Development: Planning and initial development of visualizations using matplotlib and plotly. The goal is to create clear and informative charts that will compare MicroStrategy's stock performance with Bitcoin's price over time, with a focus on the period before and after the company's Bitcoin purchases.

# Project Structure
- src/
    - main.py: The main script where all functions are imported, and executed.
    - alphavantage_get_data.py: Fetches monthly historical stock data for MicroStrategy and Bitcoin using the Alpha Vantage API.
    - coingecko_get_data.py: Retrieves data on MicroStrategy's Bitcoin holdings from the CoinGecko API.
- data/
    - coingecko_pandas_analysis.py: Leveraged the pandas library to analyze and sort the top public companies holding Bitcoin, ultimately identifying MicroStrategy (MSTR) as the most suitable company for detailed analysis.
    - alphavantage_pandas_analysis.py: Utilizes pandas for ongoing processing and analysis of stock data retrieved from the Alpha Vantage API, preparing it for deeper insights.
    - for_analysis/: Processed data output from the API calls.
- .env (not included in the repository):
    - Stores API keys required for accessing the CoinGecko and Alpha Vantage APIs.

## Getting Started:
- You'll need:
    - Python 3.6+
    - pip (install -r requirements.txt)
    - API Keys:
        - Sign up for a free CoinGecko API Key.
        - Sign up for a free Alpha Vantage API Key.
    - Create your .env file with your new API keys:
        - ALPHA_VANTAGE_API_KEY=your_alpha_vantage_api_key
        - COIN_GECKO_API_KEY=your_coin_gecko_api_key

## Future Enhancements
- In Development: Integrate matplotlib to visualize data.
- In Development: Implement the data analysis and visualization components using pandas for data processing.
- Explore further correlations between BTC price and stock price trends.

## License
This project is licensed under the MIT License. See the LICENSE file for more details.

## Contact
For questions or collaboration, feel free to contact John Lewis at linkedin.com/in/johnlewisv