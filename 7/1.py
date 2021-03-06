from collections import defaultdict

file = "7/awkedinput"
# file = "7/test-input"

all = []              # This will store all the letters
E = defaultdict(list) # Each entry is a list
L = []                # Solution

# Read all into a dict to get the V without any edges
with open(file, "r") as f:
    for line in f.readlines():
        x, y = line.split()
        all.append(x)
        all.append(y)
        E[y].append(x)

all = sorted(list(set(all)))

# Start by the ones that do not have precedence
while all:
    # Next letter 
    nodes = [a for a in all if a not in E.keys()]
    nv = sorted(nodes)[0]

    # Remove nv from all
    del all[all.index(nv)]

    del_E = []
    # Remove all nv from the dictionary
    for key, val in E.items():
        if (val[0] == nv) and (len(val) == 1):
            del_E.append(key)
        elif nv in val:
            del val[val.index(nv)]
            E[key] = val
    try:
        for k in del_E:
            del E[k]
    except: 
        pass

    L.append(nv)

print("Part 1: ")
print("".join(L))
print("")

