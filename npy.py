import pandas as pd
import numpy as np
v=pd.read_csv("F:\set5-TravelMode.csv")
m=v["income"]
n=m.to_numpy()
k=np.array(n)
print(k.sum())