import streamlit as st
import pandas as pd
import requests

st.title("Wind Turbine FL vs Raw Monitoring")

# Sidebar for controls
st.sidebar.header("Network Status")

# Fetch data from API
response = requests.get("http://localhost:8000/metrics")
data = response.json()

if data:
    df = pd.DataFrame(data)
    
    # Comparison Chart: Bandwidth
    st.subheader("Bandwidth Usage (Raw vs FL)")
    st.line_chart(df.groupby('type')['size'].sum())

    # Comparison Chart: Latency
    st.subheader("Decision Latency")
    st.bar_chart(df.groupby('type')['latency'].mean())