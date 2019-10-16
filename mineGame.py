import mineSweeper

if __name__ == '__main__' :
    game = mineSweeper.MineSweeper(10,11,6)
    while (1) :
        x=input("Pick X")
        y=input("Pick Y")
        if (game.testSpace(int(x)-1,int(y)-1)):
            # BOOM
            print("BOOM")
            exit()
        print(game.printBoard())

