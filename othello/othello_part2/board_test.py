from board import Board


def test_constructor():
    b = Board(400, 400, 4, 2)
    assert b.HEIGHT == 400
    assert b.WIDTH == 400
    assert b.NUM == 4
    assert b.StrokeWeight == 2
    