import numpy as np
import matplotlib.pyplot as plt

# Given Data
t = np.array([0, 1, 2, 3, 4, 5])
x = np.array([0, 5, 15, 30, 50, 75])

v = np.zeros(4)
t_v = t[1:5]

for i in range(1, 5):
    v[i-1] = (x[i+1] - x[i-1]) / 2

print("Velocity Estimation")
print("Time (s) | Velocity (m/s)")
for time, vel in zip(t_v, v):
    print(f"{time:8} | {vel:14.1f}")

a = np.zeros(2)
t_a = t_v[1:3]

for i in range(1, 3):
    a[i-1] = (v[i+1] - v[i-1]) / 2

print("\nAcceleration Insight (Optional Extension)")
print("Time (s) | Acceleration (m/s²)")
for time, acc in zip(t_a, a):
    print(f"{time:8} | {acc:19.1f}")

estimated_distance = np.trapezoid(v, dx=1)

actual_displacement = x[4] - x[1]

print("\nDistance Verification")
print(f"Estimated Distance (Trapezoidal Rule): {estimated_distance} m")
print(f"Actual Displacement (x(4) - x(1)): {actual_displacement} m")

plt.figure(figsize=(10,4))

plt.subplot(1,2,1)
plt.plot(t, x, marker='o')
plt.title("Position vs Time")
plt.xlabel("Time (s)")
plt.ylabel("Position (m)")

plt.subplot(1,2,2)
plt.plot(t_v, v, marker='o', color='orange')
plt.title("Velocity vs Time")
plt.xlabel("Time (s)")
plt.ylabel("Velocity (m/s)")

plt.tight_layout()
plt.show()