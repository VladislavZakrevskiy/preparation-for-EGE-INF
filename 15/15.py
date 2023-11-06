# def f(A, x):
#     return ((x & 105) == 0) <= (((x & 58) != 0) <= ((x & A) != 0))
# for A in range(1, 1000):
#     for x in range(1000):
#         if not f(A, x):
#             break
#     else:
#         print(A)
#         break

# def DEL(n, m):
#     return n % m == 0
#
# def f(A, x):
#     return (not DEL(x, A)) <= (DEL(x, 6) <= (not DEL(x, 9)))
#
# for A in range(1, 2000):
#     for x in range(1, 2000):
#         if not f(A, x):
#             break
#     else:
#         print(A)

# def f(A, x, y):
#     return ((2*x + y) != 70) or (x < y) or (A < x)
#
# for A in range(1,10000):
#     A_podoshel = True
#     for x in range(1,1000):
#         for y in range(1,1000):
#             if not f(A, x, y):
#                 A_podoshel = False
#                 break
#         if not A_podoshel:
#             break
#     if A_podoshel:
#         print(A)

# def DEL (n, m):
#     return n % m == 0
# def f(A, x):
#     return (DEL(x, 2) <= (not DEL(x, 3))) or ((x + A) >= 100)
#
# for A in range(1,1000):
#     for x in range(1, 1000):
#         if not f(A,x):
#             break
#     else: print(A)

# D = list(range(17, 59))
# C = list(range(29, 81))
# A = []
#
# def f(A,x):
#     return ((x in D) <= (((not (x in C)) and (not (x in A))) <= (not (x in D))))
#
# for x in range(-1000, 1000):
#     if not f(A, x):
#         A.append(x)
# print(A, len(A))

# Есть только числа которые были в условии изначально

# P = list(range(3,14))
# Q = list(range(12,23))
# A = list(range(0,100))
#
# def f(x):
#     return ((x in A) <= (x in P)) or (x in Q)
#
# for x in range(-1000,1000):
#     if not f(x):
#         A.remove(x)
#
# print(A)

# Обозначим через ТРЕУГ(n, m, k) утверждение
# «существует невырожденный треугольник с длинами сторон n, m и k».
# Для какого наибольшего натурального числа А формула
# ¬((ТРЕУГ(х, 11, 18) ≡ (¬(MAKC(x, 5) > 68))) ⋀ ТРЕУГ(х, А, 5))
# тождественно истинна (т. е. принимает значение 1) при любом натуральном значении переменной х?
# Примечание. МАКС(а, b) = а, если а > b и МАКС(а, b) = b, если а ≤ b.

# def MAX(a, b):
#     if a > b:
#         return a
#     if a <= b:
#         return b
#
# def t(n, m, k):
#     return max(n, m, k) < n + m + k - max(n, m, k)
#
# def f(A, x):
#     return not (( t(x,11,18) == ( not (MAX(x,5) > 68) )) and t(x, A, 5))
#
# for A in range(1000):
#     for x in range(1000):
#         if not f(A, x):
#             break
#     else: print(A)

# P = list(range(5,55))
# Q = list(range(50,94))
#
# def f(A, x):
#     return ((x not in P) and (x in Q)) <= (x > A)
#
# for A in range(0, 1000):
#     x_cnt = 0
#
#     for x in range(-1000, 1000):
#         if not f(A, x):
#             x_cnt += 1
#     # print(x_cnt)
#     if x_cnt == 20:
#         print(A)

# def DEL(n, m):
#     return n % m == 0
#
#
# P = list(range(257, 357))
# Q = list(range(5, 601))
# R = list(range(59, 229))
# A = []
#
# def f(x):
#     return ((x in R) <= (x in A)) or (DEL(x, 3) <= (x in P)) <= ((x in Q) <= (x in A))
#
# for x in range(0,1000):
#     if not f(x):
#         A.append(x)
# print(A)
# print(227 - 59 + 1)
