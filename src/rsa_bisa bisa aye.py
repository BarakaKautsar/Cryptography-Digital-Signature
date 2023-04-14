import hashlib
import random

def generate_keypair(p, q):
    n = p * q
    phi = (p-1) * (q-1)
    e = random.randrange(1, phi)
    g = gcd(e, phi)
    while g != 1:
        e = random.randrange(1, phi)
        g = gcd(e, phi)
    d = multiplicative_inverse(e, phi)
    return ((e, n), (d, n))

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def multiplicative_inverse(e, phi):
    def euclid_extended(a, b):
        if a == 0:
            return (b, 0, 1)
        else:
            g, y, x = euclid_extended(b % a, a)
            return (g, x - (b // a) * y, y)

    g, x, y = euclid_extended(e, phi)
    if g != 1:
        raise ValueError('No modular inverse exists')
    else:
        return x % phi

def sha3_256_hash(msg):
    return hashlib.sha3_256(msg.encode('utf-8')).hexdigest()

def rsa_encrypt(plaintext, public_key):
    e, n = public_key
    hashed_plaintext = sha3_256_hash(plaintext)
    print("Hashed plaintext: ", hashed_plaintext)
    plaintext_int = int(hashed_plaintext, 16)
    ciphertext_int = pow(plaintext_int, e, n)
    return ciphertext_int

def rsa_decrypt(ciphertext, private_key):
    d, n = private_key
    plaintext_int = pow(ciphertext, d, n)
    hashed_plaintext = hex(plaintext_int)[2:]
    padded_plaintext = hashed_plaintext.zfill(64)
    plaintext = hashlib.sha3_256(bytes.fromhex(padded_plaintext)).hexdigest()
    return plaintext

# Example usage:

p = 11
q = 13
public_key, private_key = generate_keypair(p, q)

plaintext = "The quick brown fox jumps over the lazy dog"
plaintext_hash = sha3_256_hash(plaintext)
ciphertext = rsa_encrypt(plaintext, public_key)
decrypted_plaintext = rsa_decrypt(ciphertext, private_key)

print("Plaintext:", plaintext)
print("Plaintext hash:", plaintext_hash)
print("Ciphertext:", ciphertext)
print("Decrypted plaintext:", decrypted_plaintext)
print("Decrypted plaintext hash:", sha3_256_hash(decrypted_plaintext))
