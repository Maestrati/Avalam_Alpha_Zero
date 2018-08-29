#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May  8 17:38:53 2018

@author: LouisMaestrati
"""

class dotdict(dict):
    def __getattr__(self, name):
        return self[name]