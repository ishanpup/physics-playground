import numpy as np
import matplotlib.pyplot as plt
import math
from scipy.integrate import solve_ivp
import pandas as pd

q1 = -1.6e-19
Voltage = 120
m = 9.11e-31
r = .001
f = 5e14
c = 3e8
E = 5

def derivatives(t, state):
    x,v = state
    dxdt = v
    dvdt = (q1 * E*(math.cos(2*math.pi*f*t)))/m
    return(dxdt, dvdt)
y0 = [0,0]
t_eval = np.linspace(0,2e-15,200)
solution  = solve_ivp(derivatives, (0,2e-15), y0 , t_eval=t_eval)
x = solution.y[0]
v = solution.y[1]
t = solution.t

lamda = c/f
print(lamda)

plt.plot(t,x)
plt.xlabel("Time (s)")
plt.ylabel("amplitude (m)")
plt.title("oscillation")
plt.grid(True)
plt.legend()
plt.show()
