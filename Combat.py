#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 11 02:25:25 2018

@author: LouisMaestrati
"""

import Arena
from MCTS import MCTS
from avalam_game import AvalamGame, display
from avalam_players import *
from NNET import NNetWrapper as NNet
from avalam_main import args
import numpy as np
from utils import *

"""
use this script to play any two agents against each other, or play manually with
any agent.
"""

g = AvalamGame(9)

# all players
rp = RandomPlayer(g).play
gp = GreedyAvalamPlayer(g).play
hp = HumanAvalamPlayer(g).play

# nnet players
#n1 = NNet(g)
#n1.load_checkpoint('./pretrained_models/othello/pytorch/','6x100x25_best.pth.tar')
#args1 = dotdict({'numMCTSSims': 50, 'cpuct':1.0})
#mcts1 = MCTS(g, n1, args1)
#n1p = lambda x: np.argmax(mcts1.getActionProb(x, temp=0))


n2 = NNet(g)
n2.load_checkpoint('temp','best.pth.tar')
args2 = dotdict({'numMCTSSims': 25, 'cpuct':1.0, 'limited':False})
mcts2 = MCTS(g, n2, args2)
n2p = lambda x: np.argmax(mcts2.getActionProb(x, temp=0)) #temp est à 0 pour prendre le meilleur choix à chaque fois

arena = Arena.Arena(n2p, rp, g, display=display)
print(arena.playGames(2, verbose=True))