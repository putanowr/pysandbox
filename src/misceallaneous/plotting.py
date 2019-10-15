# -*- coding: utf-8 -*-
"""
Created on Fri Aug  9 15:01:00 2019

@author: putanowr
"""

import matplotlib as mp

#mp.pyplot.plot([1,2,3],[1,2,1])
#mp.pyplot.plot([1,2,3],[1,-1,1])

def ala():
    a = 23
#    print ((ala.__module__.__file__) + 'obraz')
    return # end of ala

ala()

with mp.pyplot.figure(1) as fig:
#fig = mp.pyplot.figure(1)
    mp.pyplot.plot([1,2,3],[1,-1,1])
