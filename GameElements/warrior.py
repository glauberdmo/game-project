from .unit import _Unit
class Warrior(_Unit):
    """
        Warrior can move 4 spaces at a time, and has a range of 1
        Strength: 5
        Life: 10
    """

    def __init__(self,boardgame,initial_x:int,initial_y:int):
        life = 10
        strenght = 5
        range = 1
        movePoints = 4
        self.type = "Warrior"
        self.symbol = "W"
        super().__init__(boardgame,initial_x,initial_y,life,strenght,range,movePoints)
    
    def __repr__(self) -> str:
        return f"Warrior(x={self.x},y={self.y},life={self.life},strenght={self.strenght},range={self.range})"
                