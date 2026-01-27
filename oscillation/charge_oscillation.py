import numpy as np
import math
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from scipy.integrate import solve_ivp
w = 10e3
Amp = .7
fig, ax = plt.subplots()
ax.set_xlim(-1.5, 1.5)
ax.set_ylim(-1.5, 1.5)
ax.set_aspect('equal')
point, = ax.plot([10], [0], 'yo')

def update(t):
    x = (Amp*np.sin(w*t))
    y = -1.2
    point.set_data([x], [y])
    return point,

#line
x= [-1.5, 1.5]
y = [1,1]
plt.plot(x,y, 'b-')
q = 1.6e-19
d = 1.2 + 1
r = .7
A = np.pi * r**2
def B_at_time_t(t):
    dxdt = Amp*w*np.cos(w*t)
    B = 10e-7*q*dxdt*d / (2*np.pi*(d**2))
    return B

def emfA(t):
    dt = 1e-6
    B_plus = B_at_time_t(t+dt)
    B_minus = B_at_time_t(t-dt)
    dBdt = (B_plus - B_minus)/(2*dt)
    return (A*dBdt)
t_eval = np.linspace(0, .01, 2000)


plt.figure()
ani = FuncAnimation(fig, update, frames = 10000000, interval = 1)

emf_vals = np.array(emfA(t_eval))
plt.figure()
plt.plot(t_eval,emf_vals,'r-o')
plt.title('induced emf vs time')
plt.xlabel('time (s)')
plt.ylabel('emf(V)')
plt.grid('True')
plt.show()