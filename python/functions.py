


def add():
    return 10+20


# print(add())


def addArgument(a,b):
    sum =  a + b
    return "sum of {} and {} = {}".format(a,b,sum)

# print(addArgument(30,50))


def argruments(*args):
    # print(args)
    for i in range(len(args)):
        print(args[i])


# argruments(10,20,40,50)


def kword(**kwargs):
    for key,value in kwargs.items():
        print(key,value)

kword(name="ravi",age=28)