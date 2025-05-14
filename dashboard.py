import streamlit as st
import pandas as pd
import plotly.express as px

# Load data
@st.cache_data
def load_data():
    df = pd.read_csv('owid-covid-data.csv', parse_dates=['date'])
    return df

df = load_data()

# Sidebar for user input
st.sidebar.header('Filter Data')
countries = df['location'].dropna().unique()
selected_countries = st.sidebar.multiselect('Select Country/Countries', sorted(countries), default=[sorted(countries)[0]])

# Date range
min_date = df['date'].min()
max_date = df['date'].max()
date_range = st.sidebar.date_input('Select Date Range', [min_date, max_date], min_value=min_date, max_value=max_date)

# Metric selection
metrics = ['new_cases', 'new_deaths']
if 'hosp_patients' in df.columns:
    metrics.append('hosp_patients')
if 'icu_patients' in df.columns:
    metrics.append('icu_patients')
selected_metrics = st.sidebar.multiselect('Select Metrics to Display', metrics, default=['new_cases', 'new_deaths'])

# Filter data
mask = (
    df['location'].isin(selected_countries) &
    (df['date'] >= pd.to_datetime(date_range[0])) &
    (df['date'] <= pd.to_datetime(date_range[1]))
)
data = df.loc[mask]

st.title('COVID-19 Dashboard')
st.write(f'Date Range: {date_range[0]} to {date_range[1]}')
st.write(f"Countries: {', '.join(selected_countries)}")

# Summary statistics
st.subheader('Summary Statistics')
sum_stats = {}
for metric in selected_metrics:
    if metric in data.columns:
        total = data.groupby('location')[metric].sum()
        avg = data.groupby('location')[metric].mean()
        sum_stats[metric] = {'Total': total, 'Average': avg}
        st.write(f"**{metric.replace('_', ' ').title()}**")
        st.write(pd.DataFrame({'Total': total, 'Average': avg}))

# Plot selected metrics
for metric in selected_metrics:
    if metric in data.columns:
        fig = px.line(data, x='date', y=metric, color='location', title=f"Daily {metric.replace('_', ' ').title()}")
        st.plotly_chart(fig)

# Download filtered data
st.subheader('Download Data')
st.download_button('Download Filtered Data as CSV', data.to_csv(index=False), file_name='filtered_covid_data.csv')

st.write('Data Source: Our World in Data')
