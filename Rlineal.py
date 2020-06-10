#Libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = '\Resources\food_truck_data.txt'

#Load data
df  = pd.read_txt(data)
df.head()

#metrics 
df.info()
df.describe()

ax = sns.scatterplot(x='Population', y='Profit',  data= data)
ax.set_title('Población por millones de habitantes vs Profit en miles de dolares')






