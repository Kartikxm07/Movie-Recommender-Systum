import pickle
import os
from pathlib import Path

import streamlit as st
import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

TMDB_API_KEY = os.getenv("TMDB_API_KEY")

@st.cache_resource
def get_http_session():
    retry = Retry(
        total=2,
        connect=2,
        read=2,
        backoff_factor=0.5,
        status_forcelist=(429, 500, 502, 503, 504),
        allowed_methods=("GET",),
    )
    session = requests.Session()
    session.mount("https://", HTTPAdapter(max_retries=retry))
    return session

@st.cache_data(ttl=86400, show_spinner=False)
def fetch_poster(movie_id):
    if not TMDB_API_KEY:
        return None

    url = "https://api.themoviedb.org/3/movie/{}?api_key={}&language=en-US".format(movie_id, TMDB_API_KEY)
    try:
        response = get_http_session().get(url, timeout=10)
        response.raise_for_status()
        poster_path = response.json().get('poster_path')
    except (requests.RequestException, ValueError):
        return None

    if not poster_path:
        return None

    full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
    return full_path

@st.cache_data(ttl=86400, show_spinner=False)
def fetch_poster_image(movie_id):
    poster_url = fetch_poster(movie_id)
    if not poster_url:
        return None

    try:
        response = get_http_session().get(poster_url, timeout=10)
        response.raise_for_status()
    except requests.RequestException:
        return None

    return response.content

def recommend(movie, recommendation_count):
    index = movies[movies['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    recommended_movie_names = []
    recommended_movie_posters = []
    for i in distances[1:recommendation_count + 1]:
        # fetch the movie poster
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movie_posters.append(fetch_poster_image(movie_id))
        recommended_movie_names.append(movies.iloc[i[0]].title)

    return recommended_movie_names,recommended_movie_posters


st.header('Movie Recommender System')
project_dir = Path(__file__).resolve().parent
with open(project_dir / 'movie_list.pkl', 'rb') as movie_file:
    movies = pickle.load(movie_file)
with open(project_dir / 'similarity.pkl', 'rb') as similarity_file:
    similarity = pickle.load(similarity_file)

movie_list = movies['title'].values
selected_movie = st.selectbox(
    "Type or select a movie from the dropdown",
    movie_list
)
recommendation_count = st.radio(
    "Number of recommendations",
    options=[5, 10, 15],
    horizontal=True,
)

if st.button('Show Recommendation'):
    recommended_movie_names, recommended_movie_posters = recommend(
        selected_movie,
        recommendation_count,
    )
    for start in range(0, len(recommended_movie_names), 5):
        columns = st.columns(min(5, len(recommended_movie_names) - start))
        for column, name, poster in zip(
            columns,
            recommended_movie_names[start:start + 5],
            recommended_movie_posters[start:start + 5],
        ):
            with column:
                st.text(name)
                if poster:
                    st.image(poster)
                else:
                    st.caption('Poster unavailable')




