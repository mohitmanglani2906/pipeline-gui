import streamlit as st
import pandas as pd
from io import BytesIO
import json
import random
from models.dataset import KaggleDataSet


def app():
    st.header("Load And Upload Data In Mongo DB")
    st_init, st_update_views = st.columns(2)
    dataset = st.text_input("Enter dataset name ")
    #dataset += "#" + str(random.random()).split(".")[-1][0:4]
    if dataset:
        #connection = Connection(dbName='pipeline-gui')
        st.subheader("Please add csv files for dataset {}".format(dataset))
        uploaded_files = st.file_uploader("Upload csv files", accept_multiple_files=True, type=['csv'])
       # print(uploaded_files)
        dataset_json = dict()
        dataFrames = list()
        if uploaded_files is not None:
            for file in uploaded_files:
                bytes_data = file.read()
                df = pd.read_csv(BytesIO(bytes_data))
                dataFrames.append(df)
            if len(dataFrames) > 0:
                final_df = pd.concat(dataFrames, axis=0)
                final_df.reset_index(inplace=True)
                final_df.drop(['index'], axis=1, inplace=True)
                if not final_df.empty:
                    upload_button = st.button("Upload Data")
                    if upload_button:
                        #st.progress(100)
                        #st.write(upload_button)
                        #st.dataframe(final_df)
                        dataset += "_#" + str(random.random()).split(".")[-1][0:4]
                        data_json = json.loads(final_df.to_json(orient="index"))
                        dataObj = KaggleDataSet(dataset_name=dataset, dataset_json=data_json)
                        dataObj.saveDataset()
                        st.success('Dataset uploaded to MongoDB successfully! Your dataset name is {}'.format(dataset), icon="✅")

                        #st.write(data_json)
                        # df2 = pd.DataFrame.from_dict(data_json, orient="index")
                        # st.dataframe(df2)
                else:
                     st.warning("No data available in the selected csv file(s)")
           # st.write(dataset_json)
           # st.write(len(dataset_json))

