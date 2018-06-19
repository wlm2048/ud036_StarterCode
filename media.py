""" This class (Movie) creates the Movie object containing the movie information """
import webbrowser

class Movie():
    """ This class provides a way to store movie related information """

    VALID_RATINGS = ["G", "PG", "PG-13", "R"]

    def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        """ Open the web browser to show a trailer """
        webbrowser.open(self.trailer_youtube_url)
