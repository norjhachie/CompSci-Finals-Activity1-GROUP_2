# CompSci-Finals-Activity1-GROUP_2_GULENG-HADJINOR-RICO

# Case 2: Traffic Flow and Velocity Estimation

## Overview
A traffic monitoring system records the **position of a vehichle every second**. Engineers want to compute the **velocity and total distance travelled**.

## Given Data

| Time (s) | Position (m) |
|:---:|:---:|
| 0 | 0 |
| 1 | 5 |
| 2 | 15 |
| 3 | 30 |
| 4 | 50 |
| 5 | 75 |

## 1. Velocity Estimation
Because the dataset provides position at discrete 1-second intervals, we cannot use standard continuous derivatives. Instead, we estimate the instantaneous velocity at time $t$ using the **Central Difference Method**. 

This method calculates velocity by taking the difference in position between the time step immediately after ($t+1$) and the time step immediately before ($t-1$), and dividing by the total time elapsed (2 seconds):

$$v(t) = \frac{x(t+1) - x(t-1)}{2}$$

Applying this to our given data yields the following velocity estimates:

| Time (s) | Estimated Velocity (m/s) |
| :--- | :--- |
| 1 | 7.5 |
| 2 | 12.5 |
| 3 | 17.5 |
| 4 | 22.5 |

## 2. Acceleration Insight (Optional Extension)
To find the acceleration (the rate of change of velocity), we apply the Central Difference Method a second time, this time to the estimated velocity data we just calculated:

$$a(t) = \frac{v(t+1) - v(t-1)}{2}$$

* **At $t=2$:** $(17.5 - 7.5) / 2 = 5$ m/s²
* **At $t=3$:** $(22.5 - 12.5) / 2 = 5$ m/s²

**Insight:** Because the acceleration calculations yield the exact same result at different time steps, we can conclude that the vehicle is experiencing **uniformly accelerated motion** with a constant acceleration of $5$ m/s². 

## 3. Distance Verification
To verify our velocity estimates, we calculate the total distance traveled using the **Trapezoidal Rule** to approximate the area under the velocity-time curve between $t=1$ and $t=4$:

$$\text{Distance} \approx \frac{\Delta t}{2} \left[ v(1) + 2v(2) + 2v(3) + v(4) \right]$$
$$\text{Distance} \approx 0.5 \times \left[ 7.5 + 25 + 35 + 22.5 \right] = 45 \text{ meters}$$

We then compare this to the actual displacement calculated directly from the original position table:
$$\text{Displacement} = x(4) - x(1) = 50 - 5 = 45 \text{ meters}$$

**Conclusion:** The estimated distance using the Trapezoidal Rule perfectly matches the actual displacement ($45$ meters). This perfect match occurs because the vehicle's acceleration is constant, meaning the velocity increases linearly, resulting in zero estimation error from the trapezoids.

## 4. Visualization
Here is the graph of the **Position vs Time** and **Velocity vs Time**

<img width="1022" height="400" alt="c2graph" src="https://github.com/user-attachments/assets/c78a90cd-0e4a-435e-afc2-fbeabcd3bbe7" />


**Position vs. Time** ($x$ vs. $t$): This graph would look like a curve bending upwards (half of a parabola). The slope gets steeper as time goes on, representing the increasing velocity.

**Velocity vs. Time** ($v$ vs. $t$): If you plot the points (1, 7.5), (2, 12.5), (3, 17.5), and (4, 22.5), they will form a perfectly straight line trending upwards. The constant slope of this line represents the constant acceleration.

## 5. Analysis
Based on the computations above, we can conclude the following about the vehicle's traffic behavior:
* **When is the car accelerating?** The car is accelerating continuously throughout the observed timeframe. 
* **Is motion uniform?** The motion is not uniform (velocity is changing), but the *acceleration* is uniform. 
* **Identify any anomalies** (sudden jump)** There are no sudden jumps or anomalies in the dataset; the vehicle follows a predictable, mathematical pattern of constant acceleration.

## Conclusion

