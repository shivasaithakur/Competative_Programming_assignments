# 1
# 3 50
# 60 10
# 100 20
# 120 30

# output 240.000000

def fractional_knapsack(items, capacity):
    # Sort items by value/weight ratio in descending order
    items.sort(key=lambda x: x[0] / x[1], reverse=True)

    total_value = 0.0

    for value, weight in items:
        if capacity == 0:
            break

        if weight <= capacity:
            # Take whole item
            total_value += value
            capacity -= weight
        else:
            # Take fraction of item
            fraction = capacity / weight
            total_value += value * fraction
            capacity = 0

    return total_value


# Driver code
T = int(input())
for _ in range(T):
    N, W = map(int, input().split())

    items = []
    for _ in range(N):
        V, Wi = map(int, input().split())
        items.append((V, Wi))

    result = fractional_knapsack(items, W)
    print(f"{result:.6f}")
