import pandas as pd
import numpy as np

df_exams = pd.read_csv('/home/brian/Downloads/StudentsPerformance.csv')
#agregar una nueva columna al dataFrame -- se agrega con un valor constante
df_exams['language score'] = 70
#mostrar df con los datos de la primera fila:
print(df_exams.head(1))
#Agregar una nueva columna con un array
#Crear un array con 1000 elementos, para hacer el array se debe conocer el número de elementos del df
#A través del método arange se crea un array con un rango definido
language_score = np.arange(0, 1000)
#Vamos a sobreescribir los valores de la columna language score -- de este modo asignamos los valores con una sec de 0 hasta 999
df_exams['language score'] = language_score
print(df_exams.head(1))
#Ahora lo haremos con el método random de numpy y randint para crear números enteros aleatorios con la finalidad de definir la nota aleatoria entre 1 y 100
int_language_score = np.random.randint(1, 100, size=1000)
print(min(int_language_score))
print(max(int_language_score))
df_exams['language score'] = int_language_score
print(df_exams.head(5))
#crear número decimales aleatorios entre 1 y 100
np.random.uniform(1, 100, size=1000)