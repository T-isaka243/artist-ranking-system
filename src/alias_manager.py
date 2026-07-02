import json


class AliasManager:

    def __init__(
        self,
        artist_alias_file="config/artist_alias.json",
        song_alias_file="data/alias/song_alias.json",
    ):

        with open(artist_alias_file, encoding="utf-8") as f:
            self.artist_alias = json.load(f)

        with open(song_alias_file, encoding="utf-8") as f:
            self.song_alias = json.load(f)

    def normalize_artist(self, artist: str) -> str:
        """アーティスト名を統一"""
        return self.artist_alias.get(artist, artist)

    def normalize_song(self, artist: str, song: str) -> str:
        """曲名を統一（アーティストごと）"""

        artist_songs = self.song_alias.get(artist, {})
        return artist_songs.get(song, song)