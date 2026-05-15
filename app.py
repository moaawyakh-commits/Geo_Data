import streamlit as st
import pandas as pd
import plotly.express as px

# Load data
df = pd.read_csv("data/cleaned_earthquakes.csv")

st.title("QuakeAnalyze")

st.write("Earthquake Risk Analysis Dashboard")

# Metrics
st.subheader("Dataset Metrics")

col1, col2, col3 = st.columns(3)

col1.metric("Rows", len(df))
col2.metric("Columns", len(df.columns))
col3.metric("Average Magnitude", round(df["magnitude"].mean(), 2))

# Filter
st.sidebar.header("Filters")

min_mag = st.sidebar.slider(
    "Minimum Magnitude",
    float(df["magnitude"].min()),
    float(df["magnitude"].max()),
    float(df["magnitude"].min())
)

filtered_df = df[df["magnitude"] >= min_mag]

# Histogram
fig1 = px.histogram(
    filtered_df,
    x="magnitude",
    title="Magnitude Distribution"
)

st.plotly_chart(fig1)

# Scatter Plot
fig2 = px.scatter(
    filtered_df,
    x="depth",
    y="magnitude",
    color="magnitude",
    title="Depth vs Magnitude"
)

st.plotly_chart(fig2)

# Table
st.subheader("Sample Data")
st.dataframe(filtered_df.head())
