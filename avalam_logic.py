#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr  3 10:46:10 2018

@author: LouisMaestrati
"""

'''
Board class for the game of TicTacToe.
Default board size is 3x3.
Board data:
  1=white(O), -1=black(X), 0=empty
  first dim is column , 2nd is row:
     pieces[0][0] is the top left square,
     pieces[2][0] is the bottom left square,
Squares are stored and manipulated as (x,y) tuples.
Author: Evgeny Tyurin, github.com/evg-tyurin
Date: Jan 5, 2018.
Based on the board for the game of Othello by Eric P. Nichols.
'''
#pieces= board
# from bkcharts.attributes import color
class InvalidAction(Exception):

    """Raised when an invalid action is played."""

    def __init__(self, action=None):
        self.action = action

class Board():

    
     # standard avalam
    max_height = 5
    initial_board = [ [ 0,  0,  1, -1,  0,  0,  0,  0,  0],
                      [ 0,  1, -1,  1, -1,  0,  0,  0,  0],
                      [ 0, -1,  1, -1,  1, -1,  1,  0,  0],
                      [ 0,  1, -1,  1, -1,  1, -1,  1, -1],
                      [ 1, -1,  1, -1,  0, -1,  1, -1,  1],
                      [-1,  1, -1,  1, -1,  1, -1,  1,  0],
                      [ 0,  0,  1, -1,  1, -1,  1, -1,  0],
                      [ 0,  0,  0,  0, -1,  1, -1,  1,  0],
                      [ 0,  0,  0,  0,  0, -1,  1,  0,  0] ]
    # list of all 8 directions on the board, as (x,y) offsets
    __directions = [(1,1),(1,0),(1,-1),(0,-1),(-1,-1),(-1,0),(-1,1),(0,1)]

    def __init__(self, n=9,percepts=initial_board, max_height=max_height, invert=False):
        "Set up initial board configuration."
    

        self.n = n
        # Create the empty board array.
        self.pieces = percepts
        #self.m=self.pieces
        self.rows = len(self.pieces)
        self.columns = len(self.pieces[0])
        self.max_height = max_height
        
        
        #self.m = self.get_percepts(invert)  # make a copy of the percepts

    # add [][] indexer syntax to the Board
    def __getitem__(self, index): 
        return self.pieces[index]

## Fonctions auxiliaires pour get_legal_moves
    def get_towers(self):
        """Yield all towers.

        Yield the towers as triplets (i, j, h):
        i -- row number of the tower
        j -- column number of the tower
        h -- height of the tower (absolute value) and owner (sign)

        """
        for i in range(self.rows):
            for j in range(self.columns):
                if self.pieces[i][j]:
                    yield (i, j, self.pieces[i][j])

    def is_action_valid(self, action):
        """Return whether action is a valid action."""
        try:
            i1, j1, i2, j2 = action
            if i1 < 0 or j1 < 0 or i2 < 0 or j2 < 0 or \
               i1 >= self.rows or j1 >= self.columns or \
               i2 >= self.rows or j2 >= self.columns or \
               (i1 == i2 and j1 == j2) or (abs(i1-i2) > 1) or (abs(j1-j2) > 1):
                return False
            h1 = abs(self.pieces[i1][j1])
            h2 = abs(self.pieces[i2][j2])
            if h1 <= 0 or h1 >= self.max_height or h2 <= 0 or \
                    h2 >= self.max_height or h1+h2 > self.max_height:
                return False
            return True
        except (TypeError, ValueError):
            return False

    def get_tower_actions(self, i, j):
        """Yield all actions with moving tower (i,j)"""
        h = abs(self.pieces[i][j])
        if h > 0 and h < self.max_height:
            for di in (-1, 0, 1):
                for dj in (-1, 0, 1):
                    action = (i, j, i+di, j+dj)
                    if self.is_action_valid(action):
                        yield action

    def is_tower_movable(self, i, j):
        """Return wether tower (i,j) is movable"""
        for action in self.get_tower_actions(i, j):
            return True
        return False

    def get_actions(self):
        """Yield all valid actions on this board."""
        for i, j, h in self.get_towers():
            for action in self.get_tower_actions(i, j):
                yield action

#Fin de ces fonctions auxiliaires


    def get_legal_moves(self, color): #PEUT ETRE PAS: IL FAUDRA FAIRE ATTENTION DANS PLAYERS ON NE PREND PLUS LA BOARD EN APRAMETRE MAIS L ELEMENTDE LA CLASSE
        """Returns all the legal moves for the given color.
        (1 for white, -1 for black)
        @param color not used and came from previous version.        
        """
        moves = set()  # stores the legal moves.

        # Get all the empty squares (color==0)
        generateur_actions= self.get_actions()
        for m in generateur_actions:
                    moves.add(m)
        return list(moves)

    def has_legal_moves(self):
        for action in self.get_actions():
            #print(action)
            return True
        return False
    
    def is_finished(self):
        for action in self.get_actions():
            return False
        return True
    
    def get_score(self):
        """Return a score for this board.

        The score is the difference between the number of towers of each
        player. In case of ties, it is the difference between the maximal
        height towers of each player. If self.is_finished() returns True,
        this score represents the winner (<0: red, >0: yellow, 0: draw).

        """
        score = 0
        for i in range(self.rows):
            for j in range(self.columns):
                if self.pieces[i][j] < 0:
                    score -= 1
                elif self.pieces[i][j] > 0:
                    score += 1
        if score == 0:
            for i in range(self.rows):
                for j in range(self.columns):
                    if self.pieces[i][j] == -self.max_height:
                        score -= 1
                    elif self.pieces[i][j] == self.max_height:
                        score += 1
        return score
    
    def is_win(self, color):
        """Check whether the given player has collected a triplet in any direction; 
        @param color (1=white,-1=black)
        """
        
        if self.is_finished()== True:
           if (self.get_score()*color>0):
              return True
           else:
              return False
          
        else:
              return False

    def execute_move(self, action, color):
        """Perform the given move on the board; 
        color gives the color pf the piece to play (1=white,-1=black)
        """

        """Play an action if it is valid.

        An action is a 4-uple containing the row and column of the tower to
        move and the row and column of the tower to gobble. If the action is
        invalid, raise an InvalidAction exception. Return self.

        """
        #print('merde')
        #print(action)
        if not self.is_action_valid(action):
            raise InvalidAction(action)
        i1, j1, i2, j2 = action
        h1 = abs(self.pieces[i1][j1])
        h2 = abs(self.pieces[i2][j2])
        if self.pieces[i1][j1] < 0:
            self.pieces[i2][j2] = -(h1 + h2)
        else:
            self.pieces[i2][j2] = h1 + h2
        self.pieces[i1][j1] = 0
        return self