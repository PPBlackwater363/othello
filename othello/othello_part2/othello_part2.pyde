from board import Board
from tile import Tile
from tiles import Tiles
from game_controller import Gamecontroller

WIDTH = 800
HEIGHT = 800
NUM = 8
StrokeWeight = 2
black = 0
white = 255
time_duration = 1500
last_time = millis()

board = Board(WIDTH, HEIGHT, NUM, StrokeWeight)
tile = Tile(WIDTH, NUM, black)
tiles = Tiles(WIDTH, NUM)
gc = Gamecontroller(WIDTH, NUM, tiles)


def setup():
    size(WIDTH,HEIGHT)
    

def draw():
    global time_duration, last_time
    # RGB nums for background color
    background(0,130,0)
    board.display()
    tiles.display()
    if not gc.black_turn:
        if millis() - last_time > time_duration:
            gc.white_move()
    gc.update()



def mousePressed():
    global last_time
    if gc.black_turn:
        last_time = millis()
        gc.black_move(mouseY, mouseX)
        global last_time

    

        


    

    
    
    
    
    
