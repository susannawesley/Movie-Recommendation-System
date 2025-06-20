import streamlit as st
from recommender import show_recommender_page
from home import show_home_page

# Session variable to handle navigation
if "page" not in st.session_state:
    st.session_state.page = "home"

# Navigation control
if st.session_state.page == "home":
    show_home_page()
elif st.session_state.page == "recommender":
    show_recommender_page()
