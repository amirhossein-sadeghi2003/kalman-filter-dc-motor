# Kalman Filter DC Motor

This project simulates a DC motor with noisy speed measurements and uses a Kalman Filter to estimate the true motor speed.

## Description

In real systems, sensor measurements are often noisy. This project shows how a Kalman Filter can be used to estimate the hidden or true state of a dynamic system from noisy measurements.

The project uses a simulated DC motor model. The true motor speed is generated from the model, artificial measurement noise is added, and then a Kalman Filter is applied to estimate the speed.

## Main Idea

The project compares three signals:

- true motor speed
- noisy measured speed
- Kalman Filter estimated speed

The goal is to show that the Kalman Filter can reduce measurement noise and provide a smoother and more accurate estimate of the motor speed.

## DC Motor Model

The DC motor model includes:

- armature current
- angular velocity
- angular position

The simplified dynamics are based on the electrical and mechanical equations of a DC motor.

The system uses parameters such as:

- resistance
- inductance
- back EMF constant
- torque constant
- inertia
- friction
- input voltage

## Project Pipeline

### 1. DC Motor Simulation

The motor model is simulated using a step voltage input.

The simulation generates:

- current
- true speed
- true position

### 2. Noisy Measurement Generation

Gaussian noise is added to the true speed signal to simulate noisy sensor measurements.

The noisy speed measurement is then used as the input to the Kalman Filter.

### 3. Kalman Filter Estimation

A Kalman Filter estimates the motor speed using the noisy speed measurements.

The filter uses a simple state model with:

- speed
- acceleration

### 4. Error Analysis

The project compares the raw noisy measurement error with the Kalman Filter estimation error.

The error is evaluated using RMSE.

### 5. Noise Level Comparison

The project also evaluates the Kalman Filter under different noise levels.

The tested noise standard deviations are:

- `0.2`
- `0.5`
- `1.0`
- `1.5`

## Results

The Kalman Filter reduces the estimation error compared to raw noisy measurements.

Noise comparison results:

| Noise STD | Measurement RMSE | Kalman RMSE | Improvement |
|---|---:|---:|---:|
| 0.2 | 0.196 | 0.090 | 54.03% |
| 0.5 | 0.489 | 0.190 | 61.21% |
| 1.0 | 1.015 | 0.362 | 64.35% |
| 1.5 | 1.475 | 0.461 | 68.73% |

These results show that the Kalman Filter becomes especially useful when measurement noise increases.

## Output Figures

The project generates the following result figures:

- `results/speed_estimation.png`
- `results/estimation_error.png`
- `results/noise_comparison.png`

## Main Files

Important files in this project:

- `src/model.py`
- `src/simulate.py`
- `src/kalman_filter.py`
- `src/evaluate.py`
- `src/plots.py`
- `src/main.py`

## How to Run

From the project root, activate the virtual environment and run:

`python src/main.py`

To run only the noise-level evaluation:

`python src/evaluate.py`

## Main Libraries

- `numpy`
- `scipy`
- `matplotlib`
- `pandas`
- `filterpy`

## Project Goal

The goal of this project is to connect dynamic system modeling, noisy sensor measurements, and state estimation.

This project is related to:

- control systems
- state estimation
- sensor noise filtering
- robotics
- embedded systems
- intelligent physical systems

## Future Work

Possible next steps:

- estimate both speed and position
- compare different Kalman Filter parameters
- add Extended Kalman Filter for nonlinear models
- compare Kalman estimates with moving-average filtering
- apply the method to real sensor data
