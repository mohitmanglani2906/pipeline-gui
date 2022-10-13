import streamlit as st
import streamlit_authenticator as stauth


def app():
    authenticator = stauth.Authenticate(
        {"usernames": {}},
        '',
        '',
        30,
        [False]
    )

    print(authenticator)

    authenticator.register_user('Register User', preauthorization=False)
    print("in signup ", st.sidebar.id)

