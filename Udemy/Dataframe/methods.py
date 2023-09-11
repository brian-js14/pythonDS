import pandas as pd

df_exams = pd.read_csv('/home/brian/Downloads/StudentsPerformance.csv')
#mostrar df:
print(df_exams)
#mostrando las primeras 5 filas, método head
print(df_exams.head())
#mostrando información del dataframe -- nos muestra rápidamente si existen datos nulos dentro del df
print(df_exams.info())
#obteniendo valores estadísticos del dataFrame
print(df_exams.describe())