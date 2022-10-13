import streamlit as st

class MultiApp():
    def __init__(self):
        self.apps = []

    def add_app(self, title, func):
        self.apps.append({"title": title, "function": func})

    def run(self, name="Login"):
        #st.set_page_config(initial_sidebar_state="collapsed")
        st.sidebar.title('Navigation')
        # st.sidebar.markdown(f"**RUN MODE**: <font color='red'>Testing</font>", unsafe_allow_html=True)
        print("self apps", self.apps)
        app = st.sidebar.radio(name, self.apps, format_func=lambda app: app["title"])
        #print("in application",st.sidebar.title)
        print("Run Method Called ", app)
        app["function"]()