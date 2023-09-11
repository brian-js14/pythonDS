import pandas as pd

df_exams = pd.read_csv('/home/brian/repos/pythonDS/StudentsPerformance.csv')
print(df_exams.head(2))
#Operaciones con columnas
#Selecciona una columna y realiza la suma total de la columna -- se usa el método .sum()
print(df_exams['math score'].sum())
#contar
print(df_exams['math score'].count())
#promedio
print(df_exams['math score'].mean())
#desv. estandar
print(df_exams['math score'].std())
#máximo y mínimo
print(df_exams['math score'].max())
print(df_exams['math score'].min())
#verificar los valores con el describe
print(df_exams.describe())
#desv. estandar -- se agrega al resultado redondear el número a dos cifras
print(round(df_exams['math score'].std(),3))
#Operaciones con filas
print(df_exams['math score'] +df_exams['reading score']+df_exams[ 'writing score'])
#calcular el score promedio y asignar los resultados en una nueva columna
df_exams['avg'] = (df_exams['math score'] +df_exams['reading score']+df_exams[ 'writing score'])/3
print(df_exams.head(2))