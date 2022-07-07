# -*- coding: utf-8 -*-
"""
Created on Wed May 18 20:24:14 2022

@author: pruszynskam
"""

import sys

def tower_game(n, events):
    ret = [0 for _ in range(0,len(events))]
    per_placeh = dict()
    per_placeh = dict.fromkeys([el[0] for el in events], 0)
    golden_places = dict()
    hmaxstart = 0 
    punkty = 0
    

    for i in range(n):
        spada_mx = list()
        if events[i][1]<4:
            for j in range(events[i][1]):
                key = events[i][0]+j
                try:
                    per_placeh[key]=per_placeh[key]+1
                except KeyError:
                    per_placeh[key]=1
                spada_mx.append(per_placeh[key])
            hmax_iter = max(spada_mx)    
            for k in range(events[i][1]):
                key = events[i][0]+k
                per_placeh[key]= hmax_iter

        else:         
            new_k = events[i][0]
            per_placeh[new_k] += events[i][1]
            hmax_iter = max(per_placeh.values())
        
        if hmax_iter > hmaxstart:
            hmaxstart = hmax_iter
            punkty = punkty + 1
            
        
        if events[i][1]==1:
            if not hmax_iter in golden_places:
                golden_places[hmax_iter] = events[i][1]
                punkty = punkty + 1

        ret[i] = punkty
    return ret

reader = inputReader = open("input.txt","r")
 
# Reads the input
astr = reader.readline().split()
n = int(astr[0])
events = [[int(val) for val in reader.readline().split()] for _ in range(0,n)]

# Calls your function
ret = tower_game(n, events)

# Writes the output
for i in range(0,n):
    print(ret[i])
