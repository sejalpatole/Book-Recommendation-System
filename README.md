# 📚 Book Recommendation System

A Machine Learning-based **Book Recommendation System** built with **Python** and **Streamlit**. This application recommends similar books using **Content-Based Filtering** and **Cosine Similarity**, providing users with personalized book suggestions based on their selected book.

---

## 🚀 Features

- 📖 Browse books by genre
- 🔍 Select a book from the chosen genre
- 🤖 Get Top 5 similar book recommendations
- ⭐ View book ratings
- 🖼️ Display book cover images
- 🎨 Modern and interactive Streamlit user interface

---

## 🛠️ Technologies Used

- Python
- Streamlit
- Pandas
- NumPy
- Scikit-learn
- Pickle

---

## 📂 Project Structure

```
Book-Recommendation-System/
│
├── app.py                     # Main Streamlit app
├── requirements.txt
├── README.md
│
├── notebooks/
│   ├── 1. Data Cleaning and Preprocessing.ipynb
│   └── 2. Recommendation System.ipynb
│
├── data/
│   ├── books.csv
│   ├── ratings.csv
│   ├── tags.csv
│   ├── book_tags.csv
│   ├── to_read.csv
│   ├── clean_books.csv
│   └── books_cleaned.csv
│
├── models/
   ├── books.pkl
   └── similarity.pkl
```

---

## 📊 Dataset

The project is built using the **Goodbooks-10k** dataset.

Files used during preprocessing include:

- books.csv
- ratings.csv
- book_tags.csv
- tags.csv
- to_read.csv

After preprocessing, the final dataset used by the application is:

- clean_books.csv

---

## ⚙️ How It Works

1. Load the cleaned book dataset.
2. Create a combined text feature using the **Title**, **Author**, and **Genre**.
3. Convert text into numerical vectors using **TF-IDF Vectorizer**.
4. Compute similarity scores using **Cosine Similarity**.
5. Recommend the most similar books based on the selected book.

---

## ▶️ Installation

Clone the repository:

```bash
git clone https://github.com/your-username/Book-Recommendation-System.git
```

Move into the project folder:

```bash
cd Book-Recommendation-System
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
streamlit run app.py
```

---


## 📌 Future Improvements

- User authentication
- Collaborative Filtering
- Hybrid Recommendation System
- Search by author
- Book description and publication details
- Goodreads API integration
- User favorites and reading history

---

## 👩‍💻 Author

**Sejal Patole**

Diploma in Artificial Intelligence & Machine Learning

---

## ⭐ If you like this project

If you found this project useful, consider giving it a ⭐ on GitHub!