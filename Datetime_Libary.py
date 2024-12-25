# -*- coding: utf-8 -*-
"""
Created on Sun Sep 29 15:04:49 2024

@author: dell
"""
import datetime
print("Today : ",datetime.date.today())
print("Today year : ",datetime.date.today().strftime("%Y"))
print("Today Month : ",datetime.date.today().strftime("%B"))
print("Today date : ",datetime.date.today().strftime("%d"))
print("Today day : ",datetime.date.today().strftime("%A"))
print("Day in year : ",datetime.date.today().strftime("%j"))
print("Week no of the Year : ",datetime.date.today().strftime("%W"))
print("Week day in the week",datetime.date.today().strftime("%w"))
print("Date and Time : ",datetime.datetime.now())
