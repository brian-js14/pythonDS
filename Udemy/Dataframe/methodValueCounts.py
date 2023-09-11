import pandas as pd

df_exams = pd.read_csv('/home/brian/repos/pythonDS/StudentsPerformance.csv')
#contar los elementos en la columna gender
print(len(df_exams['gender']))
#método .count()
print(df_exams['gender'].count())
#contar elementos "gender" por categoria -- se agrupa por cada género y los cuenta -- como un groupBy
print(df_exams['gender'].value_counts())
#obtener la frec relativa(dividir todos los valores entre la suma total y obtener su porcentaje)
print(df_exams['gender'].value_counts(normalize=True))#muestra el porcentaje de los valores que representa el total
#contar los elementos por categoria que hay en esta columna
print(df_exams['parental level of education'].value_counts())
#obtener la proporción de c/categoria
print(df_exams['parental level of education'].value_counts(normalize=True))
#mostrar df:
print(df_exams.head(1))