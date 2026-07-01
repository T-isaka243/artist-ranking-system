from src.parser import RankingParser


def test_parser():

    sample = """
2026-01-04
1,SMD,Shake My Days
2,TFL,TIME FOR LOVE
3,籾井優里奈,透明な水
"""

    parser = RankingParser()

    parser.load_text(sample)

    assert parser.get_announce_date() == "2026-01-04"

    entries = parser.get_entries()

    assert len(entries) == 3

    assert entries[0].rank == 1
    assert entries[0].artist == "SMD"
    assert entries[0].song == "Shake My Days"

    assert entries[2].artist == "籾井優里奈"
    assert entries[2].song == "透明な水"