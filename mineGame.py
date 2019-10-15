import mineSweeper

if __name__ == '__main__' :
    game = mineSweeper.MineSweeper(10,11,3)
    while (1) :
        x=input("Pick X")
        y=input("Pick Y")
        game.testSpace(int(x),int(y))
        game.printBoard()

