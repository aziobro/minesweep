import random


class MineSweeper:

    def __init__(self,sizeX,sizeY,mineCount):
        self.sizeX = sizeX
        self.sizeY = sizeY
        self.mineCount = mineCount
        self.board = [['SafeCovered'] * sizeY for i in range(sizeX)]
        i=0
        while(i < mineCount):
            x = random.randint(0,sizeX-1)
            y = random.randint(0,sizeY-1)
            if (self.board[x][y]=="SafeCovered"):
                self.board[x][y]='MineCovered'
                i+=1

    def testSpace(self,x,y):
        if (0 <= x < self.sizeX and
                0 <= y < self.sizeY):
            if (self.board[x][y]=='SafeCovered'):
                m = self.countMines(x,y)
                self.board[x][y] = m
                if (m==0):
                    self.testSpace(x - 1,y - 1)
                    self.testSpace(x - 1,y)
                    self.testSpace(x - 1,y + 1)
                    self.testSpace(x + 1,y - 1)
                    self.testSpace(x + 1,y )
                    self.testSpace(x + 1,y + 1)
                    self.testSpace(x, y - 1)
                    self.testSpace(x, y + 1)

                return False
            if self.board[x][y] == 'MineCovered':
                self.board[x][y] = 'Boom'
                return True

    def countMines(self,x,y):
        #adjust for zero offset
        #x-=1
        #y-=1
        count = self.isMine(x - 1, y - 1) + self.isMine(x - 1, y) + self.isMine(x - 1, y + 1) + \
              self.isMine(x + 1, y - 1) + self.isMine(x + 1, y) + self.isMine(x + 1, y + 1) + \
              self.isMine(x, y - 1) + self.isMine(x, y + 1)
        return count



    def isMine(self,x,y):
        if(x>=0 and x<self.sizeX and
           y>=0 and y<self.sizeY):
            if self.board[x][y] == 'MineCovered':
                return 1
        return 0




    def printBoard(self):
        # print(self.board)
        mapCharacters = {
            'SafeCovered' : "#",
            'Cleared' : " ",
            'MineCovered' : "#",
            'Boom' : "!"
        }
        output = ""
        for row in self.board :
            for cell in row :
                output += mapCharacters.get(cell, str(cell))
            output += "\n"
        return output



