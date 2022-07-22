'''This module provides the implementation of the Gradient Descent algorithm.

Created on Jul 16, 2022
@author: 816461
'''

def f(w, points):
    """
    Returns the sum of regression distances between points and regression line
    - w is the slope of the regression line of all points
    - points is an array of points (x, y), e.g. points = [(2,4), (4,2)]
    """
    return sum((w * x - y) ** 2 for x,y in points)

def df(w, points):
    """
    Returns the corresponding derivate of the function f above with respect to w.
    - w is the slope of the regression line
    - points is an array of points (x, y), e.g. points = [(2,4), (4,2)]
    """
    return sum(2 * (w * x - y) * x for x,y in points)

# Gradient Descent
if __name__ == "__main__":
    points = [(2,4), (4,2)]
    w=0
    eta=0.01
    print(f"computing gradient descent for points {points}")
    for t in range(100):
        value = f(w, points)
        gradient = df(w, points)
        w = w - eta * gradient
        print(f"iteration {t}: w {w} / f(w) = {value} / df(w) = {gradient} ")

    points = [(2,4), (4,2), (6, 8)]
    w=0
    eta=0.01
    print(f"computing gradient descent for points {points}")
    for t in range(100):
        value = f(w, points)
        gradient = df(w, points)
        w = w - eta * gradient
        print(f"iteration {t}: w {w} / f(w) = {value} / df(w) = {gradient} ")
