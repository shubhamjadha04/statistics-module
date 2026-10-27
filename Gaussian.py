import numpy as np
import pandas as pd
import math as m

# Gaussian CDF
def Gaussian_CDF(data):
    result=[]
    meu=np.mean(data)
    sd=np.std(data)
    for i in data:
        a1=(i-meu)/(np.sqrt(2)*sd) 
        ans=1/2*(1+m.erf(a1)) 
        result.append(ans) 
    return np.array(result) 