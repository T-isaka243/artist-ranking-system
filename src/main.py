import json

from database import DatabaseManager
from parser import RankingParser

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

    print(parser.get_lines())
    
    db.close()


if __name__ == "__main__":
    main()