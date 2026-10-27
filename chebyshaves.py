import numpy as np
import pandas as pd
import math as m


# chebyshaves Inequality

def chebyshaves_inequality(data,k):
    meu = np.mean(data)
    sig = np.std(data)

    low = meu - k*sig
    high = meu + k*sig

    percentage = (1 - 1/k**2)*100

    return (low,high),percentage
