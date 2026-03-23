import unittest
from PartA import Artist, Song, Album, Playlist


class TestMusicPlaylist(unittest.TestCase):

    def setUp(self):
        self.artist = Artist("Justin Bieber", "01/03/1994", "Canada")
        self.song1 = Song("Sorry", "Justin Bieber", 2015)
        self.song2 = Song("Love Yourself", "Justin Bieber", 2015)
        self.song3 = Song("Beauty and a Beat", "Justin Bieber", 2012)
        self.album = Album("Believe", "Justin Bieber", 2012)
        self.playlist = Playlist("Test Playlist")

    # 4 tests: object IS an instance of a class
    def test_artist_is_instance_of_artist(self):
        self.assertIsInstance(self.artist, Artist)

    def test_song_is_instance_of_song(self):
        self.assertIsInstance(self.song1, Song)

    def test_album_is_instance_of_album(self):
        self.assertIsInstance(self.album, Album)

    def test_playlist_is_instance_of_playlist(self):
        self.assertIsInstance(self.playlist, Playlist)

    # 4 tests: object is NOT an instance of a class
    def test_artist_is_not_instance_of_song(self):
        self.assertNotIsInstance(self.artist, Song)

    def test_song_is_not_instance_of_album(self):
        self.assertNotIsInstance(self.song1, Album)

    def test_album_is_not_instance_of_playlist(self):
        self.assertNotIsInstance(self.album, Playlist)

    def test_playlist_is_not_instance_of_artist(self):
        self.assertNotIsInstance(self.playlist, Artist)

    # 2 tests: identical and unidentical but similar
    def test_identical_objects(self):
        another_reference = self.song1
        self.assertIs(self.song1, another_reference)

    def test_similar_but_not_identical_objects(self):
        another_song = Song("Sorry", "Justin Bieber", 2015)
        self.assertIsNot(self.song1, another_song)
        self.assertEqual(self.song1.title, another_song.title)
        self.assertEqual(self.song1.artist_name, another_song.artist_name)
        self.assertEqual(self.song1.year, another_song.year)

    # 4 tests: add_song() and add_album()
    def test_artist_add_album(self):
        self.artist.add_album(self.album)
        self.assertEqual(len(self.artist.albums), 1)
        self.assertEqual(self.artist.albums[0].title, "Believe")

    def test_artist_add_song(self):
        self.artist.add_song(self.song1)
        self.assertEqual(len(self.artist.songs), 1)
        self.assertEqual(self.artist.songs[0].title, "Sorry")

    def test_album_add_song(self):
        self.album.add_song("Boyfriend", 2012)
        self.assertEqual(len(self.album.songs), 1)
        self.assertEqual(self.album.songs[0].title, "Boyfriend")

    def test_playlist_add_song(self):
        self.playlist.add_song(self.song1)
        self.assertEqual(len(self.playlist.songs), 1)
        self.assertEqual(self.playlist.songs[0].title, "Sorry")

    # 3 tests: sort_playlist() and shuffle_playlist()
    def test_sort_playlist_ascending(self):
        self.playlist.add_song(self.song2)  # Love Yourself
        self.playlist.add_song(self.song1)  # Sorry
        self.playlist.add_song(self.song3)  # Beauty and a Beat

        self.playlist.sort_playlist("ASC")

        titles = [song.title for song in self.playlist.songs]
        self.assertEqual(titles, ["Beauty and a Beat", "Love Yourself", "Sorry"])

    def test_sort_playlist_descending(self):
        self.playlist.add_song(self.song2)
        self.playlist.add_song(self.song1)
        self.playlist.add_song(self.song3)

        self.playlist.sort_playlist("DES")

        titles = [song.title for song in self.playlist.songs]
        self.assertEqual(titles, ["Sorry", "Love Yourself", "Beauty and a Beat"])

    def test_shuffle_playlist_keeps_same_songs(self):
        self.playlist.add_song(self.song1)
        self.playlist.add_song(self.song2)
        self.playlist.add_song(self.song3)

        before_shuffle = sorted([song.title for song in self.playlist.songs])
        self.playlist.shuffle_playlist()
        after_shuffle = sorted([song.title for song in self.playlist.songs])

        self.assertEqual(before_shuffle, after_shuffle)


if __name__ == "__main__":
    unittest.main()