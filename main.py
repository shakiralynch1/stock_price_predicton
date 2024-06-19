import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# Load the data
data = pd.read_csv('Google_Stock_Price_Test.csv')
data = data.iloc[:, 1:2].values
print(data)