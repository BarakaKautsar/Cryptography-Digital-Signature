#RSA Encrypt
import math
from typing import List
import random

def encrypt(n, key, plain):
    plainblock = []
    cipherblock = []
    plaintext = plain.encode()
    size_block = math.ceil(math.log2(n)/8)
    for i in range (0, len(plaintext), size_block-1) :
        plainblock.append(b'\x00' + plaintext[i:size_block-1+i])
    #print(plainblock)
    #kasih padding ke block terakhir
    if len(plainblock[-1]) != size_block :
        while (len(plainblock[-1]) != size_block):
            plainblock[-1] = ((size_block - len(plainblock[-1])) * b'\x00') + plainblock[-1] 
    #print(plainblock)
    pad_len = size_block - len(plainblock[-1])

    #ubah ke integer
    for i in range (len(plainblock)):
        plainblock[i] = int.from_bytes(plainblock[i], byteorder='big', signed=False)
    #print(plainblock)
    #rumus enkripsi
    for char in plainblock:
        cipherblock.append((char**key)%n)
    #print(cipherblock)

    #ubah ke byte lagi
    for i in range (len(cipherblock)):
        cipherblock[i] = cipherblock[i].to_bytes(length=size_block, byteorder='big', signed=False)
    #print(cipherblock)

    ciphertext = b''
    for i in range (len(cipherblock)):
        ciphertext += cipherblock[i]
    #print(ciphertext)

    ciphertext += pad_len.to_bytes(length = 4, byteorder='big', signed=False)
    #print(ciphertext)

    #print(ciphertext.hex())
    return ciphertext.hex()

import random
import math

def rsa_encrypt(n, key, plain):
    plaintext = plain.encode()
    size_block = math.ceil(math.log2(n)/8)
    
    # Divide plaintext into blocks
    plainblock = []
    for i in range(0, len(plaintext), size_block - 1):
        plainblock.append(b'\x00' + plaintext[i:size_block - 1 + i])
        
    # Pad the last block if necessary
    if len(plainblock[-1]) != size_block:
        while (len(plainblock[-1]) != size_block):
            plainblock[-1] = ((size_block - len(plainblock[-1])) * b'\x00') + plainblock[-1]
            
    # Convert blocks to integers
    for i in range(len(plainblock)):
        plainblock[i] = int.from_bytes(plainblock[i], byteorder='big', signed=False)
    
    # Encrypt each block using RSA encryption algorithm
    cipherblock = []
    for char in plainblock:
        cipherblock.append(pow(char, key, n))
        
    # Convert encrypted blocks back to bytes
    for i in range(len(cipherblock)):
        cipherblock[i] = cipherblock[i].to_bytes(length=size_block, byteorder='big', signed=False)
    
    # Concatenate encrypted blocks and padding length
    ciphertext = b''
    for i in range(len(cipherblock)):
        ciphertext += cipherblock[i]
    pad_len = size_block - len(plainblock[-1])
    ciphertext += pad_len.to_bytes(length=4, byteorder='big', signed=False)
    
    return ciphertext.hex()


def str_to_byte(s: str) -> bytes:
    return bytes.fromhex(s)

def rsa_decrypt(ciphertext, private_key):
    n, d = private_key
    size_block = math.ceil(math.log2(n) / 8)
    
    cipher_bytes = bytes.fromhex(ciphertext)
    cipher_len = len(cipher_bytes)
    
    # Extract padding length
    pad_len = int.from_bytes(cipher_bytes[cipher_len-4:], byteorder='big')
    cipher_blocks = cipher_bytes[:cipher_len-4]
    
    # Convert cipher blocks to integers
    cipher_ints = []
    for i in range(0, len(cipher_blocks), size_block):
        cipher_ints.append(int.from_bytes(cipher_blocks[i:i+size_block], byteorder='big'))
        
    # Decrypt each cipher integer
    plain_ints = []
    for c in cipher_ints:
        p = pow(c, d, n)
        plain_ints.append(p)
        
    # Convert plain integers to bytes
    plain_blocks = []
    for p in plain_ints:
        plain_blocks.append(p.to_bytes(size_block-1, byteorder='big'))
        
    # Concatenate plain blocks and remove padding
    plain_bytes = b''.join(plain_blocks)
    plain_text = plain_bytes[:-pad_len].decode()
    
    return plain_text

    



def main():
    #input
    key = 213
    plain = "8ca66ee6b2fe4bb928a8e3cd2f508de4119c0895f22e011117e22cf9b13de7ef"
    n = 3337683129804612734618476261231
    cipher = rsa_encrypt(n, key, plain)
    print(cipher)
    print(rsa_decrypt(cipher, (n, key)))
    

if __name__ == "__main__":
    main()