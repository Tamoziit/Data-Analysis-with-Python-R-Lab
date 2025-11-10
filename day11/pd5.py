import pandas as pd
import numpy as np

df = pd.DataFrame(
    {
        'A': [1, 2, np.nan, 4],
        'B': [5, np.nan, 6, np.nan],
        'C': [np.nan, np.nan, 8, 9]
    }
)
print(df, "\n")

df2 = df.fillna(0)
print(df2, "\n")

df_ffill = df.ffill()
print("Filled using forward fill:")
print(df_ffill, "\n")

df_mean_filled = df.fillna(df.mean(numeric_only=True))
print("Filled with column mean:")
print(df_mean_filled, "\n")