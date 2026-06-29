import json
from pathlib import Path


def load_settings():
    config_path = Path("config/settings.json")

    with open(config_path, "r", encoding="utf-8") as f:
        return json.load(f)


def main():

    settings = load_settings()

    print("=" * 40)
    print(settings["project_name"])
    print(f'Version {settings["version"]}')
    print("=" * 40)
    print()
    print("System initialized successfully.")


if __name__ == "__main__":
    main()