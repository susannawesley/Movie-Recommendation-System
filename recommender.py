import streamlit as st
import pickle
import pandas as pd
from utils import recommend, fetch_poster, get_movie_details_by_genre

# Load data
movies_dict = pickle.load(open("movie_dict.pkl", "rb"))
movies = pd.DataFrame(movies_dict)
similarity = pickle.load(open("similarity.pkl", "rb"))


def show_recommender_page():
    st.markdown("""
            <style>
            .header {
                font-size: 40px;
                font-weight: 700;
                color: white;
                text-align: center;
                padding: 20px;
            }
            .nav {
                display: flex;
                justify-content: center;
                gap: 40px;
                margin-bottom: 30px;
            }
            .nav a {
                text-decoration: none;
                font-weight: bold;
                color: #ffcc00;
            }

            /* Style for the 'Pick a movie you like' label */
            .st-emotion-cache-vx3jdd.e1g8pqu43 { /* This class targets the selectbox label */
                font-size: 1.5rem; /* Increased font size significantly */
                font-weight: bold;
                color: #F0F8FF; /* AliceBlue for selectbox label */
                margin-bottom: 10px;
            }

            /* Style for the Recommend button */
            div.stButton > button {
                background: linear-gradient(135deg, #1e90ff, #00bfff); /* Matching Get Started button */
                color: white;
                border: none;
                padding: 10px 25px; /* Decreased padding to make the button smaller */
                border-radius: 8px; /* Slightly adjusted border-radius for the smaller size */
                font-size: 16px; /* Slightly decreased font size for the button text */
                font-weight: 700;
                cursor: pointer;
                transition: all 0.3s ease;
                margin-top: 30px; /* Adjust margin as needed */
            }

            div.stButton > button:hover {
                background: linear-gradient(135deg, #63b3ed, #4299e1);
                transform: scale(1.02); /* Slightly less pronounced scale on hover for smaller button */
            }

            /* Further refine poster markdown text for consistency if needed */
            .st-emotion-cache-1v0bb1h strong { /* Targeting the strong tag within the markdown */
                font-size: 1.2em; /* Make the movie title slightly larger */
                color: #FFD700; /* Gold color for movie titles */
            }

            </style>
            <div class='header'>🎬 MovieMatch Explorer</div>
        """, unsafe_allow_html=True)

    # Load your data
    movies_dict = pickle.load(open("movie_dict.pkl", "rb"))
    movies = pd.DataFrame(movies_dict)
    similarity = pickle.load(open("similarity.pkl", "rb"))

    selected_movie = st.selectbox("Pick a movie you like 🎥", movies['title'].values)

    if st.button("Recommend 🎯"):
        recommended_movies, recommended_posters = recommend(selected_movie, movies, similarity)

        cols = st.columns(5)
        for i in range(5):
            with cols[i]:
                st.image(recommended_posters[i], use_container_width=True)
                st.markdown(f"**{recommended_movies[i]}**")