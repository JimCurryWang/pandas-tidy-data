# -*- coding: utf-8 -*-

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# %%
df = pd.read_csv('data/pew.csv')
df = df.set_index('religion')
df = df.stack()
df.index = df.index.rename('income', level=1)
df.name = 'frequence'
df = df.reset_index()
df.head(10)

# %%
df = pd.read_csv('data/pew.csv')
df = pd.melt(df, id_vars=['religion'], value_vars=list(df.columns)[1:],
             var_name='income', value_name='frequency')
df = df.sort_values(by='religion')
df.head(10)

# %%
