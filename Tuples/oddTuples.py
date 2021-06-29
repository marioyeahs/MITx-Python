# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

def oddTuples(aTup):
    '''
    aTup: a tuple
    
    returns: tuple, every other element of aTup. 
    '''
    # Your Code Here
    new = ()
    index=0
    while index < len(aTup):
        new = new +(aTup[index],)
        index+=2
    print (new)
    return new

oddTuples((14, 1, 7, 8, 12, 2, 10, 12))