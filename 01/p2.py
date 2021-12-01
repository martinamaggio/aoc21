# https://adventofcode.com/2021/
# day 1, puzzle 2

with open('input.txt') as f:
  depths = [int(line.rstrip()) for line in f]
sliding = map(lambda i: depths[i] + depths[i+1] + depths[i+2], range(0, len(depths)-2))

data = list(sliding)  # using sliding window on depths as data
deeper = map(lambda i: 1 if data[i-1] < data[i] else 0, range(1, len(data)))
answer = sum(deeper)
print('Answer: %d' % answer)
