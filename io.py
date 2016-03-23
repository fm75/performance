#! /usr/bin/python3

import timeit


def wrapper(func, *args, **kwargs):
    def wrapped():
        return func(*args, **kwargs)

    return wrapped


def doitn(n):
    with open (str(n)+'.txt', 'w') as f:
        for _ in range (n):
            f.write ('{}\n'.format ('a' * 100))


def doit():
    experiments = [1000, 10000, 100000, 1000000]
    funcs = list()
    for n in experiments:
        funcs.append((n, (wrapper(doitn, n))))
    for (n, func) in funcs:
        print ('{:>8} {}'.format(n, timeit.timeit (func, number=1)))


if __name__ == '__main__':
    doit();