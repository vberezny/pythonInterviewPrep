# Iterable:

myList = [1,2,3]
for i in myList:
    print(i)

# Generator:

mygenerator = (x*x for x in range(3))
for i in mygenerator:
    print(i)


# Yield:

def createGenerator():
    mylist = range(3)
    for i in mylist:
        yield i*i

mygenerator = createGenerator()
print(mygenerator)

for i in mygenerator:
    print(i)
