class Song:
    def __init__(self, name, artist, url):
        self.__name = name
        self.__artist = artist
        self.__url = url

    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, newName):
        self.__name = newName

    @property
    def artist(self):
        return self.__artist
    
    @artist.setter
    def artist(self, nArt):
        self.__artist = nArt

    @property 
    def url(self):
        return self.__url
    
    @url.setter
    def url(self, nUrl):
        self.__url = nUrl

    def __eq__(self, song2):

        if not(isinstance(song2, Song)):
            return False
        else:
            return self.artist == song2.artist and self.name == song2.name
        
    def get_id(self):
        return self.name + "-" + self.artist