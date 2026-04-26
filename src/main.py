from simulate import generate_dataset
from kalman_filter import run_speed_kalman_filter
from plots import plot_speed_estimation, plot_estimation_error, plot_noise_comparison
from evaluate import evaluate_noise_levels


def main():
    df = generate_dataset()

    time = df["time"].values
    true_speed = df["true_speed"].values
    measured_speed = df["measured_speed"].values

    estimated_speed = run_speed_kalman_filter(measured_speed, dt=0.01)

    plot_speed_estimation(time, true_speed, measured_speed, estimated_speed)
    plot_estimation_error(time, true_speed, estimated_speed)

    noise_results = evaluate_noise_levels()
    plot_noise_comparison(noise_results)

    print("Kalman filter estimation completed.")
    print("Saved results:")
    print("- results/speed_estimation.png")
    print("- results/estimation_error.png")
    print("- results/noise_comparison.png")
    print("- data/noise_comparison.csv")


if __name__ == "__main__":
    main()
