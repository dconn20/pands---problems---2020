# a program that displays a plot of the functions 
# f(x)=x, g(x)=x2 and h(x)=x3 in the range [0, 4] 
# on the one set of axes.

import numpy as np 
import matplotlib.pyplot as plt 

x = np.arange (0, 4)

def f(x):
    (x) = x
    plt.plot(x, 'r--')
    

def g(x): 
     x= x**2
     plt.plot(x, 'b--')
    
  

def h(x): 
    x = x**3
    plt.plot(x, 'g--')
    

f(x)
g(x)
h(x)
plt.show()


# Displays all functions on same graph.
# Red, blue and green lines
plt.plot(x, x, 'r--', x, x**2, 'b--', x, x**3, 'g--')
plt.show()







