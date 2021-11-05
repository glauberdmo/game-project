from .boardgame import *

class _Unit:
    def __init__(self,boardgame:object,initial_x:int,initial_y:int,life:int,strenght:int,range:int,move_points:int=3):
        self.x = initial_x
        self.y = initial_y
        self.life = life
        self.strenght = strenght
        self.range = range
        self.alive = True
        self.move_points = move_points

        #every unit has a boardgame
        self.board = boardgame

        #add unit to boardgame
        self.board.add_unit(self)

    def __repr__(self):
        return f"_Unit(x={self.x},y={self.y},life={self.life},strenght={self.strenght},range={self.range})"

    def _execute_attack(self,enemy):
            enemy.life -= self.strenght
            print(f"{self.__repr__()} attacked {enemy.__repr__()} with {self.strenght} of damage")
            if enemy.life <= 0:
                enemy.alive = False
                print(f"{enemy.__repr__()} is dead")
            else:
                print(f"{enemy.__repr__()} has {enemy.life} life left")
            if enemy.life <= 0:
                enemy.alive = False
                enemy.life = 0                
                print(f"{enemy.__class__.__name__} is dead")
            else:
                print(f"{enemy.__class__.__name__} is alive with {enemy.life} life")

    def attack(self,defending_unit:object):
        #attacking_unit attacks defending_unit
        if self._valid_attack(defending_unit):
            self._execute_attack(defending_unit)
        else:
            print("attack failed: Not enough move points")
        if not defending_unit.alive:
            self.board.remove_unit(defending_unit)

    def move(self, new_x:int, new_y:int):
        #move unit to new xy
        if self.move_allowed(new_x, new_y):
            self.board[self.y, self.x] = EMPTY_SYMBOL
            self.x = new_x
            self.y = new_y
            self.board[self.y, self.x] = self.symbol   

    def move_allowed(self,new_x:int,new_y:int) -> bool:
        #returns true if the move is allowed verifying if xy is empty and if unit can move there
        if self.board.xy_is_valid(new_x,new_y) and self.board.xy_is_empty(new_x,new_y) and self.enough_move_points(new_x, new_y):
            return True
        else:
            return False

    def _valid_attack(self, defending_unit:object) -> bool:
        return self.board.xy_is_valid(defending_unit.x,defending_unit.y) and self.board.xy_is_valid(self.x,self.y) and self.enough_move_points(defending_unit.x, defending_unit.y)

    
    def enough_move_points(self, x:int, y:int) -> bool:
        #returns true if the unit has enough move points to move to xy
        total_moves = abs(x - self.x) + abs(y - self.y)
        if total_moves <= self.move_points:
            return True
        else:
            print("move failed: Not enough move points")
            return False   



