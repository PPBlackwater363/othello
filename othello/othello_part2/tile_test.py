from tile import Tile

Board_size = 400
Board_num = 4
# black color
color = 0


def test_constructor():
    t = Tile(Board_size, Board_num, 0)   
    assert t.Board_num == 4
    assert t.Board_size == 400
    assert t.Clearance == 10
    assert t.color_num == 0
    assert t.Radius == 90
    