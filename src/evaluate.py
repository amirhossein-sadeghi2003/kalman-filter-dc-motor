import numpy as np
import pandas as pd

from model import simulate_dc_motor
from simulate import add_measurement_noise
from kalman_filter import run_speed_kalman_filter


def compute_rmse(true_values, predicted_values):
    error = true_values - predicted_values
    return np.sqrt(np.mean(error ** 2))


def evaluate_noise_levels(output_path="data/noise_comparison.csv"):
    np.random.seed(42)

    params = {
        "R": 2.0,
        "L": 0.5,
        "Ke": 0.1,
        "Kt": 0.1,
        "J": 0.02,
        "b": 0.2,
        "V": 12.0,
    }

    dt = 0.01
    total_time = 5.0
    noise_levels = [0.2, 0.5, 1.0, 1.5]

    time, states = simulate_dc_motor(params, dt=dt, total_time=total_time)
    true_speed = states[:, 1]

    rows = []

    for noise_std in noise_levels:
        measured_speed = add_measurement_noise(true_speed, noise_std=noise_std)
        estimated_speed = run_speed_kalman_filter(measured_speed, dt=dt)

        measurement_rmse = compute_rmse(true_speed, measured_speed)
        kalman_rmse = compute_rmse(true_speed, estimated_speed)

        improvement_percent = 100 * (measurement_rmse - kalman_rmse) / measurement_rmse

        rows.append(
            {
                "noise_std": noise_std,
                "measurement_rmse": measurement_rmse,
                "kalman_rmse": kalman_rmse,
                "improvement_percent": improvement_percent,
            }
        )

    df = pd.DataFrame(rows)
    df.to_csv(output_path, index=False)

    print(f"Noise comparison saved to {output_path}")
    print(df)

    return df


if __name__ == "__main__":
    evaluate_noise_levels()
