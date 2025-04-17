# app.py

import streamlit as st
from main import get_recommendation

st.title("🎬 Movie Preference Recommender")

genre = st.selectbox("Select Genre", ["Action", "Comedy", "Drama", "Sci-Fi"])
decade = st.selectbox("Select Decade", ["80s", "90s", "2000s", "2010s"])

if st.button("Get Recommendation"):
    result = get_recommendation(genre, decade)
    if result:
        st.success(f"You should watch: *{result}* 🎉")
    else:
        st.error("No recommendation found for that combination.")