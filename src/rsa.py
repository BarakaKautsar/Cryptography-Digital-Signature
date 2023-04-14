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

p = 52218497
q = 344091697
n = 17967951247519409
d = 3383867639095039
e = 14926788939532543

prikey = (d, n)
pubkey = (e, n)

text = "pow"
haste = hashlib.sha3_256(text.encode()).hexdigest()
print(haste)

sign = encrypt_digest(prikey, haste)
print(sign)
print(decrypt_digest(pubkey, sign))
print(haste == decrypt_digest(pubkey, sign))