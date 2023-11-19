import pandas as pd

#create dataframe
bank_client_df = pd.DataFrame({'Bank Client ID':[111, 222, 333, 444],
								'Bank Client Name':['Chanel', 'Steve', 'Mitch', 'Ryan'],
								'Net Worth [$]':[3500, 29000, 10000, 2000],
								'Years with bank':[3, 4, 9, 5]})
#Let's experiment with sorting

print("Before sorting")
print(bank_client_df)
print("\n\n")

#run a sort command & print it
print("While sorting")
print(bank_client_df.sort_values(by = 'Years with bank'))
print("\n\n")

print("After sorting")
print(bank_client_df)
print("\n\n")

#use inplace = True while sorting
bank_client_df.sort_values(by = 'Years with bank', inplace = True)

print("After sorting with inplace = True")
print(bank_client_df)
print("\n\n")
