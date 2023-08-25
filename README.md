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