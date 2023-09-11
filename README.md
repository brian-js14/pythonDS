# pythonDS

Jupyter notebook --> pip install notebook
run --> jupyter notebook

type() --> data type

Mathematical Operations(- + / *):
/ --> float division
// --> interger division

hierarchy mathematical --> * > +

Strings: Stride
Name="Michael Jackson" -->
Name[0]:M
Name[6]:l
Name[-1]:n
Name[-15]:M
Name[0:4]:Mich
Name[8:12]:Jack
Name[::2]:McalJcsn
Name[0:5:2]:Mca
Name + "is the best" --> Michael Jackson is the best
Name * 3 --> the name is multiplicated for three
\n --> reprent line break
\t --> reprent space line - Example 'Brian \t Solano':'Brian    Solano'
\\ --> 'Brian \ Solano' or print(r'Brian\Solano')

String Methods:

A='Hello world'
B=A.upper()-->'HELLO WORLD'

A='Hello earth'
B=A.replace('Hello','Hi')-->'Hi earth'

Name="Michael Jackson"
Name.find('el):5 --> the output is the firts index of the sequence.

Tuples --> They are an ordered sequence.
tuple1 = ('disco',10,1.2) --> tuple -- Each element of a tuple can be accessed via an index
tuple1[0]:'disco'
tuple1[1]:10
tuple1[2]:1.2

negative index:
tuple1[-3]:'disco'
tuple1[-2]:10
tuple1[-1]:1.2

tuple2=tuple1 + ('hard rock',10)
--> tuple2:('disco',10,1.2,'hard rock',10)
tuple2[0:3]=>('disco',10,1.2)
tuple2[3:5]=>('hard rock',10)
len((('disco',10,1.2,'hard rock',10))) --> 5
-- tuples are immutable, which means we can't change them

Ratings=(10,9,6,5,10,8,9,6,2)
Ratings1=Ratings

Lists --> Lists are also ordered sequences
L=['Michaek',101.1, 1987]
L.extend(['pop']) --> adding one element
L.append('A') --> add last new element
del(A[0]) --> delete element 0 index
split() --> split for parameter -- ("A,B,C").split(",") => ["A","B","C"]
B=A[:] --> Variable 'B' references a new copy or clone of the original list "A"

B=["a","b","c"]
print(B[1:]) ---> skip to the second element

Sets -->
- Sets are a typer of collection
    This means that like lists and tuples you can input different python types
- Unlike lists and tuples they are unordered
    This means sets do not record element position

set1={"pop","rock","soul","salsa","rap","rock","disco"}
print(set1) --> When the actual set is created, duplicate items will not be present.

Set Operations
A={"Thriller","Back in black", "AC/DC"}
A.add("NSYNC")
A={"AC/DC","Back in black","NSYNC","Thriller"}
A.remove("NSYNC")
A={"AC/DC","Back in black","Thriller"}
B={"AC/DC","Back in black","The dark side of the moon"}

& --> we use the ampersand to find the union of two sets
C = A & B
C = A={"AC/DC","Back in black"}
.union => all elements
AB={"AC/DC","Back in black","Thriller","The dark side of the moon"}

method issubset -- 
B.issubset(A) --> True -- response in boolean value

Dictionaries: Type of colletions in python
Key + value
- Dictionaries are denoted with curly Brackets{}
- The keys have to be immutable and unique
- The values can be immutable, mutable and duplicates

Example:
    "Thriller":"1987"
    "Back in black":"1980"
    "Rumors":"1977"

DICT.keys() = ["Thriller","Back in black","Rumors"]
DICT.values() = ["1987","1980","1977"]


Conditions and Branching
-------------------------------------------------------------------------------
Comparison operators:
    a = 6 --> "=" equal operator of assignment
    a == 7 --> "==" operator of comparison
    a === 7 --> "===" operator of strict
        a = 5
        b = 6
        a == b --> False
    Again:
        a = 5
        b = '5'
        a == b --> true
        a === b --> false

i = [1,2,3,4,5,6,7]
i != 6
result = [1,2,3,4,5,7]


Objects and Classes:

- Python has lots of data types:
    - int: 1, 2,567...
    - float: 1.2
    - string: 'a','b'
    - List: [1,2,'abc']
    - dictionary: {"dog":1,"cat":2}
    - Bool: False/True

- Each is an object
- every object has:
    - a type
    - an internal data representation (a blueprint).
    - a set of procedures for interacting with the object(methods)
- an object is an instance of a particular type

Spanih:
POO:

Clase --> Plantilla o modelo para nuestro objeto
Objeto --> Es un algo, literalmente una cosa o un objeto
Atributos --> Son las cualidades o carácterísticas de un objeto
Métodos --> Acciones que puede realizar mi objeto

def __init__(self): --> Método de mi objeto
self --> Se guarda la referencia al objeto que se está creando.


------------------------------------------------------------------------------------------------------------------
Udemy
------------------------------------------------------------------------------------------------------------------

Lista --> Mutables, pueden cambiar su valor []
conjuntos {} --> manejan clave-valor

Funciones pre-fabricadas -- más usadas
len()
max()
min()
type()
round(2.3333,1) --> 2.3
range(1,10,2) --> Ej:
    for i in range(1, 10, 2):
        print(i)
    //1
    //3
    //5
    //7
    //9

Crear funciones con python
---------------------------------------

def funtion(<params>):
    <code>
    return <data>

def sumar_numeros(a, b):
    resultado = a + b
    return resultado

modulos en python
---------------------------------------

import os --> mod del sistema
modulo_os.py

Pandas
---------------------------------------
- Herramienta para hacer análisis de datos en Python
- limpieza de datos
- trasnformación de data compleja
- compatibilidad multiplataforma
- visualización de los datos

Arrays -->
    Lista 1D -- 1 Dimensión - Series
    Lista 2D -- DataFrame - Array de 2 Dimensiones

Dataframe -- Hace referencia a una hoja de calculo
    - series/al tener dos dimensiones tendrán filas/columnas
    - Los titulos se conocen como features
    - los valores se conocen como observaciones

Excel vs Pandas
Worksheet - Dataframe
Column - Series
Row headind(id) - Index
Row - Row
Empty Cell - NaN

Creando un Dataframe
--------------------------------
1. Arrays
    Numpy Array
    np.array([1,4],[2,5],[3,6])

    List Arrays
    data = [[1,4],[2,5],[3,6]]

2. Diccionario
my_dict = {'key1':value1, 'key2':value2}
    key => column_name
    value => data
    Series(1D array)

3. Dataframe desde csv


Atributos - Métodos - Funciones
--------------------------------
Atributos: Valor asociado con un objeto -- df.columns
Función: Grupo de setencias reacionadas que hacen una tarea específica
    - max()
    - min()
    - len()
Métodos: una función que es definida dentro del cuerpo de una clase
    - df.head()
#obteniendo valores estadísticos del dataFrame
print(df_exams.describe())
       math score  reading score  writing score
count  1000.00000    1000.000000    1000.000000
mean     66.08900      69.169000      68.054000
std      15.16308      14.600192      15.195657
min       0.00000      17.000000      10.000000
25%      57.00000      59.000000      57.750000
50%      66.00000      70.000000      69.000000
75%      77.00000      79.000000      79.000000
max     100.00000     100.000000     100.000000

std --> Desviciación estándar --
Es una medida del grado de disperción de los datos respecto al valor promedio.
- mientras más separados se encuentran los datos tendrá una desviación estandar mayor
- significa que con base al valor promedio, se mueve sobre la recta hacia la izquierda y derecha el valor de la desviación y la mayoría de los datos se encuentran dentro de ese rango.

-----s-----11-----s-------
entre s y s --> se encuentran la mayoría de los datos, estos con una muestra con valores típicos

25% - 50% - 75% --- Percentiles ---
Medida de posición que divide la distribución de datos en partes iguales hasta su 100%
