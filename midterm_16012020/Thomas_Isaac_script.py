# -*- coding: utf-8 -*-
"""
Created on Thu Jan 16 10:39:07 2020

@author: Thomas
"""
#import input_data

def Matrix(filename):
    File = open(filename, "r")
    ListofValues = []
    #ran out of time to fix
    #rowandcol = readline().split()
    #print(rowandcol)
    for line in File:
        listt = line.split()
        ListofValues.append(listt)
    del ListofValues[0]
    #print(List1)
    #Quick fix for not getting readline done in time to get matrix working
    row = "ARNDCQEGHILKMFPSTWYV"
    col = "ARNDCQEGHILKMFPSTWYV"
    Dictionary = {}
    for i in range (len(row)):
        columnNumber = 0
        for value in ListofValues[i]:
            Pair = row[i] + col[columnNumber]
            RPair = Pair[::-1]
            Dictionary[Pair] = value
            Dictionary[RPair] = value
            columnNumber = columnNumber + 1
    return Dictionary
    #print(Dictionary)
    
    
#Enter the file path
Dict = Matrix("")

#From input_data
align1 = ['GSAQVKGHGKKVADALTNAVAHVDDMPNALSALSDLHAHKL','GNPKVKAHGKKVLGAFSDGLAHLDNLKGTFATLSELHCDKL']
align2 = ['GSAQVKGHGKKVADALTNAVAHV---D--DMPNALSALSDLHAHKL','NNPELQAHAGKVFKLVYEAAIQLQVTGVVVTDATLKNLGSVHVSKG']
align3 = ['GSAQVKGHGKKVADALTNAVAHVDDMPNALSALS----DLHAHKL','GSGYLVGDSLTFVDL--LVAQHTADLLAANAALLDEFPQFKAHQE']

alignments = [align1, align2, align3]

def Scoring (listalign, Dictionary):
    for i in range(len(listalign)):
        Seq1 = listalign[i][0]
        Seq2 = listalign[i][1]
        Total_score = 0
        for i in range(len(Seq1)):
            current_score = 0
            Pair = Seq1[i] + Seq2[i]
            if "-" in Pair:
                Total_score = Total_score -2
            else:
                current_score = Dictionary[Pair]
                Total_score = Total_score + float(current_score)
        print(Seq1)
        print(Seq2)
        print (Total_score)
    
Scoring(alignments, Dict)