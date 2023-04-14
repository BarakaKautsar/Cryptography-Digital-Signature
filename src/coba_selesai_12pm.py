#digital signature using SHA256 primitive

#coba with pow

import hashlib
import random
from key_generator import *

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

"""
def encrypt(public_key, message):
    key, n = public_key
    cipher_text = [pow(ord(char), key, n) for char in message]
    return cipher_text

def decrypt(cipher_text, private_key):
    key, n = private_key
    plain_text = [chr(pow(char, key, n)) for char in cipher_text]
    return ''.join(plain_text)
"""    

    
def sha256 (text):
    return int(hashlib.sha256(text.encode()).hexdigest(), 16)

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
    hashedtext = sha256(message)
    #print(hashedtext)
    #encrypt hash
    cipher = rsa_encrypt_sign(hashedtext, prikey)
    #decrypt hash
    decrypted = rsa_decrypt_verify(cipher, pubkey)
    print("hasil decrypted text adalah : ", decrypted /n)
    print("hasil hashed text adalah : ", hashedtext)
    #compare hash
    if (decrypted == hashedtext):
        print("Hash is verified")
    else:
        print("Hash is not verified")

if __name__ == "__main__":
    main()