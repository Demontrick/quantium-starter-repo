import pandas as pd
import os

# List of input CSV files
csv_files = ["data/daily_sales_data_0.csv", "data/daily_sales_data_1.csv", "data/daily_sales_data_2.csv"]

# Empty list to store filtered data
filtered_data = []

# Loop through each CSV file
for file in csv_files:
    if not os.path.exists(file):
        print(f"🚨 ERROR: {file} not found!")
        continue  # Skip if file doesn't exist
    
    df = pd.read_csv(file)  # Read the CSV file
    print(f"📄 Reading {file} - Total Rows: {len(df)}")

    if "product" not in df.columns:
        print(f"🚨 ERROR: 'product' column not found in {file}")
        continue

    print("🛒 Available Products:", df["product"].unique())  # Debug product names

    # ✅ Corrected filter condition to match "pink morsel"
    df = df[df["product"].str.strip().str.lower() == "pink morsel"]
    
    if df.empty:
        print(f"⚠️ No 'Pink Morsel' found in {file}, skipping...")
        continue

    # Create "Sales" column (Quantity * Price)
    df["Sales"] = df["quantity"] * df["price"]

    # Keep only required columns: Sales, Date, Region
    df = df[["Sales", "date", "region"]]

    # Store filtered data
    filtered_data.append(df)

# Check if we got any data before writing
if not filtered_data:
    print("🚨 No data to save! 'pink_morsels_sales.csv' will be empty.")
else:
    # Combine all filtered data
    final_df = pd.concat(filtered_data)

    # 🔥 Clean & Format Data
    final_df["Sales"] = final_df["Sales"].round(2)  # Round sales values to 2 decimal places
    final_df = final_df.sort_values(by=["date", "region"])  # Sort by Date & Region
    final_df = final_df.drop_duplicates()  # Remove duplicate rows if any

    # Save to CSV file
    final_df.to_csv("data/pink_morsels_sales.csv", index=False)

    print("✅ All data filtered, cleaned, and saved in 'pink_morsels_sales.csv'!")
