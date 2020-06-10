# RLineal
Este repositorio espera mostrar como construir un modelo predictivo con numpy y otras herramientas para la elaborar una regresión lineal de una variable.

# Librerias

``` python 
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
```


# Preprocesing
```python
df  = pd.read_txt(data)
df.head() 
```
![](img/head.JPG)

Ahora podemos revisar algunas métricas con 

```python
df.info()
df.describe()
```
![](img/describe.JPG)

``` python 
ax = sns.scatterplot(x='Population', y='Profit', data = df)
ax.set_title('Profit vs Population')

![](img/grap_1.JPG)

<img src="http://www.sciweavers.org/tex2img.php?eq=%24%24J%28%5Ctheta%29%20%3D%20%5Cfrac%7B1%7D%7B2m%7D%20%5Csum_%7Bi%3D1%7D%5Em%20%28h_%5Ctheta%28x%5E%7B%28i%29%7D%29%20-%20y%5E%7B%28i%29%7D%20%29%5E2%24%24&bc=White&fc=Black&im=jpg&fs=12&ff=arev&edit=0" align="center" border="0" alt="$$J(\theta) = \frac{1}{2m} \sum_{i=1}^m (h_\theta(x^{(i)}) - y^{(i)} )^2$$" width="249" height="28" />




