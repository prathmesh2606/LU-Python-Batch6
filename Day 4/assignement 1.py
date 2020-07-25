# -*- coding: utf-8 -*-
"""
Created on Sat Jul 25 09:27:03 2020

@author: Prathmesh
"""


user_str = input("Enter the String: ").lower()
message  = input("occarance of which substring you want to search?: ").lower()

for i in range(len(user_str)):
    if user_str.startswith(message,i):
        print(message ,"-->",i)