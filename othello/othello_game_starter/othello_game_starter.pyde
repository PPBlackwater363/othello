from board import Board
from tile import Tile
from tiles import Tiles
from game_controller import Gamecontroller

WIDTH = 400
HEIGHT = 400
NUM = 4
StrokeWeight = 4
black = 0
white = 255

board = Board(WIDTH, HEIGHT, NUM, StrokeWeight)
tile = Tile(WIDTH, NUM, black)
tiles = Tiles(WIDTH, NUM)
gc = Gamecontroller(WIDTH, NUM, tiles)


def setup():
    size(WIDTH,HEIGHT)
    

def draw():
    # RGB nums for background color
    background(0,102,0)
    board.display()
    tiles.display()
    gc.update()


def mousePressed():
    if gc.black_turn:
        gc.black_move(mouseX, mouseY)
    else:
        gc.white_move(mouseX, mouseY)
    

        


    

    
    
    
    
    
