# experiments.py
# Runs empirical test of randomized vs deterministic selection

import time
import random
import csv
import os

from selection import kth_smallest_randomized, kth_smallest_deterministic

RESULTS_DIR = "results"
os.makedirs(RESULTS_DIR, exist_ok=True)

DISTRIBUTIONS = ["random", "sorted", "reversed", "few_unique"]


def generate(n, dist):
    if dist == "random":
        return [random.randint(0, 10**9) for _ in range(n)]
    if dist == "sorted":
        return list(range(n))
    if dist == "reversed":
        return list(range(n))[::-1]
    if dist == "few_unique":
        return [random.randint(0, 10) for _ in range(n)]
    raise ValueError("Unknown distribution")


def time_alg(func, arr, k):
    start = time.perf_counter()
    func(arr, k)
    return time.perf_counter() - start


def run_once(n, dist):
    arr = generate(n, dist)
    k = n // 2

    t_rand = time_alg(kth_smallest_randomized, arr, k)
    t_det = time_alg(kth_smallest_deterministic, arr, k)

    return [n, dist, k, t_rand, t_det]


def run_series(sizes=[1000, 5000, 10000], trials=3):
    file = os.path.join(RESULTS_DIR, "selection_results.csv")

    with open(file, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["n", "distribution", "k", "randomized_time", "deterministic_time"])

        for n in sizes:
            for dist in DISTRIBUTIONS:
                for _ in range(trials):
                    row = run_once(n, dist)
                    writer.writerow(row)
                    print("Completed:", row)

    print("Results saved to:", file)


if __name__ == "__main__":
    run_series()
