import plotly.express as px
import pandas as pd

data = {
    'Country': ['COL', 'ARG', 'CHL', 'BRA', 'URY', 'BOL', 'PER', 'PRY', 'ECU', 'VEN', 'MEX', 'CAN', 'USA', 'CRI'],
    'Latitude': [4.5709, -38.4161, -35.6751, -14.2350, -32.5228, -16.2902, -9.18997, -23.4425, -1.8312, 6.4238, 23.6345, 56.1304, 37.0902, 9.7489],
    'Longitude': [-74.2973, -63.6167, -71.5430, -51.9253, -55.7658, -63.5887, -75.0152, -58.4438, -78.1834, -66.5897, -102.5528, -106.3468, -95.7129, -83.7534],
    'Migration': [200000, 150000, 300000, 500000, 80000, 120000, 250000, 90000, 180000, 300000, 700000, 2500000, 3000000, 120000]
}

df = pd.DataFrame(data)

fig = px.scatter_geo(df, lat='Latitude', lon='Longitude', size='Migration', color='Country',
                     hover_name='Country', text='Migration', projection='natural earth',
                     title='Mapa de Migración por País', size_max=30)

fig.show()