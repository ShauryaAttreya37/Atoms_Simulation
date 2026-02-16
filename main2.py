import numpy as np
import matplotlib.pyplot as plt
from scipy.special import genlaguerre
from math import factorial
# compatibility wrapper for spherical-harmonic API across SciPy versions
try:
    from scipy.special import sph_harm
except Exception:
    from scipy.special import sph_harm_y as _sph_harm_y
    def sph_harm(m, l, phi, theta):
        # map public signature sph_harm(m, l, phi, theta) -> sph_harm_y(n, m, theta, phi)
        return _sph_harm_y(l, m, theta, phi)

plt.style.use('dark_background')

def angular_function(l, m, theta, phi):
    # ensure numpy arrays
    theta = np.asarray(theta)
    phi = np.asarray(phi)

    # use sph_harm (compatibility wrapper ensures availability)
    Y = sph_harm(m, l, phi, theta)

    return Y

theta = np.array([np.pi/2])
phi = np.array([0])

print(angular_function(1, 0, theta, phi))
