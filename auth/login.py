import streamlit as st
import streamlit_authenticator as stauth
import ui.loadData as ld
import yaml
from auth import register
from connection.ConnectWithMongo import Connection
from models.userAuth import userAuth

from ui import MultiApp


def app():


    # with open('./config.yml') as file:
    #     config = yaml.load(file, Loader=yaml.SafeLoader)

    #hashed_passwords = stauth.Hasher(['123']).generate()
    # print(hashed_passwords)
    #
    # {
    #   "usernames": {
    #     "mohit": {
    #       "email": "mohitmanglani2906@gmail.com",
    #       "name": "Mohit Manglani",
    #       "password": "123"
    #     }
    #   }
    # }
    connection = Connection(dbName='pipeline-gui')
    userAuthObj  = userAuth.getUserObjByUserName('admin')
    password = ''
    for obj in userAuthObj:
        if obj.password:
            password = obj.password

    credentials =  {
      "usernames": {
        "admin": {
          "email": "mohitmanglani2906@gmail.com",
          "name": "Mohit Manglani",
          "password": password
        }
      }
    }

    authenticator = stauth.Authenticate(
        credentials,
        "pipeline_gui",
        "",
        30,
        ["mohitmanglani2906@gmail.com"]
    )

    name, authentication_status, username =  authenticator.login('Login', 'main')
    return name, authentication_status, username, authenticator
