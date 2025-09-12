import pandas as pd
import numpy as np


data = {
    "Student_ID": [1, 2, 2, 3, 4, 5, 6],
    "Name": ["  Ali ", "Sara", "sara", "John", "Mina", "Usman", "Hira"],
    "Age": ["18", "19", np.nan, "20", "17", "19", "eighteen"],
    "Gender": ["M", "female", "F", "Male", "FEMALE", "f", "m"],
    "Marks_Math": [85, 92, 92, 105, 45, -5, 76],
    "Marks_English": [78, 88, 88, 67, 59, np.nan, 91],
    "Marks_Science": [90, 95, 95, 89, -2, 80, np.nan],
}

df = pd.DataFrame(data)
print(" Raw Data")
print(df)


df = df.drop_duplicates()
print("\n After Removing Duplicates")
print(df)


df["Name"] = df["Name"].str.strip().str.capitalize()


df["Gender"] = df["Gender"].str.lower().map({
    "m": "Male",
    "male": "Male",
    "f": "Female",
    "female": "Female"
})


df["Age"] = pd.to_numeric(df["Age"], errors="coerce")


df["Age"] = df["Age"].fillna(df["Age"].mean()).astype(int)


for col in ["Marks_Math", "Marks_English", "Marks_Science"]:
    df[col] = df[col].clip(lower=0, upper=100)   


df["Marks_English"] = df["Marks_English"].fillna(df["Marks_English"].mean())
df["Marks_Science"] = df["Marks_Science"].fillna(df["Marks_Science"].mean())
df["Total_Marks"] = df[["Marks_Math", "Marks_English", "Marks_Science"]].sum(axis=1)
df["Average_Marks"] = df[["Marks_Math", "Marks_English", "Marks_Science"]].mean(axis=1)


print("\n Cleaned Data")
print(df)