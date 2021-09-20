# -*- coding: utf-8 -*-
"""
Created on Mon Sep 20 14:57:37 2021

@author: mrzhe
"""

import pandas as pd

data = pd.read_feather("data.feather")
print(data.groupby("type").size())

print(data.groupby("sourceName").size())
