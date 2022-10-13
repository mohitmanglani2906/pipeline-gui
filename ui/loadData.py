import streamlit as st
import pandas as pd

def app():
    st.header("Load Data")
    st_init, st_update_views = st.columns(2)
    uploaded_files = st.file_uploader("Upload csv files", accept_multiple_files=True, type=['csv'])
    if uploaded_files is not None:
        for file in uploaded_files:
            print("uploaded_files", file)
            bytes_data = file.read()
            st.write("filename:", file.name)
            st.write(bytes_data)
        # df = pd.read_csv(uploaded_files)
        # st.write(df)
