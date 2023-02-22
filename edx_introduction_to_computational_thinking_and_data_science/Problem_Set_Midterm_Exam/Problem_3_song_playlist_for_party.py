"""
You are creating a song playlist for your next party.
You have a collection of songs that can be represented as a list of tuples. Each tuple has the following elements:

name: the first element, representing the song name (non-empty string)
song_length: the second, element representing the song duration (float >= 0)
song_size: the third, element representing the size on disk (float >= 0)

You want to try to optimize your playlist to play songs for as long as possible while making sure that the songs
you pick do not take up more than a given amount of space on disk (the sizes should be less than or equal to
the max_disk_size).

You decide the best way to achieve your goal is to start with the first song in the given song list.
If the first song doesn't fit on disk, return an empty list. If there is enough space for this song, add it
to the playlist.

For subsequent songs, you choose the next song such that its size on disk is smallest and that the song hasn't
already been chosen. You do this until you cannot fit any more songs on the disk.

Write a function implementing this algorithm, that returns a list of the song names
in the order in which they were chosen, with the first element in the list being the song chosen first.
Assume song names are unique and all the songs have different sizes on disk and different durations.

You may not mutate any of the arguments.

For example,

If songs = [('Roar',4.4, 4.0),('Sail',3.5, 7.7),('Timber', 5.1, 6.9),('Wannabe',2.7, 1.2)] and max_size = 12.2,
the function will return ['Roar','Wannabe','Timber']
If songs = [('Roar',4.4, 4.0),('Sail',3.5, 7.7),('Timber', 5.1, 6.9),('Wannabe',2.7, 1.2)] and max_size = 11,
the function will return ['Roar','Wannabe']
"""


def song_playlist(songs, max_size):
    """
    songs: list of tuples, ('song_name', song_len, song_size)
    max_size: float, maximum size of total songs that you can fit

    Start with the song first in the 'songs' list, then pick the next
    song to be the one with the lowest file size not already picked, repeat

    Returns: a list of a subset of songs fitting in 'max_size' in the order
             in which they were chosen.
    """
    playlist = []

    class Song(object):
        def __init__(self, name, length, size):
            self.name = name
            self.length = length
            self.size = size

        def getName(self):
            return self.name

        def getLength(self):
            return self.length

        def getSize(self):
            return self.size

        def __str__(self):
            return self.name

    def full_list(songs):  # list of tuples
        fullList = []
        for i in range(len(songs)):
            fullList.append(Song(songs[i][0], songs[i][1], songs[i][2]))
        return fullList

    list_of_songs = full_list(songs)
    totalSize = 0

    if list_of_songs[0].getSize() > max_size:
        return playlist
    else:
        playlist.append(list_of_songs[0].getName())
        totalSize += list_of_songs[0].getSize()

    list_of_songs.pop(0)
    list_of_songs = sorted(list_of_songs, key=Song.getSize, reverse=False)
    for i in range(len(list_of_songs)):
        if (totalSize + list_of_songs[i].getSize()) <= max_size:
            playlist.append(list_of_songs[i].getName())
            totalSize += list_of_songs[i].getSize()
    return playlist


# test

songs = [('Roar', 4.4, 4.0), ('Sail',3.5, 7.7), ('Timber', 5.1, 6.9), ('Wannabe', 2.7, 1.2)]
max_size = 12.2

print(song_playlist(songs, max_size)) # output: ['Roar', 'Wannabe', 'Timber']

songs = [('Roar', 4.4, 4.0), ('Sail', 3.5, 7.7), ('Timber', 5.1, 6.9), ('Wannabe', 2.7, 1.2)]
max_size = 11

print(song_playlist(songs, max_size)) # output: ['Roar', 'Wannabe']