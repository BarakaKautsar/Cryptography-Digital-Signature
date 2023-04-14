def initialize() :
    #put digital signature
    #put hash digest message
    return None

def verification(digest, signature, pubkey):
    key, n = pubkey
    decrypted_signature = decrypt_digest(signature, key)

    for i in range (len(digest)) :
        if digest[i] != decrypted_signature[i] :
            return False

    return True