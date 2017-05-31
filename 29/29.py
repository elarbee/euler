def distinct_combinations(low,high):
    combinations = []
    a = range(low, high+1)
    b = range(low, high+1)
    for i in a:
        for j in b:
            combinations.append(i**j)
    distinct_combos = set(combinations)
    return len(distinct_combos)

print distinct_combinations(2,100)
