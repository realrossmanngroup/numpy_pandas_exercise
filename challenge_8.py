import pandas as pd

#create dataframe
bank_client_df = pd.DataFrame({'Bank Client ID':[111, 222, 333, 444],
								'Bank Client Name':['Chanel', 'Steve', 'Mitch', 'Ryan'],
								'Net Worth [$]':[3500, 29000, 10000, 2000],
								'Years with bank':[3, 4, 9, 5]})
								
#fix display issue
pd.set_option('display.width', 750)

#print table								
print(bank_client_df)							

print(bank_client_df[bank_client_df['Years with bank'] >= 5])
