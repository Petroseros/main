from random import shuffle, randint

a = [randint(1, 100) for i in range(5)]
shuffle(a)
print(a)
y = a.index(min(a))
z = a.index(max(a))
t = max(a)
h = min(a)
a.pop(y)
a.insert(y, t)
a.pop(z)
a.insert(z, h)
print(a)


