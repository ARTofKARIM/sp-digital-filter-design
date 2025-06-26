"""Stability and pole-zero analysis."""
import numpy as np
from scipy import signal as sig

class FilterAnalyzer:
    def __init__(self):
        pass

    def pole_zero(self, b, a):
        zeros = np.roots(b)
        poles = np.roots(a)
        return zeros, poles

    def is_stable(self, b, a):
        _, poles = self.pole_zero(b, a)
        return np.all(np.abs(poles) < 1.0)

    def impulse_response(self, b, a, n_samples=100):
        t, response = sig.impulse((b, a), N=n_samples)
        return t, response

    def step_response(self, b, a, n_samples=100):
        t, response = sig.step((b, a), N=n_samples)
        return t, response
