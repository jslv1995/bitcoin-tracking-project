# Bitcoin and Stock Market Analysis Project

## Overview
This project aims to analyze the relationship between the Bitcoin holdings of public companies and their stock performance over time. Using data from the CoinGecko API and Alpha Vantage API, the project retrieves information about companies holding Bitcoin and their corresponding historical stock data. The goal is to assess how Bitcoin holdings might correlate with or impact stock performance over different periods, such as 1, 5, and 10 years.

## Project Goals:
- Data Retrieval:
    - Use the CoinGecko API to fetch data on public companies holding Bitcoin, including the amount of Bitcoin each company holds.
    - Utilize the Alpha Vantage API to retrieve historical stock data (monthly) for the top companies identified from the CoinGecko data.

- Data Processing and Analysis:
    - Use pandas to clean, process, and merge the data from CoinGecko and Alpha Vantage.
    - Analyze the stock performance of these companies over the past 5 years and explore potential correlations between Bitcoin holdings and stock price trends.
    - Investigate how the stock prices of these companies have changed in relation to significant fluctuations in Bitcoin's market value.

- Data Visualization:
    - Create visualizations using matplotlib or plotly to illustrate trends, correlations, and key insights derived from the data.
    - Provide clear, informative charts that compare Bitcoin holdings with stock performance over time.

## Project Structure
- src/
    - main.py: *in development*
    - alphavantage_get_data.py: Fetches monthly historical stock data for public companies using the Alpha Vantage API.
    - coingecko_get_data.py: Retrieves data on public companies holding Bitcoin from the CoinGecko API.

- data/ (not yet included in the repository)
    - companies_with_btc.json: Stores the retrieved data from CoinGecko, detailing companies and their Bitcoin holdings.
    - stock_data/: Directory where individual stock data files are saved, one for each company.

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
- Integrate pandas to further analyze data
- Integrate matplotlib to visualize data
- Implement the data analysis and visualization components using pandas for data processing.
- News and Social Media Integration: Correlate news feeds with Bitcoin price movements.

## License
This project is licensed under the MIT License. See the LICENSE file for more details.

## Contact
For questions or collaboration, feel free to contact John Lewis.