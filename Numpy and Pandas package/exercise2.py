import pandas as pd
import numpy as np

dates = pd.date_range('20130101',periods=6)
df = pd.DataFrame(np.arange(24).reshape(6,4),index=dates,
                  columns=['A','B','C','D'])
# print(df['A'])
# print(df.A)
# print(df[0:3])
# print(df['20130102':'20130104'])

# select by label:loc
# print(df.loc['20130102',['A','B']])

# select by position:iloc
# print(df.iloc[[1,3,5],1:3])

# mixed selection:ix
# print(df.ix[:3, ['A','C']])

# Boolean indexing
print(df)
print(df[df.A > 8])