# -*- coding: utf-8 -*-
"""
Created on Wed Jul 22 22:57:27 2020

@author: Prathmesh
"""
user_input = int(input("Enter the number: "))
if user_input > 1:
    for i in range(2,user_input//2):
        if user_input%i==0:
            print(user_input,"is not a prime number")
            break
    else:
        print(user_input,"is a Prime Number")
else:
    print(user_input,"is not a prime number")
