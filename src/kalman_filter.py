import numpy as np
from filterpy.kalman import KalmanFilter


def run_speed_kalman_filter(measured_speed, dt=0.01):
    kf = KalmanFilter(dim_x=2, dim_z=1)

    # State: [speed, acceleration]
    kf.x = np.array([[0.0], [0.0]])

    kf.F = np.array(
        [
            [1.0, dt],
            [0.0, 1.0],
        ]
    )

    kf.H = np.array([[1.0, 0.0]])

    kf.P = np.eye(2) * 10.0
    kf.R = np.array([[0.25]])
    kf.Q = np.array(
        [
            [0.01, 0.0],
            [0.0, 0.01],
        ]
    )

    estimated_speed = []

    for z in measured_speed:
        kf.predict()
        kf.update(np.array([[z]]))
        estimated_speed.append(kf.x[0, 0])

    return np.array(estimated_speed)

