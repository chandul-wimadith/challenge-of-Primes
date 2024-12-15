import matplotlib.pyplot as plt
from new import sum_of_even_primes
from plusprime import even_numbers

import matplotlib.pyplot as plt

def plot_even_vs_sum_of_primes(even_numbers, sum_of_even_primes):
    plt.figure(figsize=(10, 6))
    plt.scatter(even_numbers, even_numbers, color='blue', label='Even Numbers', s=100, alpha=0.6)
    plt.plot(even_numbers, sum_of_even_primes, color='red', label='Cumulative Sum of Primes', linewidth=2)
    plt.xlabel('Even Numbers', fontsize=14)
    plt.ylabel('Cumulative Sum of Primes', fontsize=14)
    plt.title('Comparison of Even Numbers and Cumulative Sum of Primes', fontsize=16)
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()
plot_even_vs_sum_of_primes(even_numbers, sum_of_even_primes)
