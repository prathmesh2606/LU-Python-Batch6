# -*- coding: utf-8 -*-
"""
Created on Wed Jul 22 22:57:27 2020

@author: Prathmesh
"""
user_input = int(input("Enter the range of number:"))
n = 0
add = 0
while n<=user_input:
    add += n
    n +=1
print(add)