from dataclasses import dataclass


@dataclass
class RankingEntry:
    rank: int
    artist: str
    song: str


class RankingParser:

    def __init__(self):
        self.text = ""

    def load_text(self, text: str):
        self.text = text.strip()

    def get_lines(self):
        return [
            line.strip()
            for line in self.text.splitlines()
            if line.strip()
        ]

    def get_announce_date(self):
        return self.get_lines()[0]

    def get_entries(self):

        entries = []

        for line in self.get_lines()[1:]:

            rank, artist, song = line.split(",", maxsplit=2)

            entries.append(
                RankingEntry(
                    rank=int(rank),
                    artist=artist.strip(),
                    song=song.strip()
                )
            )

        return entries