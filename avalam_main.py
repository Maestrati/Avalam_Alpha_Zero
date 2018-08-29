#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr  6 17:55:10 2018

@author: LouisMaestrati
"""
from Coach import Coach
from avalam_game import AvalamGame as Game
from NNET import NNetWrapper as nn
from utils import *

args = dotdict({
    'numIters': 80, # à la place de 1000,80
    'numEps': 70,   # 100
    'tempThreshold': 15,
    'updateThreshold': 0.6,
    'maxlenOfQueue': 200000,
    'numMCTSSims': 25,    # J4AI CHANGE LES EPOQUES
    'arenaCompare': 40, #40
    'cpuct': 1,

    'checkpoint': './temp/',
    'load_model': False,
    'load_folder_file': ('temp','best.pth.tar'), #/dev/models/8x100x50
    'numItersForTrainExamplesHistory': 20,
    'limiteurdescente': 30,
    'limited':False

})

if __name__=="__main__":
    g = Game(9)
    nnet = nn(g)

    if args.load_model:
        nnet.load_checkpoint(args.load_folder_file[0], args.load_folder_file[1])

    c = Coach(g, nnet, args)
    if args.load_model:
        print("Load trainExamples from file")
        c.loadTrainExamples()
    c.learn()
