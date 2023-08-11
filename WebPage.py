import streamlit as st
import pickle
import pandas as pd

movies_dictionary = pickle.load(open('Dataset/movies_dictionary.pkl', 'rb'))
movies = pd.DataFrame(movies_dictionary)

similarity_matrix = pickle.load(open('Dataset/similarity_matrix.pkl', 'rb'))

st.title("Movie Recommendation System")

selected_movie_name = st.selectbox("Movie", movies['title'].values)
