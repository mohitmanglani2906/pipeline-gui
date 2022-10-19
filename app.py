import streamlit as st
from ui import MultiApp
from auth import login
import ui.loadData as ld
import ui.fetchData as fd

name, authentication_status, username, authenticator = login.app()

if authentication_status:
    st.write(f'Welcome *{name}*')
    app = MultiApp()
    app.add_app("Upload Data", ld.app)
    app.add_app("Create Model", fd.app)
    app.run()
    authenticator.logout('Logout', 'sidebar')
elif authentication_status == False:
    st.error('Username/password is incorrect')
elif authentication_status is None:
    st.warning('Please enter your username and password')