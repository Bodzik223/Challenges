import pandas as pd


transactions = pd.read_csv("PD 2023 Wk 1 Input.csv")
targets = pd.read_csv("Targets.csv")

print(targets)
print(transactions)

transactions = transactions[transactions['Transaction Code'].str[:3] == "DSB"]

transactions['Online or In-Person'] = transactions['Online or In-Person'].apply(lambda x: "Online" if x==1 else "In-Person")

transactions['Quarter'] = pd.to_datetime(transactions['Transaction Date']).dt.quarter

transactions_sum = transactions.groupby(['Online or In-Person', 'Quarter'], as_index = False)['Value'].sum()

print(transactions_sum)

targets = targets.melt(id_vars='Online or In-Person', var_name='Quarter', value_name='Value')

targets['Quarter'] = targets['Quarter'].str.extract(r'(\d+)').astype(int)

targets = targets.rename(columns={'Value': 'Quarterly Target'})

print(targets)

task = pd.merge(transactions_sum, targets, on=['Online or In-Person', 'Quarter'])

task['Difference'] = task['Value'] - task['Quarterly Target']

print(task)
task.to_excel('task.xlsx', sheet_name='task')