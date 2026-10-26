import pandas as pd
import numpy as np
import math as m
import matplotlib.pyplot as plt 
import seaborn as sns
from scipy.stats import norm

# central limit therom

def CLT_pl(Data,no_of_sample,sample_size):
    res = []

    for i in range(no_of_sample):
        sample = np.random.choice(Data,size=sample_size, replace=True)
        res.append(np.mean(sample))

    data = np.array(res)
    return data