import pandas as pd
import numpy as np
import random

df_exams = pd.read_csv('/home/brian/repos/pythonDS/StudentsPerformance.csv')

#crear valores no repetitivos para los index
new_index = np.arange(0, 1000)
print(new_index)
#Barajar/desordenar los indices -- con el método shuffle se  desornenan
random.shuffle(new_index)
print(new_index)
#Crear una nueva columna con los nuevos index
df_exams['new_index'] = new_index
print(df_exams.head(3))
#método set para fijar una columna como index
df_exams.set_index('new_index')
#método set para fijar una columna como index y actualizar el df -- Asegurarse que el index no tenga valores duplicados
df_exams.set_index('new_index',inplace=True)
print(df_exams.head(2))

#Ordenando valores duplicados -- dataFrame por el new_index
print(df_exams.sort_index())
#Ordenando valores duplicados -- dataFrame por el new_index de forma descendente
print(df_exams.sort_index(ascending=False))
