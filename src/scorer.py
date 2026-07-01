from dataclasses import dataclass


@dataclass
class Score:
    rank_point: int
    appearance_point: int
    total_point: int


class Scorer:

    @staticmethod
    def calculate(rank: int) -> Score:

        if not 1 <= rank <= 20:
            raise ValueError("順位は1～20位である必要があります")

        rank_point = 21 - rank
        appearance_point = 1
        total_point = rank_point + appearance_point

        return Score(
            rank_point=rank_point,
            appearance_point=appearance_point,
            total_point=total_point
        )