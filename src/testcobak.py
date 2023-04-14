from key_generator import *

def rsa_encrypt_sign (hashedtext, private_key):
    print("hashed text : " + str(hashedtext))
    d, n = private_key
    temp = (pow(hashedtext, d, n))
    print("hasil pow : " + str(temp))
    cipher = hex(temp)[2:]
    print("hasil hex : " + str(cipher))
    print("hasil kembali dec : " + str(int(cipher,16)))
    return cipher

def rsa_decrypt_verify (cipher, public_key):
    print(cipher)
    e, n = public_key
    #convert cipher to int
    #for x in str(cipher).split('ox')[1:]:
    cipher = int(cipher, 16)
    temp = (pow(cipher, e, n))
    print(temp)

    return temp

def main() :
        #generate key
    p = random_prime()
    q = random_prime()
    n, totient = initiate(p,q)
    pubkey = generate_public_key(n, totient)
    #print(pubkey)
    prikey = generate_private_key(totient, pubkey)
    #print(hashedtext)
    #encrypt hash
    cipher = rsa_encrypt_sign(3512, prikey)
    #decrypt hash
    decrypted = rsa_decrypt_verify(cipher, pubkey)
    print(decrypted)
    #compare hash
    #if (decrypted == hashedtex):
        #print("Hash is verified")
    #else:
        #print("Hash is not verified")

if __name__ == "__main__":
    main()
