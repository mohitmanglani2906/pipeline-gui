import streamlit as st
import pandas as pd
from io import BytesIO
import json
import random
from models.dataset import KaggleDataSet


def app():
    st.header("Load And Upload Data In Mongo DB")
    dataset = st.text_input("Enter dataset name ")
    if dataset:
        st.subheader("Please add csv files for dataset {}".format(dataset))
        uploaded_files = st.file_uploader("Upload csv files", accept_multiple_files=True,
                                          type=['csv'])  # to upload multi files as csv type
        dataFrames = list()
        if uploaded_files is not None:
            for file in uploaded_files:
                bytes_data = file.read()
                df = pd.read_csv(BytesIO(bytes_data))
                dataFrames.append(df)  #combining all the files together and creating dataframe
            if len(dataFrames) > 0:
                final_df = pd.concat(dataFrames, axis=0)
                final_df.reset_index(inplace=True)
                final_df.drop(['index'], axis=1, inplace=True)
                if not final_df.empty:
                    upload_button = st.button("Upload Data")
                    if upload_button:
                        dataset += "_#" + str(random.random()).split(".")[-1][0:4] #here to make dataset name unique we are appending random number to dataset name
                        data_json = json.loads(final_df.to_json(orient="index"))
                        data_obj = KaggleDataSet(dataset_name=dataset, dataset_json=data_json) #Creating object of collection KaggleDataSet
                        data_obj.saveDataset()  #saving data in collection
                        st.success('Dataset uploaded to MongoDB successfully! Your dataset name is {}'.format(dataset),
                                   icon="✅")
                else:
                    st.warning("No data available in the selected csv file(s)")
