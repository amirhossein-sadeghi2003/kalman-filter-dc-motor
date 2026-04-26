from simulate import generate_dataset
from kalman_filter import run_speed_kalman_filter
from baseline_filter import moving_average_filter
from evaluate import evaluate_noise_levels
from plots import (
    plot_speed_estimation,
    plot_estimation_error,
    plot_noise_comparison,
    plot_filter_comparison,
    plot_filter_rmse_comparison,
)


def main():
    df = generate_dataset()

    time = df["time"].values
    true_speed = df["true_speed"].values
    measured_speed = df["measured_speed"].values

    kalman_speed = run_speed_kalman_filter(measured_speed, dt=0.01)
    moving_average_speed = moving_average_filter(measured_speed, window_size=15)

    plot_speed_estimation(time, true_speed, measured_speed, kalman_speed)
    plot_estimation_error(time, true_speed, kalman_speed)
    plot_filter_comparison(time, true_speed, measured_speed, moving_average_speed, kalman_speed)

    noise_results = evaluate_noise_levels()
    plot_noise_comparison(noise_results)
    plot_filter_rmse_comparison(noise_results)

    print("Kalman filter estimation completed.")
    print("Saved results:")
    print("- results/speed_estimation.png")
    print("- results/estimation_error.png")
    print("- results/noise_comparison.png")
    print("- results/filter_comparison.png")
    print("- results/filter_rmse_comparison.png")
    print("- data/noise_comparison.csv")


if __name__ == "__main__":
    main()

