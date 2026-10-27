from CLT import CLT_pl
from Gaussian import Gaussian_CDF
from chebyshaves import chebyshaves_inequality
import pandas as pd

df = pd.read_csv("Bengaluru_House_Data.csv")

new = chebyshaves_inequality(df["price"],2)
print(new)