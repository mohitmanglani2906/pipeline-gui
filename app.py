import streamlit as st
from ui import MultiApp
from auth import login, register

app = MultiApp()
app.add_app("Login", login.app)
#app.add_app("Signup", register.app)

print("App Py Called**********************")
app.run()