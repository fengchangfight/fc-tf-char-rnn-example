import matplotlib.pyplot as plt
import math

def natural(n):
    return math.pow(1+1/n, n)

def primayapproxi(x):
    return x/math.log(math.e, x)

def tanh(x):
    return (math.pow(math.e,x)-math.pow(math.e,-x))/(math.pow(math.e,x)+math.pow(math.e,-x))

t = range(-1000,1000)

plt.plot(t, [tanh(v) for v in t])

plt.show()
    