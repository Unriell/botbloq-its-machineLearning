# -*- coding: utf-8 -*-
"""
Created on Mon Mar 14 12:05:59 2016

@author: FranciscoP.Romero
"""
import codecs
def load_data_usa(path):
        
    f = codecs.open(path, "r", "utf-8")
    states = []
    count = 0
    for line in f:
        row = line.split("\t")
        row.pop(0)
        if row != []:
        	states.append(list(map(float, row)))
        count += 1

    return states