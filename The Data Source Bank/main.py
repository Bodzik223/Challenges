import pandas as pd

df = pd.read_csv('PD 2023 Wk 1 Input.csv')
print(df.head())


new_cols_dict ={ # вказівка назв стовпців, які я хочу використовувати
    'Transaction Code':'Bank',
}

df.rename(new_cols_dict, axis=1, inplace=True)  # Перейменування стовпців на вказані назви стовпців

df.Bank = df.Bank.apply(lambda x: x[:3] if len(x)>14 else x[:2]) # Зміна значення в стовпці

df['Online or In-Person'] = df['Online or In-Person'].apply(lambda x: "Online" if x==1 else "In-Person") # Перейменування стовпців на вказані назви стовпців

df['Transaction Date'] = pd.to_datetime(df['Transaction Date']) # Перетворення стовпця "Дата транзакції" в тип datetime

df['Transaction Date'] = df['Transaction Date'].dt.day_name() # Витягніть день тижня і заміна в стовпці

print(df.head())

df1 = df[['Bank', 'Value']].copy() # копіювання стовпців для знаходження загальної суми транзакцій за кожним банком
df1 = df1.groupby(['Bank'])['Value'].sum() # Знаходження загальної суми транзакцій за кожним банком

print(df1)

df2 = df[['Bank','Online or In-Person', 'Transaction Date', 'Value']].copy() # копіювання стовпців для знаходження загальної суми за банками, днями тижня та типами транзакцій (онлайн або особисто)
df2 = df2.groupby(['Bank','Online or In-Person', 'Transaction Date'])['Value'].sum() # Знаходження загальної суми за банками, днями тижня та типами транзакцій (онлайн або особисто)

print(df2)

df3 = df[['Bank','Customer Code', 'Value']].copy() # копіювання стовпців для знаходження підсумкового значення за кодом банку та кодом клієнта
df3 = df3.groupby(['Bank','Customer Code'], as_index = False)['Value'].sum() # Знаходження підсумкового значення за кодом банку та кодом клієнта

print(df3)

df1.to_csv('task_1.csv')
df2.to_csv('task_2.csv')
df3.to_csv('task_3.csv')
