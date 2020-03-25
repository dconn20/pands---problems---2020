# a program that displays a plot of the functions 
# f(x)=x, g(x)=x2 and h(x)=x3 in the range [0, 4] 
# on the one set of axes.

import numpy as np 
import matplotlib.pyplot as plt 

x = np.arange (0, 4)

def f(x):
    (x) = x
    plt.plot(x)
    plt.show()

def g(x): 
     x= x**2
     plt.plot(x)
     plt.show()
  

def h(x): 
    x = x**3
    plt.plot(x)
    plt.show()


f(x)
g(x)
h(x)






