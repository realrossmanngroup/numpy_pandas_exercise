import pandas as pd

#create dataframe
bank_client_df = pd.DataFrame({'Bank Client ID':[111, 222, 333, 444],
								'Bank Client Name':['Chanel', 'Steve', 'Mitch', 'Ryan'],
								'Net Worth [$]':[3500, 29000, 10000, 2000],
								'Years with bank':[3, 4, 9, 5]})
								
#fix display issue - makes formatting a lot better
pd.set_option('display.width', 750)

#print table								
print(str(bank_client_df) + "\n\n")

#Pick rows that satisfy a certain criteria: very loyal customers in this case
print(str(bank_client_df[bank_client_df['Years with bank'] >= 5]) + "\n\n")

#delete a column from the dataframe
del bank_client_df['Bank Client ID']
print("This is after deleting bank client ID column, let's see if it works!! \n\n" + str(bank_client_df))

#Here is mini challenge 8:

#print list of customers with net worth over $5k
print("Let's only select bank customers with a net worth of $5000 or higher:\n\n" + str(bank_client_df[bank_client_df['Net Worth [$]'] > 5000]))

#get total net worth of all individuals with net worth over $5000
print(str(bank_client_df[bank_client_df['Net Worth [$]'] > 5000].sum()) + "\n\n")

#That is messy. :( Let's see if I can print it without the names below:
print(str(bank_client_df[bank_client_df['Net Worth [$]'] > 5000]['Net Worth [$]'].sum()) + "\n\n")
