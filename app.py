import streamlit as st
import pickle
import pandas as pd
import requests

# 🔧 Updated fetch_poster using correct movie title
def fetch_poster(movie_title):
    url = f"http://www.omdbapi.com/?t={movie_title}&apikey=33dc79c1"
    response = requests.get(url)
    data = response.json()
    poster = data.get('Poster')
    if poster and poster != 'N/A':
        return poster
    else:
        return "https://via.placeholder.com/300x450.png?text=No+Image"

# 🎯 Recommend function
def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movies = []
    recommended_posters = []
    for i in movies_list:
        title = movies.iloc[i[0]].title
        recommended_movies.append(title)
        recommended_posters.append(fetch_poster(title))
    return recommended_movies, recommended_posters

# 🎬 Load data
movies_dict = pickle.load(open('movie_dict.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)
similarity = pickle.load(open('similarity.pkl', 'rb'))

# 🌟 Streamlit UI
st.title('Movie Recommendation System')
selected_movie_name = st.selectbox('How would u like?', movies['title'].values)

if st.button('Recommend Movie'):
    names, posters = recommend(selected_movie_name)
    cols = st.columns(5)
    for i in range(5):
        with cols[i]:
            st.text(names[i])
            st.image(posters[i])
