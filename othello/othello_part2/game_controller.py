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

        self.time_duration = 1500
        # input users' name
        self.user_name = False
        # direction vectors to determine legal moves
        self.x_Vec = [0, 1, -1, 0, 1, -1, 1, -1]
        self.y_Vec = [1, 0, 0, -1, 1, -1, -1, 1]

        self.score_file = 'scores.txt'
        # self.start_time = 0

    def black_move(self, x, y):
        """
        black move
        """
        ind_x = x // self.cell
        ind_y = y // self.cell
        
        # decide if black's move is legal
        if (ind_y, ind_x) in self.legal_list(0):
            self.black_num += 1
            # computer's turn
            self.black_turn = False
            next_tile = Tile(self.Board_size, self.NUM, 0)
            self.tile_lst[ind_y][ind_x] = next_tile
            self.flip_color(255, ind_y, ind_x)

    def next_turn(self):
        """
        find the one that can flip the max numbers of black tiles
        """
        legal_list = self.legal_list(255)
        max_flip = 0
        next_turn_x = None
        next_turn_y = None
        
        for point in legal_list:
            current_flip = legal_list[point]
            if current_flip > max_flip:
                max_flip = current_flip
                next_turn_y = point[0]
                next_turn_x = point[1]
                
        return next_turn_y, next_turn_x

    def white_move(self):
        """
        white move
        """
        ind_y, ind_x = self.next_turn()

        if ind_y is not None and ind_x is not None:
            self.black_turn = True
            self.white_num += 1
            next_tile = Tile(self.Board_size, self.NUM, 255)
            self.tile_lst[ind_y][ind_x] = next_tile
            self.flip_color(0, ind_y, ind_x)

    def flip_color(self, color, ind_y, ind_x):
        """
        decide when to flip and how to flip tiles as many as possible
        """
        self.start_time = millis()
        if color == 255:
            flip_color_num = 255
            final_color_num = 0
        else:
            flip_color_num = 0
            final_color_num = 255

        flip_count = 0

        for i in range(len(self.x_Vec)):
            potential_to_flip = []
            
            new_y = ind_y + self.y_Vec[i]
            new_x = ind_x + self.x_Vec[i]

            if not self.inBoard(new_y, new_x) or \
                self.tile_lst[new_y][new_x] is None or \
                    self.tile_lst[new_y][new_x].color_num == final_color_num:
                continue

            while self.inBoard(new_y, new_x) and \
                self.tile_lst[new_y][new_x] is not None and \
                    self.tile_lst[new_y][new_x].color_num == flip_color_num:
                potential_to_flip.append((new_y, new_x))
                new_x += self.x_Vec[i]
                new_y += self.y_Vec[i]

            if self.inBoard(new_y, new_x) and \
                self.tile_lst[new_y][new_x] is not None and \
                    self.tile_lst[new_y][new_x].color_num == final_color_num:
                for point in potential_to_flip:
                    self.tile_lst[point[0]][point[1]].color_num = final_color_num

                flip_count += len(potential_to_flip)

        if final_color_num == 0:
            self.black_num += flip_count
            self.white_num -= flip_count
        else:
            self.white_num += flip_count
            self.black_num -= flip_count

        return flip_count

    def update(self):
        """
        check if the game is over and decide who wins
        """
        if (self.black_num + self.white_num == self.NUM ** 2) or \
            (len(self.legal_list(0)) == 0 and \
                len(self.legal_list(255)) == 0):
            fill(255, 0, 0)
            textSize(50)
            res = ''

            if self.black_num > self.white_num:
                res = 'You win' + '\n' + 'Your Score:'+ str(self.black_num)
            elif self.black_num < self.white_num:
                res = 'Computer win' + '\n' + 'Computer\'s Score:'+ str(self.white_num)
            else:
                res = 'TIE'
            text(res, (self.Board_size - textWidth(res))// 2, self.Board_size / 2)

            if not self.user_name and millis() - self.start_time > self.time_duration:
                self.user_name = True
                name = self.input_name('Enter your name:')
                self.output_score(name, self.black_num)

        if self.black_turn is True and \
            len(self.legal_list(0)) == 0 and \
                len(self.legal_list(255)) != 0:
            self.black_turn = False

        if self.black_turn is False and \
            len(self.legal_list(255)) == 0 and \
                len(self.legal_list(0)) != 0:
            self.black_turn = True

    def inBoard(self, x, y):
        """
        check if the tile is in the board
        """
        if x >= 0 and x < self.NUM and y >= 0 and y < self.NUM:
            return True
        else:
            return False

    def legal_list(self, color_num):
        """
        Use a dictionary to record legal moves and flip counts
        """
        legal_list = {}
        
        if color_num == 0:
            flip_color_num = 255
            final_color_num = 0
        else:
            flip_color_num = 0
            final_color_num = 255

        for y in range(self.NUM):
            for x in range(self.NUM):
                if self.tile_lst[y][x] is not None:
                    continue
                for i in range(len(self.x_Vec)):
                    potential_to_flip = []

                    new_y = y + self.y_Vec[i]
                    new_x = x + self.x_Vec[i]
                    
                    # Non-flip
                    if not self.inBoard(new_y, new_x) or \
                        self.tile_lst[new_y][new_x] is None or \
                        self.tile_lst[new_y][new_x].color_num == final_color_num:
                        continue
                
                    while self.inBoard(new_x, new_y) and \
                            self.tile_lst[new_y][new_x] is not None and \
                            self.tile_lst[new_y][new_x].color_num == flip_color_num:
                        potential_to_flip.append((new_y, new_x))
                        new_x += self.x_Vec[i]
                        new_y += self.y_Vec[i]

                    if self.inBoard(new_y, new_x) and \
                            self.tile_lst[new_y][new_x] is not None and \
                            self.tile_lst[new_y][new_x].color_num == final_color_num:
                        if (y, x) in legal_list:
                            legal_list[(y, x)] += len(potential_to_flip)
                        else:
                            legal_list[(y, x)] = len(potential_to_flip)

        return legal_list

    def input_name(self, message=''):
        """
        input users' name after game is over
        """
        from javax.swing import JOptionPane
        return JOptionPane.showInputDialog(frame, message)

    def output_score(self, name, score):
        """
        read the socres.txt file and write in users' scores
        """
        f = open(self.score_file, 'r')
        scores = []

        for line in f:
            scores.append(line)

        new_score = name + ' ' + str(score) + '\n'
        if len(scores) == 0:
            scores.append(new_score)
        else:
            if score > int(scores[0].split()[-1]):
                scores.insert(0, new_score)
            else:
                scores.append(new_score)

        f = open(self.score_file, 'w')
        for line in scores:
            f.write(line)
