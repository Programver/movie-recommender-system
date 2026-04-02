# Movie Recommender System

A content-based movie recommendation web app built with Streamlit. The project suggests similar movies based on metadata-derived text features and enriches the recommendations with poster images fetched from The Movie Database (TMDb) API.

## Overview

This project allows a user to choose a movie from a dropdown and instantly receive five similar movie recommendations. The core recommendation engine uses a precomputed cosine similarity matrix generated from movie metadata such as genres, keywords, cast, crew, and overview-derived tags.

The application is lightweight, interactive, and simple to deploy, making it a good portfolio project for demonstrating:

- recommendation system fundamentals
- content-based filtering
- similarity search using cosine similarity
- Streamlit app development
- API integration with TMDb

## Demo Workflow

1. The user selects a movie title from the Streamlit dropdown.
2. The app finds that movie's index in the dataset.
3. It looks up similarity scores from the precomputed similarity matrix.
4. The top matching movies are selected.
5. Poster images are fetched through the TMDb API.
6. The recommended movies and their posters are displayed in the UI.

## Features

- Content-based movie recommendation
- Precomputed similarity matrix for fast inference
- Simple and interactive Streamlit interface
- Movie poster fetching with retry handling
- Fallback placeholder image when a poster is unavailable
- Deployment-ready setup for Streamlit hosting environments

## Tech Stack

- Python
- Streamlit
- Pandas
- Requests
- Scikit-learn
- NumPy
- Pickle
- TMDb API

## Recommendation Approach

This project uses a content-based filtering approach instead of collaborative filtering.

Each movie is represented using a combined text feature column called `tags`. These tags typically come from processed movie metadata and can include:

- genres
- plot keywords
- cast
- crew
- overview text

Once the movie vectors are prepared, cosine similarity is used to measure how closely movies relate to one another. At runtime, the app simply reads the saved similarity matrix and returns the highest-scoring similar movies for the selected title.

## Project Structure

```text
movie_recommender_system/
├── app.py               # Streamlit application
├── model_builder.py     # Script snippet for building similarity artifacts
├── movies1.pkl          # Serialized movie dataset used by the app
├── similarity1.pkl      # Precomputed cosine similarity matrix
├── requirements.txt     # Python dependencies
├── setup.sh             # Streamlit deployment configuration
└── procfile             # Process command for deployment
```

## Dataset and Saved Artifacts

The app currently loads:

- `movies1.pkl`: a Pandas DataFrame with `4806` movies and the columns `movie_id`, `title`, and `tags`
- `similarity1.pkl`: a `4806 x 4806` similarity matrix used for recommendation lookup

These serialized files let the app serve recommendations quickly without rebuilding the model every time the app starts.

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/your-username/movie_recommender_system.git
cd movie_recommender_system
```

### 2. Create a virtual environment

```bash
python -m venv venv
source venv/bin/activate
```

On Windows:

```bash
venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the application

```bash
streamlit run app.py
```

After that, open the local URL shown in the terminal, usually:

```text
http://localhost:8501
```

## Deployment

This repository already includes:

- `setup.sh` for Streamlit server configuration
- `procfile` with the startup command

That makes it easier to deploy on platforms that support Procfile-based execution or custom startup scripts.

Startup command used in this project:

```bash
sh setup.sh && streamlit run app.py
```

## How the App Works

The main logic lives in `app.py`.

- The app loads `movies1.pkl` and `similarity1.pkl`
- The user selects a movie title from the dropdown
- The `recommend()` function finds the closest matching movies using the similarity matrix
- The `fetch_poster()` function retrieves poster images from TMDb using the movie ID
- Results are displayed in a multi-column Streamlit layout

The app also includes basic retry handling for API calls and user-friendly warnings when no movie is selected or files are missing.

## Example Use Case

If a user selects `Avatar`, the app computes its nearest neighbors from the similarity matrix and returns a short list of movies with related themes, genres, or cast/crew patterns, along with their posters.

## Requirements

Current runtime dependencies listed in `requirements.txt`:

- `streamlit`
- `pandas`
- `requests`

Model-building code also relies on:

- `scikit-learn`
- `numpy`

If you plan to regenerate the model artifacts, make sure those libraries are installed as well.

## Limitations

- The recommender is content-based, so it does not learn from user behaviour or ratings
- Recommendation quality depends heavily on how the `tags` field was engineered
- Poster fetching depends on TMDb API availability
- The current app uses precomputed model files, so updating the dataset requires rebuilding artifacts

## Future Improvements

- Move the TMDb API key to environment variables
- Add search and filtering by genre, language, or year
- Improve the UI design and recommendation layout
- Add hybrid or collaborative filtering methods
- Store only top-k similar movies to reduce memory usage
- Add unit tests and better model-building documentation
## app link
https://movie-recommender-system-zdro2bzdiifh9lzibfd8af.streamlit.app/
