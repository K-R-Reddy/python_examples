# -*- coding: utf-8 -*-
"""
Created on Tue Dec  3 23:03:16 2024

@author: dell
"""

def checkNum(num):
    iterations=1
    print(num)
    while(num!=1):
        if(num%2==0):
            num=int(num/2)
            print(num)
            iterations+=1
        else:
            num=(num*3)+1
            print(num)
            iterations+=1
    print("-------------------------------------------------------------")
    print(num,iterations)