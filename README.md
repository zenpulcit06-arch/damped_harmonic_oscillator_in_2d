# 2D Damped Harmonic Oscillator Simulation

## Overview
This project presents a numerical simulation of a **two-dimensional damped harmonic oscillator** using classical mechanics.  
The system consists of a particle of mass `m` attached to independent springs along the **x** and **y** directions, with linear damping acting separately in each coordinate.

The equations of motion are solved numerically in **C**, and the resulting data is analyzed and visualized using **Python**.  
The damping coefficients are extracted from the decay of mechanical energy and compared with theoretical input values.

---

## Physical Model

The equations of motion are:

\[
m\ddot{x} + b_x \dot{x} + k_x x = 0
\]

\[
m\ddot{y} + b_y \dot{y} + k_y y = 0
\]

where:
- \( m \) is the mass of the particle
- \( k_x, k_y \) are spring constants
- \( b_x, b_y \) are damping coefficients

The total mechanical energy is:
\[
E = \frac{1}{2}m(v_x^2 + v_y^2) + \frac{1}{2}(k_x x^2 + k_y y^2)
\]

For a damped oscillator, energy decays exponentially:
\[
E(t) \propto e^{-2\gamma t}
\quad \text{with} \quad
\gamma = \frac{b}{2m}
\]

This relation is used to extract damping coefficients from simulation data.

---

## Numerical Method

- Time integration is performed using the **explicit Euler method**
- Time step `dt` is chosen small enough to ensure numerical stability
- Simulation outputs are written to CSV files for post-processing

---

## Code Structure

### C Simulation
- **File:** `simulation.c`
- Computes:
  - Position `(x, y)`
  - Velocity `(vx, vy)`
  - Acceleration `(ax, ay)`
  - Energy components `(E_x, E_y, E)`
- Outputs:
  - `data.csv` → time-dependent variables
  - `const.csv` → physical constants used

### Python Analysis
- **File:** `analysis.py`
- Tasks:
  - Plot spatial trajectory
  - Plot position vs time
  - Plot phase space
  - Plot energy decay
  - Perform linear fit of `ln(E)` vs `t`
  - Extract damping coefficients
  - Compute percentage error vs theoretical values

---

## Results

The simulation produces:
- Elliptical or spiral trajectories depending on damping
- Exponential decay of energy
- Linear behavior of `ln(E)` vs time
- Accurate recovery of damping coefficients within numerical error

A validation message is printed based on percentage error:
- **Excellent simulation** (≤ 2%)
- **Acceptable range** (2–10%)
- **Parameters need refinement** (> 10%)

---

## How to Run

### Compile and Run C Code
```bash
gcc simulation.c -o simulation -lm
./simulation
```
## Run Analysis
```bash
python analysis.py
```

## Dependencies
# c 
Standard C compiler (GCC)
# Python
numpy

pandas

matplotlib

```bash

Install with:

pip install numpy pandas matplotlib
```

## Learning Outcomes

Numerical solution of coupled ODEs

Energy-based damping analysis

Data-driven parameter extraction

Scientific plotting and validation

Separation of simulation and analysis pipelines

## Possible Extensions

Higher-order integration methods (Velocity Verlet, Runge–Kutta)

Coupled oscillators

Nonlinear damping

External driving forces

Phase difference analysis

## Author

Pulkit Jain
BS–MS Physics Student
