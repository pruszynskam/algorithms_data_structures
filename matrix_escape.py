# -*- coding: utf-8 -*-
"""
Created on Fri Apr 29 11:02:46 2022

@author: pruszynskam
"""

import numpy as np


def escape_matrix(p, n, m, a, b):
    #matrix
    pos = 0
    baza = [-1 for _ in range(0,n*m)]
    for i in range(0,n):
        for j in range(0,m):
            baza[pos] = (a[i]*b[j])%p
            pos+=1
    M = np.array(baza).reshape(n,m)
    ret = [-1 for _ in range(0,m)]

    M[0,0] = 0
    for k in range(1,n):
        M[k,0] = M[k,0]+M[k-1,0]
    for l in range(1,m):
        M[0,l] = 2*M[0,l]+M[0,l-1]

    for o in range(1,n):
        for p in range(1,m):
            if (M[o-1,p] + M[o,p]) > (M[o,p-1]+2*M[o,p]):
                M[o,p] = 2*M[o,p]+M[o,p-1]
            else:
                M[o,p] = M[o,p]+M[o-1,p]

    ret = M[n-1,0:m]
    return ret
 
reader = inputReader = open("input0.txt","r")
 
# Reads the input
astr = reader.readline().split()
p=int(astr[0])
n=int(astr[1])
m=int(astr[2])
a = [int(val) for val in reader.readline().split()]
b = [int(val) for val in reader.readline().split()]

# Calls your function
ret = escape_matrix(p, n, m, a, b)

# Writes the output
for i in range(0,m):
    print(ret[i])
