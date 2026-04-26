import numpy as np
import pandas as pd

from model import simulate_dc_motor


def add_measurement_noise(signal, noise_std=0.5):
    noise = np.random.normal(0, noise_std, size=len(signal))
    return signal + noise


def generate_dataset(output_path="data/dc_motor_noisy_data.csv"):
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

    time, states = simulate_dc_motor(params, dt=dt, total_time=total_time)

    current = states[:, 0]
    true_speed = states[:, 1]
    true_position = states[:, 2]

    measured_speed = add_measurement_noise(true_speed, noise_std=0.5)

    df = pd.DataFrame(
        {
            "time": time,
            "current": current,
            "true_speed": true_speed,
            "true_position": true_position,
            "measured_speed": measured_speed,
        }
    )

    df.to_csv(output_path, index=False)
    print(f"Dataset saved to {output_path}")

    return df


if __name__ == "__main__":
    generate_dataset()

