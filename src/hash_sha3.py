import hashlib

# BUF_SIZE is totally arbitrary, change for your app!
BUF_SIZE = 65536  # lets read stuff in 64kb chunks!

def hashfile(filename):
    sha1 = hashlib.sha1()
    with open(filename, 'rb') as f:
        while True:
            data = f.read(BUF_SIZE)
            if not data:
                break
            sha1.update(data)
    return sha1.hexdigest()

def convHextoDec(hex):
    return int(hex, 16)

def hash_sha3_256(message):
    return convHextoDec(hashlib.sha3_256(message.encode()).hexdigest()) 

# def main():
#     message = "Hello World"
#     filename = "test.txt"
#     print(hash_sha3_256(message))
#     print(hashfile(filename))


# if __name__ == "__main__":
#     main()


