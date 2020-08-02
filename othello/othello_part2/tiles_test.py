from tiles import Tiles
from tile import Tile

Board_size = 400
Board_num = 4


def test_constructor():
    t = Tiles(Board_size, Board_num)

    for i in range(t.Board_num//2 - 1, t.Board_num//2 + 1):
        for j in range(t.Board_num//2 - 1, t.Board_num//2 + 1):
            if (i + j) % 2 == 0:
                t.lst[i][j] = Tile(t.Board_size, t.Board_num, 255).color_num
            else:
                t.lst[i][j] = Tile(t.Board_size, t.Board_num, 0).color_num

    assert t.Board_size == 400
    assert t.Board_num == 4
    assert t.cell == 100
    assert t.lst == [[None, None, None, None], [None, 255, 0, None],
                     [None, 0, 255, None], [None, None, None, None]]
