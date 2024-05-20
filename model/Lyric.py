class Lyric:
    def __init__(self, song, timeS, timeE, artist, text):
        self.__song = song
        self.__timeStart = timeS
        self.__timeEnd = timeE
        self.__artist = artist
        self.__rating = 0.0
        self.__text = text

    @property
    def song(self):
        return self.__song
    
    @song.setter
    def set_song(self, nSong):
        self.__song = nSong

    @property
    def timeStart(self):
        return self.__timeStart
    
    @timeStart.setter
    def set_timeStart(self, nTimeStart):
        self.__timeStart = nTimeStart

    @property 
    def timeEnd(self):
        return self.__timeEnd
    
    @timeEnd.setter
    def set_timeEnd(self, nTimeEnd):
        self.__timeEnd = nTimeEnd

    @property
    def artist(self):
        return self.__artist
    
    @artist.setter
    def set_artist(self, nArtist):
        self.__artist = nArtist

    @property
    def rating(self):
        return self.__rating
    
    @rating.setter
    def set_rating(self, nRating):
        self.__rating = nRating

    @property
    def text(self):
        return self.__text
    
    @text.setter
    def set_text(self, nText):
        self.__text = nText
    