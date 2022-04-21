from cryptography.fernet import Fernet
import os

# messages are encryptes using a secret key stored in the securekey.txt file.
fileName = 'securekey.txt'

if not os.path.exists(fileName):
    with open(fileName, 'w') as f:
        key = Fernet.generate_key()
        f.write(key.decode('utf-8'))

f = None

with open(fileName, 'r') as f:
    key = f.read().encode()
    f = Fernet(key)


def encrypt(value):
    return f.encrypt(value.encode()).decode('utf-8')


def decrypt(value):
    return f.decrypt(value.encode()).decode('utf-8')
