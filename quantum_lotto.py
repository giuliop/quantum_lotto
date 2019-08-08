import argparse
from itertools import combinations

parser = argparse.ArgumentParser()
parser.add_argument("binary", help="a binary string indicating a series of universe splits :)")
args = parser.parse_args()

numbers = range(1,91)
plays = combinations(numbers, 6)
max = 622614630

n = int(args.binary, 2) % max

for i, p in enumerate(plays):
    if i == n:
        print('\rThe winning combinations is: ' + " ".join([str(x) for x in p]))
        break

    if (i % 1000000) == 0:
        print('\rCombinations countdown: ' + f"{(n-i):,d}", end='')
