import pandas as pd
from datetime import datetime
import numpy as np

# Prepares the data and sorts
df = pd.read_csv("4/input",sep=" ", header=None)
df[0] = df[0] + " " + df[1]
df.drop(1, axis=1, inplace=True)
df[0] = df[0].apply(lambda x: datetime.strptime(x, "%Y-%m-%d %H:%M"))
df.sort_values(0, inplace=True)


df[3] = df[2].apply(lambda x: x.isnumeric())
i = df[df[3] == True].index
df.loc[i, 3] = df.loc[i, 2]
df[3].replace(0, np.nan, inplace=True)
df[3].fillna(method="ffill", inplace=True)
df.drop(df[df[2] == df[3]].index, axis=0, inplace=True)
df.reset_index(inplace=True, drop=True)
df.columns = ["Date", "State", "ID"]

# Find the time
for index in df[df["State"] == "asleep"].index:
    sleeptime = df.loc[index+1, "Date"] - df.loc[index, "Date"]
    df.drop(index+1, axis=0 ,inplace=True)
    df.loc[index, "Date"] = sleeptime

df.drop("State", axis=1, inplace=True)

# Answer
df.groupby("ID").sum().sort_values("Date").tail(1)

