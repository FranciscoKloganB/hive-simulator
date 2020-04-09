import logging

import numpy as np
import matplotlib.pyplot as plt

from typing import Tuple, Union
from scipy.stats import skewnorm


def generate_skewed_samples(sample_count: int = 10000, skewness: float = -90.0) -> np.array:
    """
    Generates samples from a skewed normal distribution.
    Note:
     If you use this sample generation, simply select pick up the elements and assign them to a label in sequence.
     In this case sample_count is just the number of samples I wish to take. See difference w.r.t extended version
    :param int sample_count: the number of skewed samples to be drawn
    :param float skewness: where peak density will be found. (-) values are left skewed, (+) values are right skewed
    :return np.array samples: drawn from skewed normal distribution
    """
    results = skewnorm.rvs(a=skewness, size=sample_count)  # Skew norm function
    results = results - min(results)  # Shift the set so the minimum value is equal to zero
    results = results / max(results)  # Normalize all the values to be between 0 and 1.
    results = results * 100.0         # Multiply the standardized values by the maximum value.
    return results


def generate_skewed_samples_extended(bin_count: int = 7001, sample_count: int = 10000, skewness: float = -90.0) -> Tuple[np.array, np.array]:
    """
    Generates samples from a skewed normal distribution.
     bin_count at 7001 represents all values between [30.00, 100.00] with 0.01 step
     bin_count at 800001 would represents all values between [20.0000, 100.000] with 0.0001 step, and so on...
     To let matplotlib.skewnorm module define an automatic number of bins use bin_count='auto'
     Keeping bins_count = sample_count is just an hack to facilitate np.random.choice(bins_count, sample_count)
     Because we are using bin_counts here, it is advised not to draw to many results, as the function will be
     exponentially slower
    :param int bin_count: the number of bins to be created in the matplotlib.pyplot.hist.bins
    :param int sample_count: the number of skewed results to be drawn
    :param float skewness: where peak density will be found. (-) values are left skewed, (+) values are right skewed
    :returns Tuple[np.array, np.array] results, bin_probability: sample and respective probability of occurring
    """
    results: np.array = generate_skewed_samples(sample_count, skewness)
    bin_density, bins, patches = plt.hist(results, bins=bin_count, density=True)

    size: int = len(bin_density)

    total_density: float = 0.0
    for i in range(size):
        total_density += bin_density[i]

    total_probability: float = 0.0
    bin_probability = bin_density
    for i in range(size):
        bin_probability[i] = bin_density[i] / total_density
        total_probability += bin_probability[i]

    if total_probability != 1.0:
        logging.warning("probability_compensation: " + str(1.0 - total_probability))

    return results, bin_probability


def plot_uptime_distribution(bin_count: Union[int, str] = 'auto', skewness: float = -60.0) -> None:
    results: np.array = generate_skewed_samples(skewness=skewness)
    plt.hist(results, bin_count, density=True)
    plt.title("Peer Uptime Distribution")
    plt.xlabel("Time Spent Online")
    plt.ylabel("Frequency")
    plt.xlim(0.0, 100.0)
    plt.show()


if __name__ == "__main__":
    """
    Displays generate_skewed_samples in a two axis plot
    :param Union[int, str] surveys: the number of bins to be depicted in the matplotlib.pyplot.hist plot
    :param int sample_count: the number of skewed samples to be drawn
    :param float skewness: where peak density will be found. (-) values are left skewed, (+) values are right skewed
    """
    samples: np.array = generate_skewed_samples(skewness=float(input("input skewness: ")))
    plt.hist(samples, 'auto', density=True)
    plt.title("Peer Uptime Distribution")
    plt.xlabel("Time Spent Online")
    plt.ylabel("Frequency")
    plt.xlim(0.0, 100.0)
    plt.show()
