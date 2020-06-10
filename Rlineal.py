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

#
def cost_function(X, y, theta):
    m = len(y)
    y_pred = X.dot(theta)
    error = (y_pred - y) ** 2
    
    return 1 / (2 * m) * np.sum(error)

m = df.Population.values.size
X = np.append(np.ones((m, 1)), df.Population.values.reshape(m, 1), axis=1)
y = df.Profit.values.reshape(m, 1)
theta = np.random.rand(2,1)

cost_function(X, y, theta)






