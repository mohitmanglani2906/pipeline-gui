import streamlit as st
from models.dataset import KaggleDataSet
import pandas as pd
from datetime import datetime
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
from sklearn.model_selection import cross_val_score, StratifiedKFold
import matplotlib.pyplot as plt

def app():
    st.header("Choose Dataset To Create A Model")
    datasetNames = KaggleDataSet.fetchAllDatasetName()
    if datasetNames and len(datasetNames[1:]) > 0:
        selected_dataset = st.selectbox('Choose one of the dataset to create a model!', datasetNames)
        if selected_dataset and selected_dataset != 'Choose Dataset':
            datasetJson = KaggleDataSet.fetchDatasetJsonByName(selected_dataset) #Loading the data
            #st.write(len(datasetJsonObj))
            if datasetJson and datasetJson != dict():
                #st.write(datasetJson)
                df = pd.DataFrame.from_dict(datasetJson, orient='index')
                #st.dataframe(df)
                #st.dataframe(df.describe())
                #feature selection from data
                y = df['DEATH_EVENT'] #dependent variable
                x = df.drop("DEATH_EVENT", axis=1)  #independent variables
                # st.write(y)
                # st.write(x)

                #splliting training and testing data
                x_train, x_test, y_train, y_test = train_test_split(x,y,
                                                                    test_size=0.2,
                                                                    shuffle=True,
                                                                    random_state=4)
                # st.write(x_train)
                # st.write(x_test)
                # st.write(y_train)
                # st.write(y_test)

                scaler = StandardScaler() #to equally contribution of data we do standrization
                scaler.fit(x_train)
                st.write(x_train)
                x_train = scaler.transform(x_train)
                x_test = scaler.transform(x_test)
                # st.write(x_train)
                # st.write(x_test)

                #Model Evaluation

                models = []
                models.append(('LR',LogisticRegression(solver='liblinear', multi_class='ovr')))
                models.append(("DT", DecisionTreeClassifier()))

                results =[]
                names = []
                for name, model in models:
                    kfold = StratifiedKFold(n_splits=20)
                    cv_results = cross_val_score(model, x_train, y_train, cv = kfold, scoring='accuracy')
                    results.append(cv_results)
                    names.append(name)
                   # print('%s: %f (%f)' %(name, cv_results.mean(),cv_results.std()))
                    st.write('%s: %f (%f)' %(name, cv_results.mean(),cv_results.std()))
                # st.write(results)
                # chart_data = pd.DataFrame(results, columns=names)
                # st.line_chart(chart_data)

                # fig  =  plt.box(results, labels=names)
                #fig.title("Algorithm Comparison")
                #st.pyplot(fig.show())

                # names = []
                # models = []
                #Building the Model
                LRCClassifier = LogisticRegression(max_iter=1000, random_state=1, solver='liblinear', penalty='l1')
                LRCClassifier.fit(x_train, y_train)
                y_pred_LR = LRCClassifier.predict(x_test)
                LRAcc = accuracy_score(y_pred_LR, y_test)
                names.append("LR")
                models.append(('LR', LRAcc))
                st.write(LRAcc * 100)

                dtc_c = DecisionTreeClassifier(max_depth=3, min_samples_leaf=5,
                                            criterion='entropy', min_samples_split=5, splitter='random', random_state=1)
                dtc_c.fit(x_train, y_train)
                y_pred_dtc = dtc_c.predict(x_test)
                DTCAcc = accuracy_score(y_pred_dtc, y_test)
                names.append("DT")
                models.append(('DT', DTCAcc))
                st.write(DTCAcc*100)




            else:
                st.warning('No dataset json available for selected dataset {}'.format(selected_dataset))
    else:
        st.warning("No any dataset available! Please create one dataset.")
            # st.write(datasetJson.dataset_json)
            # st.write(datasetJson.dataset_name)
            # st.write(selected_dataset)
        #st.button(obj.dataset_name + " " + obj.createdAt.strftime("%m/%d/%Y %H:%M:%S"))
        # st.write(data_json)
        #st.write(obj.dataset_name)
        #st.write(obj.dataset_name)
       # df2 = pd.DataFrame.from_dict(obj.dataset_json, orient="index")
        #st.dataframe(df2)
        # st.write(obj.dataset_name)
        #st.write(obj.createdAt.strftime("%m/%d/%Y %H:%M:%S"))
