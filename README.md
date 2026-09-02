# 🎬 Movie Recommender System

A **content-based Movie Recommender System** built with Python and Streamlit that recommends movies similar to a movie selected by the user.

The system uses movie metadata such as **genres, keywords, cast, crew, and overview** to calculate similarity between movies. Recommended movies are displayed with their posters using the **TMDB API**.

![App Interface](interface_strreamlit.png)

---

## 📌 Project Overview

Finding a good movie to watch can be difficult when there are thousands of options available.

This project solves that problem by recommending movies based on the characteristics of a movie the user already likes.

---

## ✨ Features

- 🔍 Search and select any movie from 5000+ movies
- 🎯 Choose how many recommendations you want (5–20)
- 🖼️ Displays movie posters fetched from the TMDB API
- ⚡ Fast recommendations using precomputed similarity matrix
- 🛡️ Graceful fallback if poster cannot be fetched

---

## 🛠️ Tech Stack

| Tool | Purpose |
|---|---|
| Python | Core language |
| Streamlit | Web UI |
| Scikit-learn | Cosine similarity |
| Pandas / NumPy | Data processing |
| TMDB API | Movie poster images |
| python-dotenv | Secure API key loading |

---

## 📂 Project Structure

```
Movie-Recommender-System/
│
├── app.py                    # Main Streamlit application
├── recommender_model.ipynb   # ML notebook (data processing + model)
├── requirements.txt          # Python dependencies
├── .env.example              # API key template
├── .gitignore                # Files excluded from Git
└── README.md                 # Project documentation
```

> **Note:** `movie_list.pkl`, `similarity.pkl`, and the CSV dataset files are NOT included in this repo due to size limits. See the **Setup** section below to generate them.

---

## ⚙️ Setup & Installation

### 1. Clone the repository
```bash
git clone https://github.com/Kartikxm07/Movie-Recommender-System.git
cd Movie-Recommender-System
```

### 2. Create a virtual environment
```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

### 3. Download the dataset
Download the TMDB 5000 Movie Dataset from Kaggle:
👉 https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata

Place both CSV files in the project root:
- `tmdb_5000_movies.csv`
- `tmdb_5000_credits.csv`

### 4. Generate the model files
Run all cells in `recommender_model.ipynb` to generate:
- `movie_list.pkl`
- `similarity.pkl`

### 5. Add your TMDB API key
Get a free API key from: https://www.themoviedb.org/settings/api

Copy the example file and add your key:
```powershell
copy .env.example .env
```
Then edit `.env`:
```
TMDB_API_KEY=your_actual_api_key_here
```

### 6. Run the app
```powershell
streamlit run app.py
```

Open the local URL shown in the terminal (usually http://localhost:8501).

---

## 🖥️ How It Works

1. Movie metadata (genres, keywords, cast, crew, overview) is combined into **tags**
2. Tags are vectorized using **CountVectorizer**
3. **Cosine similarity** is computed between all movie pairs
4. When you select a movie, the top N most similar movies are returned
5. Poster images are fetched live from the **TMDB API**

---

## 📸 Interface Preview

![Movie Recommender Interface](interface_strreamlit.png)

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).