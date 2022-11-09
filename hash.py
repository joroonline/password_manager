# -*- coding: utf-8 -*-

import base64
import bcrypt
import hashlib


def gen_password_hash(password: str):
    password = password.encode('utf-8')
    password = base64.b64encode(hashlib.sha256(password).digest())
    hashed = bcrypt.hashpw(
        password,
        bcrypt.gensalt(12)
    )
    return hashed.decode()

def check_password(password: str, hash: str):
    password = password.encode('utf-8')
    password = base64.b64encode(hashlib.sha256(password).digest())
    hash = hash.encode('utf-8')
    if bcrypt.checkpw(password, hash):
        return True
    else:
        return False


if __name__ == "__main__":
    password = "hdaskhsahdk"
    hash = gen_password_hash(password)
    print(check_password("hdaskhsahdl", hash))
