import streamlit as st
import pickle
import pandas as pd

books = pickle.load(open("models/books.pkl", "rb"))
similarity = pickle.load(open("models/similarity.pkl", "rb"))

st.set_page_config(
    page_title="Book Recommendation System",
    page_icon="📚",
    layout="wide"
)

st.title("📚 Book Recommendation System")
st.write("Find books you'll love based on your favorite reads.")

genres = sorted(books["Genre"].dropna().unique())

selected_genre = st.selectbox(
    "Select Genre",
    genres
)

genre_books = books[books["Genre"] == selected_genre]

selected_book = st.selectbox(
    "Select Book",
    genre_books["Title"].values
)

def recommend(book_name):
    index = books[books["Title"] == book_name].index[0]

    distances = similarity[index]

    recommended = sorted(
        list(enumerate(distances)),
        reverse=True,
        key=lambda x: x[1]
    )[1:6]

    recommended_books = []

    for i in recommended:
        recommended_books.append(books.iloc[i[0]])

    return recommended_books

if st.button("Recommend Books"):
    recommendations = recommend(selected_book)

    st.subheader("Recommended Books")

    for book in recommendations:
        st.image(book["Image_URL"], width=150)
        st.write(f"### {book['Title']}")
        st.write(f"👤 {book['Author']}")
        st.write(f"⭐ {book['Rating']}")
        st.write("---")