import pandas as pd

df_exams = pd.read_csv('/home/brian/Downloads/StudentsPerformance.csv')
#llamar los encabezados del archivo csv + las 5 primeras filas
#print(df_exams.head())
#seleccionar 2 columnas o más columnas
print(df_exams[['gender','math score','reading score', 'writing score']].head(1))