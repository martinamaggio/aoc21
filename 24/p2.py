import math


def run():
  data = [line.split() for line in open("input.txt")]
  params = []
  for i in range(0, 18 * 14, 18):
    p1 = int(data[i + 4][-1])   # A
    p2 = int(data[i + 5][-1])   # B
    p3 = int(data[i + 15][-1])  # C
    params.append((p1, p2, p3))

  # After analysing the code, this is the function performed on each input
  def f(params, z, w):
    if (z % 26 + params[1]) != w:
      z = math.floor(z/params[0]) * 26 + w + params[2]
    else:
      z = math.floor(z/params[0])
    return z

  zs = {0: [0, 0]}
  for i, p in enumerate(params):
    new_zs = {}
    for z, inp in zs.items():
      for w in range(1, 10):
        new_z = f(p, z, w)

        if p[0] == 1 or (p[0] == 26 and new_z < z):
          if new_z not in new_zs:
            new_zs[new_z] = [inp[0] * 10 + w, inp[1] * 10 + w]
          else:
            new_zs[new_z][0] = min(new_zs[new_z][0], inp[0] * 10 + w)
            new_zs[new_z][1] = max(new_zs[new_z][1], inp[1] * 10 + w)

    zs = new_zs
  return zs


answer = run()[0][0]
print("Answer: %d" % answer)
