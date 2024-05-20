class Song:
    def __init__(self, name, artist, features, duration, genre, url):
        self.__name = name
        self.__artist = artist
        self.__features = features
        self.__duration = duration
        self.__genre = genre
        self.__rating = 0.0
        self.__url = url

    @property
    def name(self):
        return self.__name
    
    @name.setter
    def set_name(self, newName):
        self.__name = newName

    @property
    def artist(self):
        return self.__artist
    
    @artist.setter
    def set_artist(self, nArt):
        self.__artist = nArt

    @property
    def features(self):
        return self.__features

    @features.setter
    def set_features(self, nFeat):
        self.__features = nFeat

    @property
    def duration(self):
        return self.__duration
    
    @duration.setter
    def set_duration(self, nDur):
        self.__duration = nDur

    @property 
    def genre(self):
        return self.__genre
    
    @genre.setter
    def set_genre(self, nGen):
        self.__genre = nGen

    @property
    def rating(self):
        return self.__rating
    
    @rating.setter
    def set_rating(self, nRating):
        self.__rating = nRating

    @property 
    def url(self):
        return self.__url
    
    @url.setter
    def set_url(self, nUrl):
        self.__url = nUrl

    def __eq__(self, song2):

        if not(isinstance(song2, Song)):
            return False
        else:
            return self.artist == song2.artist and self.name == song2.name
        
    def get_id(self):
        return self.name + "-" + self.artist