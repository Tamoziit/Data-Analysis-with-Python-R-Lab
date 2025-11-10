import pandas as pd

data = {'a': 100, 'b': 200, 'c': 300,'d': 400}
print(data)
print(data.keys())
print(data.values())
print(max(data, key = data.get), "\n")

srs = pd.Series(data)
print(srs, "\n")

srs2 = pd.Series(data, index = ['d','b','e','a'])
print(srs2, "\n")
print(srs.isnull())
print(srs.notnull())
print(srs2.isnull())
print(srs2.notnull())