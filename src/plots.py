import matplotlib.pyplot as plt


def plot_speed_estimation(time, true_speed, measured_speed, estimated_speed):
    plt.figure(figsize=(10, 6))
    plt.plot(time, true_speed, label="True speed")
    plt.plot(time, measured_speed, label="Noisy measurement", alpha=0.6)
    plt.plot(time, estimated_speed, label="Kalman estimate")

    plt.title("DC Motor Speed Estimation with Kalman Filter")
    plt.xlabel("Time")
    plt.ylabel("Angular Velocity")
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.savefig("results/speed_estimation.png", dpi=300)
    plt.show()


def plot_estimation_error(time, true_speed, estimated_speed):
    error = true_speed - estimated_speed

    plt.figure(figsize=(10, 6))
    plt.plot(time, error)

    plt.title("Speed Estimation Error")
    plt.xlabel("Time")
    plt.ylabel("Error")
    plt.grid(True)
    plt.tight_layout()
    plt.savefig("results/estimation_error.png", dpi=300)
    plt.show()



def plot_noise_comparison(df):
    plt.figure(figsize=(10, 6))

    plt.plot(df["noise_std"], df["measurement_rmse"], marker="o", label="Noisy measurement RMSE")
    plt.plot(df["noise_std"], df["kalman_rmse"], marker="o", label="Kalman estimate RMSE")

    plt.title("RMSE Comparison Across Noise Levels")
    plt.xlabel("Measurement Noise Standard Deviation")
    plt.ylabel("RMSE")
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.savefig("results/noise_comparison.png", dpi=300)
    plt.show()




def plot_filter_comparison(time, true_speed, measured_speed, moving_average_speed, kalman_speed):
    plt.figure(figsize=(10, 6))

    plt.plot(time, true_speed, label="True speed")
    plt.plot(time, measured_speed, label="Noisy measurement", alpha=0.5)
    plt.plot(time, moving_average_speed, label="Moving average")
    plt.plot(time, kalman_speed, label="Kalman estimate")

    plt.title("Filter Comparison for DC Motor Speed Estimation")
    plt.xlabel("Time")
    plt.ylabel("Angular Velocity")
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.savefig("results/filter_comparison.png", dpi=300)
    plt.show()


def plot_filter_rmse_comparison(df):
    plt.figure(figsize=(10, 6))

    plt.plot(df["noise_std"], df["measurement_rmse"], marker="o", label="Noisy measurement")
    plt.plot(df["noise_std"], df["moving_average_rmse"], marker="o", label="Moving average")
    plt.plot(df["noise_std"], df["kalman_rmse"], marker="o", label="Kalman estimate")

    plt.title("RMSE Comparison of Filtering Methods")
    plt.xlabel("Measurement Noise Standard Deviation")
    plt.ylabel("RMSE")
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.savefig("results/filter_rmse_comparison.png", dpi=300)
    plt.show()



