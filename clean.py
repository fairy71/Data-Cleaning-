import pandas as pd
import re

# ----------------------------
# 1. LOAD DATA
# ----------------------------
df = pd.read_csv("customer_contacts.csv")

print("Original Data:")
print(df.head())


# ----------------------------
# 2. REMOVE DUPLICATES
# ----------------------------
df = df.drop_duplicates(subset=['email'], keep='first')


# ----------------------------
# 3. CLEAN & STANDARDIZE PHONE NUMBERS
# ----------------------------

def clean_phone(phone):
    if pd.isna(phone):
        return None
    
    # Remove all non-numeric characters
    digits = re.sub(r"\D", "", phone)
    
    # Assume it's a 10-digit number and format: (XXX) XXX-XXXX
    if len(digits) == 10:
        return f"({digits[:3]}) {digits[3:6]}-{digits[6:]}"
    else:
        return None  # invalid numbers removed

df["clean_phone"] = df["phone"].apply(clean_phone)


# ----------------------------
# 4. VALIDATE & CLEAN EMAILS
# ----------------------------

def clean_email(email):
    if pd.isna(email):
        return None
    
    email = email.strip().lower()
    
    pattern = r"^[a-zA-Z0-9._%+-]+@[a-z0-9.-]+\.[a-z]{2,}$"
    if re.match(pattern, email):
        return email
    return None

df["clean_email"] = df["email"].apply(clean_email)


# ----------------------------
# 5. SPLIT NAME INTO FIRST & LAST NAME
# ----------------------------

def split_name(fullname):
    if pd.isna(fullname):
        return pd.Series([None, None])
    
    parts = fullname.strip().split()
    if len(parts) >= 2:
        return pd.Series([parts[0], " ".join(parts[1:])])
    return pd.Series([parts[0], None])

df[["first_name", "last_name"]] = df["name"].apply(split_name)


# ----------------------------
# 6. DROP UNUSED / DIRTY COLUMNS
# ----------------------------
df_cleaned = df[["first_name", "last_name", "clean_email", "clean_phone"]]


# ----------------------------
# 7. SAVE CLEANED DATA
# ----------------------------

df_cleaned.to_csv("customer_contacts_cleaned.csv", index=False)

print("Cleaned dataset saved!")
print(df_cleaned.head())
