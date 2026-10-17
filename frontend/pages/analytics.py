import streamlit as st
import requests
import pandas as pd
import plotly.express as px

st.title("📊 Compliance Analytics")

response = requests.get(
    "https://ai-mask-detction-system-1.onrender.com"
)

logs = response.json()

if not logs:

    st.warning("No analytics data available")

else:

    df = pd.DataFrame(logs)

    st.dataframe(df)

    fig = px.line(
        df,
        x="timestamp",
        y="compliance",
        title="Compliance Trend"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )