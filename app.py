import streamlit as st
from ui import MultiApp
from auth import login, register
import ui.loadData as ld
import ui.fetchData as fd

from connection.ConnectWithMongo import Connection
from models.userAuth import userAuth
import streamlit_authenticator as stauth

# connection = Connection(dbName='pipeline-gui')
# print(userAuth.getUserByUserName('admin'))

# def addUserInDB():
#     connection = Connection(dbName='pipeline-gui')
#     password = stauth.Hasher(['admin123']).generate() #creating hashed password as per requirenment
#     userAuthObj = userAuth(userName='admin', userEmail='mohitmanglani2906@gmail.com', fullName='Mohit Manglani', password=password[0])
#     userAuthObj.save()
#
# addUserInDB()

name, authentication_status, username, authenticator = login.app()
#
if authentication_status:
  st.write('Welcome *%s*' % (name))
  connection = Connection(dbName='pipeline-gui')
  app = MultiApp()
  app.add_app("Upload Data", ld.app)
  app.add_app("Create Model", fd.app)
  app.run()
  authenticator.logout('Logout', 'sidebar')

  # app.run("Duplicate App")
  # print("sesstion ", st.session_state)
  # st.sidebar.title('Navigation 2')
  # del st.sidebar

elif authentication_status == False:
  st.error('Username/password is incorrect')
elif authentication_status == None:
  st.warning('Please enter your username and password again')

# app = MultiApp()
# app.add_app("Login", login.app)
#app.add_app("Signup", register.app)

print("App Py Called**********************")
# app.run()