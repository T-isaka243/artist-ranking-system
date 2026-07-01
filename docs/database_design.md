# Database Design
Version: 0.1.0

## weekly_ranking

週間ランキングの元データを保存する。

## artist_alias

アーティスト名の表記統一を管理する。

例

- Shake My Days → SMD
- TIME FOR LOVE → TFL

## song_alias

曲名の表記統一を管理する。

同一曲判定は自動では行わず、
ユーザー確認後に登録する。

必要に応じて備考（remarks）を保持する。