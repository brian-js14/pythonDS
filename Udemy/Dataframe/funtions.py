import pandas as pd

df_exams = pd.read_csv('/home/brian/Downloads/StudentsPerformance.csv')
#obtener el tamaño del dataframe(filas)
print(len(df_exams))
#obtener el max index
print(max(df_exams.index))
#obtener el minimo index
print(min(df_exams.index))
#obtener el tipo de dato del DF -- el tipo de data es dataFrame
print(type(df_exams))
#redondear valores del dataFrame -- funciona cuando tenemos valores decimales
print(round(df_exams, 2))