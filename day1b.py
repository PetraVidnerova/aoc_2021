import pandas as pd

df = pd.read_csv("input", header=None)
df.columns = ["value"]
df["sum"] = df["value"].rolling(3).sum()
df["res"] = df["sum"] < df["sum"].shift(-1)

print(df["res"].sum())
