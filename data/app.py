import dash
from dash import dcc, html, Input, Output
import pandas as pd
import plotly.express as px
from pathlib import Path

# Load the data
csv_path = Path(__file__).resolve().parent / "pink_morsels_sales.csv"
if not csv_path.exists():
    raise FileNotFoundError(f"CSV file not found at {csv_path}")

print(f"Loading CSV from: {csv_path}")  # Optional: for debugging path

df = pd.read_csv(csv_path)

# Clean columns and date
df.columns = df.columns.str.strip()
df['Date'] = pd.to_datetime(df['Date'])
df = df.sort_values(by='Date')

# Initialize Dash app
app = dash.Dash(__name__)

# Layout
app.layout = html.Div([
    html.H1("Pink Morsel Sales Visualizer", style={'textAlign': 'center'}),

    html.Div([
        dcc.RadioItems(
            id='region-filter',
            options=[
                {'label': 'All', 'value': 'all'},
                {'label': 'North', 'value': 'north'},
                {'label': 'East', 'value': 'east'},
                {'label': 'South', 'value': 'south'},
                {'label': 'West', 'value': 'west'},
            ],
            value='all',
            labelStyle={'display': 'inline-block', 'margin-right': '10px'}
        )
    ], style={'textAlign': 'center', 'margin-bottom': '20px'}),

    dcc.Graph(id='sales-graph')
])

@app.callback(
    Output('sales-graph', 'figure'),
    Input('region-filter', 'value')
)
def update_graph(selected_region):
    if selected_region == 'all':
        filtered_df = df
    else:
        filtered_df = df[df['Region'].str.lower() == selected_region]

    fig = px.line(
        filtered_df,
        x='Date',
        y='Sales',
        color='Region',
        title="Pink Morsel Sales Over Time by Region"
    )
    return fig

# Run the app
if __name__ == "__main__":
    app.run(debug=True)
