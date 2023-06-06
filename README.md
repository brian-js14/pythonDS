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
print(set1) --> When the actual set is created, duplicate items will not be present