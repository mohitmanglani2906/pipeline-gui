import streamlit as st
import streamlit_authenticator as stauth


#this app we are not using right now, but this is useful to register users
def app():
    authenticator = stauth.Authenticate(
        {"usernames": {}},
        '',
        '',
        30,
        [False]
    )

    authenticator.register_user('Register User', preauthorization=False)
    print("in signup ", st.sidebar.id)

