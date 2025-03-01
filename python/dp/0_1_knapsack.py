# Base case:
# Either no items (i == 0) or no capacity (capacity == 0)
#
# Recursive relation:
#   Exclude:
#       max_value[i][capacity] = max_value[i - 1][capacity] 
#
#   Include:
#       max_value[i][capacity] = max_value[i - 1][capacity - weight[i]] + value[i]
#
#   max_value[i][capacity] = max(include, exclude)


def knapsack_rec(i, W, values, weights, memo):
    if i <= 0 or W <= 0:
        return 0
    
    if memo[i][W] != None:
        return memo[i][W]
    
    # Exclude:
    exclude = knapsack_rec(i - 1, W, values, weights, memo)

    # Include:
    include = knapsack_rec(i - 1, W - weights[i - 1], weights, values, memo)

    memo[i][W] = max(include, exclude)

    return memo[i][W]


def knapsack_tab(values, weights, capacity):
    n = len(weights)
    memo = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]

    for i in range(n + 1):
        for c in range(capacity + 1):
            if i == 0 or c == 0:
                memo[i][c] = 0
            elif weights[i - 1] <= c:
                memo[i][c] = max(memo[i - 1][c], \
                                 memo[i - 1][c - weights[i - 1]] + values[i - 1])
            else:
                memo[i][c] = memo[i - 1][c]

    return memo[n][capacity]


# Test case
values = [60, 100, 120]
weights = [10, 20, 30]
capacity = 50

max_value = knapsack_tab(values, weights, capacity)