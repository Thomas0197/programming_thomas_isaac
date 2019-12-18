#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 18 13:21:25 2019

@author: thomas
"""

def complreve():
    s = 0
    n = 0
    L1 = raw_input("enter 1st seq: ")
    L2 = raw_input("enter 1st seq: ")
   # L1 = ["A","T","G","C"]
    #L2 = ["A","T","G","T"]
    if len(L1)>len(L2):
        a = len(L2)
    else:
        a = len(L1)
        
    for letter in range(a):
        if L1[letter] == L2[letter]:
            s +=1
        elif L1[letter] != L2[letter]:
            n -= 1
    
    print "score: ", (s+n)

complreve()