from src.parser import RankingParser


def test_parser():

    text = """
2026-07-01

1,SMD,Shake My Days
2,TFL,TIME FOR LOVE
3,籾井優里奈,透明な水
"""

    parser = RankingParser()

    announce_date, rankings = parser.parse(text)

    assert announce_date == "2026-07-01"

    assert len(rankings) == 3

    assert rankings[0].rank == 1
    assert rankings[0].artist == "SMD"
    assert rankings[0].song == "Shake My Days"

    assert rankings[2].artist == "籾井優里奈"