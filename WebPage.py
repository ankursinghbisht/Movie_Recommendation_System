import streamlit as st
import pickle
import pandas as pd


def recommend(movie_name):
    movie_index = movies[movies['title'] == movie_name].index[0]
    # finding the index of movie mentioned, & finding its similarity matrix

    top_n_movies = similarity_matrix.get(movie_index, [])

    output = []
    for index, similarity_score in top_n_movies:
        output.append(movies.iloc[index]['title'])
        # finding title for the indices that were the most similar
    return output


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
    recommendations = recommend(selected_movie_name)
    for movie in recommendations:
        st.write(movie)
