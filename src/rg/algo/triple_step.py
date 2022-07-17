"""This module provides a recursive solution to the tripe step problem

Created on Jul 11, 2022
@author: Rubens Gomes
"""
import time


class TripleStep(object):
    """A type that provides the implementation of triple step problem.
    """

    # dictionary used in dynamic programming to store previous calculated values.
    _memo = {}

    def __init__(self):
        """Constructor to initialize an object instance of this type
        :param self: refers to any object instance of this type
        """

    @staticmethod
    def get_memo():
        """Returns the value of the class variable _memo containing previously stored Fibonacci numbers

        Keyword arguments:
        :param self: refers to any object instance of this type
        """
        return TripleStep._memo

    @staticmethod
    def clear_memo():
        """Clears the value of the class variable _memo containing previously stored Fibonacci numbers

        Keyword arguments:
        :param self: refers to any object instance of this type
        """
        return TripleStep._memo.clear()


    def triple_step(self, n):
        """Return how many possible ways a child can run up the stairs with n steps 
        hopping either 1 step, 2 steps, or 3 steps at a time.
        :param n: number of steps in the stairs
        """
        assert isinstance(n, int), "n must be integer"
    
        if n < 0:
            return 0
    
        if n == 0:
            return 1
    
        return self.triple_step(n - 1) + self.triple_step(n - 2) + self.triple_step(n - 3)
    
    def triple_step_dp(self, n):
        """Return how many possible ways a child can run up the stairs with n steps 
        hopping either 1 step, 2 steps, or 3 steps at a time.  This solution makes
        use of Memoization to improve the algorithm runtime performance.
        :param n: number of steps in the stairs
        """
        assert isinstance(n, int), "n must be integer"
    
        # Dynamic Programming Technique
        # Memoization Step
        if n in TripleStep._memo:
            return TripleStep._memo[n]
    
        if n < 0:
            TripleStep._memo[n] = 0
            return 0
        elif n == 0:
            TripleStep._memo[0] = 1
            return 1
        else:
            # recursive step
            TripleStep._memo[n] = self.triple_step_dp(n - 1) + self.triple_step_dp(n - 2) + self.triple_step_dp(n - 3)
    
        return TripleStep._memo[n]


if __name__ == "__main__":
    MIN_RANGE = 3
    MAX_RANGE = 10
    NS_TO_MS_FACTOR = 0.000001
    MAX_STEP_SIZE = 22

    # obj is an object used to test this type
    obj = TripleStep()

    for i in range(MIN_RANGE, MAX_RANGE):
        tic = time.perf_counter_ns()
        ans = obj.triple_step(i)
        toc = time.perf_counter_ns()
        elapsed_ms = (toc - tic) * NS_TO_MS_FACTOR
        print(f"regular stairs size: {i} / nr of possible steps: {ans} /   elapsed: {elapsed_ms:.4f} ms")

    tic = time.perf_counter_ns()
    ans = obj.triple_step(MAX_STEP_SIZE)
    toc = time.perf_counter_ns()
    elapsed_ms = (toc - tic) * NS_TO_MS_FACTOR
    print(f"triple_step with size: {MAX_STEP_SIZE} / ans: {ans} /  elapsed: {elapsed_ms:.4f} ms")

    print("-----------------------------------------")
    TripleStep.clear_memo()

    for i in range(MIN_RANGE, MAX_RANGE):
        tic = time.perf_counter_ns()
        ans = obj.triple_step_dp(i)
        toc = time.perf_counter_ns()
        elapsed_ms = (toc - tic) * NS_TO_MS_FACTOR
        print(f"DP stairs size: {i} / nr of possible steps: {ans} /  elapsed: {elapsed_ms:.4f} ms")
        TripleStep.clear_memo()

    TripleStep.clear_memo()
    tic = time.perf_counter_ns()
    ans = obj.triple_step_dp(MAX_STEP_SIZE)
    toc = time.perf_counter_ns()
    elapsed_ms = (toc - tic) * NS_TO_MS_FACTOR
    print(f"triple_step_dp with size: {MAX_STEP_SIZE} / ans: {ans} /  elapsed: {elapsed_ms:.4f} ms")
