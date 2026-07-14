import streamlit as st
import pandas as pd
import pickle

# ---------------- PAGE CONFIG ---------------- #

st.set_page_config(
    page_title="Book Recommendation System",
    page_icon="📚",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ---------------- LOAD DATA ---------------- #

books = pickle.load(open("models/books.pkl", "rb"))
similarity = pickle.load(open("models/similarity.pkl", "rb"))

# ---------------- CUSTOM CSS ---------------- #

st.markdown("""
<style>

/* Import Font */
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700&display=swap');

html, body, [class*="css"] {
    font-family: 'Poppins', sans-serif;
}

/* Main Background */
.stApp{
    background: #F5F1E8;
    color:#2C2C2C;
}

/* Remove Streamlit Header */
header{
    visibility:hidden;
}

footer{
    visibility:hidden;
}

/* Hero Card */
.hero{
    background: #FFFFFF;
    backdrop-filter: blur(15px);
    border-radius:25px;
    padding:40px;
    text-align:center;
    border:1px solid #E5D8C5;
    margin-bottom:30px;
    box-shadow:0 8px 25px rgba(109,76,65,.15);
}

/* Gradient Title */
.hero h1{
    font-size:48px;
    font-weight:700;
    background:linear-gradient(90deg,#6D4C41,#C49A6C);
    -webkit-background-clip:text;
    -webkit-text-fill-color:transparent;
    margin-bottom:10px;
}

/* Subtitle */
.hero p{
    color:#5C4A42;
    font-size:18px;
}

/* Dashboard Cards */
.metric-card{
    background:#FFFFFF;
    backdrop-filter:blur(15px);
    border-radius:20px;
    padding:20px;
    text-align:center;
    border:1px solid #E8DDCE;
    transition:0.3s;
    margin-bottom:20px;
}

.metric-card:hover{
    transform:translateY(-6px);
    box-shadow:0 12px 25px rgba(196,154,108,.35);
}

.metric-number{
    font-size:34px;
    font-weight:bold;
    color:#6D4C41;
}

.metric-text{
    color:#6B5B53;
    font-size:16px;
}
            

            
/* Selection Card */

.select-card{
    background:#FFFFFF;
    border-radius:20px;
    padding:20px;
    border:1px solid #E8DDCE;
    margin-top:15px;
    margin-bottom:20px;
}

.select-title{
    color:#4A3227;
    font-size:22px;
    font-weight:600;
    margin-bottom:15px;
}

/* Selectbox */

.stSelectbox > div > div{
    background:#F9F7F4;
    border-radius:12px;
    border:1px solid #D8C9B7;
}

/* Button */

.stButton>button{
    width:100%;
    background:linear-gradient(90deg,#6D4C41,#C49A6C);
    color:white;
    border:none;
    border-radius:12px;
    padding:12px;
    font-size:18px;
    font-weight:bold;
    transition:.3s;
}

.stButton>button:hover{
    transform:scale(1.03);
    box-shadow:0px 10px 25px rgba(196,154,108,.45);
}

</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="hero">

<h1>📚 Book Recommendation System</h1>

<p>
Discover your next favorite book using Machine Learning and
Content-Based Filtering.
</p>

</div>
""", unsafe_allow_html=True)

total_books = len(books)
total_genres = books["Genre"].nunique()
avg_rating = round(books["Rating"].mean(), 2)

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown(f"""
    <div class="metric-card">
        <div class="metric-number">{total_books}</div>
        <div class="metric-text">Books</div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown(f"""
    <div class="metric-card">
        <div class="metric-number">{total_genres}</div>
        <div class="metric-text">Genres</div>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown(f"""
    <div class="metric-card">
        <div class="metric-number">{avg_rating}</div>
        <div class="metric-text">Average Rating</div>
    </div>
    """, unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

left, right = st.columns(2)

with left:

    st.markdown("""
    <div class="select-card">
        <div class="select-title">
        📂 Select Genre
        </div>
    """, unsafe_allow_html=True)

    genres = sorted(books["Genre"].dropna().unique())

    selected_genre = st.selectbox(
        "",
        genres
    )

    st.markdown("</div>", unsafe_allow_html=True)


with right:

    st.markdown("""
    <div class="select-card">
        <div class="select-title">
        📖 Select Book
        </div>
    """, unsafe_allow_html=True)

    genre_books = books[books["Genre"] == selected_genre]

    selected_book = st.selectbox(
        "",
        genre_books["Title"].tolist()
    )

    st.markdown("</div>", unsafe_allow_html=True)


selected = books[books["Title"] == selected_book].iloc[0]

st.markdown("### 📖 Selected Book")

col1, col2 = st.columns([1, 3])

with col1:
    st.image(selected["Image_URL"], width=220)

with col2:
    st.markdown(f"## {selected['Title']}")
    st.markdown(f"**👤 Author:** {selected['Author']}")
    st.markdown(f"**⭐ Rating:** {selected['Rating']}")
    st.markdown(f"**📂 Genre:** {selected['Genre']}")

# ==========================
# RECOMMENDATION FUNCTION
# ==========================

def recommend_books(book_name):

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

st.markdown("<br>", unsafe_allow_html=True)

recommend = st.button("✨ Recommend Books", use_container_width=True)

if recommend:

    recommendations = recommend_books(selected_book)

    st.markdown("<br>", unsafe_allow_html=True)

    st.markdown("## 📚 Recommended Books")

    cols = st.columns(5)

    for idx, book in enumerate(recommendations):

        with cols[idx]:

            st.image(book["Image_URL"], use_container_width=True)

            st.markdown(f"### {book['Title']}")

            st.caption(f"👤 {book['Author']}")

            st.success(f"⭐ {book['Rating']}")