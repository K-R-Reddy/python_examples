# -*- coding: utf-8 -*-
"""
Created on Sun Sep 29 14:08:53 2024

@author: dell
"""

import string
import random
symbols=[]
symbols=list(string.ascii_letters)
card1=[0]*8
card2=[0]*8
pos1=random.randint(0,7)
pos2=random.randint(0,7)
samesymbol=random.choice(symbols)
symbols.remove(samesymbol)
if(pos1==pos2):
    card2[pos1]=samesymbol
    card1[pos1]=samesymbol
else:
    card1[pos1]=samesymbol
    card2[pos2]=samesymbol
    card1[pos2]=random.choice(symbols)
    symbols.remove(card1[pos2])
    card2[pos1]=random.choice(symbols)
    symbols.remove(card2[pos1])
i=0
while(i<8):
    if(i!=pos1 and i!=pos2):
        alphabet1=random.choice(symbols)
        symbols.remove(alphabet1)
        alphabet2=random.choice(symbols)
        symbols.remove(alphabet2)
        card1[i]=alphabet1
        card2[i]=alphabet2
    i=i+1
print(card1)
print(card2)
ch=input("Spot the Similar Symbol : ")
if(ch==samesymbol):
    print("You Win")
else:
    print("You Lose")
