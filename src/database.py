from pathlib import Path
import sqlite3


class DatabaseManager:
    """SQLiteデータベース管理"""

    def __init__(self, db_path: str):
        self.db_path = Path(db_path)
        self.connection = None

        # DBフォルダ作成
        self.db_path.parent.mkdir(parents=True, exist_ok=True)

    def connect(self):
        """データベースへ接続"""
        if self.connection is None:
            self.connection = sqlite3.connect(self.db_path)

    def close(self):
        """接続を閉じる"""
        if self.connection:
            self.connection.close()
            self.connection = None

    def initialize(self):
        """必要なテーブルを作成"""

        self.connect()
        cursor = self.connection.cursor()

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS weekly_ranking(
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
        CREATE TABLE IF NOT EXISTS artist_alias(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            original_name TEXT UNIQUE,
            alias_name TEXT
        )
        """)

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS song_alias(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            artist TEXT,
            original_title TEXT,
            alias_title TEXT
        )
        """)

        self.connection.commit()

    def insert_weekly_ranking(
        self,
        announce_date: str,
        rank: int,
        artist: str,
        song: str,
        rank_point: int,
        appearance_point: int,
        total_point: int,
    ):
        """週間ランキングを登録"""

        self.connect()
        cursor = self.connection.cursor()

        cursor.execute(
            """
            INSERT INTO weekly_ranking(
                announce_date,
                rank,
                artist,
                song,
                rank_point,
                appearance_point,
                total_point
            )
            VALUES (?, ?, ?, ?, ?, ?, ?)
            """,
            (
                announce_date,
                rank,
                artist,
                song,
                rank_point,
                appearance_point,
                total_point,
            ),
        )

        self.connection.commit()

    def get_weekly_rankings(self):
        """週間ランキング一覧を取得"""

        self.connect()

        cursor = self.connection.cursor()

        cursor.execute("""
            SELECT
                announce_date,
                rank,
                artist,
                song
            FROM weekly_ranking
            ORDER BY announce_date, rank
        """)

        return cursor.fetchall()

    def exists_announce_date(self, announce_date: str):
        """指定日のランキングが登録済みか確認"""

        self.connect()

        cursor = self.connection.cursor()

        cursor.execute(
            """
            SELECT COUNT(*)
            FROM weekly_ranking
            WHERE announce_date = ?
            """,
            (announce_date,),
        )

        return cursor.fetchone()[0] > 0