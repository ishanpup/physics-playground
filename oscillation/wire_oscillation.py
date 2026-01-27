import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

w = 10e3
Amp = 0.7
q = 1.6e-19
r = 0.7
A = np.pi * r**2

fig, ax = plt.subplots()
ax.set_xlim(-1.5, 1.5)
ax.set_ylim(-1.5, 1.5)
ax.set_aspect('equal')

x_charge = 0
y_charge = -1.2
point, = ax.plot([x_charge], [y_charge], 'yo')

x_line = [-1.5, 1.5]
line, = ax.plot(x_line, [1, 1], 'b-')

def update(frame):
    t = frame * 0.00001
    y_line = 0.3 * np.sin(w*t)
    line.set_data(x_line, [y_line, y_line])
    return point, line

def B_at_time_t(t, y_line):
    d = y_line - y_charge
    dxdt = Amp * w * np.cos(w*t)
    B = 1e-6 * q * dxdt * d / (d**2)
    return B


def emfA(t):
    dt = 1e-8
    y_line = 0.3 * np.sin(w*t)
    B_plus = B_at_time_t(t+dt, y_line)
    B_minus = B_at_time_t(t-dt, y_line)
    dBdt = (B_plus - B_minus)/(2*dt)
    return A * dBdt


t_eval = np.linspace(0, 0.01, 20000)
emf_vals = np.array([emfA(t) for t in t_eval])


ani = FuncAnimation(fig, update, frames=20000000, interval=1, blit=True)
plt.show()


plt.figure()
plt.plot(t_eval, emf_vals, 'g-o')
plt.title('Induced EMF vs Time')
plt.xlabel('time (s)')
plt.ylabel('emf(V)')
plt.grid(True)
plt.show()
