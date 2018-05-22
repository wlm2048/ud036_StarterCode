"""Loads and parses the movies file; then presents them"""
import os
import sys
import json
import media
import fresh_tomatoes

def load_movies():
    """Load the movies json file into an object"""
    try:
        json_movies = open(os.path.join(sys.path[0], 'movies.json'), 'r')
    except IOError, err:
        raise Exception("Sorry, there was an error loading the movies file: " + err.strerror)
    else:
        movies_data = json.load(json_movies)
        return movies_data

DATA = load_movies()
MOVIES = {}

for movie in DATA['movies']:
    MOVIES[movie['title']] = media.Movie(
        movie['title'],
        movie['synopsis'],
        movie['poster_url'],
        movie['preview_url']
    )

fresh_tomatoes.open_movies_page(MOVIES)
