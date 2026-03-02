import pandas as pd

df = pd.read_csv("bakery.csv")

print("Shape:", df.shape)
print("\nColumns:", df.columns)
print("\nFirst 5 Rows:")
print(df.head())
print("\nData Info:")
print(df.info())
# Convert DateTime column properly
df['DateTime'] = pd.to_datetime(df['DateTime'], errors='coerce')

# Extract Date
df['Date'] = df['DateTime'].dt.date

# Extract Time
df['Time'] = df['DateTime'].dt.time

# Extract Year, Month, Hour
df['Year'] = df['DateTime'].dt.year
df['Month'] = df['DateTime'].dt.month
df['Hour'] = df['DateTime'].dt.hour

print("\nAfter Feature Engineering:")
print(df.head())
print(df.info())
df['Items'] = df['Items'].str.strip().str.lower()
df['Daypart'] = df['Daypart'].str.strip().str.lower()
df['DayType'] = df['DayType'].str.strip().str.lower()
df.to_csv("bakery_cleaned.csv", index=False)
print("Cleaning Completed Successfully!")
