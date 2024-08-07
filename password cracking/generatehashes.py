import hashlib

password = "1q2w3e4r"
hash=hashlib.sha256(password.encode('utf-8'))

print(hash.hexdigest())