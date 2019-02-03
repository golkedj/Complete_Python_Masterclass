class Song:
    """Class to represent a song

    Attributes:
        title {str}: The title of the song
        artist {Artist}: An artist object representing the songs creator.
        duration {int}: The duration of the song in seconds. May be zero
    """

    def __init__(self, title, article, duration=0):
        """Song init method
        
        Arguments:
            title {str} -- Initializes the 'title' attribute
            article {Artist} -- At Artist object representing the song's creator.
        
        Keyword Arguments:
            duration {int} -- Initial value for the 'duration' attribute. (default: {0})
        """


