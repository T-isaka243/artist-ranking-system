import json
import sys

from exporter import Exporter
from alias_manager import AliasManager
from database import DatabaseManager
from parser import RankingParser
from scorer import Scorer

def load_settings():
    with open("config/settings.json", encoding="utf-8") as f:
        return json.load(f)


def main():

    settings = load_settings()

    print("=" * 40)
    print(settings["project_name"])
    print(f"Version {settings['version']}")
    print("=" * 40)

    db = DatabaseManager(settings["database"])
    db.initialize()

    print("Database Ready!")

    parser = RankingParser()

    alias = AliasManager()
    
    if len(sys.argv) < 2:
        print("使い方:")
        print("python src/main.py data/input/2026-01-04.txt")
        db.close()
        return

    input_file = sys.argv[1]

    with open(input_file, encoding="utf-8") as f:
        text = f.read()

    parser.load_text(text)

    announce_date = parser.get_announce_date()

    if db.exists_announce_date(announce_date):
        print(f"{announce_date} は既に登録されています。")
    else:

        entries = parser.get_entries()

        for entry in entries:

            score = Scorer.calculate(entry.rank)
            artist = alias.normalize_artist(entry.artist)
            song = alias.normalize_song(artist, entry.song)
        
            db.insert_weekly_ranking(
                announce_date=announce_date,
                rank=entry.rank,
                artist=artist,
                song=song,
                rank_point=score.rank_point,
                appearance_point=score.appearance_point,
                total_point=score.total_point,
            )

        print("Import Complete!")

    print("\n=== Weekly Rankings ===\n")

    rankings = db.get_weekly_rankings()

    current_date = ""

    for announce_date, rank, artist, song in rankings:

        if announce_date != current_date:
            current_date = announce_date
            print(current_date)

        print(f"{rank:>2}  {artist:<10} {song}")

    print("\n=== Artist Ranking ===\n")

    artist_rankings = db.get_artist_ranking()

    for index, (artist, total_points, appearances, best_rank) in enumerate(artist_rankings, start=1):
        print(
            f"{index:>2}. "
            f"{artist:<15} "
            f"{total_points:>5} pt   "
            f"{appearances:>2}回   "
            f"最高順位 {best_rank}"
        )
    db.close()

    exporter = Exporter()
    exporter.export_artist_ranking(artist_rankings)

if __name__ == "__main__":
    main()