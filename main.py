import numpy as np
import matplotlib.pyplot as plt
from scipy.special import genlaguerre
from math import factorial
from scipy.special import sph_harm_y
plt.style.use('dark_background')

# Define the radial wavefunction for the hydrogen atom
def radial_function(n, l ,r):
    normalization = np.sqrt((2/n)**3)*np.sqrt(factorial(n-l-1)/(2*n* factorial(n+l+1)))
    exponential = np.exp(-r/n)
    rho = 2*r/n
    power = rho**l
    laguerre = genlaguerre(n-l-1, 2*l +1)(rho)
    return normalization * exponential * power * laguerre
    
    
r = np.linspace(0, 20, 500)
R = radial_function(2, 1, r)
plt.plot(r, R)
plt.title("Radial Function $R_{2,1}(r)$")
plt.xlabel("r")
plt.ylabel("R(r)")
plt.show()