class Comment:
    def __init__(self, commentId, user, post, text):
        self.__commentId = commentId
        self.__user = user
        self.__post = post
        self.__text = text

    @property
    def user(self):
        return self.__user
    
    @property
    def post(self):
        return self.__post

    @property
    def text(self):
        return self.__text
    
    @property 
    def commentId(self):
        return self.__commentId
    

    