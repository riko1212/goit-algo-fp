def greedy_algorithm(items, budget):
    sorted_items = sorted(items.items(), key=lambda x: x[1]['calories'] / x[1]['cost'], reverse=True)
    
    total_cost = 0
    total_calories = 0
    selected_items = []

    for item, info in sorted_items:
        if total_cost + info['cost'] <= budget:
            selected_items.append(item)
            total_cost += info['cost']
            total_calories += info['calories']

    return selected_items, total_cost, total_calories

def dynamic_programming(items, budget):
    n = len(items)
    dp = [[0 for _ in range(budget + 1)] for _ in range(n + 1)]
    item_names = list(items.keys())

    for i in range(1, n + 1):
        item = item_names[i - 1]
        cost = items[item]['cost']
        calories = items[item]['calories']

        for w in range(1, budget + 1):
            if cost <= w:
                dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - cost] + calories)
            else:
                dp[i][w] = dp[i - 1][w]

    selected_items = []
    total_calories = dp[n][budget]
    w = budget

    for i in range(n, 0, -1):
        if dp[i][w] != dp[i - 1][w]:
            selected_items.append(item_names[i - 1])
            w -= items[item_names[i - 1]]['cost']

    total_cost = sum(items[item]['cost'] for item in selected_items)

    return selected_items, total_cost, total_calories

items = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350}
}

budget = 100

# Використання жадібного алгоритму
greedy_result = greedy_algorithm(items, budget)
print("Жадібний алгоритм:")
print(f"Обрані страви: {greedy_result[0]}")
print(f"Загальна вартість: {greedy_result[1]}")
print(f"Загальна калорійність: {greedy_result[2]}")

# Використання динамічного програмування
dp_result = dynamic_programming(items, budget)
print("\nДинамічне програмування:")
print(f"Обрані страви: {dp_result[0]}")
print(f"Загальна вартість: {dp_result[1]}")
print(f"Загальна калорійність: {dp_result[2]}")
