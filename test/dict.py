def test1():
    a = 1
    b = 2
    return {'a':a,'b':b}

m = test1()
f = m.get('a')
print(type(f),f)