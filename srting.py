import pandas as pd
v=pd.read_csv("F:\set5-TravelMode.csv")
print(v.sort_values("gcost",ascending=False))