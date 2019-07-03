import hashlib

def make_password(passwd_str):
    return hashlib.md5(("9@^"+passwd_str+"$&").encode()).hexdigest()


if __name__ == '__main__':
    print(make_password('123'))