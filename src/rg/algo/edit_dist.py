"""Implementation of the compute edit distance between 2 (two) strings.

Solution based on Video lecture:
Overview Artificial Intelligence Course | Stanford CS221: Learn AI (Autumn 2019)

Created on July 16, 2022
@author: Rubens Gomes
"""
import time

def edit_dist(s, t):
    """
    Return the minimum number of operations (add, delete, substitue) required
    to make string 's' match string 't'. 
    
    For example, if s is 'a cat' and t is 'the cats', then the number of
    operations to make s the same as t is 4
    
    - s text string
    - t text string
    """
    def recurse(m, n):
        """
        Return the minimum edit distance between:
        - First m letters of s
        - First n letters of t
        """
        if m == 0: # base case
            result = n
        elif n == 0: # base case
            result = m
        elif s[m - 1] == t[n - 1]: # last letter matches
            result = recurse(m - 1, n - 1)
        else:
            subCost = 1 + recurse(m - 1, n - 1)
            delCost = 1 + recurse(m - 1, n)
            insCost = 1 + recurse(m, n - 1)
            result = min(subCost, delCost, insCost)
        return result

    return recurse(len(s), len(t))


def edit_dist_dp(s, t):
    """
    Return the minimum number of operations (add, delete, substitue) required
    to make string 's' match string 't'. This function uses dynamic programming,
    or 'Memoization'.
    
    For example, if s is 'a cat' and t is 'the cats', then the number of
    operations to make s the same as t is 4
    
    - s text string
    - t text string
    """
    cache = {} # (m, n) => result
    def recurse(m, n):
        """
        Return the minimum edit distance between:
        - First m letters of s
        - First n letters of t
        """
        if (m, n) in cache:
            return cache[(m,n)]
        if m == 0: # base case
            result = n
        elif n == 0: # base case
            result = m
        elif s[m - 1] == t[n - 1]: # last letter matches
            result = recurse(m - 1, n - 1)
        else:
            subCost = 1 + recurse(m - 1, n - 1)
            delCost = 1 + recurse(m - 1, n)
            insCost = 1 + recurse(m, n - 1)
            result = min(subCost, delCost, insCost)
        cache[(m, n)] = result
        return result

    return recurse(len(s), len(t))

if __name__ == "__main__":
    NS_TO_MS_FACTOR=0.000001

    print("running case 1...")

    s = "a cat"
    t = "the cats"
    print("running edit_dist...")
    tic = time.perf_counter_ns()
    ans = edit_dist(s, t)
    toc = time.perf_counter_ns()
    elapsed_ms = (toc - tic) * NS_TO_MS_FACTOR
    print(f"regular edit_dist: s is '{s}' and t is '{t}' / result is {ans} / elapsed: {elapsed_ms:.4f} ms")

    print("running edit_dist_dp...")
    tic = time.perf_counter_ns()
    ans = edit_dist_dp(s, t)
    toc = time.perf_counter_ns()
    elapsed_ms = (toc - tic) * NS_TO_MS_FACTOR
    print(f"dynamic prog edit_dist_dp: s is '{s}' and t is '{t}' / result is {ans} / elapsed: {elapsed_ms:.4f} ms")

    # --------------------------------------------------------------------------

    print("running case 2...")

    s = "Vasco"
    t = "Vasco da Gama"
    print("running edit_dist...")
    tic = time.perf_counter_ns()
    ans = edit_dist(s, t)
    toc = time.perf_counter_ns()
    elapsed_ms = (toc - tic) * NS_TO_MS_FACTOR
    print(f"regular edit_dist: s is '{s}' and t is '{t}' / result is {ans} / elapsed: {elapsed_ms:.4f} ms")

    print("running edit_dist_dp...")
    tic = time.perf_counter_ns()
    ans = edit_dist_dp(s, t)
    toc = time.perf_counter_ns()
    elapsed_ms = (toc - tic) * NS_TO_MS_FACTOR
    print(f"dynamic prog edit_dist_dp: s is '{s}' and t is '{t}' / result is {ans} / elapsed: {elapsed_ms:.4f} ms")

    # --------------------------------------------------------------------------

    print("running case 3...")

    s = "CRVG"
    t = "Clube de Regatas Vasco da Gama"
    print("running edit_dist...")
    tic = time.perf_counter_ns()
    ans = edit_dist(s, t)
    toc = time.perf_counter_ns()
    elapsed_ms = (toc - tic) * NS_TO_MS_FACTOR
    print(f"regular edit_dist: s is '{s}' and t is '{t}' / result is {ans} / elapsed: {elapsed_ms:.4f} ms")

    print("running edit_dist_dp...")
    tic = time.perf_counter_ns()
    ans = edit_dist_dp(s, t)
    toc = time.perf_counter_ns()
    elapsed_ms = (toc - tic) * NS_TO_MS_FACTOR
    print(f"dynamic prog edit_dist_dp: s is '{s}' and t is '{t}' / result is {ans} / elapsed: {elapsed_ms:.4f} ms")
