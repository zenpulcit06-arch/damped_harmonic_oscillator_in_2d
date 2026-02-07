# file name analysis
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

data = pd.read_csv("data.csv")
t = data["t"]
x = data["x"]
y = data["y"]
vx = data["vx"]
vy = data["vy"]
ax = data["ax"]
ay = data["ay"]
Ex = data["Ex"]
Ey = data["Ey"]
E = data["E"]

const = pd.read_csv("const.csv")
m = const["m"].iloc[0]
bx_th = const["bx"].iloc[0]
by_th = const["by"].iloc[0]
kx = const["kx"].iloc[0]
ky = const["ky"].iloc[0]

plt.plot(x, y)
plt.title("Path of particle (Spatial Trajectory)")
plt.xlabel("X - axis")
plt.ylabel("Y - axis")
plt.grid()
plt.show()

fig, ax = plt.subplots(1, 2)

ax[0].plot(t, x)
ax[0].set_ylabel("x(m)")
ax[0].set_xlabel("Time (s)")
ax[0].set_title("SHM with respect to x_axis")
ax[0].grid(True)

ax[1].plot(t, y)
ax[1].set_ylabel("y(m)")
ax[1].set_xlabel("Time (s)")
ax[1].set_title("SHM with respect to y_axis")
ax[1].grid(True)

plt.tight_layout()
plt.show()

plt.plot(t, E)
plt.title("Energy vs Time")
plt.xlabel("Time(s)")
plt.ylabel("Energy (J)")
plt.grid()
plt.show()

fig, ax = plt.subplots(1, 2)

ax[0].plot(x, vx)
ax[0].set_xlabel("x(m)")
ax[0].set_ylabel("Velocity in x (m/s)")
ax[0].set_title("SHM with respect to x_axis")
ax[0].grid(True)

ax[1].plot(y, vy)
ax[1].set_xlabel("y(m)")
ax[1].set_ylabel("Velocity in y (m/s)")
ax[1].set_title("SHM with respect to y_axis")
ax[1].grid(True)

plt.tight_layout()
plt.show()

Ex0 = Ex.iloc[0]
mask = (Ex > 0.05 * Ex0) & (Ex > 0)
t_fit_x = t[mask]
Ex_fit = Ex[mask]

Ey0 = Ey.iloc[0]
mask = (Ey > 0.05 * Ey0) & (Ey > 0)
t_fit_y = t[mask]
Ey_fit = Ey[mask]

slope_x, intercept_x = np.polyfit(t_fit_x, np.log(Ex_fit), 1)
gamma_x = -slope_x / 2
b_x_sim = 2 * m * gamma_x
print(f"damping constant in x = {gamma_x:.4f}")
print(f"damping cofficient in x = {b_x_sim :.4f}")

slope_y, intercept_y = np.polyfit(t_fit_y, np.log(Ey_fit), 1)
gamma_y = -slope_y / 2
b_y_sim = 2 * m * gamma_y
print(f"damping constant in y = {gamma_y:.4f}")
print(f"damping cofficient in y = {b_y_sim :.4f}")
if bx_th == 0:
    damped_error_x = np.inf
else:
    damped_error_x = ((b_x_sim - bx_th) / bx_th) * 100

if by_th == 0 :
    damped_error_y = np.inf
else:
    damped_error_y = ((b_y_sim - by_th) / by_th) * 100

print(f"percent error in damping cofficient in x = {damped_error_x :.2f}%")
print(f"percent error in damping cofficient in y = {damped_error_y :.2f}%")

fig, ax = plt.subplots(1, 2)

ax[0].scatter(t_fit_x, np.log(Ex_fit))
ax[0].plot(t_fit_x, t_fit_x * slope_x + intercept_x, color="red")
ax[0].set_title(f"X-Decay (b_sim={b_x_sim:.2f})")
ax[0].set_xlabel("Time (s)")
ax[0].set_ylabel("ln(E_x)")
ax[0].grid()

ax[1].scatter(t_fit_y, np.log(Ey_fit))
ax[1].plot(t_fit_y, t_fit_y * slope_y + intercept_y, color="red")
ax[1].set_title(f"Y-Decay (b_sim={b_y_sim:.2f})")
ax[1].set_xlabel("Time (s)")
ax[1].set_ylabel("ln(E_y)")
ax[1].grid()

plt.tight_layout()
plt.show()

if abs(damped_error_x) <= 2 and abs(damped_error_y) <= 2:
    print("Excellent simulation")
elif 2 < abs(damped_error_x) <= 10 and 2 < abs(damped_error_y) <= 10:
    print("simulation in acceptable range")
else:
    print("parameter should be more defined")
