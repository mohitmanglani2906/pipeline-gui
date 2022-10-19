import streamlit as st

#This class we using to create our side bar navigation
class MultiApp():
    def __init__(self):
        self.apps = []

    def add_app(self, title, func):
        self.apps.append({"title": title, "function": func})

    def run(self, name="Pipeline"):
        st.sidebar.title('Navigation')
        app = st.sidebar.radio(name, self.apps, format_func=lambda app: app["title"])
        app["function"]()