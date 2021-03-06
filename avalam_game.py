#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr  3 10:25:41 2018

@author: LouisMaestrati
"""
from __future__ import print_function
import sys
sys.path.append('..')
from Game import Game
from avalam_logic import Board
import numpy as np

"""
Game class implementation for the game of TicTacToe.
Based on the OthelloGame then getGameEnded() was adapted to new rules.
Author: Evgeny Tyurin, github.com/evg-tyurin
Date: Jan 5, 2018.
Based on the OthelloGame by Surag Nair.
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
    




class AvalamGame(Game):
    def __init__(self, n=8):
        self.n = n

    def getInitBoard(self):
        # return initial board (numpy board)
        b = Board(self.n)
        return np.array(b.pieces)

    def getBoardSize(self):
        # (a,b) tuple
        return (self.n, self.n)

    def getActionSize(self):
        # return number of actions
        return  self.n*self.n*self.n*self.n+1#len(self.get_legal_moves())#self.n*self.n + 1

    
    
    
    
    
    def getNextState(self, board, player, action):
        # if player takes action on board, return next (board,player)
        # action must be a valid move
        if action == self.n*self.n*self.n*self.n:
            return (board, -player)
        b = Board(self.n)
        b.pieces = np.copy(board)
        R=repr_baseb(action,9)
        move = (R[0],R[1],R[2],R[3])#(int(action/self.n), action%self.n)
        b.execute_move(move, player) #!!!!
        return (b.pieces, -player) #!!!!!

    def getValidMoves(self, board, player):
        # return a fixed size binary vector
        valids = [0]*self.getActionSize()
        b = Board(self.n)
        b.pieces = np.copy(board)
        legalMoves =  b.get_legal_moves(player)
        if len(legalMoves)==0:
            valids[-1]=1
            return np.array(valids)
        for x, y,z,a in legalMoves:
            valids[self.n**(3)*x+self.n**(2)*y+self.n*z+a]=1
        return np.array(valids)

    def getGameEnded(self, board, player):
        # return 0 if not ended, 1 if player 1 won, -1 if player 1 lost
        # player = 1
        b = Board(self.n)
        b.pieces = np.copy(board)

        if b.is_win(player):
            return 1
        if b.is_win(-player):
            return -1
        if b.has_legal_moves():
            return 0
        # draw has a very little value 
        #print(b.pieces)
        return 1e-4

    def getCanonicalForm(self, board, player):
        # return state if player==1, else return -state if player==-1
        return player*board

    def getSymmetries(self, board, pi): # on ne peut pas garder rotation et fliplr sauf rot de 180
        # mirror, rotational
        assert(len(pi) == self.n**4+1)  # 1 for pass #4--)2
        pi_board = np.reshape(pi[:-1], (self.n, self.n))
        l = []

        for i in range(1, 5):
            for j in [True, False]:
                newB = np.rot90(board, i)
                newPi = np.rot90(pi_board, i)
                if j:
                    newB = np.fliplr(newB)
                    newPi = np.fliplr(newPi)
                l += [(newB, list(newPi.ravel()) + [pi[-1]])]
        return l

    def stringRepresentation(self, board):
        # 8x8 numpy array (canonical board)
        return board.tostring()

def display(board):
    n = board.shape[0]

    print("   ", end="")
    for y in range(n):
        print (y,"", end="")
    print("")
    print("  ", end="")
    for _ in range(n):
        print ("-", end="-")
    print("--")
    for y in range(n):
        print(y, "|",end="")    # print the row #
        for x in range(n):
            piece = board[y][x]    # get the piece to print
            #if piece == -1: print("X ",end="")
            #elif piece == 1: print("O ",end="")
            if x<n:
                print(str(piece)+ " ", end="")
                
            else:
                if x==n:
                    print("-",end="")
                else:
                    print("- ",end="")
        print("|")

    print("  ", end="")
    for _ in range(n):
        print ("-", end="-")
    print("--")
    
    
    
    #TEST PERSO
     
    tab= [[ 0,  0,  3,  0,  0,  0,  0,  0,  0],
 [ 0  ,0 ,-5  ,0 ,-2  ,0  ,0  ,0  ,0],
 [ 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0],
 [ 0  ,0  ,0  ,0  ,0  ,0  ,0  ,0  ,0],
 [ 0  ,5 ,-5,  0,  0,  5,  0, -3,  4],
 [ 2  ,0  ,0  ,0  ,0  ,0  ,0  ,0  ,0],
 [ 0 , 0 , 0 , 0 , 5 , 0 ,-4 , 0,  0],
 [ 0  ,0  ,0  ,0  ,0 ,-5  ,0  ,0  ,0],
 [ 0  ,0 , 0,  0,  0,  0,  0,  0,  0]]
    
