import dash
from dash import dcc, html
import pandas as pd
import plotly.express as px

# Load the data
df = pd.read_csv("data/pink_morsels_sales.csv")

# Fix: Rename columns to remove any extra spaces (important!)
df.columns = df.columns.str.strip()

# Convert 'Date' column to datetime format
df['Date'] = pd.to_datetime(df['Date'])

# Sort by Date
df = df.sort_values(by='Date')

# Create the line chart
fig = px.line(df, x='Date', y='Sales', title="Pink Morsel Sales Over Time")

# Initialize Dash app
app = dash.Dash(__name__)

# Layout
app.layout = html.Div([
    html.H1("Pink Morsel Sales Visualizer", style={'textAlign': 'center'}),
    dcc.Graph(
        figure=px.line(
            df,
            x='Date',
            y='Sales',
            color='Region',  # <-- THIS is new (different color for each region)
            title="Pink Morsel Sales Over Time by Region"
        )
    )
])

# Run the app
if __name__ == "__main__":
    app.run(debug=True)

