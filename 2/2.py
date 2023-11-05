# print('w x y z')
# for w in range(2):
#     for x in range(2):
#         for y in range(2):
#             for z in range(2):
#                 F1 = (x<=y) or ((not w) == z)
#                 F2 = (x<=y) == (w and (not z))
#                 if F1 == F2:
#                     print (w, x, y, z, F1, F2)


print('c a d b')
c = 1
for a in range(2):
    for d in range(2):
        for b in range(2):
            F1 = ((a and b) == (not c)) and (b and d)
            F2 = ((a and b) == (not c)) and (b == d)
            F3 = ((a and b) == (not c)) and (b <= d)
            F4 = ((a and b) == (not c)) and (b or d)
            if F3:
                print(c, a ,d, b, F3)