#! /usr/bin/python3

import timeit


def wrapper(func, *args, **kwargs):
    def wrapped():
        return func(*args, **kwargs)

    return wrapped


def doitn(n):
    t = 0
    for i in range(n + 1):
        t += i
    return t


def doit():
    experiments = [1000, 10000, 100000, 1000000, 10000000]
    funcs = list()
    for n in experiments:
        funcs.append((n, (wrapper(doitn, n))))    for (n, func) in funcs:
            print ('{:>8} {}'.format(n, min(timeit.repeat(func, repeat=2, number=3))))


if __name__ == '__main__':
    doit();
