from typing import List
import numpy as np
EMPTY_SYMBOL = "_"

class Boardgame:
    def __init__(self, board_h:int, board_w:int):
        #boardgame is a 2d numpy array        
        self.board_h = board_h
        self.board_w = board_w
        self.board = np.zeros((board_h, board_w), dtype=str)
        self.board.fill(EMPTY_SYMBOL)                   
        self.units_in_play = [object]        
    
    def print_board(self):
        print(self.board) 
        print("\n")   

    def get_unit_by_xy(self, x:int, y:int) -> object:
        for unit in self.units_in_play:
            try:
                if unit.x == x and unit.y == y:
                    return unit
            except AttributeError:
                pass
        return None

    def add_unit(self, new_unit:object):
        self.units_in_play.append(new_unit)
        self.board[new_unit.y, new_unit.x] = new_unit.symbol

    def remove_unit(self, unit_to_remove:object):
        self.board[unit_to_remove.y, unit_to_remove.x] = EMPTY_SYMBOL
        pass  

    def xy_is_empty(self, x:int, y:int) -> bool:
        #returns true if the xy is empty
        if self.board[y, x] == EMPTY_SYMBOL:
            return True
        else:
            print("move failed: there is a unit in this position")
            return False
    
    def enough_move_points(self, unit:object, x:int, y:int) -> bool:
        #returns true if the unit has enough move points to move to xy
        total_moves = abs(x - unit.x) + abs(y - unit.y)
        if total_moves <= unit.move_points:
            return True
        else:
            print("move failed: Not enough move points")
            return False
            
    
    def xy_is_valid(self, x:int, y:int) -> bool:
        #returns true if xy is inside the board
        if x < self.board_w and x >= 0 and y < self.board_h and y >= 0:
            return True
        else:
            return False

    def move_allowed(self, unit_to_move:object,new_x:int,new_y:int) -> bool:
        #returns true if the move is allowed verifying if xy is empty and if unit can move there
        if self.xy_is_valid(new_x,new_y) and self.xy_is_empty(new_x,new_y) and self.enough_move_points(unit_to_move, new_x, new_y):
            return True
        else:
            return False
            print ("move failed: Not enough move points")
        
    def move_unit(self, unit_to_move:object, new_x:int, new_y:int):
        #move unit to new xy
        if self.move_allowed(unit_to_move, new_x, new_y):
            self.board[unit_to_move.y, unit_to_move.x] = EMPTY_SYMBOL
            unit_to_move.x = new_x
            unit_to_move.y = new_y
            self.board[unit_to_move.y, unit_to_move.x] = unit_to_move.symbol
        
    