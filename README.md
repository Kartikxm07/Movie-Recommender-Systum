# Movie Recommender System

A Streamlit movie recommender that uses a pre-trained similarity model to find similar movies and fetches their posters from The Movie Database (TMDB).

## Features

- Search and select a movie from the dataset.
- Choose 5, 10, or 15 recommendations.
- Display poster images when TMDB is available.
- Continue working when a poster cannot be fetched.

## Requirements

- Python 3.10 or newer
- A TMDB API key for poster images

## Setup

Create and activate a virtual environment, then install dependencies:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

Create a `.env` file in this folder and add your TMDB key as an environment variable. On PowerShell:

```powershell
$env:TMDB_API_KEY = "your_tmdb_api_key_here"
```

The application still runs without the key, but posters will show as unavailable.

## Run

```powershell
streamlit run app.py
```

Open the local URL shown by Streamlit in your browser.

## Project Files

- `app.py`: Streamlit application.
- `movie_list.pkl`: Movie data used by the recommender.
- `similarity.pkl`: Pre-computed similarity matrix.
- `recommender_model.ipynb`: Notebook used to develop the model.
- `tmdb_5000_movies.csv` and `tmdb_5000_credits.csv`: Source datasets.

## GitHub

Do not commit API keys. The `.gitignore` file excludes `.env`; use `.env.example` as a template.