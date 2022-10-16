from connection.ConnectWithMongo import Connection
from models.userAuth import userAuth
import streamlit_authenticator as stauth

def addUserInDB():
    connection = Connection(dbName='pipeline-gui')
    password = stauth.Hasher(['admin123']).generate() #creating hashed password as per requirenment
    userAuthObj = userAuth(userName='admin', userEmail='mohitmanglani2906@gmail.com', fullName='Mohit Manglani', password=password)
    userAuthObj.save()

addUserInDB()