import pandas as pd
import numpy as np

dates = pd.date_range('20130101',periods=6)
df = pd.DataFrame(np.arange(24).reshape(6,4),index=dates,
                  columns=['A','B','C','D'])

df.iloc[2,2] = 1111
df.loc['20130101','B'] = 2222
df.B[df.A > 4] = 0
df['F'] = np.nan
# Add one column
df['E'] = pd.Series(range(6),index=pd.date_range('20130101',periods=6))
print(df)