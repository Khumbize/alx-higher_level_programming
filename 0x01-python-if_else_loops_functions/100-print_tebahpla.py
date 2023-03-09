#!/usr/bin/python3


nc = 0
for n in range(122, 96, -1):
    if num % 2 == 0:
        nc = num
    else:
        nc = num - 32
    print("{}".format(chr(nc)), end='')
