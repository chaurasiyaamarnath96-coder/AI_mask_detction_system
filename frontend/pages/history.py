import streamlit as st
import requests
import pandas as pd
import plotly.express as px

st.title("📊 Compliance Analytics")

response = requests.get(
    "http://127.0.0.1:8000/logs"
)

logs = response.json()

st.write("Raw Logs")
st.json(logs)

if not logs:
    st.warning("No logs found")
    st.stop()

if isinstance(logs, dict):
    logs = [logs]

df = pd.DataFrame(logs)

st.write("Columns:")
st.write(df.columns.tolist())

required_cols = [
    "timestamp",
    "compliance",
    "masked",
    "unmasked",
    "incorrect"
]

missing = [
    c for c in required_cols
    if c not in df.columns
]

if missing:
    st.error(f"Missing columns: {missing}")
    st.stop()

df["timestamp"] = pd.to_datetime(
    df["timestamp"]
)

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

latest = df.iloc[-1]

pie = px.pie(
    values=[
        latest["masked"],
        latest["unmasked"],
        latest["incorrect"]
    ],
    names=[
        "Masked",
        "Unmasked",
        "Incorrect"
    ]
)

st.plotly_chart(
    pie,
    use_container_width=True
)
