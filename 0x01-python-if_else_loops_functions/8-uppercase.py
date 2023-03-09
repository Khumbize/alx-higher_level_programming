#!/usr/bin/python3


def uppercase(str):
    new_str = ''
    for k in str:
        if ord(k) >= 97 and ord(k) <= 122:
            new_str += chr(ord(k) - 32)
        else:
            new_str += k
    print('{}'.format(new_str))
