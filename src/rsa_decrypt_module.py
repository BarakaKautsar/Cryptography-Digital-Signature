
#Coba Metode RSA Modul by Modul

from typing import List
import math
def baseDecrypt(c: int, e: int, n: int) -> int:

    try:
        return pow(c, e, n)
    except Exception as E:
        raise(E)


def binaryPadding(bits: str, n: int) -> str :
    try:
        while len(bits) % n != 0:
            bits = '0'+bits
        return bits
    except Exception as E:
        raise(E)

def convertBytetoIntArray(bytesInput: bytes, digitDiv: int) -> List[int]:

    try:
        result = []
        binInput = bin(int.from_bytes(bytesInput, "big"))[2:]
        binInput = binaryPadding(binInput, digitDiv)
        for index in range(0, len(binInput), digitDiv):
            result.append(int(binInput[index : index + digitDiv], 2))
        return result
    except Exception as E:
        raise(E)

def convertIntArraytoByte(inputList: List[int], digit: int) -> bytes:
    try:
        binary = ''
        for i, val in enumerate(inputList):
            if i != len(inputList)-2 :
                binary+=bin(val)[2:].zfill(digit)
            else:
                binary+=bin(val)[2:].zfill(inputList[-1])
                break
        intResult = int(binary, 2)
        result = intResult.to_bytes((len(binary) + 7) // 8, "big", signed=False)


        return result
    
    except Exception as E:
        raise(Exception("kunci tidak cocok!"))

def digitDivider(n: int) -> int:
    try:
        return math.floor(math.log2(n))
    except Exception as E:
        raise(E)
    
def maxBitLength(n: int) -> int:

    try:
        return (n-1).bit_length()
    except Exception as E:
        raise(E)

def decryptBytes(message: bytes, pubkey: (int, int)):

    try:
        e, n = pubkey
        cipherBytes = message
        digitDiv = digitDivider(n)
        intValue = convertBytetoIntArray(cipherBytes, maxBitLength(n))
        plainInt = [baseDecrypt(val, e, n) for val in intValue]
        plainBytes = convertIntArraytoByte(plainInt, digitDiv)
        return plainBytes
    except Exception as E:
        raise(E)