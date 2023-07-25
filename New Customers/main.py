import pandas as pd
January = pd.read_excel('New Customers.xlsx', sheet_name='January')
January = January.pivot(index=['ID', 'Joining Day'], columns='Demographic', values='Value').reset_index()
January.columns = ['ID', 'Joining Day', 'Account Type', 'Date of Birth', 'Ethnicity']
January['Date of Birth'] =  pd.to_datetime(January['Date of Birth']).dt.strftime('%d/%m/%Y')
January['Joining Day'] = pd.to_datetime(January['Joining Day'].astype(str) + '/01/2023', format='%d/%m/%Y').dt.strftime('%d/%m/%Y')

February = pd.read_excel('New Customers.xlsx', sheet_name='February')
February = February.pivot(index=['ID', 'Joining Day'], columns='Demographic', values='Value').reset_index()
February.columns = ['ID', 'Joining Day', 'Account Type', 'Date of Birth', 'Ethnicity']
February['Date of Birth'] =  pd.to_datetime(February['Date of Birth']).dt.strftime('%d/%m/%Y')
February['Joining Day'] = pd.to_datetime(February['Joining Day'].astype(str) + '/02/2023', format='%d/%m/%Y').dt.strftime('%d/%m/%Y')

March = pd.read_excel('New Customers.xlsx', sheet_name='March')
March = March.pivot(index=['ID', 'Joining Day'], columns='Demographic', values='Value').reset_index()
March.columns = ['ID', 'Joining Day', 'Account Type', 'Date of Birth', 'Ethnicity']
March['Date of Birth'] =  pd.to_datetime(March['Date of Birth']).dt.strftime('%d/%m/%Y')
March['Joining Day'] = pd.to_datetime(March['Joining Day'].astype(str) + '/03/2023', format='%d/%m/%Y').dt.strftime('%d/%m/%Y')

April = pd.read_excel('New Customers.xlsx', sheet_name='April')
April = April.pivot(index=['ID', 'Joining Day'], columns='Demographic', values='Value').reset_index()
April.columns = ['ID', 'Joining Day', 'Account Type', 'Date of Birth', 'Ethnicity']
April['Date of Birth'] = pd.to_datetime(April['Date of Birth']).dt.strftime('%d/%m/%Y')
April['Joining Day'] = pd.to_datetime(April['Joining Day'].astype(str) + '/04/2023', format='%d/%m/%Y').dt.strftime('%d/%m/%Y')

May = pd.read_excel('New Customers.xlsx', sheet_name='May')
May = May.pivot(index=['ID', 'Joining Day'], columns='Demographic', values='Value').reset_index()
May.columns = ['ID', 'Joining Day', 'Account Type', 'Date of Birth', 'Ethnicity']
May['Date of Birth'] = pd.to_datetime(May['Date of Birth']).dt.strftime('%d/%m/%Y')
May['Joining Day'] = pd.to_datetime(May['Joining Day'].astype(str) + '/05/2023', format='%d/%m/%Y').dt.strftime('%d/%m/%Y')

June = pd.read_excel('New Customers.xlsx', sheet_name='June')
June = June.pivot(index=['ID', 'Joining Day'], columns='Demographic', values='Value').reset_index()
June.columns = ['ID', 'Joining Day', 'Account Type', 'Date of Birth', 'Ethnicity']
June['Date of Birth'] = pd.to_datetime(June['Date of Birth']).dt.strftime('%d/%m/%Y')
June['Joining Day'] = pd.to_datetime(June['Joining Day'].astype(str) + '/06/2023', format='%d/%m/%Y').dt.strftime('%d/%m/%Y')

July = pd.read_excel('New Customers.xlsx', sheet_name='July')
July = July.pivot(index=['ID', 'Joining Day'], columns='Demographic', values='Value').reset_index()
July.columns = ['ID', 'Joining Day', 'Account Type', 'Date of Birth', 'Ethnicity']
July['Date of Birth'] = pd.to_datetime(July['Date of Birth']).dt.strftime('%d/%m/%Y')
July['Joining Day'] = pd.to_datetime(July['Joining Day'].astype(str) + '/07/2023', format='%d/%m/%Y').dt.strftime('%d/%m/%Y')

August = pd.read_excel('New Customers.xlsx', sheet_name='August')
August = August.pivot(index=['ID', 'Joining Day'], columns='Demographic', values='Value').reset_index()
August.columns = ['ID', 'Joining Day', 'Account Type', 'Date of Birth', 'Ethnicity']
August['Date of Birth'] = pd.to_datetime(August['Date of Birth']).dt.strftime('%d/%m/%Y')
August['Joining Day'] = pd.to_datetime(August['Joining Day'].astype(str) + '/08/2023', format='%d/%m/%Y').dt.strftime('%d/%m/%Y')

September = pd.read_excel('New Customers.xlsx', sheet_name='September')
September = September.pivot(index=['ID', 'Joining Day'], columns='Demographic', values='Value').reset_index()
September.columns = ['ID', 'Joining Day', 'Account Type', 'Date of Birth', 'Ethnicity']
September['Date of Birth'] = pd.to_datetime(September['Date of Birth']).dt.strftime('%d/%m/%Y')
September['Joining Day'] = pd.to_datetime(September['Joining Day'].astype(str) + '/09/2023', format='%d/%m/%Y').dt.strftime('%d/%m/%Y')

October = pd.read_excel('New Customers.xlsx', sheet_name='October')
October = October.pivot(index=['ID', 'Joining Day'], columns='Demographic', values='Value').reset_index()
October.columns = ['ID', 'Joining Day', 'Account Type', 'Date of Birth', 'Ethnicity']
October['Date of Birth'] = pd.to_datetime(October['Date of Birth']).dt.strftime('%d/%m/%Y')
October['Joining Day'] = pd.to_datetime(October['Joining Day'].astype(str) + '/10/2023', format='%d/%m/%Y').dt.strftime('%d/%m/%Y')

November = pd.read_excel('New Customers.xlsx', sheet_name='November')
November = November.pivot(index=['ID', 'Joining Day'], columns='Demographic', values='Value').reset_index()
November.columns = ['ID', 'Joining Day', 'Account Type', 'Date of Birth', 'Ethnicity']
November['Date of Birth'] = pd.to_datetime(November['Date of Birth']).dt.strftime('%d/%m/%Y')
November['Joining Day'] = pd.to_datetime(November['Joining Day'].astype(str) + '/11/2023', format='%d/%m/%Y').dt.strftime('%d/%m/%Y')

December = pd.read_excel('New Customers.xlsx', sheet_name='December')
December = December.pivot(index=['ID', 'Joining Day'], columns='Demographic', values='Value').reset_index()
December.columns = ['ID', 'Joining Day', 'Account Type', 'Date of Birth', 'Ethnicity']
December['Date of Birth'] = pd.to_datetime(December['Date of Birth']).dt.strftime('%d/%m/%Y')
December['Joining Day'] = pd.to_datetime(December['Joining Day'].astype(str) + '/12/2023', format='%d/%m/%Y').dt.strftime('%d/%m/%Y')

result = pd.concat([January, February, March, April, May, June, July, August, September, October, November, December])

result['Joining Day'] = pd.to_datetime(result['Joining Day'])
result = result.sort_values(by='Joining Day')
result = result.drop_duplicates(subset='ID', keep='first')
result = result.reset_index(drop=True)
result['Joining Day']  = result['Joining Day'].dt.strftime('%d/%m/%Y')
print(result)
print(result.info())
result.to_excel('task.xlsx', sheet_name='Result')