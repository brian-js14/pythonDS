import pandas as pd

df_exams = pd.read_csv('/home/brian/Downloads/StudentsPerformance.csv')
#mostrar df:
print(df_exams)
#Atributo shapre
print(df_exams.shape)
#Atributo index -- Tiene la forma de un rango, estos tienen 2 argumentos escenciales [start, stop], step
print(df_exams.index)
#obteniendo acceso al atributo de columns -- se obtienen los nombres de las columnas
print(df_exams.columns)
#obteniendo el tipo de dato
print(df_exams.dtypes)