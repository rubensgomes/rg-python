"""Implementation of the compute edit distance between 2 (two) strings.

Solution based on Video lecture:
Overview Artificial Intelligence Course | Stanford CS221: Learn AI (Autumn 2019)

Created on July 16, 2022
@author: Rubens Gomes
"""

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
        if m == 0:
            result = n
        elif n == 0:
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

if __name__ == "__main__":
    s = "a cat"
    t = "the cats"
    ans = edit_dist(s, t)
    print(f"s is '{s}' and t is '{t}' / result is {ans}")

    s = "Vasco"
    t = "Vasco da Gama"
    ans = edit_dist(s, t)
    print(f"s is '{s}' and t is '{t}' / result is {ans}")

    s = "Rubens"
    t = "Rubinho"
    ans = edit_dist(s, t)
    print(f"s is '{s}' and t is '{t}' / result is {ans}")
