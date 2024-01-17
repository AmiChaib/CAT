import streamlit as st
import dotenv
from os import environ

env_file = '.env'

def main():
    dotenv.load_dotenv(env_file, override=True)
    st.title("Hello World")

if __name__ == "__main__":
    main()