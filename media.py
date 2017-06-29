import webbrowser


class Movie():

    """This class provides a way to store movie related information"""

    def __init__(self, movie_title, movie_storyline, poster_image,
                 trailer_youtube):
        #  Things for class movie to remember
        self.title = movie_title
        #  Movie title
        self.storyline = movie_storyline
        #  Movie Storyline
        self.poster_image_url = poster_image
        #   Moive poster
        self.trailer_youtube_url = trailer_youtube
        #  Movie trailer link

    def show_trailer(self):
        # open the output file in the browser
        webbrowser.open(self.trailer_youtube_url)
