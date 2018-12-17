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

time = 0
time_dict = dict(zip((all), [a for a in range(1, len(all) + 1)]))
workers = 2

current_jobs = {}               # Jobs currently being done

# Start by the ones that do not have precedence
while all:
    # Next letter 
    # Available jobs 
    # E is a dict that contains the precedences for action
    # If some letter is in all but not on E that means that that job
    # has no predecence and therefore can be done in the present turn
    nodes = sorted([a for a in all if a not in E.keys()])

    # Decrement time in current jobs, if there are current jobs
    completed_jobs = []

    if len(current_jobs.keys()) > 0:
        for key in current_jobs.keys():
            current_jobs[key] -= 1
            if current_jobs[key] == 0:
                completed_jobs.append(key)

        # Remove completed jobs from dict and add them to L 
        # by alphabetic order
        for cjob in completed_jobs:
            L.append(cjob)
            del current_jobs[cjob]
            workers += 1

    # Checks if there are jobs and workers available
    if workers > 0 and len(nodes) > 0:
    # Assign workers to jobs
        for job in nodes[:workers]:
            # Add 60 here afterwards
            current_jobs[job] = time_dict[job]
            workers -= 1            # Decrement workers

    # remove completed jobs from E and all
    for nv in L:
        # Remove nv from all
        if nv in all:
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

    # Increment time
    time += 1

    print("TIME: ", time)
    print("CurrentJobs: ", current_jobs)
    print("AvailableJobs:", nodes)
    print("Nworkers: ", workers)
    print("All: ", all)
    print("L: ", L)
    print("E: ", E)
    print("")

    if time > 5:break

