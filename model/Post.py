class Post:
    def __init__(self, user, song, lyric, caption):
        self.__user = user
        self.__song = song
        self.__lyric = lyric
        self.__likes = 0
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
    def likes(self):
        return self.__likes
    
    @property
    def caption(self):
        return self.__caption
    
    def likePost(self):
        self.__likes = self.__likes + 1

    def removeLike(self):
        self.__likes = self.__likes - 1