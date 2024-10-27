import random
import matplotlib.pyplot as plt

def monte_carlo_simulation(num_rolls):
    sum_counts = {i: 0 for i in range(2, 13)}
    
    for _ in range(num_rolls):
        die1 = random.randint(1, 6)
        die2 = random.randint(1, 6)
        dice_sum = die1 + die2
        sum_counts[dice_sum] += 1
    
    probabilities = {s: (count / num_rolls) * 100 for s, count in sum_counts.items()}
    return probabilities

def plot_probabilities(probabilities, analytical_probs):
    sums = list(probabilities.keys())
    sim_probs = list(probabilities.values())
    ana_probs = [analytical_probs[s] for s in sums]

    plt.figure(figsize=(10, 6))
    plt.bar(sums, sim_probs, width=0.4, label='Метод Монте-Карло', alpha=0.7)
    plt.bar([s + 0.4 for s in sums], ana_probs, width=0.4, label='Аналітичні ймовірності', alpha=0.7)
    plt.xlabel('Сума')
    plt.ylabel('Ймовірність (%)')
    plt.title('Порівняння ймовірностей суми двох кубиків')
    plt.legend()
    plt.show()

analytical_probs = {
    2: 2.78,
    3: 5.56,
    4: 8.33,
    5: 11.11,
    6: 13.89,
    7: 16.67,
    8: 13.89,
    9: 11.11,
    10: 8.33,
    11: 5.56,
    12: 2.78
}

num_rolls = 1_000_000
simulation_results = monte_carlo_simulation(num_rolls)

plot_probabilities(simulation_results, analytical_probs)

print("Ймовірності, отримані за методом Монте-Карло:")
for sum_value, prob in simulation_results.items():
    print(f"Сума {sum_value}: {prob:.2f}%")
