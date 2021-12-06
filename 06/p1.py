# https://adventofcode.com/2021/
# day 6, puzzle 1

with open('input.txt') as f:
  population = [line.rstrip() for line in f]

num_days = 80

fish = list(map(lambda x: int(x), population[0].split(",")))
num = list(map(lambda x: fish.count(x), range(9)))

for i in range(num_days):
  num = [num[1], num[2], num[3], num[4], num[5], num[6], num[7]+num[0], num[8], num[0]]

answer = sum(num)
print("Answer: %d" % answer)
