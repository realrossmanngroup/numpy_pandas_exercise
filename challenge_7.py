import pandas as pd

'''
practice exercises

#scrape websiste
house_price_df = pd.read_html('https://www.livingin-canada.com/house-prices-canada.html')

#fix display issue
pd.set_option('display.width', 750)

#show table of house prices
print(house_price_df[0].to_string() + '\n\n\n\n\n\n\n\n')
'''

#read retirement data

us_retirement_data = pd.read_html('https://www.ssa.gov/oact/progdata/nra.html')

print(us_retirement_data)
