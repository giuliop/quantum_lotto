from itertools import combinations

# total_combinations = 622,614,630
numbers = range(1,91)
plays = combinations(numbers, 6)

with open("all_combinations", "w") as myfile:

    for i, p in enumerate(plays):
        s = [str(n) for n in p]
        myfile.write(' '.join(s) + '\n')

        if (i % 1000000) == 0:
            print("At line " + f"{i:,d}")
