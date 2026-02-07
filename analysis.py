#file name analysis
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

data = pd.read_csv("data.csv")
t = data["t"]
x = data["x"]
y = data['y']
vx = data['vx']
vy = data['vy']
ax = data['ax']
ay = data['ay']
Ex = data['Ex']
Ey = data['Ey']
E = data['E']

const = pd.read_csv("const.csv")
m = const['m'].iloc[0]
bx_th = const['bx'].iloc[0]
by_th = const['by'].iloc[0]
kx = const['kx'].iloc[0]
ky = const['ky'].iloc[0]

plt.plot(x,y)
plt.title ("Path of particle (Spatial Trajectory)")
plt.xlabel("X - axis")
plt.ylabel("Y - axis")
plt.grid()
plt.show()

fig , ax = plt.subplots(1,2)

ax[0].plot(t,x)
ax[0].set_ylabel("x(m)")
ax[0].set_xlabel("Time (s)")
ax[0].set_title("SHM with respect to x_axis")
ax[0].grid(True)

ax[1].plot(t,y)
ax[1].set_ylabel("y(m)")
ax[1].set_xlabel("Time (s)")
ax[1].set_title("SHM with respect to y_axis")
ax[1].grid(True)

plt.tight_layout()
plt.show()

plt.plot(t,E)
plt.title("Energy vs Time")
plt.xlabel("Time(s)")
plt.ylabel("Energy (J)")
plt.grid()
plt.show()

fig , ax = plt.subplots(1,2)

ax[0].plot(x,vx)
ax[0].set_xlabel("x(m)")
ax[0].set_ylabel("Velocity in x (m/s)")
ax[0].set_title("SHM with respect to x_axis")
ax[0].grid(True)

ax[1].plot(y,vy)
ax[1].set_xlabel("y(m)")
ax[1].set_ylabel("Velocity in y (m/s)")
ax[1].set_title("SHM with respect to y_axis")
ax[1].grid(True)

plt.tight_layout()
plt.show()
