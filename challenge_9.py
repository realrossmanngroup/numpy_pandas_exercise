import pandas as pd

#create dataframe
bank_client_df = pd.DataFrame({'Bank Client ID':[111, 222, 333, 444],
								'Bank Client Name':['Chanel', 'Steve', 'Mitch', 'Ryan'],
								'Net Worth [$]':[3500, 29000, 10000, 2000],
								'Years with bank':[3, 4, 9, 5]})
								
#define function that increases all client's net worth by a fixed value of 20%

def networth_update(balance):
	return balance * 1.2
	
print(str(bank_client_df) + "\n\n")	

'''
#apply function to a dataframe - test, comment this out to not ruin final exercise
bank_client_df['Net Worth [$]'] = bank_client_df['Net Worth [$]'].apply(networth_update)
print(bank_client_df)
print(bank_client_df['Bank Client Name'].apply(len))
'''

#I mistakenly thought he wanted me to multiply each stock from exercise 6 by 3 and add $200. Doh. Ignore all of this. 

'''
#create stock portfolio dataframe
portfolio_df = pd.DataFrame({'Stock':["SPY", "DVYE", "OIEIX"],
							'Share count':[96, 581, 1021],
							'Share price':[450.79, 25.27, 21.46]})
							
#make it easy at a glance to tell how much $$ of each stock we own							
portfolio_df['Total share value'] = portfolio_df['Share count'] * portfolio_df['Share price']

#print portfolio_df before applying function
print(str(portfolio_df) + "\n\n")

	
#apply function to value of stocks in portfolio
portfolio_df['Share price'] = portfolio_df['Share price'].apply(times3plus200)

print("This is before re-running the fourth column add, of total share value. I am curious to see if it actually calculates this when I update the share price of the stocks.\n\n" + str(portfolio_df) + "\n\n")

#I am curious if the column "Total share value" is calculated each time, or if it entered static values into the table. One way to find out, right?

portfolio_df['Total share value'] = portfolio_df['Share count'] * portfolio_df['Share price']

print("This is AFTER re-running the fourth column add\n\n" + str(portfolio_df) + "\n\n")
'''
#create function to triple stock price & add $200 to it
def times3plus200(balance):
	return ((balance * 3) + 200)

total_client_net_worth = bank_client_df['Net Worth [$]'].apply(times3plus200)

print("Total net worth of all clients at bank, after applying new formula to their net worth is: $" + str(total_client_net_worth.sum()))
