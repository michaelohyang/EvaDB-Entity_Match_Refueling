import streamlit as st
from plotly import graph_objs as go
import pandas as pd


START = "2007-11-25"
STOP = "2021-04-30"

st.title("_Stock.ai_ :sunglasses:")

data_file = st.file_uploader("Stock Market Data", ["csv"], help="Please upload a 1 csv file at a time", )
df = None

# If a file is uploaded, read it into a DataFrame
if data_file is not None:
    df = pd.read_csv(data_file)
    # Display the DataFrame
    st.dataframe(df)

    title = st.text_input('', 'Ask me about the stock')

