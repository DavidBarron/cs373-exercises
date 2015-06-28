#!/usr/bin/env python3

# ---------------
# Prime Generator
# ---------------

import types
from types import GeneratorType
from math import sqrt, ceil

def first_five_primes () :
    yield 2
    yield 3
    yield 5
    yield 7
    yield 11

def isPrime (i) :
    if (i == 2 or i % 2) :
        for j in range(3, int(sqrt(i))+1, 2) :
            if i%j == 0 :
                return False
        return True
    else :  # even is never prime
        return False

class FirstPrimes :
    class It :
        def __init__ (self,i) :
            assert i >= 0
            self.p = 2   # first prime is 2
            self.c = i   # counter of primes we need to output

        def __iter__ (self) :
            return self

        def __next__ (self) :
            if self.c <= 0 :
                raise StopIteration
            else :
                ret = self.p   # make copy to return
                self.c -= 1
                self.p += 1
                while not isPrime(self.p) :   # find next prime
                    self.p += 1
                return ret 

    def __init__ (self,i) :
        assert i >= 0
        self.i = i

    def __iter__ (self) :
        return FirstPrimes.It(self.i)

class RangePrimes :
    class It :
        def __init__ (self,i,j) :
            self.f = i  # beginning of primes we may output
            self.l = j  # end of primes we may ouput

        def __iter__ (self) :
            return self

        def __next__ (self) :
            if self.f > self.l :
                raise StopIteration
            else :
                while self.f <= self.l :
                    if isPrime(self.f) :
                        ret = self.f
                        self.f += 1
                        return ret
                    self.f +=1
                raise StopIteration

    def __init__ (self, i, j) :
        self.i = i
        self.j = j

    def __iter__ (self) :
        return RangePrimes.It(self.i, self.j)



