import pandas as pd

df = pd.read_csv('PD 2023 Wk 1 Input.csv')
print(df.head())

new_cols_dict ={ # вказівка назв стовпців, які я хочу використовувати
    'Transaction Code':'Bank',
}

df.rename(new_cols_dict, axis=1, inplace=True)  # Перейменування стовпців на вказані назви стовпців

df.Bank = df.Bank.apply(lambda x: x[:3] if len(x)>14 else x[:2]) # Зміна значення в стовпці

print(df.head())

df['Transaction Date'] = pd.to_datetime(df['Transaction Date']).dt.strftime('%B')

df = df.groupby(['Transaction Date','Bank'], as_index = False)['Value'].sum()

df['Rank'] = df.groupby('Transaction Date')['Value'].rank(ascending=False).astype(int)

average_rank_per_bank = df.groupby('Bank')['Rank'].mean().reset_index()
average_rank_per_bank.columns = ['Bank', 'Avg Rank per Bank']

average_transaction_value_per_rank = df.groupby('Rank')['Value'].mean().reset_index()
average_transaction_value_per_rank.columns = ['Rank', 'Avg Transaction Value per Rank']

df = df.merge(average_rank_per_bank, on='Bank').merge(average_transaction_value_per_rank, on='Rank')

df = df[['Transaction Date', 'Bank', 'Value', 'Rank', 'Avg Rank per Bank', 'Avg Transaction Value per Rank']]
