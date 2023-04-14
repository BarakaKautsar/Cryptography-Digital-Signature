#coba based on tutorial youtube

from key_generator import *
import random
from hashlib import sha3_256

def encrypt(prikey , msg):
    cipher = ""
    e, N = prikey
    for c in msg:
        m = ord(c)
        cipher += str(pow(m, e, N)) + " "

    return cipher

def decrypt(pubkey, cipher):
    msg = ""
    d, N = pubkey
    parts = cipher.split()
    for part in parts:
        if part:
            c = int(part)
            msg += chr(pow(c, d, N))

    return msg

def main():
    #generate key
    p = random_prime()
    q = random_prime()
    n, totient = initiate(p,q)
    pubkey = generate_public_key(n, totient)
    print(pubkey)
    prikey = generate_private_key(totient, pubkey)
    print(prikey)
    #print(private_key)
    #get message
    message = input("Enter message: ")
    #print(message)
    #hash message
    hashedtext = sha3_256(message.encode()).hexdigest()
    #print(hashedtext)
    #encrypt hash
    cipher = encrypt(prikey, hashedtext)
    #decrypt hash
    result = decrypt(pubkey, cipher)
    if result == True:
        print("Message is authentic")
    else:
        print("Message is not authentic")

if __name__ == "__main__":
    main()