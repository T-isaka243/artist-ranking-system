import json


class AliasManager:

    def __init__(self, alias_file="config/artist_alias.json"):

        with open(alias_file, encoding="utf-8") as f:
            self.alias = json.load(f)

    def normalize_artist(self, artist: str) -> str:
        """アーティスト名を統一する"""

        return self.alias.get(artist, artist)