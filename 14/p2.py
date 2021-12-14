# https://adventofcode.com/2021/
# day 14, puzzle 2

rules = dict()
cc = dict()  # character count
pc = dict()  # pair count
steps = 40

# parsing input
with open('input.txt') as f:
  content = [line.rstrip() for line in f]

polymer = content[0]
for x in content[2:len(content)]:
  start, end = x.split("->")[0].rstrip(), x.split("->")[1].lstrip()
  rules[start] = end

for x in polymer:
  cc[x] = 1 if x not in cc else cc[x] + 1  # character count
for x in range(len(polymer)-1):
  pair = polymer[x] + polymer[x+1]
  pc[pair] = 1 if pair not in pc else pc[pair] + 1  # pair count

for i in range(steps):

  pc_next = dict()

  for p in pc.keys():  # p will cycle through all the pairs in the polymer
    if p in rules:  # if I hape a rule for p then I need to apply it
      nc = rules[p]  # new char to add
      cc[nc] = pc[p] if nc not in cc else cc[nc] + pc[p]  # adding new char to count
      np1, np2 = p[0] + nc, nc + p[1]  # counting pairs with the two new pairs
      pc_next[np1] = pc[p] if np1 not in pc_next else pc_next[np1] + pc[p]
      pc_next[np2] = pc[p] if np2 not in pc_next else pc_next[np2] + pc[p]
    else:  # no rule for p, just bringing p it with me
      pc_next[p] = pc[p]

  pc = pc_next

answer = max(cc.values()) - min(cc.values())
print("Answer: %d" % answer)
