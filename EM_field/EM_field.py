import numpy as np
import matplotlib.pyplot as plt
import math
from scipy.integrate import solve_ivp
import pandas as pd

motion_type = input("Enter motion type(straight/circle): ")
if motion_type == "straight":
    print("great! you selected straight motion")
    f = float(input("input frequency of acceleration (HAS TO BE PERIODIC)(cycles/s): "))
    lamda = 3e8/f
    print("you will get an EM wave of wavelength", lamda)
    yn = input("curious to learn more? (y/n): ")
    if yn == "y":
        print("imagine an antennae with a AC voltage run through it. The electric field is changing with a high frequency, in the scale of MHz or GHz. ")
        print("Each electron in the antennae experiences a force from that field in the magnitude of qE. As the field oscillates, the charges oscillate very rapidly as well. They don't move far, but that oscillation is what propagates electromagnetic waves outwards")
    else:
        print("have a good day!")
if motion_type == "circle":
    print("great! you selected circle motion")
    v = float(input("input velocity(m/s): "))
    r = float(input("input radius(m): "))
    T = (2*math.pi)*r/v
    f = 1/T
    lamda = 3e8 / f
    print("you will get an EM wave of wavelength", lamda)

