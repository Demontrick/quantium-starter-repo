import pandas as pd
import os

# Define file paths
data_dir = "data"
files = ["daily_sales_data_0.csv", "daily_sales_data_1.csv", "daily_sales_data_2.csv"]

# Initialize an empty list to store dataframes
dfs = []

# Process each file
for file in files:
    file_path = os.path.join(data_dir, file)
    print(f"📄 Reading {file_path}")
    df = pd.read_csv(file_path)
    print(f"🛒 Available Products: {df['product'].unique()}")
    
    # Filter only 'pink morsel' sales
    df = df[df['product'] == 'pink morsel']
    
    # Clean and convert 'price' column
    df['price'] = df['price'].replace('[\$,]', '', regex=True).astype(float)
    
    # Ensure 'quantity' is numeric
    df['quantity'] = pd.to_numeric(df['quantity'], errors='coerce')
    
    # Calculate 'Sales' column
    df['Sales'] = df['price'] * df['quantity']
    
    # Round to 2 decimal places
    df['Sales'] = df['Sales'].round(2)
    
    # Keep only required columns
    df = df[['date', 'region', 'Sales']]
    df.rename(columns={'date': 'Date', 'region': 'Region'}, inplace=True)
    
    # Append to list
    dfs.append(df)

# Combine all dataframes into one
final_df = pd.concat(dfs, ignore_index=True)

# Save cleaned data
output_file = os.path.join(data_dir, "pink_morsels_sales.csv")
final_df.to_csv(output_file, index=False)

print(f"✅ Process completed! Final dataset saved to {output_file}")