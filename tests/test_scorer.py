from src.scorer import Scorer


def test_rank_1():

    score = Scorer.calculate(1)

    assert score.rank_point == 20
    assert score.appearance_point == 1
    assert score.total_point == 21


def test_rank_20():

    score = Scorer.calculate(20)

    assert score.rank_point == 1
    assert score.appearance_point == 1
    assert score.total_point == 2