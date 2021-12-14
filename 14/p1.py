# https://adventofcode.com/2021/
# day 14, puzzle 1

rules = dict()
characters = dict()
steps = 10

# parsing input
with open('input.txt') as f:
  content = [line.rstrip() for line in f]

polymer = content[0]
for x in content[2:len(content)]:
  start, end = x.split("->")[0].rstrip(), x.split("->")[1].lstrip()
  rules[start] = end

# initialising character count
for x in polymer:
  characters[x] = 1 if x not in characters else characters[x] + 1

for i in range(steps):

  new_polymer = polymer[0]
  for x in range(len(polymer)-1):
    first, second = polymer[x], polymer[x+1]
    pair = first + second

    if pair in rules:
      c = rules[pair]
      characters[c] = 1 if c not in characters else characters[c] + 1
      new_polymer += c

    new_polymer += second
  polymer = new_polymer

answer = max(characters.values()) - min(characters.values())
print("Answer: %d" % answer)
