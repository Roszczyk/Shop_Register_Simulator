import matplotlib.pyplot as plt


def plot_simulation_results(simulation_results : dict, sample_size : int):
    N_values = sorted(simulation_results.keys())
    results = [simulation_results[N] for N in N_values]

    plt.figure(figsize=(10, 6))
    plt.plot(N_values, results, marker="o", linestyle="-")

    plt.title(f"Simulation results for {sample_size} customerss")
    plt.xlabel("N strategy")
    plt.ylabel("Time elapsed")
    plt.xticks(N_values)
    plt.grid(True, alpha=0.3)

    plt.tight_layout()
    plt.show()