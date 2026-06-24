class Score:
    def __init__(self, initial_score: int) -> None:
        self.score = initial_score

    def decreas(self, penalty: int = 10) -> None:
        """Decrease score by a certain penalty"""
        self.score -= penalty
        self.score = max(0, self.score)

    def get_score(self) -> int:
        """Return the current score."""
        return self.score
