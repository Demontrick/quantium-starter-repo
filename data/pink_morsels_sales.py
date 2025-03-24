import pandas as pd

# List of input CSV files
csv_files = ["data/daily_sales_data_0.csv", "data/daily_sales_data_1.csv", "data/daily_sales_data_3.csv"]

# Empty list to store filtered data
filtered_data = []

# Loop through each CSV file
for file in csv_files:
    df = pd.read_csv(file)  # Read the CSV file
    
    # Filter only "Pink Morsels"
    df = df[df["product"] == "Pink Morsels"]
    
    # Create "Sales" column (Quantity * Price)
    df["Sales"] = df["quantity"] * df["price"]
    
    # Select only required columns: Sales, Date, Region
    df = df[["Sales", "date", "region"]]
    
    # Store filtered data
    filtered_data.append(df)

# Combine all filtered data
final_df = pd.concat(filtered_data)

# Save to the final output CSV file
final_df.to_csv("data/pink_morsels_sales.csv", index=False)

print("✅ all data filtered in pink_morsels_sales'")
