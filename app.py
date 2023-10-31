import os

os.system("pip install -r packages.txt")

import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import matplotlib.pyplot as plt
import seaborn as sns

import wbgapi as wb

import json
import csv

wb.series.metadata.get('SL.UEM.TOTL.ZS')
Total_unemployment = wb.data.DataFrame('SL.UEM.TOTL.ZS', economy=['COL','ARG','CHL','BRA', 'URY', 'BOL','PER','PRY','ECU','VEN','MEX','CAN','USA','CRI'], time= range(2002,2020), labels=True).reset_index(drop=True).rename(columns={'SL.UEM.TOTL.ZS':'Unemployment'})
Total_unemployment

wb.series.metadata.get('NY.GDP.PCAP.CD')
GDP_per_capita = wb.data.DataFrame('NY.GDP.PCAP.CD', economy=['COL','ARG','CHL','BRA', 'URY', 'BOL','PER','PRY','ECU','VEN','MEX','CAN','USA','CRI'], time= range(2002,2020), labels=True).reset_index(drop=True).rename(columns={'SL.UEM.TOTL.ZS':'Unemployment'})
GDP_per_capita
wb.series.metadata.get('SP.DYN.LE00.IN')

Life_expectancy_at_birth = wb.data.DataFrame('SP.DYN.LE00.IN', economy=['COL','ARG','CHL','BRA', 'URY', 'BOL','PER','PRY','ECU','VEN','MEX','CAN','USA','CRI'], time= range(2002,2020), labels=True).reset_index(drop=True).rename(columns={'SL.UEM.TOTL.ZS':'Unemployment'})
Life_expectancy_at_birth
wb.series.metadata.get('SM.POP.NETM')

Migration= wb.data.DataFrame('SM.POP.NETM', economy=['COL','ARG','CHL','BRA', 'URY', 'BOL','PER','PRY','ECU','VEN','MEX','CAN','USA','CRI'], time= range(2002,2020), labels=True).reset_index(drop=True).rename(columns={'SL.UEM.TOTL.ZS':'Unemployment'})
Migration
wb.series.metadata.get('EG.ELC.ACCS.ZS')
Energy_access= wb.data.DataFrame('EG.ELC.ACCS.ZS', economy=['COL','ARG','CHL','BRA', 'URY', 'BOL','PER','PRY','ECU','VEN','MEX','CAN','USA','CRI'], time= range(2002,2020), labels=True).reset_index(drop=True).rename(columns={'SL.UEM.TOTL.ZS':'Unemployment'})
Energy_access
Energy_access.set_index('Country').unstack().reset_index()


st.write("""
*Migración por país*
""")

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


Total = pd.read_csv("total_migration.csv")

st.plotly_chart(fig, use_container_width=True)

fig2 = px.line(Total, x='Years', y='Migration', color='Contry',
              title='Migración por País a lo largo de los Años',
              labels={'Years': 'Año', 'Migration': 'Migración'})

st.plotly_chart(fig2, use_container_width=True)



contry_to_plot = 'Colombia'
filtered_data = Total[Total['Contry'] == contry_to_plot]
fig3 = px.scatter(
    filtered_data,
    x='GDP_per_capita',
    y='Total_unemployment',
    text='Years',
    title=f'Gráfico de Dispersión: PIB per Capita vs. Tasa de Desempleo Colombia',
    labels={'GDP_per_capita': 'PIB per Capita', 'Total_unemployment': 'Tasa de Desempleo'},
)

st.plotly_chart(fig3, use_container_width=True)


