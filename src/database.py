from pathlib import Path
import sqlite3


class DatabaseManager:
    """SQLiteデータベース管理クラス"""

    def __init__(self, db_path: str):
        self.db_path = Path(db_path)

        # databaseフォルダが無ければ作成
        self.db_path.parent.mkdir(parents=True, exist_ok=True)

    def initialize(self):

        conn = sqlite3.connect(self.db_path)

        cursor = conn.cursor()

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS weekly_ranking (

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            announce_date TEXT NOT NULL,

            rank INTEGER NOT NULL,

            artist TEXT NOT NULL,

            song TEXT NOT NULL,

            rank_point INTEGER NOT NULL,

            appearance_point INTEGER NOT NULL,

            total_point INTEGER NOT NULL

        )
        """)

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS artist_alias (

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            original_name TEXT UNIQUE,

            alias_name TEXT

        )
        """)

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS song_alias (

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            artist TEXT,

            original_title TEXT,

            alias_title TEXT

        )
        """)

        conn.commit()

        conn.close()

        print("Database initialized successfully.")