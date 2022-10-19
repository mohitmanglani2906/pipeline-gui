import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

def visualizeModelEvaluation(data, names):
    st.info('Model Evaluation Results')
    for i in range(len(data)):
        st.write('%s %f' % (names[i], data[i].mean()))
    fig = plt.figure()
    plt.boxplot(data, labels=names)
    plt.title("Model Evaluation")
    st.pyplot(fig)

def visualizeDiscreteAndContinuousData(discreteColumns, continuousColumns, df):

    st.info("Showing Count Plot for Discreate Data")

    for col in discreteColumns:
        fig = plt.figure()
        g = sns.countplot(x=df[col], data=df, hue=df.DEATH_EVENT)
        st.pyplot(fig)

    st.info("Showing Box Plot for Continuous Data")

    for col in continuousColumns:
        fig = plt.figure()
        g = sns.boxplot(y=df[col], x=df.DEATH_EVENT)
        st.pyplot(fig)