By applying numerical methods to discrete position data, we successfully reconstructed the vehicle's motion profile. Central Difference calculations revealed that the car's velocity steadily increased from 7.5 m/s to 22.5 m/s, driven by a constant acceleration of 5 m/s². Because this acceleration was uniform, estimating the total distance using the Trapezoidal Rule yielded exactly 45 meters—matching the vehicle's actual displacement with zero mathematical error. Ultimately, this case study proves that numerical techniques can accurately determine speed, acceleration, and distance without needing a continuous mathematical function.




# Case Study 3: Diffusion Process Simulation (Heat Spread)

## Overview
A metal rod is heated at one end. Engineers want to estimate how heat spreads along the rod over time using discrete 
measurements. 

Computatinal Task
- Approximate temperature gradient (derivative) 
- Estimate total heat distribution (integration) 
- Analyze diffusion behavior
  
## Given Data

| Position (cm) | Temperature (°C)  |
|:---:|:---:|
| 0 | 100 |
| 2 | 80 |
| 4 | 65 |
| 6 | 55 |
| 8 | 48 |
| 10 | 45 |

The methods used include the central difference method for derivatives and Simpson’s Rule (with trapezoidal correction) for integration.

# SUMMARY OF RESULTS

## Temperature Gradient
| Position (cm) | dT/dx (°C/cm))  |
|:---:|:---:|
| 2 | -8.75 |
| 4 | -6.25 |
| 6 | -4.25 |
| 8 | -2.50 |

The gradient is negative at all points, indicating that temperature decreases as distance from the heat source increases.

## Total Heat Distribution
The total heat along the rod (from 0 cm to 10 cm) was approximated as:
TOTAL HEAT ≈ 638.33
This value represents the area under the temperature curve, indicating the overall thermal energy distribution.

## Graphical Interpretation
Two graphs were generated:

## Temperature vs Position
Shows a decreasing curve that gradually flattens

<img width="640" height="480" alt="Temperature vs Position" src="https://github.com/user-attachments/assets/bc2c23cd-70a1-4ceb-b1ea-9578a63abc69" />

## Gradient vs Position
Shows decreasing magnitude of slope as distance increases

<img width="640" height="480" alt="Gradient vs Position" src="https://github.com/user-attachments/assets/dc479010-6433-4b67-a91b-c6f96cbb73fe" />

These graphs visually confirm the numerical findings.

## Analysis of Heat Diffusion Behavior
1. Where is heat transfer fastest?
Heat transfer (in this simplified interpretation) is fastest where the magnitude of the gradient |dT/dx| is largest.
From the computed gradient values:
At x = 2 cm,
dT/dx≈−8.75 °C/cm
This is the largest magnitude gradient among the interior points, indicating the steepest temperature drop.
Therefore, heat transfer is fastest near the heated end, particularly around 2 cm, and likely even closer to 0 cm (though endpoint gradients were not computed).

2. Does temperature decrease linearly?
No, the temperature does not decrease linearly.
If the temperature profile were linear: The gradient would remain constant

However, the computed gradients show:
−8.75→−6.25→−4.25→−2.50

This clearly indicates: The slope is changing and The curve is nonlinear. The temperature profile flattens as distance increases, which is characteristic of diffusion processes.

3. What happens farther from the heat source?
As we move farther from the heat source (toward 10 cm), the temperature decreases more gradually, causing the curve to flatten and the magnitude of the gradient to decrease. This indicates that the temperature becomes less sensitive to changes in position and that heat transfer slows down. Such behavior is consistent with diffusion phenomena, where the influence of the heat source weakens as the distance increases.

## Conclusion

The numerical analysis shows that heat transfer is strongest near the source and gradually weakens along the rod, the temperature distribution is nonlinear rather than uniform, and the system follows typical diffusion behavior in which temperature gradients decrease with distance, while numerical methods such as the central difference and Simpson’s Rule prove to be effective tools for analyzing physical systems using discrete data.





# Case Study 5: Electricity Consumption and Power Analysis

## Overview
A household records electric energy consumption (kWh) at different times of the day. Using only these discrete data points, we apply two numerical methods to analyze electricity usage:

- **Numerical Differentiation** — instantaneous power usage (rate of change)
- **Numerical Integration** — total energy consumed over time

## Given Data

