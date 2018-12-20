# Based on an answer from
# https://www.reddit.com/r/adventofcode/comments/a5eztl/2018_day_12_solutions/

import matplotlib.pyplot as plt
import numpy as np

file = "12/input"
# file = "12/test-input"

with open(file, "r") as f:
    lines = f.readlines()
    init = lines[0].strip()

    pats = set()
    for line in lines[1:]:
        pat, res = line.split()
        if res == '#':
            pats.add(pat)

used_pots = set(i for i, a in enumerate(init) if a == '#')

def next_gen(pot_n, pat_list):
    ''' Returns the used pot number of the next generation '''
    start = min(pot_n)
    end = max(pot_n)
    x = set()

    for i in range(start - 3, end + 4):
        pat = ''.join('#' if i + k in pot_n else '.' for k in [-2, -1, 0, 1, 2])
        if pat in pat_list:
            x.add(i)

    return x


# Part 2
# Try to find a pattern, a perios of time where the pattern repeats
n_its = 200
val_list = [0] * n_its
len_list = [0] * n_its
time = 0
while time < n_its:
    used_pots = next_gen(used_pots, pats)

    val_list[time] = sum(used_pots)
    time += 1

# # Part 1
# gen_lim = 20
# for _ in range(gen_lim):
#     used_pots = next_gen(used_pots, pats)
# print(sum(used_pots))

# Part 2
val = 50000000000
diff = np.array(val_list)[1:] - np.array(val_list)[:-1]
ans = (val - n_its) * plot_diff[-1] + val_list[-1]
print(ans)

