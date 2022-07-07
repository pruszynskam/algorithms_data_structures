# -*- coding: utf-8 -*-
"""
Created on Sun Jun 12 21:39:42 2022

@author: pruszynskam
"""

import numpy as np


def best_influencer(n, m, s, links, inf_vals):
    
    ret = [-1 for _ in range(s)]
    INF = 1000000000

    delta = [ [INF] * n for v in range(n)]

    for (s,t,c) in links:
        delta[s][t] =  min(delta[s][t], c)
            
    for v in range(n):
        delta[v][v] = 0
        
    for k in range(n):
        for i in range(n):
            for j in range(n):
                delta[i][j] = min(delta[i][j], delta[i][k] + delta[k][j])
    
    for n in range(n):
        delta[n].pop(n)

    ret = [ 0 for v in range(len(inf_vals))]

    for h in range(len(inf_vals)):
        maxi=0
        for u in range(n+1):
            v = (np.subtract(np.array(inf_vals[h][u]),np.array(delta[u])))
            p = sum(v[v>0])
            if p > maxi:
                ret[h]=u
                maxi=p
    
    return ret


reader = inputReader = open("input1.txt","r")
 
# Reads the input
astr = reader.readline().split()
n=int(astr[0])
m=int(astr[1])
s=int(astr[2])
reader.readline()
links = [[int(val) for val in reader.readline().split()] for _ in range(m)]
reader.readline()
inf_vals = [[int(val) for val in reader.readline().split()] for _ in range(s)]

# Calls your function
ret = best_influencer(n, m, s, links, inf_vals)

# Writes the output
for i in range(s):
    print(ret[i])
    