| Time (hours) | Energy (kWh) |
|:---:|:---:|
| 0 | 0 |
| 2 | 1.5 |
| 4 | 3.5 |
| 6 | 6.0 |
| 8 | 9.0 |
| 10 | 13.0 |

> Step size: **h = 2 hours**

## Solution Approach

### Step 1 — Numerical Differentiation (Central Difference)

Power is the rate of change of energy with respect to time:

```
P(t) = dE/dt
```

Since we only have discrete data points (not a continuous function), we estimate power using the **Central Difference Formula**:

```
P(t) = [ E(t + h) - E(t - h) ] / (2 * h)
```

---

### Step 2 — Numerical Integration (Trapezoidal Rule)

To estimate the total area under the Energy vs. Time curve, we use the **Trapezoidal Rule**. This method connects each pair of data points with a straight line, forming trapezoid-shaped strips, and sums their areas.

**Single strip area:**
```
Area = (E(t0) + E(t1)) / 2 * h
```

**Full formula (shortcut):**
```
Total = (h/2) * [ E(0) + 2*E(2) + 2*E(4) + 2*E(6) + 2*E(8) + E(10) ]
```

> The middle values are multiplied by 2 because each interior point is shared between two neighboring strips — it acts as the right edge of one strip and the left edge of the next. Only the first and last points belong to a single strip, so they remain as-is.

We also apply the trapezoidal rule on the computed **P(t) values** to verify that the integral of power approximates total energy = 13 kWh.

---

## Expected Results

### Power Table (Step 1)

| Time (hrs) | E(t+h) | E(t-h) | Numerator | Denominator (2h) | Power (kW) |
|:---:|:---:|:---:|:---:|:---:|:---:|
| 2 | 3.5 | 0.0 | 3.5 | 4 | **0.875** |
| 4 | 6.0 | 1.5 | 4.5 | 4 | **1.125** |
| 6 | 9.0 | 3.5 | 5.5 | 4 | **1.375** |
| 8 | 13.0 | 6.0 | 7.0 | 4 | **1.750** |

---

### Integration Results (Step 2)

**Trapezoidal Rule on E(t):**

| Strip | Time Range | Calculation | Area (kWh·hr) |
|:---:|:---:|:---:|:---:|
| 1 | t = 0 → 2 | (0 + 1.5) / 2 × 2 | 1.50 |
| 2 | t = 2 → 4 | (1.5 + 3.5) / 2 × 2 | 5.00 |
| 3 | t = 4 → 6 | (3.5 + 6.0) / 2 × 2 | 9.50 |
| 4 | t = 6 → 8 | (6.0 + 9.0) / 2 × 2 | 15.00 |
| 5 | t = 8 → 10 | (9.0 + 13.0) / 2 × 2 | 22.00 |
| **Total** | | | **53.00 kWh·hr** |

**Trapezoidal Rule on P(t) (verification):**

```
= (2/2) * [ 0.875 + 2(1.125) + 2(1.375) + 1.750 ]
= 1 * [ 0.875 + 2.25 + 2.75 + 1.750 ]
= 7.625 kWh
```

> This does not perfectly equal 13 kWh. This is an expected limitation — since central difference cannot compute power at t = 0 and t = 10, those boundary contributions are missing from the integration, reducing the accuracy of the result.

---

## Analysis

| Question | Answer |
|---|---|
| When is electricity usage highest? | At **t = 8 hrs** with 1.750 kW, and still rising toward t = 10 |
| Is consumption steady or increasing? | **Accelerating** — power doubles from 0.875 to 1.750 kW over the period |
| Is the pattern linear or non-linear? | **Non-linear** — the energy curve bends upward, confirming accelerating growth |

**Suggestions to reduce peak usage:**
- Shift heavy appliances (washer, oven, dishwasher) to earlier hours (t = 0–4) when power usage is lowest
- Use smart timers or home automation to distribute energy load more evenly
- Install solar panels to offset rising energy demand in later hours
- Upgrade to energy-efficient appliances that draw less power during peak periods

---

## Graphs

- **Energy vs Time** — shows how total energy consumption grows over the 10-hour period
- **Power vs Time** — shows instantaneous power at each computed interior point

![Graphs](Visualizations/case_study_5_graphs.png)
