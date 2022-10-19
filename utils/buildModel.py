from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
import streamlit as st
import  time

def buildModels(x_train, y_train, x_test, y_test):
    LRCClassifier = LogisticRegression(max_iter=1000, random_state=1, solver='liblinear',
                                       penalty='l1')  #using LogisticRegression  to create a model
    LRCClassifier.fit(x_train, y_train)
    y_pred_LR = LRCClassifier.predict(x_test)
    LRAcc = accuracy_score(y_pred_LR, y_test)

    dtc_c = DecisionTreeClassifier(max_depth=3, min_samples_leaf=5,
                                   criterion='entropy', min_samples_split=5, splitter='random',
                                   random_state=1)  #using Decition Tree to create a model

    dtc_c.fit(x_train, y_train)
    y_pred_dtc = dtc_c.predict(x_test)
    DTCAcc = accuracy_score(y_pred_dtc, y_test)
    build_model_progress = st.progress(0)
    for i in range(101):
        build_model_progress.progress(i)
    time.sleep(0.5)
    st.info("Build Models Results")

    return {"LR": LRAcc, "DTC": DTCAcc}