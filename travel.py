import pandas as pd
v=pd.read_csv("F:\set5-TravelMode.csv")
x=v.loc[(v["mode"]=="air") & (v["choice"]=="no")]
y=v.loc[v["choice"]=="yes"]
y=y.drop_duplicates(["individual"])
print(y.to_string())