from dataclasses import dataclass


@dataclass
class RankingEntry:
    rank: int
    artist: str
    song: str


class RankingParser:

    def parse(self, text: str):

        lines = [line.strip() for line in text.splitlines() if line.strip()]

        announce_date = lines[0]

        rankings = []

        for line in lines[1:]:

            rank, artist, song = line.split(",", maxsplit=2)

            rankings.append(
                RankingEntry(
                    rank=int(rank),
                    artist=artist.strip(),
                    song=song.strip()
                )
            )

        return announce_date, rankings