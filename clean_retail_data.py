import pandas as pd

# Load
df = pd.read_csv("retail_sales_data.csv")

df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_")

df['sale_date'] = pd.to_datetime(df['sale_date'], errors='coerce')
df['sale_time'] = pd.to_datetime(df['sale_time'], format='%H:%M:%S', errors='coerce').dt.time


df = df[df['quantity'] > 0]
df = df[df['price_per_unit'] > 0]
df = df[df['cogs'] >= 0]

df['profit'] = df['total_sale'] - (df['cogs'] * df['quantity'])
df['month'] = df['sale_date'].dt.month
df['day_of_week'] = df['sale_date'].dt.day_name()
df['hour'] = pd.to_datetime(df['sale_time'], format='%H:%M:%S', errors='coerce').apply(lambda x: x.hour if pd.notnull(x) else None)
df['age_group'] = pd.cut(df['age'], bins=[0, 17, 25, 35, 50, 65, 100], labels=['<18', '18-25', '26-35', '36-50', '51-65', '65+'])

# Save
df.to_csv("retail_sales_cleaned.csv", index=False)

print("Cleaning complete. File saved as 'retail_sales_cleaned.csv'")
