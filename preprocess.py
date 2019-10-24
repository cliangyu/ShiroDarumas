# Preprocess data and plot

import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns
import json_tricks as json
from collections import OrderedDict
import os
import sys

# AVERAGE_CHILDREN_BY_AGE = pd.read_excel("Births and Fertility.xlsx", sheet_name="T1")
AVERAGE_CHILDREN_BY_EDUCATION = pd.read_excel("Births and Fertility.xlsx", sheet_name="T2")
BIRTHS_AND_FERTILITY = pd.read_excel("Births and Fertility.xlsx", sheet_name="T3")
# AVERAGE_CHILDREN = pd.read_excel("Births and Fertility.xlsx", sheet_name="T1")
MARRIAGE_RATE_BY_AGE = pd.read_excel("Marriage.xlsx", sheet_name="T2")
MARRIAGE_RATE_BY_AGE = pd.read_excel("Marriage.xlsx", sheet_name="T2")

AVERAGE_CHILDREN_BY_EDUCATION = AVERAGE_CHILDREN_BY_EDUCATION.iloc[5:12, 1:]
BIRTHS_AND_FERTILITY = BIRTHS_AND_FERTILITY.iloc[4:21, 1:]
MALE_MARRIAGE_RATE_BY_AGE = MARRIAGE_RATE_BY_AGE.iloc[5:17, 1:]
FEMALE_MARRIAGE_RATE_BY_AGE = MARRIAGE_RATE_BY_AGE.iloc[17:30, 1:]



print(BIRTHS_AND_FERTILITY)