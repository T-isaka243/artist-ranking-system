# Artist Ranking System (ARS)
## Architecture Design
Version: 0.1.0

---

# 1. システム概要

ARS（Artist Ranking System）は、毎週発表されるランキングデータを管理し、

- SQLiteへ保存
- 月間・半期・年間集計
- Excel出力
- HTML出力

を行うランキング管理システムである。

---

# 2. ディレクトリ構成

artist-ranking-system/

├── config/
│   └── settings.json
│
├── data/
│   ├── database/
│   └── output/
│
├── docs/
│   ├── architecture.md
│   └── roadmap.md
│
├── src/
│   ├── main.py
│   ├── database.py
│   ├── parser.py
│   ├── scorer.py
│   ├── aggregator.py
│   ├── excel_export.py
│   └── html_export.py
│
├── tests/
│
├── requirements.txt
└── README.md

---

# 3. データの流れ

Weekly Ranking

↓

Parser

↓

SQLite Database

↓

Aggregator

↓

Excel Export

↓

HTML Export

---

# 4. モジュール

## parser.py

ランキング入力解析

---

## database.py

SQLite管理

---

## scorer.py

順位点計算

登場点計算

---

## aggregator.py

月間集計

半期集計

年間集計

---

## excel_export.py

Excel生成

---

## html_export.py

HTML生成

---

# 5. 今後追加予定

・Artist Alias

・Song Alias

・Import Wizard

・Web Dashboard

・検索機能

・ランキング比較