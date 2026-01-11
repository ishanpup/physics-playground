import math
import geocoder
import osmnx as ox
import requests
from sympy.codegen.ast import continue_

city_name = input("Enter city name: ")
def ask_float(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input — please enter a number.")

gdf = ox.geocode_to_gdf(city_name)
gdf_meter = gdf.to_crs(epsg=3395)
polygon = gdf_meter.loc[0, 'geometry']
A_city = polygon.area /2   #found out experimentally that actual area is ~ polygon.area/2
print("City area (km²):", (A_city)/(10e5))
yn = input("is this accurate? (y/n): ")
if yn == "y":
    Aa_city = A_city
else:
    Aa_city = (ask_float("put the actual area in km²: ")*10e6)

v_term = 10 #terminal velocity of water drop
r = ask_float("radius of a droplet(mm): ")*.001
A = math.pi*(r**2) #cross-sectional area of water drop
rho = 1000 #density of water
V = 4*math.pi*(r**3)/3 #volume of droplet
m = rho*V #mass of droplet
K = 2.2 * (10**9) #bulk modulus of water
L = r # radius of drop
k = K*(A/L) #spring constant of water
t = .00024
F = m*v_term/t #force per droplet

print(F, 'N per drop')

I = .01 #m/hr
V_intensity = I*Aa_city/3600 #m^3/s
n = V_intensity/V #droplets/s
print(n,'droplets over the whole city of', city_name, 'per second')
P_net = F * n/ Aa_city
print(P_net, 'Pa over the whole city of', city_name)

