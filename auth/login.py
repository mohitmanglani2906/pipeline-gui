import streamlit as st
import streamlit_authenticator as stauth
import ui.loadData as ld
import yaml
from auth import register

from ui import MultiApp


def app():


    # with open('./config.yml') as file:
    #     config = yaml.load(file, Loader=yaml.SafeLoader)

    hashed_passwords = stauth.Hasher(['123']).generate()
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

    credentials =  {
      "usernames": {
        "mohit": {
          "email": "mohitmanglani2906@gmail.com",
          "name": "Mohit Manglani",
          "password": hashed_passwords[0]
        }
      }
    }

    authenticator = stauth.Authenticate(
        credentials,
        "some_cookie_name",
        "some_signature_key",
        30,
        ["mohitmanglani2906@gmail.com"]
    )

    name, authentication_status, username = authenticator.login('Login', 'main')
    #authenticator.register_user('Register User', preauthorization=False)
    # print("Here\n", st.session_state)

    #
    if authentication_status:
       # del st.sidebar.radio
        authenticator.logout('Logout', 'sidebar')
        st.write('Welcome *%s*' % (name))
        ld.app()
        # app = MultiApp()
        # app.add_app("Another App", register.app)
        # app.run("Duplicate App")
        #print("sesstion ", st.session_state)
        #st.sidebar.title('Navigation 2')
        #del st.sidebar

    elif authentication_status == False:
        st.error('Username/password is incorrect')
    elif authentication_status == None:
        st.warning('Please enter your username and password again')
