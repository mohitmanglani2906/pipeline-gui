import streamlit as st
from ui import MultiApp
from auth import login
import ui.loadData as ld
import ui.fetchData as fd
from connection.ConnectWithMongo import Connection
from models.userAuth import userAuth
import streamlit_authenticator as stauth
#
# connection = Connection(dbName='pipeline-gui')
# print(userAuth.getUserObjByUserName('Annabel'))

# def addUserInDB():
#     connection = Connection(dbName='pipeline-gui')
#     password = stauth.Hasher(['']).generate() #creating hashed password as per requirenment
#     userAuthObj = userAuth(userName='', userEmail='', fullName='', password=password[0])
#     userAuthObj.save()
#
# addUserInDB()

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