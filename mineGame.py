import mineSweeper

if __name__ == '__main__' :
    game = mineSweeper.MineSweeper(10,11,2)
    while (1) :
        x=input("Pick X?")
        y=input("Pick Y?")
        if (game.testSpace(int(x)-1,int(y)-1)):
            # BOOM
            print("BOOM")
            exit(False)
        if game.checkWin():
            print(game.printBoard())
            print("You WIN!!!")
            exit(True)
        print(game.printBoard())

