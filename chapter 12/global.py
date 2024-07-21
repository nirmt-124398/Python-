a=89
def fun():
    global a
    a=2
    print(a)

fun()
print(a)