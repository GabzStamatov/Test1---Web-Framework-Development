#music system
import random #for song to be able to be shuffled

#blueprint
class Artist: #template for artist
    def __init__(self, name, dob, country, albums=None, songs=None): #constructor
        self.name = name
        self.dob = dob
        self.country = country
        #starts albums and songs as empty lists if none are provided
        self.albums = albums if albums is not None else []
        self.songs = songs if songs is not None else []

    def add_album(self, album): #add item/song to the end of the list
        self.albums.append(album)

    def add_song(self, song): # same thing adds a song
        self.songs.append(song)

    def display_info(self):
        print("****** Artist Information ******")
        print(f"Name: {self.name}")
        print(f"Date of Birth: {self.dob}")
        print(f"Country: {self.country}")
        print(f"Albums: {len(self.albums)}") #counts how many albums and songs they have
        print(f"Songs: {len(self.songs)}")


class Song: #template for song
    def __init__(self, title, artist_name, year): #constructor
        self.title = title
        self.artist_name = artist_name
        self.year = year

    def display_info(self): #will print the song info
        print("Song Information")
        print(f"Title: {self.title}")
        print(f"Artist: {self.artist_name}")
        print(f"Year: {self.year}")


class Album: #template for the album
    def __init__(self, title, artist_name, year, songs=None):# constructor
        self.title = title
        self.artist_name = artist_name
        self.year = year
        self.songs = songs if songs is not None else [] #start with empty list if so songs were given

    def add_song(self, title, year):
        new_song = Song(title, self.artist_name, year)
        self.songs.append(new_song) #add new song into the album list
        return new_song

    def display_info(self):
        print("Album Information")
        print(f"Title: {self.title}")
        print(f"Artist: {self.artist_name}")
        print(f"Year: {self.year}")
        print(f"Songs in album: {len(self.songs)}")


class Playlist: #craete a collection of songs (add, sort, and shuffle)
    def __init__(self, title, songs=None): #constructor
        self.title = title
        self.songs = songs if songs is not None else []

    def add_song(self, song): #adds song to the playlist
        self.songs.append(song)

    def print_all_song(self): #prints all songs in the playlist
        print(f"Playlist: {self.title}")
        for song in self.songs:
            print(f"{song.title} - {song.artist_name} ({song.year})")

    #sorts songs alphabetically by title (ascending or descending)
    def sort_playlist(self, order='ASC'):
        reverse_order = order.upper() == 'DES'
        self.songs.sort(key=lambda song: song.title.lower(), reverse=reverse_order)

    def shuffle_playlist(self):#randomly mix the order of song
        random.shuffle(self.songs)


# Demonstration
if __name__ == "__main__":
    # Create an artist
    artist = Artist("Justin Bieber", "01/03/1994", "Canada")

    # Create an album
    album = Album("Justice", "Justin Bieber", 2021)

    # Create a few songs for the artist
    song1 = Song("Peaches", "Justin Bieber", 2021)
    song2 = Song("Sorry", "Justin Bieber", 2015)

    # Use Album.add_song() to add two songs
    song3 = album.add_song("Beauty and a Beat", 2012)
    song4 = album.add_song("Boyfriend", 2012)

    # Update artist information
    artist.add_album(album)
    artist.add_song(song1)
    artist.add_song(song2)
    artist.add_song(song3)
    artist.add_song(song4)

    # Create a playlist
    playlist = Playlist("My Favourite Justin Songs")

    # Add all songs from the album to the playlist
    for song in album.songs:
        playlist.add_song(song)

    # Show how everything works
    artist.display_info()
    print()
    album.display_info()
    print()
    song1.display_info()
    print()
    playlist.print_all_song()
    print()

    print("Sorted ASC:")
    playlist.sort_playlist("ASC")
    playlist.print_all_song()
    print()

    print("Sorted DES:")
    playlist.sort_playlist("DES")
    playlist.print_all_song()
    print()

    print("Shuffled:")
    playlist.shuffle_playlist()
    playlist.print_all_song()