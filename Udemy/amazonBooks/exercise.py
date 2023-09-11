import pandas as pd
import numpy as np
import random


# Opcional: usa el pd.set_option() para mostrar todas las filas de un dataframe por defecto
pd.set_option('display.max_rows',100)
print(pd.get_option("display.max_rows"))

#1.Crear un DataFrame
df_AwsBooksSales = pd.DataFrame()
print(type(df_AwsBooksSales))
# acceder al atributo shape -- retorna la cantidad de columnas y número de filas encontradas
print(df_AwsBooksSales.shape)
# leer el archivo csv "bestsellers with categories" (data sobre los 50 libros más vendidos de Amazon de 2009 a 2019.)
df_AwsBooksSales = pd.read_csv('/home/brian/repos/pythonDS/bestsellers+with+categories.csv')
# encontrar el tipo de data de cada columna
print(df_AwsBooksSales.dtypes)

#2 Mostrar un DataFrame
print(df_AwsBooksSales)
# mostrar primeras 5 filas de un dataframe
print(df_AwsBooksSales.head())
# encontrar valores estadisticos de un dataframe (mean, std, min, max)
print(df_AwsBooksSales.describe())

#3. Agregar una nueva columna
# Tu tarea es crear una columna llamada 'Critic Rating' que deberia tener numeros random enteros entre 1 y 4
df_AwsBooksSales['Critic Rating'] = random.randint(1, 4)
print(df_AwsBooksSales)
# 3.1.importar numpy y crear 550 numeros random enteros entre 1 y 4
cr_random = np.random.randint(1, 4, size=550)
# 3.2.agregar nueva columna 'Critic Rating' al dataframe usando los numeros random creados
df_AwsBooksSales['Critic Rating'] = cr_random
# Obs: Los numeros aleatorios en la columna 'Critic Rating' seran diferentes entre tu solucion y la mia, pero vamos a concetrarnos en el codigo en esta seccion.
# mostrar 5 primeras filas
print(df_AwsBooksSales.head())

#4.Atributos, Metodos y Funciones Basicas
# acceder al atributo "columns"
print(df_AwsBooksSales.columns)
#5.Seleccionar 2 o Mas Columnas de un Dataframe
print(df_AwsBooksSales[['Name', 'Author', 'User Rating', 'Reviews', 'Price']].head(1))
# mover la columna 'Critic Rating' entre las columnas "User Rating" y "Reviews" Luego actualizar el dataframe
df_AwsBooksSales = df_AwsBooksSales[['Name', 'Author', 'User Rating', 'Critic Rating', 'Reviews', 'Price', 'Year', 'Genre']]
# Tip: Copiar y pegar los nombres de columna obtenidos con el atributo "columns" y reordenar los elementos usando [[]]
# mostrar 5 primeras filas
print(df_AwsBooksSales.head())

#6. Operaciones en Dataframes
# crear una columna llamada "Average Rating" usando la sigueinte formula: Average Rating = (User Rating + Critic Rating)/2
# usar la funcion "round" para redondear los valores del dataframe a 1 decimal y actualizar el dataframe
df_AwsBooksSales['Average Rating'] = round((df_AwsBooksSales['User Rating'] + df_AwsBooksSales['Critic Rating']/2),1)
print(df_AwsBooksSales['Average Rating'])

#7. Contar valores
# contar elementos en columna "Genre" por categoria y devolver la frecuencia relativa
print(df_AwsBooksSales['Genre'].value_counts(normalize=True))
#8.Renombrar Columnas
# renombrar columnas "User Rating," "Critic Rating" y "Average Rating" a "UR," "CR" y "AR" Luego actualizar el dataframe con el parametro "inplace"
df_AwsBooksSales.rename(columns={'User Rating':'UR',
                                 'Critic Rating': 'CR',
                                 'Average Rating': 'AR'},inplace=True)
# mostrar 5 primeras filas
print(df_AwsBooksSales.head())
# seleccionar solo columnas "Name", "Author", "UR", "CR", "AR" y "Year" y actualizar el dataframe
print(df_AwsBooksSales[['Name','Author','UR','CR','AR','Year']].head(1))

#9. Ordenar el dataframe
# ordenar el dataframe en forma descendente segun las columnas "UR" y "CR"
df_AwsBooksSales.sort_values(['UR','CR'],ascending=False, inplace=True)
print(df_AwsBooksSales.head(10))

