import streamlit as st
from models.dataset import KaggleDataSet
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

from utils.buildModel import buildModels
from utils.modelEvaluation import evaluationModel
from utils.visualizeData import visualizeDiscreteAndContinuousData, visualizeModelEvaluation

def app():
    st.header("Choose Dataset To Create A Model")
    datasetNames = KaggleDataSet.fetchAllDatasetName()
    if datasetNames and len(datasetNames[1:]) > 0:
        selected_dataset = st.selectbox('Choose one of the dataset to create a model!', datasetNames)
        if selected_dataset and selected_dataset != 'Choose Dataset':
            datasetJson = KaggleDataSet.fetchDatasetJsonByName(selected_dataset) #Loading the data
            if datasetJson and datasetJson != dict():
                df = pd.DataFrame.from_dict(datasetJson, orient='index')

                #feature selection
                y = df['DEATH_EVENT'] #dependent variable
                x = df.drop("DEATH_EVENT", axis=1)  #independent variables

                #splliting training and testing data
                x_train, x_test, y_train, y_test = train_test_split(x,y,
                                                                    test_size=0.2,
                                                                    shuffle=True,
                                                                    random_state=4)
                scaler = StandardScaler() #to equally contribution of data we do standrization
                scaler.fit(x_train)
                x_train = scaler.transform(x_train)
                x_test = scaler.transform(x_test)

                vis_data_bt, model_evaluate_bt, build_model_bt  = st.columns(3)

                visualize_data = vis_data_bt.button('Visualise Data')

                #Data Visualization
                if visualize_data:
                    #Here we will show graphs based on data we have
                    discrete_columns = ['anaemia', 'diabetes','high_blood_pressure', 'sex', 'smoking']
                    continuous_columns = ['age', 'creatinine_phosphokinase', 'ejection_fraction', 'platelets',
                                          'serum_creatinine', 'serum_sodium', 'time']
                    visualizeDiscreteAndContinuousData(discrete_columns, continuous_columns ,df)

                model_evaluate = model_evaluate_bt.button("Evaluate Model")

                #Model Evaluation
                if model_evaluate:
                    results, names = evaluationModel(x_train, y_train)
                    if results and names:
                        visualizeModelEvaluation(results, names)

                # Building the Model
                build_model = build_model_bt.button("Build Model")
                if build_model:
                    buildModelResults = buildModels(x_train, y_train, x_test, y_test)
                    st.success("Accuracy of Logistic Regression " + str(buildModelResults.get("LR") * 100))
                    st.success("Accuracy of Decision Tree " + str(buildModelResults.get("DTC") * 100))
            else:
                st.warning('No dataset json available for selected dataset {}'.format(selected_dataset))
    else:
        st.warning("No any dataset available! Please create one dataset.")