class Post:
    def __init__(self, user, song, lyric, caption):
        self.__user = user
        self.__song = song
        self.__lyric = lyric
        self.__rating = 0.0
        self.__caption = caption

    @property
    def user(self):
        return self.__user
    
    @property
    def song(self):
        return self.__song
    
    @property
    def lyric(self):
        return self.__lyric
    
    @property
    def rating(self):
        return self.__rating
    
    @property
    def caption(self):
        return self.__caption
    
    def update_rating(self, nRating):
        self.__rating = nRating
