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
```

Este es el diagrama de dispersión
![](img/grap_1.JPG |width ) 

Ahora calculemos la funcíon de pérdida  para iniciar nuestra regresión

![](img/Latex_1.JPG)



