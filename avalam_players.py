#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May  8 15:33:33 2018

@author: LouisMaestrati
"""

import numpy as np
from avalam_game import Board

"""
Random and Human-ineracting players for the game of TicTacToe.
Author: Evgeny Tyurin, github.com/evg-tyurin
Date: Jan 5, 2018.
Based on the OthelloPlayers by Surag Nair.
"""

  #Fonction auxiliaire représentation en base b:
def repr_baseb(n,b):
       c = []
       while n!= 0:
         c.append(n%b)
         n = n//b
       
       while len(c)!=4:
           c.append(0)
       c.reverse()
       return c


class RandomPlayer():
    def __init__(self, game):
        self.game = game

    def play(self, board):
        a = np.random.randint(self.game.getActionSize())
        valids = self.game.getValidMoves(board, 1)
        while valids[a]!=1:
            a = np.random.randint(self.game.getActionSize())
        return a


class HumanAvalamPlayer():
    def __init__(self, game):
        self.game = game

    def play(self, board):
        # display(board)
        valid = self.game.getValidMoves(board, 1)
        for i in range(len(valid)):
            if valid[i]:
                R= repr_baseb(i,9)
                print(self.game.n*R[0]+R[1],self.game.n*R[2]+R[3]) #int(i%self.game.n), je passe par une écriture intermédiaire pour le split
        while True: 
            # Python 3.x
            a = input()
            # Python 2.x 
            # a = raw_input()

            x,y = [int(x) for x in a.split(' ')]
            a=int(x/self.game.n)
            b=int(x%self.game.n)
            c=int(y/self.game.n)
            d= int(y%self.game.n)
            
            a = self.game.n**(3)*a+self.game.n**(2)*b+self.game.n*c+d if x!= -1 else self.game.n ** 4
            if valid[a]:
                break
            else:
                print('Invalid')

        return a
    
class GreedyAvalamPlayer():
    def __init__(self, game):
        self.game = game

    def play(self, board):
        valids = self.game.getValidMoves(board, 1)
        candidates = []
        for a in range(self.game.getActionSize()):
            if valids[a]==0:
                continue
            nextBoard, _ = self.game.getNextState(board, 1, a)
            score = self.game.getScore(nextBoard, 1)
            candidates += [(-score, a)]
        candidates.sort()
        return candidates[0][1]