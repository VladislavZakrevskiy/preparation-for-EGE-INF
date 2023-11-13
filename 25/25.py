# 23?456?89
# I
# from fnmatch import *
# for x in range(170000000, 240000000, 17):
#     if fnmatch(str(x), '23?456?89'):
#         print(x, x // 17)
# II
# for x in range(0,10):
#     for y in range(0,10):
#         if int(f'23{x}456{y}89') % 17 == 0:
#             print(f'23{x}456{y}89')

# ---------------------------------------------------------

#345*789?
# I
# from fnmatch import fnmatch
# for x in range(16900000, 10**9, 169):
#     if fnmatch(str(x), '345*789?'):
#         print(x, x // 169)
# II
# for c1 in '0123456789':
#     a = f'345789{c1}'
#     if int(a) % 169 == 0:
#         print(a, int(a) // 169)
# for c1 in '0123456789':
#     for c2 in '0123456789':
#         a = f'345{c1}789{c2}'
#         if int(a) % 169 == 0:
#             print(a, int(a) // 169)
# for c1 in '0123456789':
#     for c2 in '0123456789':
#         for c3 in '0123456789':
#             a = f'345{c1+c2}789{c3}'
#             if int(a) % 169 == 0:
#                 print(a, int(a) // 169)

# -----------------------------------------------

# 56*98*
# I
# from fnmatch import *
# for x in range(0, 10**6, 51):
#     if fnmatch(str(x), '56*98*'):
#         print(x, x // 51)
# II
# for x in range(102, 10**6, 51):
#     s = str(x)
#     if s[0]+s[1] == '56' and '98' in s:
#         print(s)

# ---------------------------------------------

# ?8*8*?8
# from fnmatch import *
#
# def find_divs(x):
#     arr = set()
#     for i in range(1, int(x ** 0.5) + 1):
#         if x % i == 0:
#             arr.add(i)
#             arr.add(x // i)
#     return sorted(arr)
#
# count = 0
# for x in range(1, 10**8):
#     if fnmatch(str(x), '?8*8*?8') and x % 6 == 0 and x % 7 == 0 and x % 8 == 0:
#         if count > 6:
#             break
#         print(x, sum(find_divs(x)))
#         count += 1

# -------------------------------------------------

# 27?7*
# from fnmatch import *
# def find_divs(x):
#     arr = set()
#     for i in range(1, int(x**0.5) + 1):
#         if x % i == 0:
#             arr.add(i)
#             arr.add(x // i)
#     return sorted(arr)
# count = 0
# for x in range(10**7, 0, -1):
#     if fnmatch(str(x), '27?7*') and x % 217 == 0:
#         if count > 7:
#             break
#         print(x, sum([i for i in find_divs(x) if i%2 != 0]))
#         count += 1

# ---------------------------------------------------------------

# 1?DED?CED
# for c1 in '0123456789ABCDEF':
#     for c2 in '0123456789ABCDEF':
#         a = f'1{c2}DED{c1}CED'
#         if int(a, 16) % int("79", 16) == 0:
#             print(a, int(a, 16) // int("79", 16))

# 1FDED8CED 70703893
# 17DED3CED 52955925
# 12DEDFCED 41863957

# -----------------------------------------------------

# 11Ч??Н11
# from fnmatch import *
# for x in range(0, 10**8, 2023):
#     if fnmatch(str(x), '11[02468]??[13579]11'):
#         print(x, x // 2023)

# -----------------------------------------------------

# 123*НЧ56
# from fnmatch import *
# for x in range(0, 10**8, 206):
#     if fnmatch(str(x), '123*[13579][02468]56'):
#         print(x, x // 206)

