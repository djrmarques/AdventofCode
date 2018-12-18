from collections import Counter

# Read the file
file = "8/input"
# file = "8/test-input"
with open(file, "r") as f: 
    input =[int(a) for a in f.readline().rstrip().split()]  # rstrip to remove the \n at the end


# Test Data
# 2 3 0 3 10 11 12 1 1 0 1 99 2 1 1 2
# A----------------------------------
#     B----------- C-----------
#                      D-----

# 1+1+2+10+11+12+2+99=138

def serial(l):

    n_childs, n_meta = l[:2]
    l = l[2:]
    val = 0
    sum_metadata = 0

    m_data_list = []
    for child in range(n_childs):
        sum_child_mdata, valc, l = serial(l)
        sum_metadata += sum_child_mdata
        m_data_list.append(valc)

    metadata = l[:n_meta]
    meta_counter = Counter(metadata)
    sum_metadata += sum(metadata)

    for child in range(1, n_childs+1):
        if child in meta_counter.keys():
            val += (meta_counter[child] * m_data_list[child-1])

    if n_childs == 0:
        val = sum(metadata)

    return sum_metadata, val, l[n_meta:]

print(serial(input))
