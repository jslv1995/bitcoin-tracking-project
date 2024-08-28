import pandas as pd
import json

btc_companies = pd.read_json('data/for_analysis/companies_with_btc.json')

# Flatten the companies column to analyze further
companies_expanded = pd.json_normalize(btc_companies['companies']) 

### After analyzing the data, it is most consistent to filter by Nasdaq and country,
#      as there are some foreign companies with US as their country

# Extract American companies trading on NASDAQ
american_nasdaq_companies = companies_expanded[\
                            (companies_expanded['symbol'].str.contains('NASDAQ')) & \
                            (companies_expanded['country'] == 'US')]

# Sort by BTC holdings
sorted_nasdaq_companies = american_nasdaq_companies.sort_values(by='total_holdings', ascending=False)

# Clean up symbol, removing exchange from results
sorted_nasdaq_companies.loc[:, 'symbol'] = sorted_nasdaq_companies['symbol'].str.replace('NASDAQ:', '', regex=False)

# Decided symbols for analysis
symbols_to_keep = ['MSTR', 'MARA', 'TSLA', 'CLSK']
companies_for_review = sorted_nasdaq_companies[sorted_nasdaq_companies['symbol'].isin(symbols_to_keep)]

# Create final DataFrame with US companies holding BTC
filtered_companies = companies_for_review[['name', 'symbol', 'total_holdings']]
filtered_companies.reset_index(drop=True, inplace=True)

# Dictionary with the each company's initial purchase dates
began_purchasing_in = {
    "MSTR": "08/2020",
    "MARA": "01/2021",
    "TSLA": "02/2021",
    "CLSK": "12/2020"
    }

# Add new column to completed list
final_companies_with_btc_list = filtered_companies.assign(began_purchasing_in=filtered_companies['symbol'].map(began_purchasing_in))

