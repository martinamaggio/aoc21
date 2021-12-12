# https://adventofcode.com/2021/
# day 12, puzzle 2

# g: graph, s: starting node, e: ending node
def find_all_valid_paths(g, s, e, result=[]):

  result = result + [s]
  if s == e:  # we are done and reached the end
    return [result]

  paths = []
  for node in g[s]:  # explore successors

    # 0. we will not go back to the starting node
    # additionally, there are two conditions (in or) that allow us to explore the paths:
    # 1. the node we are adding is not lowercase (or is the end)
    # 2. the lowercase node satisfy the criterion (visited once etc)

    c0 = node != 'start'
    c1 = not node.islower() or node == 'end'
    c2 = (node not in result) or \
         (not any(result.count(x) > 1 for x in list(filter(lambda x: x.islower() and x != 'start', result))))

    if c0 and (c1 or c2):
      paths = paths + find_all_valid_paths(g, node, e, result)

  return paths


# parsing input
graph = {}
with open('input.txt') as f:
  for line in f:
    (n1, n2) = line.rstrip().split('-')
    graph.setdefault(n1, []).append(n2)
    graph.setdefault(n2, []).append(n1)

paths = find_all_valid_paths(graph, 'start', 'end')
answer = len(paths)
print("Answer: %d" % answer)
