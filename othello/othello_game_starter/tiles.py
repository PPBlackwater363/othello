from tile import Tile


class Tiles:
    def __init__(self, Board_size, Board_num):
        self.Board_size = Board_size
        self.Board_num = Board_num
        self.cell = self.Board_size // self.Board_num
        self.lst = [[None for x in range(self.Board_num)]
                    for y in range(self.Board_num)]
        
        # draw the first 4 tiles
        for i in range(self.Board_num//2 - 1, self.Board_num//2 + 1):
            for j in range(self.Board_num//2 - 1, self.Board_num//2 + 1):
                if (i + j) % 2 == 0:
                    self.lst[i][j] = Tile(self.Board_size, self.Board_num, 255)
                else:
                    self.lst[i][j] = Tile(self.Board_size, self.Board_num, 0)

    def display(self):
        for i in range(self.Board_num):
            for j in range(self.Board_num):
                if self.lst[i][j] is None:
                    continue
                x = i * self.cell + self.cell / 2
                y = j * self.cell + self.cell / 2
                self.lst[i][j].display(x, y)
