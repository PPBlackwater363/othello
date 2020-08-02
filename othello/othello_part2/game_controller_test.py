from tile import Tile
from tiles import Tiles
from game_controller import Gamecontroller

WIDTH = 800
HEIGHT = 800
Board_size = 800
Board_num = 8
NUM = 8


def test_constructor():
    tiles = Tiles(Board_size, Board_num)
    gc = Gamecontroller(Board_size, NUM, tiles)
    assert gc.cell == 100
    assert gc.black_turn is True
    assert gc.black_num == 2
    assert gc.white_num == 2
    assert gc.user_name is False
    assert gc.time_duration == 1500
    assert gc.x_Vec == [0, 1, -1, 0, 1, -1, 1, -1]
    assert gc.y_Vec == [0, 1, -1, 0, 1, -1, 1, -1]
    assert gc.score_file == 'scores.txt'


def test_black_move():
    # since the millis() function can't be run in python, so disable the 
    # statement self.start_time = millis() (line 78 in the game_controller.py) 
    # first before run py test.
    tiles = Tiles(Board_size, Board_num)
    gc = Gamecontroller(Board_size, NUM, tiles)
    gc.black_move(250, 350)
    # print(gc.tile_lst[3][2].color_num)
    assert gc.tile_lst[3][2].color_num == 0
    assert gc.black_num == 3


def test_next_turn():
    # since the millis() function can't be run in python, so disable the
    # statement self.start_time = millis() (line 78 in the game_controller.py)
    # first before run py test.
    tiles = Tiles(Board_size, Board_num)
    gc = Gamecontroller(Board_size, NUM, tiles)
    y, x = gc.next_turn()
    assert y == 2
    assert x == 4


def test_white_move():
    # since the millis() function can't be run in python, so disable the
    # statement self.start_time = millis() (line 78 in the game_controller.py)
    # first before run py test.
    tiles = Tiles(Board_size, Board_num)
    gc = Gamecontroller(Board_size, NUM, tiles)
    gc.white_move()
    # print(gc.tile_lst[2][4].color_num)
    assert gc.tile_lst[2][4].color_num == 255


def test_flip_color():
    # since the millis() function can't be run in python, so disable the
    # statement self.start_time = millis() (line 78 in the game_controller.py)
    # first before run py test.
    tiles = Tiles(Board_size, Board_num)
    gc = Gamecontroller(Board_size, NUM, tiles)
    gc.flip_color(0, 50, 20)
    assert gc.tile_lst[3][3].color_num == 255


def test_inBoard():
    tiles = Tiles(Board_size, Board_num)
    gc = Gamecontroller(Board_size, NUM, tiles)
    assert gc.inBoard(1, 7) is True
    assert gc.inBoard(1, 8) is False
    assert gc.inBoard(-1, 7) is False
    assert gc.inBoard(4, 5) is True


def test_legal_list():
    tiles = Tiles(Board_size, Board_num)
    gc = Gamecontroller(Board_size, NUM, tiles)
    black_move_list = gc.legal_list(255)
    white_move_list = gc.legal_list(0)
    assert black_move_list == {(2, 4): 1, (3, 5): 1, (4, 2): 1, (5, 3): 1}
    assert white_move_list == {(2, 3): 1, (3, 2): 1, (4, 5): 1, (5, 4): 1}
