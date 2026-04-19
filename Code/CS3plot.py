import numpy as np
import matplotlib.pyplot as plt

# Data
x = np.array([0, 2, 4, 6, 8, 10])
T = np.array([100, 80, 65, 55, 48, 45])
h = 2

# --- Gradient (Central Difference) ---
grad_x = x[1:-1]
grad_T = (T[2:] - T[:-2]) / (2*h)

print("Gradient Table:")
for i in range(len(grad_x)):
    print(f"x = {grad_x[i]} cm, dT/dx = {grad_T[i]:.2f} °C/cm")

# --- Simpson's Rule (0 to 8) ---
simpson = (h/3) * (T[0] + 4*(T[1] + T[3]) + 2*(T[2]) + T[4])

# --- Trapezoidal (8 to 10) ---
trap = (h/2) * (T[4] + T[5])

total_heat = simpson + trap

print("\nTotal Heat Distribution:", total_heat)

# --- Graphs ---
plt.figure()
plt.plot(x, T, marker='o')
plt.title("Temperature vs Position")
plt.xlabel("Position (cm)")
plt.ylabel("Temperature (°C)")
plt.grid()
plt.show()

plt.figure()
plt.plot(grad_x, grad_T, marker='o')
plt.title("Gradient vs Position")
plt.xlabel("Position (cm)")
plt.ylabel("dT/dx (°C/cm)")
plt.grid()
plt.show()