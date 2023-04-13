import hashlib

def convHextoDec(hex):
    return int(hex, 16)

def hash_sha3_256(message):
    return convHextoDec(hashlib.sha3_256(message.encode()).hexdigest()) 

def main():
    message = "Hello World"
    print(hash_sha3_256(message))

if __name__ == "__main__":
    main()


