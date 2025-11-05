import pandas as pd
import re

df = pd.read_csv("messy_customers.csv")

df['Name'] = df['Name'].str.title().str.strip()

df.drop_duplicates(subset='Email', keep='first', inplace=True)

def clean_email(email):
    if re.match(r"[^@]+@[^@]+\.[^@]+", str(email)):
        return email.lower()
    return None

df['Email'] = df['Email'].apply(clean_email)

df['Phone'] = df['Phone'].astype(str).str.replace(r'\D', '', regex=True)

print(df.head())
