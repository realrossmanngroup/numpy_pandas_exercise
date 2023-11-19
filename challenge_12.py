import pandas as pd

#make dataframe for first set of bank customers
bank_df_1 = pd.DataFrame({'Client ID':[1, 2, 3, 4, 5],
							'First name':['Marjorie', 'Andrew', 'Stephen', 'Michael', 'Paul'],
							'Last name':['Flowers', 'Stephenson', 'Michaels', 'Logan', 'Andrews']})

print("Print dataframe 1")
print(bank_df_1)
print("\n\n")

#make dataframe for second set of bank customers		
bank_df_2 = pd.DataFrame({'Client ID':[6, 7, 8, 9, 10],
							'First name':['John', 'Oreo', 'Ashton', 'Preston', 'Dick'],
							'Last name':['Sprewell', 'Roberts', 'Kutcher', 'MacNamera', 'Simpson']})
print("Print dataframe 2")
print(bank_df_2)
print("\n\n")

#print concatenated dataframes
print("Print dataframes concatenated")
print(pd.concat([bank_df_1, bank_df_2]))
print("\n\n")

#create customer salary dataframe
bank_customer_salary = pd.DataFrame({'Client ID':[1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
									'Salary':[50000, 100000, 90000, 40403, 160000, 285000, 125000, 750493, 250000, 320000]})

print("Print customer salaries from another dataframe")
print(bank_customer_salary)									
print("\n\n")

#make new dataframe combining customer 1 & 2
print("Print new dataframe created by combining bank_df_1 & bank_df_2")
bank_customers_combined = pd.concat([bank_df_1, bank_df_2])
print(bank_customers_combined)
print("\n\n")

#merge bank_customer_salary with bank_customers_combined
bank_df_all = pd.merge(bank_customers_combined, bank_customer_salary, on='Client ID')
print("bank customers combined + salary data")
print(bank_df_all)
print("\n\n")

#add myself to the dataframe, by making a dataframe for me & merging it to the original
my_info = pd.DataFrame({'Client ID':[11],
						'First name':["Louis"],
						'Last name':["Rossmann"],
						'Salary':[370000]})
print("printing my dataframe with just me in it")
print(my_info)
print("\n\n")

#merge new dataframe to original						
bank_df_all = pd.concat([bank_df_all, my_info])

print("Adding myself to it!")
print(bank_df_all)	



