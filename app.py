import streamlit as st
import pickle as pkl
import pandas as pd
import requests
import time
def fetch_poster(movie_id):
    for attempt in range(6):
        try:
            api_key = '8265bd1679663a7ea12ac168da84d2e8'
            url = f'https://api.themoviedb.org/3/movie/{movie_id}?api_key={api_key}&language=en-US'
            response = requests.get(url,timeout=10)
            response.raise_for_status()
            data = response.json()
            poster_path = data.get('poster_path')
            if poster_path:
                return "https://image.tmdb.org/t/p/w500/" + poster_path
            else:
                return "https://via.placeholder.com/500x750.png?text=No+Image"
        except requests.exceptions.RequestException as e:
            print(f"Attempt {attempt + 1} failed for movie_id {movie_id}: {e}")
            time.sleep(0.5)
    st.error(f"Failed to fetch poster for movie ID {movie_id} after 6 attempts.")
    return "https://via.placeholder.com/500x750.png?text=Error"


def recommend(movie):
    movie_index = movies_list[movies_list['title'] == movie].index[0]
    distances = similarity[movie_index]
    top_movies = sorted(list(enumerate(distances)),reverse=True,key=lambda x:x[1])[1:6]
    recommended_movies = []
    recommended_movies_posters = []
    for i in top_movies:
        movie_id = movies_list.iloc[i[0]].movie_id
    #fetch poster from API
        recommended_movies.append(movies_list.iloc[i[0]].title)
        recommended_movies_posters.append(fetch_poster(movie_id))
        time.sleep(0.5)
    return recommended_movies,recommended_movies_posters
try:
    movies_list = pkl.load(open('movies1.pkl', 'rb'))
    similarity = pkl.load(open('similarity1.pkl', 'rb'))
except FileNotFoundError:
    st.error("Model files not found. Make sure 'movies1.pkl' and 'similarity1.pkl' are in the correct directory.")
    st.stop()

st.title('Movie Recommender System')

selected_movie_name = st.selectbox(
    "By - Natabar Pradhan",
    movies_list['title'].values,
    index=None,
    placeholder="Select Movie",
)
if st.button('Recommend Movies'):
    if selected_movie_name:
        names, posters = recommend(selected_movie_name)

        # Check if recommendation returned anything
        if names:
            cols = st.columns(len(names))
            for i, col in enumerate(cols):
                with col:
                    st.text(names[i])
                    st.image(posters[i])
        else:
            st.warning("Could not find recommendations.")

    else:
        st.warning("Please select a movie.")


