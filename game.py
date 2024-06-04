class BowlingGame:
    def __init__(self) -> None:
        self.total_score = 0
        self.frames = [None for i in range(10)]

    def roll(self, pins = 0):
        if not 0 <= pins <= 10:
            raise ValueError('invalid amount of pins')
        elif self.total_score + pins > 10:
            raise ValueError('frame roll can\'t exceed 10')
        self.total_score += pins
        self.frames[0] = (self.frames[0] + pins) if self.frames[0] else pins
7