#!/usr/bin/env python3
"""
Derive happiness in oneself from a good day's work
"""


def poly_derivative(poly):
    """
    function that calculates the derivative of a polynomial:
    """
    new = []
    if type(poly) is not list or len(poly) == 0:
        return None
    if len(poly) == 1:
        return [0]
    for i in range(1, len(poly)):
        new.append(i * poly[i])
    return new
