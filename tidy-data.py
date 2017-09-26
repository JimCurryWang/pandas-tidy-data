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
df = pd.read_csv('data/billboard.csv')
df = pd.melt(df, id_vars=list(df.columns)[:5], value_vars=list(df.columns)[5:],
             var_name='week', value_name='rank')
df['week'] = df['week'].str[2:].astype(int)
df['date.entered'] = pd.to_datetime(df['date.entered']) + pd.to_timedelta((df['week'] - 1) * 7, 'd')
df.columns.values[4] = 'date'
df

# %%
