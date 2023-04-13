import math
#input
key = 213
plain = "10ec87fb5a3469ef7f4b5b0a0025ecdf290f77336378f6db5608086f8bbbe7a56c9159b99786e30c874c8f0459b8e17b053398c12581e0d38fa8f67f66b673acbe17b17298344bd2e92e5cebbd0b" 
n = 3337683129804612734618476261231
cipherblock = []
plainblock = []

#memasukan ke blok
size_block = math.ceil(math.log2(n)/8)

