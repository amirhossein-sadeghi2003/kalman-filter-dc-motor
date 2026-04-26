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
