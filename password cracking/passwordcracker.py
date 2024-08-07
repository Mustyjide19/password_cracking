import hashlib

user_hash_dict = {}

# Load common passwords from the file
with open('common_passwords.txt', 'r') as f:
    common_passwords = f.read().splitlines()

# Load username and hash pairs from the file
with open('username_hashes.txt', 'r') as f:
    text = f.read().splitlines()
    for user_hash in text:
        username, user_hash_value = user_hash.split(':')
        user_hash_dict[username] = user_hash_value

# Check common passwords against the user hashes
found = False
for password in common_passwords:
    hashed_password = hashlib.md5(password.encode('utf-8')).hexdigest()  # Change to hashlib.sha256 if using sha256
    for username, user_hash_value in user_hash_dict.items():
        if hashed_password == user_hash_value:
            print(f'HASH FOUND\n{username}:{password}')
            found = True

if not found:
    print('No hashes matched any common passwords.')

