from parser import RankingParser

sample = """
2026-01-04
1,SMD,Shake My Days
2,TFL,TIME FOR LOVE
3,籾井優里奈,透明な水
"""

parser = RankingParser()

parser.load_text(sample)

print(parser.get_lines())