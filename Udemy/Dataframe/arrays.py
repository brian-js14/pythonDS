import pandas as pd
import numpy as np

#creando un array
data = np.array([[1,4],[2,5],[3,4]])

#creando un dataframe
df = pd.DataFrame(data, columns=['col1', 'col2'])
#print(df)

#creando un array en forma de lista
dataLista = [[1,4],[2,5],[3,4]]

#creando un df en forma de lista
dfLista = pd.DataFrame(dataLista, columns=['col1', 'col2'])
#print(dfLista)

#creando un array en forma de diccionario
states = ['California','Texas','Florida','NY']
population = [39615, 53318,218889,19299981]

#Almacenando listas en un diccionario
dict_states = {'States':states, 'Population':population}

#creando un df con base al diccionario
df_population = pd.DataFrame(dict_states)
#print(df_population)

#Leyendo archivos csv -- se lee a través de la librería de pandas
#Los archivos que tienen formato csv se conocen como dataset
df_exams = pd.read_csv('/home/brian/Downloads/StudentsPerformance.csv')
#mostrando archivo csv
print(df_exams)