import random


class MineSweeper:

    def __init__(self,sizeX,sizeY,mineCount):
        self.sizeX = sizeX
        self.sizeY = sizeY
        self.mineCount = mineCount
        self.board = [['SafeCovered'] * sizeX for i in range(sizeY)]
        i=0
        while(i < mineCount):
            x = random.randint(0,sizeX-1)
            y = random.randint(0,sizeY-1)
            if (self.board[y][x]=="SafeCovered"):
                self.board[y][x]='MineCovered'
                i+=1

    def testSpace(self,x,y):
        if (0 <= x < self.sizeX and
                0 <= y < self.sizeY):
            if (self.board[y][x]=='SafeCovered'):
                m = self.countMines(x,y)
                self.board[y][x] = m
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
            if self.board[y][x] == 'MineCovered':
                self.board[y][x] = 'Boom'
                return True

    def countMines(self,x,y):
        count = self.isMine(x - 1, y - 1) + self.isMine(x - 1, y) + self.isMine(x - 1, y + 1) + \
              self.isMine(x + 1, y - 1) + self.isMine(x + 1, y) + self.isMine(x + 1, y + 1) + \
              self.isMine(x, y - 1) + self.isMine(x, y + 1)
        return count



    def isMine(self,x,y):
        if(0 <= x < self.sizeX and
                0 <= y < self.sizeY):
            if self.board[y][x] == 'MineCovered':
                return 1
        return 0




    def printBoard(self):
        #Print board mapping stored values to Characters for display
        mapCharacters = {
            'SafeCovered' : "#",
            'Cleared' : " ",
            'MineCovered' : "#",
            'Boom' : "!"
        }
        output = ""
        for row in self.board :
            for cell in row :
                output += mapCharacters.get(cell, str(cell)) #Unmapped Characters are number of mines
            output += "\n"
        return output

    def checkWin(self):
        # Check for only mines left
        # Return False if there is more work to be done
        for row in self.board :
            for cell in row :
                if cell == 'SafeCovered' :
                    return False
        return True


