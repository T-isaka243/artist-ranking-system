import json

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

    sample = """
    2026-01-04
    1,SMD,Shake My Days
    2,TFL,TIME FOR LOVE
    3,籾井優里奈,透明な水
    """

    parser.load_text(sample)

    entries = parser.get_entries()

    for entry in entries:

        score = Scorer.calculate(entry.rank)

        db.insert_weekly_ranking(
            announce_date=parser.get_announce_date(),
            rank=entry.rank,
            artist=entry.artist,
            song=entry.song,
            rank_point=score.rank_point,
            appearance_point=score.appearance_point,
            total_point=score.total_point,
        )

    print("Import Complete!")

    db.close()

if __name__ == "__main__":
    main()