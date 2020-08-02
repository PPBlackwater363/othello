from tile import Tile
from tiles import Tiles


class Gamecontroller:

    def __init__(self, Board_size, NUM, tiles):
        self.Board_size = Board_size
        self.NUM = NUM
        self.cell = self.Board_size // self.NUM
        self.tile_lst = tiles.lst
        self.black_turn = True
        # there are already two black tiles and 2 white tiles
        self.black_num = 2
        self.white_num = 2

    def black_move(self, x, y):
        ind_x = x // self.cell
        ind_y = y // self.cell

        if self.tile_lst[ind_x][ind_y] is None:
            self.black_num += 1
            new_tile = Tile(self.Board_size, self.NUM, 0)
            self.tile_lst[ind_x][ind_y] = new_tile
            self.black_turn = False

    def white_move(self, x, y):
        ind_x = x // self.cell
        ind_y = y // self.cell

        if self.tile_lst[ind_x][ind_y] is None:
            self.white_num += 1
            new_tile = Tile(self.Board_size, self.NUM, 255)
            self.tile_lst[ind_x][ind_y] = new_tile
            self.black_turn = True

    def update(self):
        if self.black_num + self.white_num == self.NUM ** 2:
            fill(255, 0, 0)
            textSize(100)
            if self.black_num > self.white_num:
                text("Black Wins", self.Board_size/2 - 75, self.Board_size//2 + 25)
            elif self.black_num < self.white_num:
                text("White Wins", self.Board_size/2 - 75, self.Board_size//2 + 25)
            else:
                text("TIE", self.Board_size//2 - 75, self.Board_size//2 + 25)
