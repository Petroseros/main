coordinates = [5, 3]
x = coordinates[0]
y = coordinates[1]
a = 0
p = 0
instructions = ["left","down"]
for i in range(len(instructions)):
    if instructions[i] == "left":
        coordinates.pop(0)
        coordinates.insert(0, x - 1)
        p = p - 1
    elif instructions[i] == "right":
        coordinates.pop(0)
        coordinates.insert(0, x + 1)
        p = p + 1
    elif instructions[i] == "up":
        coordinates.pop(1)
        coordinates.insert(1, y + 1)
        a = a + 1
    elif instructions[i] == "down":
        coordinates.pop(1)
        coordinates.insert(1, y - 1)
        a = a - 1
print(coordinates)
print((p*p+a*a)**0.5)