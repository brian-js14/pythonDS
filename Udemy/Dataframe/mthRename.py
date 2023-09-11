import pandas as pd

df_exams = pd.read_csv('/home/brian/repos/pythonDS/StudentsPerformance.csv')
#renombrar una columna y sobreescribir los valores del df
df_exams.rename(columns={'gender':'Gender_pro'})
#renombrar y reemplazar el dataFrame -- parámetro inplace
df_exams.rename(columns={'math score':'MS', 
                         'reading score':'RS',
                         'writing score':'WS'}, inplace=True)
#renombrar index 0, 1, 2 y actualizar el df
df_exams.rename(index={0:'A', 1:'B', 2:'C'}, inplace=True)
#mostrar DF:
print(df_exams.head(5))