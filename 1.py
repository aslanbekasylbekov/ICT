import numpy as np
import sklearn.linear_model as skmod
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_parquet("Data_to_analyse.parquet")
df_select = df[df]