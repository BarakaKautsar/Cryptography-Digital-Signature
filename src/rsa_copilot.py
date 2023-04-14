#rsa encryption and decryption with sha3-256 hashed text but without library beside sha-3 library and basic libraries

from key_generator import *
from hashlib import sha3_256
import random

def convHextoDec(hex):
    return int(hex, 16)

def hash_sha3_256(message):
    return (sha3_256(message.encode()).hexdigest())

def rsa_encrypt_sign (hashedtext, private_key):
    #print("hashed text : " + str(hashedtext)) # hasil hash text
    d, n = private_key 
    temp = (pow(hashedtext, d, n)) # encrypt hash text
    #print("hasil enc : " + str(temp))
    cipher = hex(temp)[2:] # hasil hash di hexa
    #print("hasil hexed cipher : " + str(cipher))
    return cipher

def rsa_decrypt_verify (cipher, public_key):
    #print(cipher)
    e, n = public_key
    #convert cipher to int
    #for x in str(cipher).split('ox')[1:]:
    cipher = int(cipher, 16)
    temp = (pow(cipher, e, n))
    #print("the decrypted cipher is : ", temp)

    return temp

def main():
    #generate key
    p = random_prime()
    q = random_prime()
    n, totient = initiate(p,q)
    pubkey = generate_public_key(n, totient)
    #print(pubkey)
    prikey = generate_private_key(totient, pubkey)
    #print(prikey)
    #print(private_key)
    #get message
    message = input("Enter message: ")
    #print(message)
    #hash message
    hashedtext = convHextoDec(hash_sha3_256(message))
    #print(hashedtext)
    #encrypt hash
    cipher = rsa_encrypt_sign(hashedtext, prikey)
    #decrypt hash
    decrypted = rsa_decrypt_verify(cipher, pubkey)
    #compare hash
    if (decrypted == hashedtext):
        print("Hash is verified")
    else:
        print("Hash is not verified")

if __name__ == "__main__":
    main()