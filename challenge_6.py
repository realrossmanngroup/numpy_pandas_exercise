import pandas as pd

#create dataframe
portfolio_df = pd.DataFrame({'Stock':["SPY", "DVYE", "OIEIX"],
							'Share count':[96, 581, 1021],
							'Share price':[450.79, 25.27, 21.46]})
							
#make it easy at a glance to tell how much $$ of each stock we own							
portfolio_df['Total share value'] = portfolio_df['Share count'] * portfolio_df['Share price']

#print the portfolio dataframe
print(str(portfolio_df) + "\n\n")

#print with the total portfolio value
print("Here's the total portfolio value: $" + str(portfolio_df['Total share value'].sum()) + "\n\n")

