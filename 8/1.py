# Read the file
file = "8/input"
file = "8/test-input"

# Test Data
# 2 3 0 3 10 11 12 1 1 0 1 99 2 1 1 2
# A----------------------------------
#     B----------- C-----------
#                      D-----

# 1+1+2+10+11+12+2+99=138


with open(file, "r") as f: 
    input = f.readline().rstrip().split()  # rstrip to remove the \n at the end

meta_sum = 0
def sum_metadata(l, meta_sum):
    metadata_sum = 0
    n_child = l[0]
    n_metadata = l[1]
    
    # If has node childs get metadata from them
    if n_child > 0:
        # Cycles every child
        for child in range(n_child):
            

    # No childs, get metadata
    elif n_child == 0:
        return sum(l[1:n_metadata+1])

    return metadata_sum

sum_metadata(input, meta_sum)

def recur_test(i=0):
    ''' Testing recursion '''
    i += 1
    print(i)
    if i == 5:
        return i
    else:
        return i + recur_test(i)

