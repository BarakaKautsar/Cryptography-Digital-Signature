#digital signature using SHA256 primitive

#coba with pow

import hashlib
import random
from key_generator import *

def rsa_encrypt_sign (hashedtext, private_key):
    d, n = private_key
    temp = (pow(hashedtext, d, n))
    cipher = hex(temp)[2:]
    return cipher

def rsa_decrypt_verify (cipher, public_key, plaintext):
    
    e, n = public_key
    temp = (pow, plaintext, e, n)
    #cipher_temp = hex(temp)[2:]
    print(temp)
    if cipher == temp:
        return True
    else:
        return False
    
def encrypt(public_key, message):
    key, n = public_key
    cipher_text = [pow(ord(char), key, n) for char in message]
    return cipher_text

def decrypt(private_key, cipher_text):
    key, n = private_key
    plain_text = [chr(pow(char, key, n)) for char in cipher_text]
    return ''.join(plain_text)
    
def sha256 (text):
    return int(hashlib.sha256(text.encode()).hexdigest(), 16)

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
    hashedtext = sha256(message)
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

