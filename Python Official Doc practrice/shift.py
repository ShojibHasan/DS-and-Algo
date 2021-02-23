import numpy as np
import pandas as pd

df = pd.DataFrame({'C1': [20, 30, 25, 40, 55],
                   'C2': [23, 33, 18, 36, 58],
                   'C3': [27, 37, 21, 47, 62]})

df.shift(periods=3)
