import pandas as pd
from datetime import datetime
import numpy as np

# Input was created by the sh script 

# prepares the data and sorts
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

# Create and populate the answer table
ans_df = pd.DataFrame(columns=np.arange(0, 60, 1), index=df["ID"].unique())
ans_df.fillna(0, inplace=True)

for index in df[df["State"] == "asleep"].index:
    start_min = df.loc[index, "Date"].minute
    end_min = df.loc[index+1, "Date"].minute

    ans_df.loc[df.loc[index, "ID"], np.arange(start_min, end_min)] += 1

ans_df["SUM"] = ans_df.sum(axis=1)

sleepy_guard = ans_df["SUM"].idxmax()
minute = ans_df.drop("SUM", axis=1).loc[sleepy_guard, :].idxmax()

# Anwer to 1
print("Answer to 1")
print(int(minute) * int(sleepy_guard))

# Answer to 2
print("Answer to 2")
guard = ans_df.drop("SUM", axis=1).iloc[:, :-1].max(axis=1).idxmax()
minute = ans_df.drop("SUM", axis=1).loc[guard, :].idxmax()
print(int(guard)*int(minute))

