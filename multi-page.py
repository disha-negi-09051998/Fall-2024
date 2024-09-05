import streamlit as st

# Define the pages
lab1_page = st.Page("LAB-01.py", title="Lab 1", icon=":books:")
lab2_page = st.Page("LAB-02.py", title="Lab 2", icon=":books:")

# Setup the navigation
pg = st.navigation([lab1_page, lab2_page])

# Configure global page settings
st.set_page_config(page_title="Multi-Page Labs App", page_icon=":atom:")

# Run the selected page
pg.run()