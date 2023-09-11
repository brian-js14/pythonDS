import pandas as pd
import numpy as np


#leyendo el archivo de CSV
df_exams = pd.read_csv('/home/brian/Downloads/StudentsPerformance.csv')
#obtener las 5 primeras filas del dataframe -- head -> Cabeza
df_exams.head()
print(df_exams)
print(df_exams.head())
#obtener las 5 ultimas filas del dataframe -- tail -> Cola
print(df_exams.tail())
#podemos especificar n cantidad de filas a mostrar -- se asigna el parámetro dentro del método head
print(df_exams.head(10))
#accediento al atributo shape
#mostrar n filas
print(pd.set_option('display.max_rows',100))
#muestra la información del dataFrame en formato(filas, columnas)
print(df_exams.shape)