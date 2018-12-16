import pandas as pd
import numpy as np
from scipy.spatial import distance
import itertools

# Target Coordinates
file = "6/input"
c = np.loadtxt(file, delimiter=",")

# Max and minimium values 
xmax, ymax = c.max(axis=0)
xmin, ymin = c.min(axis=0)

# Create coord values
xspace = np.arange(xmin, xmax+1)
yspace = np.arange(ymin, ymax+1)

# Target Coordinates
targets = np.array(list(itertools.product(xspace, yspace)))

# distance
d = distance.cdist(c, targets, metric="cityblock")

# Closeste coordinate
dmin = np.argmin(d, axis=0).reshape(xspace.shape[0], yspace.shape[0])

# Remove values on the border (infinite)
ignore_list = np.unique(np.concatenate(
    [np.unique(dmin[0]), np.unique(dmin[-1]), np.unique(dmin[:, 0]), np.unique(dmin[:, -1]), [-1]]))

# Minimum distance
min_distances = np.min(d, axis=0)
competing_locations_filter = (d == min_distances).sum(axis=0) > 1

dmin[competing_locations_filter.reshape(xspace.shape[0], yspace.shape[0])] = -1

# Answer to Part 1
val, count = np.unique(dmin, return_counts=True)
final_count = np.ma.array(count, mask=False)
final_count.mask[(np.isin(val, ignore_list))] = True
print("Answer to Part 1:\n{}\n".format(final_count.max()))

# Part 2
d_sum = d.sum(axis=0)
area = (d_sum < 10000).flatten().sum()
print("Asnwer to Part 2:\n{}".format(area))

