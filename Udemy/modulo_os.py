import os
#ruta del directorio donde estoy trabajando
print(os.getcwd())
#lista de archivos en la ubicación
print(os.listdir())
#crear un nuevo directorio dentro de la ruta
os.makedirs("new")