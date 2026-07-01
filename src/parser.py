class RankingParser:
    """ランキングデータを解析するクラス"""

    def __init__(self):
        pass

    def load_text(self, text: str):
        """ランキングテキストを読み込む"""
        self.text = text

    def get_lines(self):
        """行ごとのリストを返す"""
        return self.text.strip().splitlines()