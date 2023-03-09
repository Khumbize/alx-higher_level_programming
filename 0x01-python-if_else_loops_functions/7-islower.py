#!/usr/bin/python3


def islower(k):
    if ord(k) >= 97 and ord(k) <= 122:
        return True
    return False


if __name__ == '__main__':
    print(islower('C'))
