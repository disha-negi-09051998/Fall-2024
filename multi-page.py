import streamlit as st
import LAB_01
import LAB_02

# Setup the navigation sidebar
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Lab 1", "Lab 2"])

# Configure global page settings
st.set_page_config(page_title="Multi-Page Labs App", page_icon=":atom:")

# Render the selected page
if page == "Lab 1":
    LAB_01.app()  # Call the app function from LAB_01.py
elif page == "Lab 2":
    LAB_02.app()  # Call the app function from LAB_02.py