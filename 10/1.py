import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

file = "10/sed_input"
# file = "10/sed_test_input"

df = pd.read_csv(file, delimiter=r"\s+", names=["x", "y", "dx", "dy"])

init_time = 0
time = 0
df['x'] = df['x'] + (init_time*df['dx'])
df['y'] = df['y'] + (init_time*df['dy'])
d_min = 100000000000000000000000000000000000000000
while 1:

    # Apply changes to matrix
    df['x'] = df['x'] + df['dx']
    df['y'] = df['y'] + df['dy']

    max_x, max_y = df[['x', 'y']].max()
    min_x, min_y = df[['x', 'y']].min()

    # Dimension 
    d = (max_x - min_x) * (max_y - min_y)
    if d < d_min:
        d_min = d
        time += 1
    elif d > d_min:
        print(time - 1)
        # Apply changes to matrix
        df['x'] = df['x'] - df['dx']
        df['y'] = df['y'] - df['dy']

        fig = plt.figure()
        ax = plt.gca()
        plt.scatter(df['x'], df['y'])
        ax.invert_yaxis()

        plt.show()

        break
