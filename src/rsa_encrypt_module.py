#Coba Metode RSA Modul by Modul

from typing import List
import math

def baseEncrypt(m: int, d: int, n: int) -> int:

    return pow(m, d, n)

def convertBytetoIntArray(bytesInput: bytes, digitDiv: int) -> List[int]:
    result = []
    binInput = bin(int.from_bytes(bytesInput, "big"))[2:]
    for index in range(0, len(binInput), digitDiv):
        result.append(int(binInput[index : index + digitDiv], 2))
        result.append(len(binInput) % digitDiv)
    return result

def convertIntArraytoByte(inputList: List[int], digit: int) -> bytes:

    binary = ''.join([bin(val)[2:].zfill(digit) for val in inputList])
    intResult = int(binary, 2)
    result = intResult.to_bytes((len(binary) + 7) // 8, "big")
    return result

def digitDivider(n: int) -> int:

    return math.floor(math.log2(n))

def maxBitLength(n: int) -> int:
    return (n-1).bit_length()

def encryptBytes(message: bytes, prikey: (int, int)) -> bytes:

    d, n = prikey
    plainBytes = message
    digitDiv = digitDivider(n)
    intValue = convertBytetoIntArray(plainBytes, digitDiv)
    cipherInt = [baseEncrypt(val, d, n) for val in intValue]
    cipherBytes = convertIntArraytoByte(cipherInt, maxBitLength(n))
    return cipherBytes






#if __name__ == "__main__":
    #main()