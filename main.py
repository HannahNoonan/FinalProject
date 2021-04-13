import numpy as np
import pandas as pd
import matplotlib as plt

dataset = pd.read_csv("amazon bestsellers.csv")

print(dataset)

### check null values
print(dataset.isnull().sum())

print(dataset.sort_values("Year"))