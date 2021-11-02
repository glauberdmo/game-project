class _Unit:
    def __init__(self,initial_x:int,initial_y:int,life:int,strenght:int,range:int,move_points:int=3):
        self.x = initial_x
        self.y = initial_y
        self.life = life
        self.strenght = strenght
        self.range = range
        self.alive = True
        self.move_points = move_points

    def move(self,x:int,y:int):
        if x+y>self.movePoints:
            print("You can't move that far")
        else:
            self.x += x
            self.y += y
    
    def __repr__(self):
        return f"_Unit(x={self.x},y={self.y},life={self.life},strenght={self.strenght},range={self.range})"
        

class Warrior(_Unit):
    """

        Warrior can move 4 spaces at a time, and has a range of 1
        Strength: 5
        Life: 10

    """

    def __init__(self,initial_x:int,initial_y:int):
        life = 10
        strenght = 5
        range = 1
        movePoints = 4
        self.type = "Warrior"
        self.symbol = "W"
        super().__init__(initial_x,initial_y,life,strenght,range,movePoints)
    
    def __repr__(self) -> str:
        return f"Warrior(x={self.x},y={self.y},life={self.life},strenght={self.strenght},range={self.range})"
                