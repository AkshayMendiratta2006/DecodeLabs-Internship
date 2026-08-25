import pandas as pd

df = pd.read_excel('Dataset for Data Analytics.xlsx')

mode_coupon = df['CouponCode'].mode()[0]
df['CouponCode'] = df['CouponCode'].fillna(mode_coupon)

df = df.drop_duplicates(subset=['OrderID'])

df['Date'] = pd.to_datetime(df['Date']).dt.strftime('%Y-%m-%d')

text_cols = ['Product', 'ShippingAddress', 'PaymentMethod', 'OrderStatus', 'ReferralSource']
for col in text_cols:
    df[col] = df[col].astype(str).str.strip().str.title()

numeric_cols = ['UnitPrice', 'TotalPrice']
for col in numeric_cols:
    df[col] = df[col].round(2)

df.to_excel('Cleaned_Dataset.xlsx', index=False)
print("Data Cleaning complete! File saved as Cleaned_Dataset.xlsx")