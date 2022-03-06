# -*- coding: utf-8 -*-
"""
Created on Fri Mar  4 10:27:31 2022

@author: iernst
"""
def convert(hours,minutes):
    if hours<0 or minutes<0:
        return print("Input error!")
    else:        
        hours= hours*60*60
        minutes=minutes*60
        return(hours+minutes)

