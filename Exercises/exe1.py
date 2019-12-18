#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 18 10:04:33 2019

@author: thomas
"""
import math
def Readsome(filepath, filepath2):
    h = 0
    k = 0
    L1 =[]
    L2 = []
    p=0 
    for line in open(filepath , "r"):
        line = line.rstrip()
        Idunno = line.split()
        if Idunno[0] == "ATOM" and Idunno[2] == "CA" and Idunno[5] != p:
            p = Idunno[5]
            k = k +1
            T1 = (Idunno[6],Idunno[7],Idunno[8])
            L1.append(T1)
            
            
    for line in open(filepath2 , "r"):
        line = line.rstrip()
        Idunno = line.split()
        if Idunno[0] == "ATOM" and Idunno[2] == "CA":
            h += 1
            T2 = (Idunno[5],Idunno[6],Idunno[7])
            L2.append(T2)
    
    x = 0    
    for i in range(len(L1)):
        #f = float((L1[i][0])) - float((L1[i][0])) + float((L1[i][1])) - float((L1[i][1]) + (L1[i][2]) - (L1[i][2])
        for j in range(3):
            co1 = float(L1[i][j])
            co2 = float(L2[i][j])
            t = co1 - co2 
            t = t**2
            x = x+t
    rmsd = math.sqrt((x/100))
            
            
    print L2
    print k
    print h
    print rmsd
    
Readsome("/home/thomas/Documents/Python2/prog2_1", "/home/thomas/Documents/Python2/programming2_1")