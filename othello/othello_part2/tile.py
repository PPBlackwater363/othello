class Tile:

    def __init__(self, Board_size, Board_num, color):
        self.Board_size = Board_size
        self.Board_num = Board_num
        self.Clearance = 10
        self.Radius = Board_size // Board_num - self.Clearance
        self.color_num = color

    def display(self, x, y):
        if self.color_num == 0:
            fill(0)
        if self.color_num == 255:
            fill(255)
        # if self.color == 125:
        #     fill(125)
        ellipse(x, y, self.Radius, self.Radius)
        
