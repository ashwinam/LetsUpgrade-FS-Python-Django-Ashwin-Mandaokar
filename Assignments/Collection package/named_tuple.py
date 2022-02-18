from collections import namedtuple

# what would be the fields and name of data struture

emp1 = namedtuple("lets",'Name age emcode')
# creation of new data types.

record1 = emp1("ABC",24,'1212d')
print(record1)
print(type(record1))

print(record1.Name)
print(record1[0])



