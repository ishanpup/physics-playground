import numpy as np
import matplotlib.pyplot as plt
import math
from scipy.integrate import solve_ivp
import pandas as pd

data = pd.read_csv('projectile_data.csv')
def ask_float(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input — please enter a number.")
#anti-crash

g = 9.8
m = 30
d = 1
db = ask_float('db: ')
duration_of_collision = 0.01

plt.figure(figsize=(9,5))
etas = []#list for eta values

#derivative of velocity is acceleration, derivative of position is v
def derivatives(t, y):
    v, x = y
    return [-g, v]
#when an event occurs at time t, return the x position
#scipy is always checking for when x = 0
def hit_ground(t, y):
    return y[1]

hit_ground.terminal = True #when the event holds true, terminate the integration
hit_ground.direction = -1 #tells it only to detect when going from + -> -
# this is so we don't get false stops

for index, row in data.iterrows():
    hi = row['hi']
    hf = row['hf']
    duration_of_collision = row['duration_of_collision']
    sol1 = solve_ivp(derivatives, [0,100], [0,hi], events=hit_ground, max_step = .01) #when the event holds true (x=0), terminate

    t1 = sol1.t
    x1 = sol1.y[1]

    v_impact = sol1.y_events[0][0][0]#find velocity when event holds true
    t_impact = sol1.t_events[0][0]#find time of event

    v_rebound = math.sqrt(2 * g * hf)
#rinse and repeat for the second bounce
    sol2 = solve_ivp(derivatives, [t_impact, t_impact +100], [v_rebound, 1e-6], events=hit_ground, max_step = .01)#made x value very small (not 0) to ensure proper graphs

    t2 = sol2.t
    x2 = sol2.y[1]

    e = -v_rebound/v_impact
    t_full = np.concatenate([t1, t2])
    x_full = np.concatenate([x1, x2])

    plt.plot(t_full, x_full, label=f'Row {index+1}')

    deltaKE = 0.5 * m * (v_impact**2 - v_rebound**2)

    I = 1e-12 * 10**(db / 10)

    Esound = I * (4 * math.pi * d**2) * duration_of_collision
    eta = Esound / deltaKE
    etas.append(eta)

    print(f"Row {index+1}: eta = {eta:.3e},  n = {e:.3e} ")

#how does this process work?
#input experimental height initial and final height, and the program will graph that motion for you (this is for straight up/down motion)
#on top of that, if you know the decibel level of the sound produced by contact, you can input that in. it will NOT change the graph
#by inputting sound, you can find an eta value, which is ratio of energy lost to sound vs the mechanical energy lost
#note that you cannot assume all change in mechanical energy is due to sound, most of it is actually due to heat.

plt.xlabel("Time (s)")
plt.ylabel("Height (m)")
plt.title("Ball Drop with Bounce (All Trials)")
plt.grid(True)
plt.legend()
plt.show()
