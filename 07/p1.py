# https://adventofcode.com/2021/
# day 7, puzzle 1
import math

with open('input.txt') as f:
  positions = [line.rstrip() for line in f]

all_crabs = list(map(lambda x: int(x), positions[0].split(',')))
best_cost = math.inf

for i in range(max(all_crabs)):
  costs = list(map(lambda x: abs(i-x), all_crabs))
  best_cost = sum(costs) if best_cost > sum(costs) else best_cost

answer = best_cost
print("Answer: %d" % answer)
