import random
import sys
import hashlib
import math
from pathlib import Path
from tkinter import *
import tkinter.messagebox as tkmb
import tkinter.filedialog as fd
import sys

def is_prime(num):
    if num <= 1 :
        return False
    
    for i in range (2, int(num**0.5)+1):
        if num % i == 0 :
            return False
   
    return True

def random_prime():
    num = random.randrange(1, 1000000000)
    while not(is_prime(num)):
        num = random.randrange(1, 1000000000)

    return num

def initiate(p,q):
    n = p*q
    totient = (p-1)*(q-1)
    
    return n, totient

def generate_public_key(n, totient):
    e = random.randrange(1, totient)
    while greatest_common_divisor(e, totient) != 1:
        e = random.randrange(1, totient)
    
    return (e,n)

def generate_private_key(totient,pubkey):
    e, n = pubkey
    k = 1
    d = (1 + (k*totient))/e
    while (d % 1 != 0.0) :
        d = (1 + (k*totient))/e
        k = k + 1
    
    return (int(d),n)
        
def greatest_common_divisor(a, b):
    while b != 0 :
        temp = a
        a = b
        b = temp % b
    return a

#contoh cara kerja
"""
p = random_prime()
q = random_prime()
print(q)
print(p)
n, totient = initiate(p,q)
print(n)
print(totient)
pubkey = generate_public_key(n, totient)
prikey = generate_private_key(totient, pubkey)
print("pubkey" + str(pubkey))
print("prikey" + str(prikey))
"""
