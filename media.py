import webbrowser

class Movie():
    """ Class Movie, takes in details about movies. Title, Storyline, Poster and Youtube Trailer """
    def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        """ Opens webbrowser and launches youtube url taken in from Movie """
        webbrowser.open(self.trailer_youtube_url)
