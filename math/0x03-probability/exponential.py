#!/usr/bin/env python3
""" Poisson Distribution """


class Exponential:
    """ that represents an exponential distribution
    """

    def __init__(self, data=None, lambtha=1.):
        """Instantiation
        Args:
            data (list): data to be used to estimate the
                distribution. Defaults to None.
            lambtha (float): expected number of occurences
                in a given time frame. Defaults to 1..
        """
        self.e = 2.7182818285
        if data is not None:
            if not isinstance(data, list):
                raise TypeError("data must be a list")
            if len(data) <= 2:
                raise ValueError("data must contain multiple values")
            self.lambtha = 1 / float(sum(data) / len(data))
        else:
            if lambtha <= 0:
                raise ValueError("lambtha must be a positive value")
            self.lambtha = float(lambtha)

    def pdf(self, x):
        """Probability density function
        Args:
            x (int): time period
        """
        if x < 0:
            return 0
        return self.lambtha * self.e**(-self.lambtha*x)

    def cdf(self, x):
        """continuous density function
        Args:
            x ([type]): [description]
        """
        if x < 0:
            return 0
        return 1 - self.e**(-self.lambtha*x)
