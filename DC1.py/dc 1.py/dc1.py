import pandas as pd
import numpy as np

df = pd.read_csv("dirty_sales.csv")

print("Initial Data:")
print(df.head())

print("\nMissing Values Before Cleaning:")
print(df.isnull().sum())

df = df.dropna(subset=["CustomerID"])

df["Age"].fillna(df["Age"].mean(), inplace=True)

df["Sales"].fillna(df["Sales"].median(), inplace=True)

df["Country"] = df["Country"].str.strip().str.title()

df["Gender"] = df["Gender"].replace({"M": "Male", "F": "Female"})

df = df.drop_duplicates()

df["CustomerID"] = df["CustomerID"].astype(int)
df["Date"] = pd.to_datetime(df["Date"], errors='coerce')

Q1 = df["Sales"].quantile(0.25)
Q3 = df["Sales"].quantile(0.75)
IQR = Q3 - Q1
lower_limit = Q1 - 1.5 * IQR
upper_limit = Q3 + 1.5 * IQR
df["Sales"] = np.where(df["Sales"] > upper_limit, upper_limit, df["Sales"])
df["Sales"] = np.where(df["Sales"] < lower_limit, lower_limit, df["Sales"])

df = df[(df["Age"] > 10) & (df["Age"] < 100)]

df.reset_index(drop=True, inplace=True)

print("\nCleaned Data:")
print(df)

print("\nSummary after cleaning:")
print(df.info())
print(df.describe())
