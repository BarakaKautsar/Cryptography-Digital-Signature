import random
import sys
import hashlib
import math

if sys.version_info < (3, 6):
    import sha3

string = "Hello"
encoded_str = string.encode()
obj_sha3_256 = hashlib.sha3_256(encoded_str)
 
# print in hexadecimal
print("\nSHA3-256 Hash: ", obj_sha3_256.hexdigest())
hash_text = obj_sha3_256.hexdigest()

p = int(input("Masukkan nilai p: "))
q = int(input("Masukkan nilai q: "))

n = p*q
phi = (p-1)*(q-1)

def is_prime(num):
    if num <= 1 :
        return False
    
    for i in range (2, int(num**0.5)+1):
        if num % i == 0 :
            return False
   
    return True

def generate_public_key(phi, n):
    e = random.randrange(1, phi)
    while greatest_common_divisor(e, phi) != 1:
        e = random.randrange(1, phi)
    
    return (e,n)

def generate_private_key(phi,pubkey):
    e, n = pubkey
    k = 1
    d = (1 + (k*phi))/e
    while (d % 1 != 0.0) :
        d = (1 + (k*phi))/e
        k = k + 1
    
    return (int(d),n)
        
def greatest_common_divisor(a, b):
    while b != 0 :
        temp = a
        a = b
        b = temp % b
    return a

def encrypt_digest(prikey, plaintext):
    # key, n = prikey
    
    # ciphertext = []
    # key, n = prikey
    # for char in plaintext:
    #     ciphertext.append((ord(char)**key) % n)

    # hex_sign = f''
    # for char in ciphertext:
    #     hex_sign = hex_sign + hex(char)#[2:]
    # print(ciphertext)
    # return (hex_sign)
    return None

def decrypt_digest(pubkey, ciphertext):
    # plaintext = ""
    # key, n = pubkey
    
    # for char in ciphertext:
    #     plaintext += (chr((char**key)%n))
    # return (plaintext)
    return None

pubkey = generate_public_key(phi, n)
prikey = generate_private_key(phi, pubkey)
print("is p prime: " + str(is_prime(p)))
print("is q prime: " + str(is_prime(q)))
print("n: " + str(n))
print("phi: " + str(phi))
print("public key: " + str(pubkey))
print("private key: " + str(prikey))

sign = encrypt_digest(prikey, hash_text)
print(sign)
print(decrypt_digest(pubkey,sign))