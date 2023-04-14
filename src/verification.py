from RSA import *


def verification(digest, signature, pubkey):
    decrypted_signature = decrypt_digest(pubkey, signature)
    if digest == decrypted_signature:
        return True
    else:
        return False