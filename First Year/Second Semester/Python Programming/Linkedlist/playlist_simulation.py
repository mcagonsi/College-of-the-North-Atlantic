from dataclasses import dataclass


@dataclass
class Song:
    title:object
    nextSong = None
    previousSong = None

    def __repr__(self):
        return self.title


@dataclass
class Playlist:
    song = None
    playlist = ['Despacito','All of Me', 'Perfect', 'Stay with me', 'Silence', 'Someone You Loved']
    def __repr__(self):
        if self.song is not None:
            previousSong = self.song.previousSong
            next = self.song.nextSong
            return f'Previous Song: {previousSong} Current Song: {self.song.title} Next Song: {next}'
        else:
            input('Playlist is empty. Press Enter to Load Playlist from device...')
            return self._loadPlaylist()
    def _loadPlaylist(self):
        self.song = Song(self.playlist.pop())
        currentSong = self.song
        currentSong.nextSong = Song(self.playlist.pop())
        next = currentSong.nextSong
        previous = currentSong.previousSong
        return f'Previous Song: {str(previous)} Current Song: {self.song.title} Next Song: {next}'

    def nextSong(self):
        self.song.previousSong = self.song
        self.song = self.song.nextSong
        self.song.nextSong = Song(self.playlist.pop())


pl = Playlist()

print(pl)

pl.nextSong()

print(pl)




