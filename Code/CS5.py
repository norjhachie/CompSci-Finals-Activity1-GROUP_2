import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import trapezoid

# given data from the problem
time = [0, 2, 4, 6, 8, 10]       # hours
energy = [0, 1.5, 3.5, 6.0, 9.0, 13.0]  # kWh
h = 2  # step size (hours)

print("===================================================")
print("  Case Study 5: Electricity Consumption & Power")
print("===================================================")


#step 1: calculate instantaneous power usage using central difference method

print("\nStep 1 - Instantaneous Power Usage (Central Difference Method)")
print(f"{'Time (hrs)':<15} {'E(t+h)':<12} {'E(t-h)':<12} {'Power (kW)'}")
print("-" * 52)

power_t = []
power_v = []

# we skip first and last since we need values on both sides
for i in range(1, len(time) - 1):
    t = time[i]
    forward = energy[i + 1]
    backward = energy[i - 1]
    P = (forward - backward) / (2 * h)
    power_t.append(t)
    power_v.append(P)
    print(f"{t:<15} {forward:<12} {backward:<12} {P:.4f}")


# step 2: calculate total energy consumed over time using trapezoidal rule
print("\nStep 2 - Total Energy Consumed Over Time (Trapezoidal Rule)")

total = trapezoid(energy, time)
print(f"  Integrated total energy consumed = {total:.4f} kWh·hr")
print(f"  Actual recorded total energy     = {energy[-1]} kWh")

# showing the manual breakdown per interval
print("\n  Manual computation per interval:")
manual = 0
for i in range(len(time) - 1):
    area = (energy[i] + energy[i + 1]) / 2 * (time[i + 1] - time[i])
    print(f"    t={time[i]} to t={time[i+1]}: ({energy[i]} + {energy[i+1]}) / 2 x {h} = {area:.2f}")
    manual += area
print(f"  Total energy consumed over time = {manual:.4f} kWh·hr")


# step 3: create graphs for energy consumption and instantaneous power usage
fig, axes = plt.subplots(1, 2, figsize=(12, 5))
fig.suptitle("Case Study 5: Electricity Consumption & Power Analysis", fontsize=14, fontweight='bold')

# graph 1 - energy consumption vs time
axes[0].plot(time, energy, 'o-', color='steelblue', linewidth=2, markersize=7, label='Energy (kWh)')
axes[0].fill_between(time, energy, alpha=0.15, color='steelblue')
axes[0].set_xlabel("Time (hours)")
axes[0].set_ylabel("Energy Consumed (kWh)")
axes[0].set_title("Energy Consumption vs Time")
axes[0].grid(True, linestyle='--', alpha=0.5)
axes[0].legend()
for t, e in zip(time, energy):
    axes[0].annotate(f"{e}", (t, e), textcoords="offset points", xytext=(0, 8),
                     ha='center', fontsize=9, color='steelblue')

# graph 2 - instantaneous power usage vs time
axes[1].plot(power_t, power_v, 's--', color='tomato', linewidth=2, markersize=7, label='Power (kW)')
axes[1].fill_between(power_t, power_v, alpha=0.15, color='tomato')
axes[1].set_xlabel("Time (hours)")
axes[1].set_ylabel("Instantaneous Power (kW)")
axes[1].set_title("Instantaneous Power Usage vs Time")
axes[1].grid(True, linestyle='--', alpha=0.5)
axes[1].legend()
for t, p in zip(power_t, power_v):
    axes[1].annotate(f"{p:.3f}", (t, p), textcoords="offset points", xytext=(0, 8),
                     ha='center', fontsize=9, color='tomato')

plt.tight_layout()
plt.savefig("case_study_5_graphs.png", dpi=150, bbox_inches='tight')
plt.show()
print("\n  Graphs saved as 'case_study_5_graphs.png'")


