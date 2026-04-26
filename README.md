# Kalman Filter DC Motor

This project simulates a DC motor with noisy speed measurements and uses a Kalman Filter to estimate the true motor speed.

It also compares the Kalman Filter with a simple Moving Average baseline to evaluate how different filtering methods behave under different noise levels.

## Description

In real systems, sensor measurements are often noisy. This project shows how filtering methods can be used to estimate the true state of a dynamic system from noisy measurements.

The project uses a simulated DC motor model. The true motor speed is generated from the model, artificial measurement noise is added, and then two filtering methods are applied:

- Kalman Filter
- Moving Average Filter

## Main Idea

The project compares four signals:

- true motor speed
- noisy measured speed
- Moving Average estimate
- Kalman Filter estimate

The goal is to show how filtering can reduce measurement noise and improve speed estimation.

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

The noisy speed measurement is used as the input to both filters.

### 3. Kalman Filter Estimation

A Kalman Filter estimates the motor speed using noisy speed measurements.

The filter uses a simple state model with:

- speed
- acceleration

### 4. Moving Average Baseline

A Moving Average Filter is also applied as a simple baseline method.

This baseline helps compare the Kalman Filter against a basic smoothing technique.

### 5. Error Analysis

The project compares the raw noisy measurement error, Moving Average error, and Kalman Filter error.

The error is evaluated using RMSE.

### 6. Noise Level Comparison

The project evaluates filtering performance under different measurement noise levels.

The tested noise standard deviations are:

- `0.2`
- `0.5`
- `1.0`
- `1.5`

## Results

The Kalman Filter and Moving Average Filter both reduce the estimation error compared to raw noisy measurements.

Noise comparison results:

| Noise STD | Measurement RMSE | Moving Average RMSE | Kalman RMSE | Moving Average Improvement | Kalman Improvement |
|---|---:|---:|---:|---:|---:|
| 0.2 | 0.196 | 0.132 | 0.090 | 32.75% | 54.03% |
| 0.5 | 0.489 | 0.201 | 0.190 | 58.94% | 61.21% |
| 1.0 | 1.015 | 0.277 | 0.362 | 72.70% | 64.35% |
| 1.5 | 1.475 | 0.360 | 0.461 | 75.62% | 68.73% |

The results show that:

- both filters improve estimation compared to raw noisy measurements
- the Kalman Filter performs better for lower and moderate noise levels in this setup
- the Moving Average baseline performs better for higher noise levels with the current Kalman tuning
- Kalman Filter performance depends on proper tuning of process noise and measurement noise parameters

This makes the project a small but useful comparison study of state estimation and signal filtering for a dynamic system.

## Output Figures

The project generates the following result figures:

- `results/speed_estimation.png`
- `results/estimation_error.png`
- `results/noise_comparison.png`
- `results/filter_comparison.png`
- `results/filter_rmse_comparison.png`

## Main Files

Important files in this project:

- `src/model.py`
- `src/simulate.py`
- `src/kalman_filter.py`
- `src/baseline_filter.py`
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

The goal of this project is to connect dynamic system modeling, noisy sensor measurements, state estimation, and baseline filtering.

This project is related to:

- control systems
- state estimation
- sensor noise filtering
- robotics
- embedded systems
- intelligent physical systems

## Future Work

Possible next steps:

- tune Kalman Filter parameters for different noise levels
- estimate both speed and position
- compare with exponential moving average filtering
- add Extended Kalman Filter for nonlinear models
- apply the method to real sensor data
