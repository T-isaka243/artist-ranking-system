import json
from pathlib import Path

from database import DatabaseManager


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

    print()
    print("System initialized successfully.")


if __name__ == "__main__":
    main()