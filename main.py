import streamlit as st
import requests

API_KEY = "3c7bb4ca"
BASE_URL = "http://www.omdbapi.com/"

def search_movies(title):
    params = {"apikey": API_KEY, "s": title}
    response = requests.get(BASE_URL, params=params)
    data = response.json()
    if data.get("Response") == "True":
        return data.get("Search", [])
    return []

def get_movie_details(imdb_id):
    params = {"apikey": API_KEY, "i": imdb_id, "plot": "full"}
    response = requests.get(BASE_URL, params=params)
    data = response.json()
    if data.get("Response") == "True":
        return data
    return None

st.set_page_config(page_title="HTL Film-Suchbrowser", layout="wide")
st.title("HTL Film-Suchbrowser")

title = st.text_input("Filmtitel eingeben:")

if title:
    movies = search_movies(title)
    
    if not movies:
        st.warning("Keine Filme gefunden.")
    else:
        st.subheader(f"Gefundene Filme für '{title}':")
        
        for movie in movies:
            with st.expander(f"{movie['Title']} ({movie['Year']})"):
                details = get_movie_details(movie['imdbID'])

                # Einfachere Spalten-Zuweisung
                col1, col2 = st.columns([1, 3])

                # Poster anzeigen 
                poster = None
                if details and details.get("Poster") and details["Poster"] != "N/A":
                    poster = details["Poster"]

                if poster:
                    col1.image(poster, width=150)
                else:
                    col1.write("Kein Poster verfügbar")

                # Filmdetails anzeigen
                if details:
                    col2.write(f"**Titel:** {details.get('Title','')}")
                    col2.write(f"**Jahr:** {details.get('Year','')}")
                    col2.write(f"**Regisseur:** {details.get('Director','')}")
                    col2.write(f"**Genre:** {details.get('Genre','')}")
                    col2.write(f"**IMDb Bewertung:** {details.get('imdbRating','')}")
                    col2.write(f"**Plot:** {details.get('Plot','')}")
                else:
                    col2.write("Details konnten nicht geladen werden.")
