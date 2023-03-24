from os import urandom
from Crypto.Cipher import AES
#from secret import MESSAGE
'''
assert all([x.isupper() or x in '{_} ' for x in MESSAGE])
'''

class Cipher:

    def __init__(self):
        self.salt = urandom(15)
        key = urandom(16)
        self.cipher = AES.new(key, AES.MODE_ECB)

    def encrypt(self, message):
        return [self.cipher.encrypt(c.encode() + self.salt) for c in message]


def main():
    '''
    cipher = Cipher()
    encrypted = cipher.encrypt("TEST")
    encrypted = "\n".join([c.hex() for c in encrypted])
    print(encrypted)

    with open("output.txt", 'w+') as f:
        f.write(encrypted)
'''
    block_occurence = {}
    with open("output.txt", 'r') as f:
        for line in f.readlines():
            line = line.strip()
            if line not in block_occurence:
                block_occurence[line] = 1
            else:
                block_occurence[line] = block_occurence[line] + 1

    print(block_occurence)

if __name__ == "__main__":
    main()
