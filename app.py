import pandas as pd
import plotly.express as px
import plotly.io as pio

# Load all datasets
df_2015 = pd.read_csv('./data/2015.csv')
df_2016 = pd.read_csv('./data/2016.csv')
df_2017 = pd.read_csv('./data/2017.csv')
df_2018 = pd.read_csv('./data/2018.csv')
df_2019 = pd.read_csv('./data/2019.csv')

# Standardize column names and select relevant columns for each year
# 2015
df_2015 = df_2015.rename(columns={
    'Happiness Score': 'Score',
    'Country': 'Country or region',
    'Region': 'Region'
})[['Country or region', 'Region', 'Score']]
df_2015['Year'] = 2015

# 2016
df_2016 = df_2016.rename(columns={
    'Happiness Score': 'Score',
    'Country': 'Country or region'
})[['Country or region', 'Region', 'Score']]
df_2016['Year'] = 2016

# 2017
df_2017 = df_2017.rename(columns={
    'Happiness.Score': 'Score',
    'Country': 'Country or region'
})[['Country or region', 'Score']]
df_2017['Year'] = 2017

# 2018
df_2018 = df_2018.rename(columns={
    'Score': 'Score',
    'Country or region': 'Country or region'
})[['Country or region', 'Score']]
df_2018['Year'] = 2018

# 2019
df_2019 = df_2019.rename(columns={
    'Score': 'Score',
    'Country or region': 'Country or region'
})[['Country or region', 'Score']]
df_2019['Year'] = 2019

# Combine all years into one DataFrame
all_years = pd.concat([df_2015, df_2016, df_2017, df_2018, df_2019])

# Clean country names to match Plotly's country names
country_name_mapping = {
    'United States': 'United States of America',
    'South Korea': 'South Korea',
    'Taiwan Province of China': 'Taiwan',
    'Hong Kong S.A.R., China': 'Hong Kong',
    'Trinidad & Tobago': 'Trinidad and Tobago',
    'Congo (Brazzaville)': 'Congo',
    'Congo (Kinshasa)': 'Democratic Republic of the Congo',
    'Palestinian Territories': 'Palestine',
    'North Cyprus': 'Northern Cyprus',
    'Somaliland region': 'Somaliland',
    'Syria': 'Syrian Arab Republic',
    'Libya': 'Libyan Arab Jamahiriya',
    'Russia': 'Russian Federation',
    'Ivory Coast': "Côte d'Ivoire"
}

all_years['Country or region'] = all_years['Country or region'].replace(country_name_mapping)

# Create the animated choropleth map
fig = px.choropleth(all_years, 
                    locations="Country or region",
                    locationmode='country names',
                    color="Score",
                    hover_name="Country or region",
                    animation_frame="Year",
                    color_continuous_scale=px.colors.sequential.Plasma,
                    range_color=(2.5, 8),
                    title="World Happiness Report (2015-2019)",
                    labels={'Score': 'Happiness Score'})

# Customize the layout
fig.update_layout(
    geo=dict(
        showframe=False,
        showcoastlines=True,
        projection_type='equirectangular'
    ),
    coloraxis_colorbar=dict(
        title='Happiness Score',
        thickness=20,
        len=0.75,
        yanchor='middle'
    ),
    margin=dict(l=0, r=0, t=50, b=0)
)

# Show the figure
fig.show()