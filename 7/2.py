from collections import defaultdict

file = "7/awkedinput"

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
workers = 5

current_jobs = {}               # Jobs currently being done

# Start by the ones that do not have precedence
while all or current_jobs:
    # E is a dict that contains the precedences for action
    # If some letter is in all but not on E that means that that job
    # has no predecence and therefore can be done in the present turn
    nodes = sorted([a for a in all if a not in E.keys()])

    # Assign job to workers
    for job in nodes[:workers]:
        current_jobs[job] = 60 + time_dict[job]
        workers -= 1

        # Remove job from all
        del all[all.index(job)]

    if workers < 0:
        raise Exception("Negative Workers: {}".format(workers))

    # Decrement time in current jobs
    del_current = []
    if current_jobs:
        for key, val in current_jobs.items():
            # Delete jobs that are finished
            if val == 1:
                del_current.append(key)
            elif val > 1: 
                current_jobs[key] = val - 1
            else: 
                raise Exception("Error deleting current jobs")

    # Remove finished jobs
    for job in del_current:
        del current_jobs[job]
        L.append(job)
        workers += 1

        # Remove the assigned jobs from E
        del_E = []
        for key, val in E.items():
            if (val[0] == job) and (len(val) == 1):
                del_E.append(key)

            elif job in val:
                del val[val.index(job)]
                E[key] = val

        for k in del_E:
            del E[k]

    time += 1

    # print("TIME: ", time)
    # print("ALL: ", all)
    # print("AvailableWorks: ", nodes)
    # print("E: ", E)
    # print("NWorkers: ", workers)
    # print("CurrentWork: ", current_jobs)
    # print("L: ", L)
    # print("")
time
