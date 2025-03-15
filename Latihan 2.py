class Music:
    def __init__(self, title, artist):
        self.title = title
        self.artist = artist
    def show(self):
        pass

class Pop(Music):
    def show(self):
        return f"Pop Music - Title: {self.title}, Artist: {self.artist}"
class Rock(Music):
    def show(self):
        return f"Rock Music - Title: {self.title}, Artist: {self.artist}"
class Jazz(Music):
    def show(self):
        return f"Jazz Music - Title: {self.title}, Artist: {self.artist}"
    
def cetak_info(music):
    print(music.show())

music1 = Pop("Hot To Go", "Chapple Roan")
music2 = Pop("Abracadabra", "Lady Gaga")
music3 = Rock("Hard Times", "Paramore")
music4 = Jazz("So What", "Miles Davis")

cetak_info(music1)  
cetak_info(music2)  
cetak_info(music3)  
cetak_info(music4)  
 