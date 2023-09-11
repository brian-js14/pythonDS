import pandas as pd

df_exams = pd.read_csv('/home/brian/Downloads/StudentsPerformance.csv')
#llamar los encabezados del archivo csv + las 5 primeras filas
print(df_exams.head())
#Seleccionar una columna con []
print(df_exams['gender'])
#revisar el tipo de data de una columna -- se identifica que es una serie, esta comparte unos atributos y métodos con un DF
print(type(df_exams['gender']))
#Al validar el atributo index para la columna gender se identifica que comparte el atributo con el DF
print(df_exams['gender'].index)
print(df_exams['gender'].head())

#seleccionar una columna con "." no es muy utilizado porque no distingue los espacios
print(df_exams.gender)