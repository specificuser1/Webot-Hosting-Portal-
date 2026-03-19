from hashlib import sha256

def hash_token(token: str):
    return sha256(token.encode()).hexdigest()
