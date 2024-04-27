# 2 --------------------------------------------------------------------------
# print('x y z w F')
# for x in range(2):
#     for y in range(2):
#         for z in range(2):
#             for w in range(2):
#                 F = (x and (not z)) or (y == z) or (not w)
#                 if not F: print(w, y, z, x, int(F))
# 5 --------------------------------------------------------------------------
# def f(n):
#     n_2 = bin(n)[2:]
#     if n % 2 == 0:
#         n_2 += '01'
#     if n % 2 != 0:
#         n_2 = '1' + n_2 + '1'
#     return int(n_2, 2)
# for i in range(1000):
#     if f(i) > 156:
#         print(i)
#         break
# 7 --------------------------------------------------------------------------
# S = 2764 * 1793
# i = 13
# V = S * i * 148
# u = 18_349_566
# print(V / u)
# 8 --------------------------------------------------------------------------
# from itertools import product
# n = 0
# for word in product('АПРСУ', repeat=5):
#     n += 1
#     s = ''.join(word)
#     if s.count('У') <= 1 and 'АА' not in s:
#         print(s, n)
#         break
# 12 --------------------------------------------------------------------------
# def f(s):
#     while '1111' in s or '8888' in s:
#         if '1111' in s:
#             s = s.replace('1111', '88', 1)
#         else:
#             s = s.replace('8888', '11', 1)
#     return s
# print(f('8'*45))
# 13 --------------------------------------------------------------------------
# print(bin(255)[2:].zfill(8), bin(255)[2:].zfill(8), bin(255)[2:].zfill(8), bin(224)[2:].zfill(8))
# print(bin(105)[2:].zfill(8), bin(224)[2:].zfill(8), bin(200)[2:].zfill(8), bin(224)[2:].zfill(8))
# print('01101001 11100000 11001000 11100000'.count('1'))
# 14 --------------------------------------------------------------------------
# n = 3 * 2187**2020 + 3 * 729**2021 - 2*81**2022 + 27**2023 - 4*3**2024 - 2029
# def convert_27 (n):
#     alf = '0123456789abcdefghijklmnopqrstuvwxyz'
#     s = ''
#     while n > 0:
#         s += str(alf[n % 27])
#         n //= 27
#     return s[::-1]
# s = convert_27(n)
# c = 0
# for i in s:
#     if i not in '0123456789': c += 1
# print(c)

# for x in '0123456789abcdefghijklmnopq':
#     n = int(f'123{x}24', 27) + int(f'135{x}78', 27)
#     if n % 26 == 0: print(x, n // 26)
# 15 --------------------------------------------------------------------------
# def DEL(n, m): return n % m == 0
# for A in range(1, 1000):
#     for x in range(1, 1000):
#         F = (not (DEL(x, A))) <= (DEL(x, 28) <= (not (DEL(x, 49))))
#         if not F: break
#     else: print(A)

# B = list(range(24, 91))
# C = list(range(47, 116))
# A = []
# for x in range(-1000, 1000):
#     F = (x in C) <= ((not (x in A)) and (x in B) <= (not (x in C)))
#     if not F: A.append(x)
# print(len(A) - 1)
# 16 --------------------------------------------------------------------------
# print(2024+2023+2022+2021+8)
# 17 --------------------------------------------------------------------------
# f = open('17_15333.txt')
# a = [int(x) for x in f]
# max_19 = 89737
# c = 0
# max_s = -37819813
# for i in range(len(a)-1):
#     a_0 = a[i]
#     a_1 = a[i+1]
#     cond = (a_0 > max_19) + (a_1 > max_19) >=  1
#     if cond:
#         c += 1
#         max_s = max(max_s, a_0 + a_1)
# print(c, max_s)
# 19-21 --------------------------------------------------------------------------
# def win(s1,s2,m):
#     if s1 + s2 >= 123: return m % 2 == 0
#     if m == 0: return 0
#     nextWin = [
#         win(s1 + 1, s2, m - 1),
#         win(s1 * 2, s2, m - 1),
#         win(s1, s2 + 1, m - 1),
#         win(s1, s2 * 2, m - 1),
#     ]
#     return any(nextWin) if (m-1) % 2 == 0 else all(nextWin)
# print('19)', [s for s in range(1,110) if win(13,s,2)])
# print('20)', [s for s in range(1,110) if not win(13,s,1) and win(13,s,3)])
# print('21)', [s for s in range(1,110) if not win(13,s,2) and win(13,s,4)])
# 23 --------------------------------------------------------------------------
# def f(s, e):
#     if s > e: return 0
#     if s == e: return 1
#     return f(s+1, e) + f(s*2, e)
# print(f(4, 8) * f(8,10) * f(10,  15))
# 24 --------------------------------------------------------------------------

# 25 --------------------------------------------------------------------------
from fnmatch import fnmatch
for i in range(0, 10**10, 2024):
    if fnmatch( str(i), '1*2322?2'):
        print(i, i // 2024)
# 26 --------------------------------------------------------------------------

# 27 --------------------------------------------------------------------------


