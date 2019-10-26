# Preprocess data and plot

import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns
import json_tricks as json
from collections import OrderedDict
import os
import sys

sns.set(style="darkgrid")

# AVERAGE_CHILDREN_BY_AGE = pd.read_excel("Births and Fertility.xlsx", sheet_name="T1")
AVERAGE_CHILDREN_BY_EDUCATION = pd.read_excel("Births and Fertility.xlsx", sheet_name="T2")
BIRTHS_AND_FERTILITY = pd.read_excel("Births and Fertility.xlsx", sheet_name="T3")
# AVERAGE_CHILDREN = pd.read_excel("Births and Fertility.xlsx", sheet_name="T1")
MARRIAGE_RATE_BY_AGE = pd.read_excel("Marriage.xlsx", sheet_name="T2")
# MARRIAGE_RATE_BY_AGE = pd.read_excel("Marriage.xlsx", sheet_name="T2")

AVERAGE_CHILDREN_BY_EDUCATION = AVERAGE_CHILDREN_BY_EDUCATION.iloc[4:12, 1:]
BIRTHS_AND_FERTILITY = BIRTHS_AND_FERTILITY.iloc[4:21, 1:]
MALE_MARRIAGE_RATE_BY_AGE = MARRIAGE_RATE_BY_AGE.iloc[5:17, 1:]
FEMALE_MARRIAGE_RATE_BY_AGE = MARRIAGE_RATE_BY_AGE.iloc[17:30, 1:]

x=AVERAGE_CHILDREN_BY_EDUCATION.iloc[0,:]
# print(x)

AVERAGE_CHILDREN_BY_EDUCATION = AVERAGE_CHILDREN_BY_EDUCATION.astype(np.float64)
print(AVERAGE_CHILDREN_BY_EDUCATION.dtypes)


plot1 = sns.lineplot(data=AVERAGE_CHILDREN_BY_EDUCATION, x=AVERAGE_CHILDREN_BY_EDUCATION.iloc[0],
                     y=AVERAGE_CHILDREN_BY_EDUCATION.iloc[1],)
plot1.set_title('AVERAGE_CHILDREN_BY_EDUCATION')
plot1.set_ylabel('avaerage birth rate')
plot1.set_xlabel('year')

fig1 = plot1.get_figure()
fig1.savefig("output_1.png")

# print(BIRTHS_AND_FERTILITY)