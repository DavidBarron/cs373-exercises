#!/usr/bin/env python3

# ---------------
# Collatz Generator
# ---------------

from types import GeneratorType

def collatz_cycle (i) :
    yield i
    while(i != 1) :
        if(i%2) :  # odd
            i = i*3+1
            yield i
        else :     #even
            i = int(i//2)
            yield i
