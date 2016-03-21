#! /usr/bin/python3

import sys

def doit (n):
    t = 0
    for i in range (n+1):
        t += i
    return t

if __name__ == '__main__':
    n = int (sys.argv[1])
    print ('{} sum {}'.format (n, doit (n)))
