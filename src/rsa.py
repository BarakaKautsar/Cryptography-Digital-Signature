import hashlib


def encrypt_digest(prikey, plaintext):
    key, n = prikey
    ciphertext = []
    
    for char in plaintext:
        ciphertext.append(pow(ord(char),key,n))

    hex_sign = f''
    for char in ciphertext:
        hex_sign = hex_sign + hex(char)

    return (hex_sign)

def decrypt_digest(pubkey, ciphertext):
    plaintext_arr = []
    key, n = pubkey
    ciphertext = ciphertext.strip()
    if ciphertext.startswith('0x'):
        parts = ciphertext.split('0x')[1:]
        for part in parts:
            plaintext_arr.append(int(part, 16))

    plaintext =""
    for char in plaintext_arr:
        plaintext += (chr(pow(char, key, n)))

    return plaintext

BUF_SIZE = 65536  # lets read stuff in 64kb chunks!

def hashfile(filename):
    sha3 = hashlib.sha3_256()
    with open(filename, 'rb') as f:
        while True:
            data = f.read(BUF_SIZE)
            if not data:
                break
            sha3.update(data)
    return sha3.hexdigest()

def hashstring(string):
    sha3 = hashlib.sha3_256()
    sha3.update(string.encode())
    return sha3.hexdigest()

def sign_message(message, private_key):
    message_hashed = hashlib.sha3_256(message.encode()).hexdigest()
    return encrypt_digest(private_key, message_hashed)

def sign_file(file_path, private_key):
    file_hashed = hashfile(file_path)
    return encrypt_digest(private_key, file_hashed)

# p = 52218497
# q = 344091697
# n = 17967951247519409
# d = 3383867639095039
# e = 14926788939532543

# prikey = (d, n)
# pubkey = (e, n)

# text = "pow"
# haste = hashlib.sha3_256(text.encode()).hexdigest()
# print(haste)

# sign = encrypt_digest(prikey, haste)
# print(sign)
# print(decrypt_digest(pubkey, sign))
# print(haste == decrypt_digest(pubkey, sign))