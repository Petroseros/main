import random
j = 0
p = []
for i in range(5):
    m = random.randint(1, 50)
    j = j + m
    p.append(m)
r = random.randint(0, 4)
t = p[r]
p.pop(r)
p.insert(r,"GHOST")
print(p,j)
o = int(input("What is GHOST? "))
if o == t:
    print("Yay!!!!!!!!!!!!!!!!!!!!!!!!!!")
else:
    print("Noooooooooooooooooooooooooooo")