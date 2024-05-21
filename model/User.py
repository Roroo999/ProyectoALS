import flask_login
import werkzeug.security as safe
import sirope

class User(flask_login.mixins.UserMixin):
    def __init__(self, username, email, passwd):
        self.__username = username
        self.__email = email
        self.__passwd = safe.generate_password_hash(passwd)
        self.__followed = []
        self.__followers = []
        self.__posts = []

    @property
    def username(self):
        return self.__username

    @property
    def email(self):
        return self.__email
    
    @property
    def passwd(self):
        return self.__passwd
    
    @property
    def followed(self):
        return self.__followed
    
    @property
    def followers(self):
        return self.__followers
    
    @property 
    def posts(self):
        return self.__posts

    def get_id(self):
        return self.username
    
    def addFollow(self, username):
        self.followed.append(username)

    def addFollower(self, username):
        self.followers.append(username)

    def stopFollowing(self, username):
        self.followed.remove(username)

    def removeFollower(self, username):
        self.followers.remove(username)

    def addPost(self, post):
        self.posts.append(post)

    def compare_passwd(self, other_pass):
        return safe.check_password_hash(self.passwd, other_pass)
    
    @staticmethod
    def current_user():
        user = flask_login.current_user

        if  user.is_anonymous:
            user.logout_user()
            user = None

        return user
    
    @staticmethod
    def find(srp: sirope.Sirope, username: str) -> "User":
        return srp.find_first(User, lambda u: u.username == username)
        
    def __str__(self):
        return "Username: " + self.__username + "\nEmail: " + self.__email