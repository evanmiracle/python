# test import of iris
import pandas as pd

df = pd.read_csv('https://archive.ics.uci.edu/ml/'
        'machine-learning-databases/iris/iris.data', header=None)
data_tail_check = df.tail()

print(data_tail_check)