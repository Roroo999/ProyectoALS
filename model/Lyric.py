class Lyric:
    def __init__(self, song, artist, text):
        self.__song = song
        self.__artist = artist
        self.__text = text

    @property
    def song(self):
        return self.__song
    
    @song.setter
    def set_song(self, nSong):
        self.__song = nSong

    @property
    def artist(self):
        return self.__artist
    
    @artist.setter
    def set_artist(self, nArtist):
        self.__artist = nArtist

    @property
    def text(self):
        return self.__text
    
    @text.setter
    def set_text(self, nText):
        self.__text = nText
    