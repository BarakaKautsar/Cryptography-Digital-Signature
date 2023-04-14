from key_generator import *
from rsa_encrypt_module import *
from rsa_decrypt_module import *

def main():
    p = random_prime()
    q = random_prime()
    n, totient = initiate(p,q)
    pubkey = generate_public_key(n, totient)
    print(pubkey)
    prikey = generate_private_key(totient, pubkey)
    print(prikey)
    print(encryptBytes("helloworld", prikey))
    print(decryptBytes(prikey, pubkey))

if __name__ == "__main__":
    main()


