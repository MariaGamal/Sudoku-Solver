import numpy as np
import random

class Sudoko:
    def __init__(self):
        self.board = None # Random numbers initialization Use opencv or prettytable or strings
        self.difficulty = None # User choses game difficulty from checkbox

    def createBoard(self):
        self.board = np.zeros((9,9), dtype = int)
        if self.difficulty == "Easy":
            n = random.randint(4*9, 5*9)
        elif self.difficulty == "Medium":
            n = random.randint(3*9, 4*9)
        else:
            n = random.randint(2*9, 3*9)

    def newMove(self):
        '''
        Takes input number from user
        checks for validation
        exits when complete
        :return:
        '''
        pass

    def printBoard(self):
        '''

        :return:
        Updated board every loop
        '''
        pass
