# Topological Sorting!
# L ← Empty list that will contain the sorted elements
# S ← Set of all nodes with no incoming edge
# while S is non-empty do
#     remove a node n from S
#     add n to tail of L
#     for each node m with an edge e from n to m do
#         remove edge e from the graph
#         if m has no other incoming edges then
#             insert m into S
# if graph has edges then
#     return error   (graph has at least one cycle)
# else 
#     return L   (a topologically sorted order)

from collections import defaultdict

file = "7/awkedinput"
file = "7/test-input"

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

    # Remove all nv from the dictionary
    del_list = []
    for key, val in E.items():
        if val[0] == nv:
            del_list.append(key)
    for key in del_list:
        del E[key]

    print(E)
    L.append(nv)
print(L)
