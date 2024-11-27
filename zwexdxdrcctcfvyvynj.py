p = input()
n = ""
lives = 5
for i in range(100):
     print()
for i in range(len(p)):
    n=n+"*"
print(n)
g = input()
if g in p:
    print("Right! Now you have",lives,"lives.")
    p = list(p)
    n = list(n)
    for i in range(len(n)):
        if p[i] == g:
            n.pop(i)
            n.insert(i, g)
            n = ''.join(n)
            p = ''.join(p)
            print(n)
else:
    lives = lives - 1
    print("False... You have one live less. Now you have",lives,"lives.")