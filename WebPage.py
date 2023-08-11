import streamlit as st
import pickle
import pandas as pd
import requests


def fetch_poster(movie_id):
    response = requests.get(
        "https://api.themoviedb.org/3/movie/{}?api_key=e006e57ee414fd74972cec97c4cd8f62".format(movie_id))
    data = response.json()
    return "https://image.tmdb.org/t/p/original" + data['poster_path']


def recommend(movie_name):
    movie_index = movies[movies['title'] == movie_name].index[0]
    # finding the index of movie mentioned, & finding its similarity matrix

    top_n_movies = similarity_matrix.get(movie_index, [])

    recommended_movie = []
    recommended_movie_poster = []
    for index, similarity_score in top_n_movies:
        # fetching poster from TMDB API
        movie_id = movies.iloc[index].movie_id
        recommended_movie_poster.append(fetch_poster(movie_id))

        recommended_movie.append(movies.iloc[index]['title'])
        # finding title for the indices that were the most similar
    return recommended_movie, recommended_movie_poster


# importing movie dictionary consisting of movie name & movie id
movies_dictionary = pickle.load(open('Dataset/movies_dictionary.pkl', 'rb'))
# converting it into pandas DF, to show it in selectbox of streamlit
movies = pd.DataFrame(movies_dictionary)

# importing similarity matrix
similarity_matrix = pickle.load(open('Dataset/similarity_matrix.pkl', 'rb'))

# declaring title of website
st.title("Movie Recommendation System")

# showing the selectbox, with all movie options available
selected_movie_name = st.selectbox("Movies", movies['title'].values)

# adding a button , which when pressed - will call recommend function
if st.button("Recommend"):
    names, posters = recommend(selected_movie_name)

    num_columns = 5
    col_layout = st.columns(num_columns)

    for i in range(num_columns):
        with col_layout[i]:
            st.text(names[i])
            st.image(posters[i])
