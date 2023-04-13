import math
#input
key = 3033
plain = "8ca66ee6b2fe4bb928a8e3cd2f508de4119c0895f22e011117e22cf9b13de7ef"
n = 3337
cipherblock = []
plainblock = []

#memasukan ke blo
plaintext = plain.encode()
size_block = math.ceil(math.log2(n)/8)
for i in range (0, len(plaintext), size_block-1) :
    plainblock.append(b'\x00' + plaintext[i:size_block-1+i])

#kasih padding ke block terakhir
if len(plainblock[-1]) != size_block :
    while (len(plainblock[-1]) != size_block):
        plainblock[-1] = ((size_block - len(plainblock[-1])) * b'\x00') + plainblock[-1] 

pad_len = size_block - len(plainblock[-1])
#ubah ke integer
for i in range (len(plainblock)):
    plainblock[i] = int.from_bytes(plainblock[i], byteorder='big', signed=False)
print(plainblock)
#rumus enkripsi
for char in plainblock:
    cipherblock.append((char**key)%n)
print(cipherblock)

#ubah ke byte lagi
for i in range (len(cipherblock)):
    cipherblock[i] = cipherblock[i].to_bytes(length=size_block, byteorder='big', signed=False)
print(cipherblock)

ciphertext = b''
for i in range (len(cipherblock)):
    ciphertext += cipherblock[i]
print(ciphertext)

ciphertext += pad_len.to_bytes(length = 4, byteorder='big', signed=False)
print(ciphertext)

print(ciphertext.hex())