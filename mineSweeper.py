import random


class MineSweeper:

    def __init__(self,sizeX,sizeY,mineCount):
        self.sizeX = sizeX
        self.sizeY = sizeY
        self.mineCount = mineCount
        self.board = [['SafeCovered'] * sizeY for i in range(sizeX)]
        for i in range(mineCount):
            self.board[random.randint(0,sizeX-1)][random.randint(0,sizeY-1)]='MineCovered'
    def testSpace(self,x,y):
        if (self.board[x-1][y-1]=='SafeCovered'):
            self.board[x-1][y-1]='Cleared'

    def printBoard(self):
        print(self.board)



