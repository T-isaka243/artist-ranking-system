import csv
from pathlib import Path


class Exporter:

    def export_artist_ranking(self, rankings):

        output_dir = Path("output/csv")
        output_dir.mkdir(parents=True, exist_ok=True)

        output_file = output_dir / "artist_ranking.csv"

        with open(output_file, "w", newline="", encoding="utf-8-sig") as f:

            writer = csv.writer(f)

            writer.writerow(
                ["順位", "アーティスト", "ポイント", "登場回数", "最高順位"]
            )

            for i, row in enumerate(rankings, start=1):

                artist, point, count, best = row

                writer.writerow(
                    [
                        i,
                        artist,
                        point,
                        count,
                        best,
                    ]
                )

        print(f"CSV出力: {output_file}")