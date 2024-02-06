#!/usr/bin/env python3
import random

BLOCKSIZE=4
BLOCKCOUNT=4
BLOCK_SEPERATOR="-"
ORD_MIN=ord("0")
ORD_MAX=ord("z")

BLOCKSUM_MIN=BLOCKSIZE*ORD_MIN
BLOCKSUM_MAX=BLOCKSIZE*ORD_MAX

# ref https://stackoverflow.com/a/3035188 primes from n to m
def gen_primes(n, m):
    """ Input n>=6, Returns a list of primes, n <= p < m """
    n, m, correction = max(n, 2), m-m%6+6, 2-(m%6>1)
    sieve = [True] * (m//3)
    for i in range(1,int(m**0.5)//3+1):
      if sieve[i]:
        k=3*i+1|1
        sieve[      k*k//3      ::2*k] = [False] * ((m//6-k*k//6-1)//k+1)
        sieve[k*(k-2*(i&1)+4)//3::2*k] = [False] * ((m//6-k*(k-2*(i&1)+4)//6-1)//k+1)
    return list(range(n,4)) + [3*i+1|1 for i in range(max(1,n//3),m//3-correction) if sieve[i]]

def createBlock(blocksum):
    global BLOCKSIZE
    blockbase=blocksum//BLOCKSIZE
    extra=blocksum%BLOCKSIZE
    return chr(blockbase)*(BLOCKSIZE-extra)+chr(blockbase+1)*extra

def buildKey(key_sums):
    basestring=""
    for i in key_sums:
        basestring += createBlock(i) + BLOCK_SEPERATOR
    return basestring[:-1]

def genKey():
    key_sums=sorted(random.sample(gen_primes(BLOCKSUM_MIN, BLOCKSUM_MAX), BLOCKCOUNT))
    return buildKey(key_sums)

print(genKey())


# See https://stackoverflow.com/a/3590105 as reference
# Return a randomly chosen list of n positive integers between min_val and max_val summing to total.
# Each such list is equally likely to occur.
#def constrained_sum_sample_pos(n, total, min_val=0, max_val=None):
#    if max_val is None: max_val = total
#    dividers = sorted(random.sample(range(min_val, total-min_val*n), n - 1))
#    return [a - b + min_val for a, b in zip(dividers + [total-min_val*n], [min_val] + dividers)]
    
# diff = (maxval-max(lst))/4
# lst /= (max(lst)/maxval)
# 
