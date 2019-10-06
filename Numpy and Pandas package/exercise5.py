import numpy as np
import pandas as pd

data = pd.read_csv('student.csv')
print(data)

data.to_pickle('student.pickle')