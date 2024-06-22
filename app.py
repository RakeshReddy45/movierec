import pandas as pd
import numpy as np

import streamlit as st
import pickle
import requests

def fetch_poster(id):
    # res = requests.get('https://api.themoviedb.org/3/movie/{}?api_key=45d9b1d03d0577c9d815b47843f6b2b2&language=en-US'.format(id))

    url = "https://api.themoviedb.org/3/movie/{}?api_key=45d9b1d03d0577c9d815b47843f6b2b2&language=en-US%22".format(id)
    data = requests.get(url)
    data = data.json()
    # st.text(data)
    poster_path = data['poster_path']
    # print(poster_path)
    full_path = "https://image.tmdb.org/t/p/w500" + poster_path
    return full_path


def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)),reverse=True,key = lambda x: x[1])[1:6]

    recommended_movies = []
    recommended_movies_posters = []

    for j in movies_list:
        movie_id = movies.iloc[j[0]].id
        #
        recommended_movies.append(movies.iloc[j[0]].title)
        recommended_movies_posters.append(fetch_poster(movie_id))
    return recommended_movies,recommended_movies_posters


movies_dict = pickle.load(open('movies_dict.pkl','rb'))

movies = pd.DataFrame(movies_dict)
similarity = pickle.load(open('similarity.pkl','rb'))

st.title("Movie Rec system")

sel_movie_name = st.selectbox(
"how  wo",
movies['title'].values)

if st.button('recommend'):
    recommended_movie_names, recommended_movie_posters = recommend(sel_movie_name)
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(recommended_movie_names[0])
        st.image(recommended_movie_posters[0])
    with col2:
        st.text(recommended_movie_names[1])
        st.image(recommended_movie_posters[1])

    with col3:
        st.text(recommended_movie_names[2])
        st.image(recommended_movie_posters[2])
    with col4:
        st.text(recommended_movie_names[3])
        st.image(recommended_movie_posters[3])
    with col5:
        st.text(recommended_movie_names[4])
        st.image(recommended_movie_posters[4])
