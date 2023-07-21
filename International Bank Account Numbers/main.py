import pandas
import pandas as pd


swift_codes = pd.read_csv("Swift Codes.csv")
transactions = pd.read_csv("Transactions.csv")

transactions["Sort Code"] = transactions["Sort Code"].apply(lambda x: x.replace("-", ""))

df = pd.merge(swift_codes, transactions, on='Bank', how='inner')

df["Country Code"] = "GB"

df["IBAN"] = df["Country Code"].astype('str')+df["Check Digits"].astype('str')+df["SWIFT code"].astype('str')+df["Sort Code"].astype('str')+df["Account Number"].astype('str')

df_res = df[["Transaction ID", "IBAN"]].copy()
df_res = df_res.reset_index(drop=True)
print(df_res.head)

df_res.to_excel('task.xlsx', sheet_name='Data')