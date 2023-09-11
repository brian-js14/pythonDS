import pandas as pd

df_exams = pd.read_csv('/home/brian/Downloads/StudentsPerformance.csv')
#ordenar el DataFrame por una columna -- por defecto se genera ascendente
print(df_exams.sort_values('math score').head(2))
#ordenar el DataFrame por una columna de forma descendente
print(df_exams.sort_values('math score', ascending=False).head(2))
#ordenar el Dataframe según multiples columnas
print(df_exams.sort_values(['math score','reading score'], ascending=False).head(2))
#ordenar el Dataframe según multiples columnas y actualizar DF -- se agrega el elemento inplace
print(df_exams.sort_values(['math score','reading score'], ascending=False, inplace=True))
#orden descendiente con una función key
print(df_exams.sort_values('race/ethnicity', ascending=True, key=lambda col:col.str.lower()))
