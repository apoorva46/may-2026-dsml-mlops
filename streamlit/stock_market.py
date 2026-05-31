import streamlit as st
import pandas as pd
import numpy as np
import datetime
import yfinance as yf
from curl_cffi import requests

session = requests.Session(impersonate="chrome")

st.title("Stock Market Data Analysis!!")

# ticker_symbol = 'AAPL'
ticker_symbol = st.text_input("Please enter Ticker Symbol", "AAPL")

ticker_data = yf.Ticker(ticker_symbol, session=session)

col1, col2 = st.columns(2)

with col1:
    start_date = st.date_input(
        "Please enter Starting Date",
        datetime.date(2019, 1, 1)
    )

with col2:
    end_date = st.date_input(
        "Please enter End Date",
        datetime.date(2022, 12, 31)
    )

try:
    ticker_df = ticker_data.history(
        start=start_date,
        end=end_date
    )

    if ticker_df.empty:
        st.error("No data found for the selected ticker/date range.")
        st.stop()

except Exception as e:
    st.error(f"Error fetching stock data: {e}")
    st.stop()

st.dataframe(ticker_df)

st.write("## Closing price of " + ticker_symbol)
st.line_chart(ticker_df["Close"])

st.write("## Volume price of " + ticker_symbol)
st.line_chart(ticker_df["Volume"])

col1, col2 = st.columns(2)

with col1:
    st.write("## Opening price of " + ticker_symbol)
    st.line_chart(ticker_df["Open"])

with col2:
    st.write("## High price of " + ticker_symbol)
    st.line_chart(ticker_df["High"])

# Exponential Moving Average
st.write("## Exponential Moving Average")

alpha = st.slider(
    "Select Alpha value for EMA",
    min_value=0.01,
    max_value=1.0,
    value=0.1,
    step=0.01
)

ema_values = []

ema = ticker_df["Close"].iloc[0]
ema_values.append(ema)

for i in range(1, len(ticker_df)):
    ema = alpha * ticker_df["Close"].iloc[i] + (1 - alpha) * ema
    ema_values.append(ema)

ticker_df["EMA"] = ema_values

st.line_chart(ticker_df[["Close", "EMA"]])

num = st.number_input("Insert a number")

if st.button("Calculate Square"):
    result = num ** 2
    st.text("Square of " + str(num) + " is " + str(result))