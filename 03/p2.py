# https://adventofcode.com/2021/
# day 3, puzzle 2

with open('input.txt') as f:
  diag = [line.rstrip() for line in f]

n = len(diag[0])
ox_candidates = diag
co2_candidates = diag

for i in range(n):
  bts_ox = [int(ox_candidates[x][i]) for x in range(len(ox_candidates))]
  cmp_ox = '0' if bts_ox.count(0) > bts_ox.count(1) else '1'
  if len(ox_candidates) > 1:
    ox_candidates = list(filter(lambda x: x[i] == cmp_ox, ox_candidates))

  bts_co2 = [int(co2_candidates[x][i]) for x in range(len(co2_candidates))]
  cmp_co2 = '1' if bts_co2.count(0) > bts_co2.count(1) else '0'
  if len(co2_candidates) > 1:
    co2_candidates = list(filter(lambda x: x[i] == cmp_co2, co2_candidates))

ox_rate = int(ox_candidates[0], 2)
co2_rate = int(co2_candidates[0], 2)
answer = ox_rate * co2_rate

print("Answer: %d" % answer)
