from CLT import CLT_pl
from Gaussian import Gaussian_CDF
import pandas as pd

df = pd.read_csv("Bengaluru_House_Data.csv")

new = Gaussian_CDF(df["price"])
print(new)