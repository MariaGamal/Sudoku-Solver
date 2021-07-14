import numpy as np
import random

class Sudoko:
    def __init__(self):
        self.board = None # Random numbers initialization Use opencv or prettytable or strings
        self.difficulty = None # User choses game difficulty from checkbox
        self.gameon = True

    def createFullBoard(self):
        '''
        Creates full 9x9 board with correct numbering.
        
        :return:
        '''
        pass

    def randomRemove(self):
        '''
        Removes random spots from full board according to difficulty.
        Prints the board.
        
        :return:
        '''
        pass

    def makeMove(self, x,y):
        '''
        Takes input coordinates from user.
        Applies input to the board.
        
        :return:
        '''
        pass

    def validate(self):
        '''
        Validates user new input number.
        
        :return:
        '''
        pass

    def checkDone(self):
        '''
        Goes over the 9x9 board to check if the board is completed successfully.
        
        :return:
        '''
        pass


sd = Sudoko()
while sd.gameon:
    sd.createBoard()
    sd.newMove(int(input().split()))
