from GameElements.boardgame import Boardgame
from GameElements.unit import Warrior
def main():
    currentBoardgame = Boardgame(10,10)   
    warrior1 = Warrior(currentBoardgame,1,1)   
    warrior2 = Warrior(currentBoardgame,2,2)
    warrior1.move(2,2)
    currentBoardgame.get_unit_by_xy(1,1).attack(warrior2)
    warrior1.attack(currentBoardgame.get_unit_by_xy(2,2))
    currentBoardgame.print_board()


main()