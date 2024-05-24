class Post:
    def __init__(self, postId, user, song, lyric, lyricSing, caption):
        self.__postId = postId
        self.__user = user
        self.__song = song
        self.__lyric = lyric
        self.__lyricSing = lyricSing
        self.__likes = 0
        self.__caption = caption
        self.__comments = []

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
    
    @property
    def lyricSing(self):
        return self.__lyricSing
    
    @property 
    def comments(self):
        return self.__comments
    
    @property
    def postId(self):
        return self.__id
    
    def addComment(self, comment):
        self.__comments.append(comment)
    
    def likePost(self):
        self.__likes = self.__likes + 1

    def removeLike(self):
        self.__likes = self.__likes - 1