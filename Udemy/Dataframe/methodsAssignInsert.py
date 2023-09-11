import pandas as pd
import numpy as np

df_exams = pd.read_csv('/home/brian/repos/pythonDS/StudentsPerformance.csv')
#crear número aleatorios para nuestra nueva columna "score"
score1 = np.random.randint(1, 100, size=1000)
score2 = np.random.randint(1, 100, size=1000)
#crear una serie usando los números aleatorios
series1 = pd.Series(score1, index=np.arange(0, 1000))
series2 = pd.Series(score2, index=np.arange(0, 1000))
print(series1)
#usando assign() para agregar múltiples columnas
df_exams = df_exams.assign(score1=series1, score2=series2)
print(df_exams.head(2))
#Usar el método insert para agregar una columna en una posición específica
df_exams.insert(1, 'test', series1)
print(df_exams.head(2))
