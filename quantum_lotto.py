import argparse
from itertools import combinations

parser = argparse.ArgumentParser()
parser.add_argument("filename",
        help="a file containing a series of universe splits as lines of 0 and 1 :)")
args = parser.parse_args()

numbers = range(1,91)
plays = combinations(numbers, 6)
max = 622614630

with open(args.filename, 'r') as f:
    n = f.read().replace('\n', '')

n = '000100011010111101011000010111'
n = int(n, 2) % max

for i, p in enumerate(plays):
    if i == n:
        print('\rThe winning combinations is: ' + " ".join([str(x) for x in p]))
        print('\n')
        break

    if (i % 1000000) == 0:
        print('\rCombinations countdown: ' + f"{(n-i):,d}", end='')
