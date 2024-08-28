# Bitcoin and Stock Market Analysis Project

## Overview

This project analyzes the stock performance of selected American public companies with the largest holdings of Bitcoin (BTC) as an asset. The focus is on four companies: MicroStrategy Inc. (MSTR), Marathon Digital Holdings (MARA), Tesla, Inc. (TSLA), and CleanSpark Inc. (CLSK). The analysis covers their stock performance from 2017 to the present, with particular attention to the period around late 2020 and early 2021, when these companies first purchased Bitcoin.

The goal is to assess how Bitcoin holdings may correlate with or impact stock performance over various periods. Data from the CoinGecko API and Alpha Vantage API is used to retrieve information about these companies' Bitcoin holdings and their corresponding historical stock data.

## Project Goals:
- Data Retrieval:
    - Use the CoinGecko API to fetch data on public companies holding Bitcoin
    - Utilize the Alpha Vantage API to retrieve historical stock data (monthly) for the top companies identified from the CoinGecko data.
    - Alpha Vantage is also supplying historical price data for Bitcoin.

- Data Processing and Analysis:
    - Use pandas to clean, process, and merge the data from CoinGecko and Alpha Vantage.
    - Analyze the stock performance of these companies from 2017 to August 2024, and explore potential correlations between Bitcoin holdings and stock price trends.
    - Investigate how the stock prices of these companies have changed in relation to significant fluctuations in Bitcoin's market value.

- Data Visualization:
    - Create visualizations using matplotlib or plotly to illustrate trends, correlations, and key insights derived from the data.
    - Provide clear, informative charts that compare Bitcoin holdings with stock performance over time.

## Project Structure
- src/
    - main.py: *in development*
    - alphavantage_get_data.py: Fetches monthly historical stock data for public companies and Bitcoin using the Alpha Vantage API.
    - coingecko_get_data.py: Retrieves data on public companies holding Bitcoin from the CoinGecko API.
    - __init__.py: Allows use of functions in other folders

- data/ (*in development* not yet included in the repository)

- .env (not included in the repository)
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
- Integrate matplotlib to visualize data.
- Implement the data analysis and visualization components using pandas for data processing.
- Integrate news and social media data to correlate with Bitcoin price movements.
- Explore further correlations between BTC price and stock price trends.

## License
This project is licensed under the MIT License. See the LICENSE file for more details.

## Contact
For questions or collaboration, feel free to contact John Lewis at linkedin.com/in/johnlewisv