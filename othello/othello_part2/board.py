from tile import Tile


class Board:

    def __init__(self, WIDTH, HEIGHT, NUM, StrokeWeight):
        self.HEIGHT = HEIGHT
        self.WIDTH = WIDTH
        self.NUM = NUM
        self.StrokeWeight = StrokeWeight

    def display(self):
        """Draw the board"""
        strokeWeight(self.StrokeWeight)
        cell = int(self.WIDTH / self.NUM)
        # draw row lines
        for i in range(1, self.NUM):
            line(0, cell * i, self.WIDTH, cell * i)
        # draw column lines
        for i in range(1, self.NUM):
            line(cell * i, 0, cell * i, self.WIDTH)
            