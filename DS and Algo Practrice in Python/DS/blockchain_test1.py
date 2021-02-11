import hashlib
hash = hashlib.sha256("secret message".encode()).hexdigest()
print(hash)