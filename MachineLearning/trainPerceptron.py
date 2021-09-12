import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


df = pd.read_csv('https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data', header=None)
# print(df.tail())

y = df.iloc[0:100, 4].values
print(y)
