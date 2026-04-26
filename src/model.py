import numpy as np


def step_input(time, voltage=12.0):
    return voltage


def dc_motor_derivative(state, time, params):
    current = state[0]
    omega = state[1]
    theta = state[2]

    R = params["R"]
    L = params["L"]
    Ke = params["Ke"]
    Kt = params["Kt"]
    J = params["J"]
    b = params["b"]

    voltage = step_input(time, params["V"])

    didt = (voltage - R * current - Ke * omega) / L
    domegadt = (Kt * current - b * omega) / J
    dthetadt = omega

    return np.array([didt, domegadt, dthetadt])


def simulate_dc_motor(params, dt=0.01, total_time=5.0):
    time = np.arange(0, total_time, dt)

    states = np.zeros((len(time), 3))
    states[0] = np.array([0.0, 0.0, 0.0])

    for i in range(1, len(time)):
        derivative = dc_motor_derivative(states[i - 1], time[i - 1], params)
        states[i] = states[i - 1] + derivative * dt

    return time, states
