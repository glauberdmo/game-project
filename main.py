from GameElements.boardgame import Boardgame
from GameElements.unit import Warrior
def main():
    currentBoardgame = Boardgame(10,10)
    
    warrior1 = Warrior(1,1)
    warrior2 = Warrior(2,3)
    currentBoardgame.add_unit(warrior1)
    currentBoardgame.add_unit(warrior2)
    currentBoardgame.print_board()
    currentBoardgame.move_unit(currentBoardgame.get_unit_by_xy(1,1),2,3)
    currentBoardgame.attack_unit(currentBoardgame.get_unit_by_xy(2,3),currentBoardgame.get_unit_by_xy(1,1))
    currentBoardgame.attack_unit(currentBoardgame.get_unit_by_xy(2,3),currentBoardgame.get_unit_by_xy(1,1))
    currentBoardgame.print_board()

main()