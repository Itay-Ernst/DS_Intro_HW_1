# -*- coding: utf-8 -*-
"""
Created on Thu Mar  3 17:55:33 2022

@author: iernst
"""

def my_func(x1,x2,x3):
    
    if type(x1) is not float or type(x2) is not float or type(x3) is not float:
        return print("Error: parameters should be float")
    sum1=x1+x2+x3
    if sum1==0 :
        return print("Not a number - denominator equals zero")
    return(float(sum1*(x2+x3)*x3/sum1))  