import numpy as np


def moving_average_filter(signal, window_size=15):
    filtered = []

    for i in range(len(signal)):
        start = max(0, i - window_size + 1)
        window = signal[start:i + 1]
        filtered.append(np.mean(window))

    return np.array(filtered)
