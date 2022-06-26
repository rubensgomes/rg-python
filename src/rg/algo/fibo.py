'''
This module provides implementations of Fibonacci numbers
that is, f(n) = f(n-1) + f(n-2).
Sample fibonacci numbers: 0, 1, 1, 2, 3, 5, 8, ....


Created on Jun 25, 2022

@author: Rubens Gomes
'''
import time

memo = {}


def fibo(n):
    '''
    Calculates fibonacci number using regular recursion function
 
    :param n: the fibonacci number to calculate
    '''

    assert n > 0, 'n must be greater or equal to 0'

    if n <= 2:
        f = 1
    else:
        f = fibo(n - 1) + fibo(n - 2)

    return f


def fiboDP(n):
    '''
    Calculates fibonacci number using recursion function with dynamic programming
 
    :param n: the fibonacci number to calculate
    '''

    assert n > 0, 'n must be greater or equal to 0'

    if n in memo: 
        return memo[n]
    elif n <= 2:
        f = 1
    else:
        f = fiboDP(n - 1) + fiboDP(n - 2)

    memo[n] = f
    return f


if __name__ == '__main__':
    memo.clear()
    N = [5, 10, 20, 30, 35]

    for n in N:
        print("n: ", n)

        tic = time.perf_counter_ns()
        f = fibo(n)
        toc = time.perf_counter_ns()
        elapsed = (toc - tic)
        print("f: ", f, " / elapsed: ", elapsed)

        ticDP = time.perf_counter_ns()
        fDP = fiboDP(n)
        tocDP = time.perf_counter_ns()
        elapsedDP = (tocDP - ticDP)
        print("fDP: ", fDP, " / elapsed: ", elapsedDP)

        print("fiboDP is ", elapsed/elapsedDP, " times faster")
        memo.clear()
