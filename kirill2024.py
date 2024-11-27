import random


# p = input()
# p = list(p)
# r=1
# for i in range(len(p)):
#     m = random.randint(1, 5)
#     for i in range(m):
#         p.insert(r, " ")
#     r=r+m+1
# p = "".join(p)
# print(p)


print(''.join([symbol + random.randint(1, 5) * ' ' for symbol in input()]))
