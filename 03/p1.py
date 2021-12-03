# https://adventofcode.com/2021/
# day 3, puzzle 1

with open('input.txt') as f:
  diag = [line.rstrip() for line in f]

n = len(diag[0])
gamma_rate_str = ''
epsilon_rate_str = ''

for i in range(n):
  bts = [int(diag[x][i]) for x in range(len(diag))]
  if bts.count(1) > bts.count(0):
    gamma_rate_str += '1'
    epsilon_rate_str += '0'
  else:
    gamma_rate_str += '0'
    epsilon_rate_str += '1'

gamma_rate = int(gamma_rate_str, 2)
epsilon_rate = int(epsilon_rate_str, 2)
answer = gamma_rate * epsilon_rate

print("Answer: %d" % answer)
