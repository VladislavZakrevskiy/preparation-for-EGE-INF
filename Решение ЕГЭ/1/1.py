# 1 ------------------------------------------------------------

# 2 ------------------------------------------------------------
# print('z x y F')
# for x in range(2):
#     for y in range(2):
#         for z in range(2):
#             F = (y <= z) and (not(z and x))
#             if F: print(z, x, y , F)
# 3 ------------------------------------------------------------

# 4 ------------------------------------------------------------

# 5 ------------------------------------------------------------
# def f(x):
#     bin_x = bin(x)[2:]
#     s = ''
#     for i in bin_x:
#         if i == '0': s += '1'
#         else: s += '0'
#     num = int(s, 2)
#     return num
# for N in range(1,10000):
#     if (N - f(N)) == 979:
#         print(N)
#         break
# 6 ------------------------------------------------------------

# 7 ------------------------------------------------------------

# 8 ------------------------------------------------------------
# from itertools import *
# c = 0
# for el in product('МЕЧТА', repeat=6):
#     if el.count('А') >= 3: c += 1
# print(c)
# 9 ------------------------------------------------------------

# 10 ------------------------------------------------------------

# 11 ------------------------------------------------------------

# 12 ------------------------------------------------------------
# def f(s):
#     while ('111' in s) or ('88888' in s):
#         if ('111' in s): s = s.replace('111', '88', 1)
#         if ('88888' in s): s = s.replace('88888', '8', 1)
#     return s
# mx = [0, 0]
# for i in range(100, 1000):
#     s = '1' * i
#     res = f(s)
#     if mx[1] < res.count('8'):
#         mx = [i, res.count('8')]
# print(mx)
# 13 ------------------------------------------------------------
# print(bin(255)[2:].zfill(8), bin(255)[2:].zfill(8),bin(255)[2:].zfill(8),bin(240)[2:].zfill(8), 'mask')
# print(bin(192)[2:].zfill(8),bin(168)[2:].zfill(8),bin(32)[2:].zfill(8),bin(160)[2:].zfill(8), 'web')
# print('11000000 10101000 00100000 1010'.count('1'))
# 14 ------------------------------------------------------------
# for x in range(36):
#     a = 36**4 + 2*36**3 + x*36**2 + 4*36 + 5
#     b = 12345 + x
#     if (a+b)%13 == 0:
#         print(x, (a+b)//13)
# 15 ------------------------------------------------------------
# def DEL(n,m):
#     return n%m == 0
# for A in range(1,1000):
#     for x in range(1,1000):
#         F = (not DEL(x, A)) <= (DEL(x, 35) <= DEL(x, 10))
#         if not F: break
#     else: print(A)

# 16 ------------------------------------------------------------
# def F(n):
#     if n <= 2: return 1
#     if n > 2: return F (n-1) + 2*F(n-2)
# print(F(17))
# 17 ------------------------------------------------------------
# f = open('17_2993.txt')
# a = [int(x) for x in f]
# mx_111 = max(x for x in a if x % 111 == 0)
# mn = 10**20
# c = 0
# for i in range(len(a)-1):
#     a_0 = a[i]
#     a_1 = a[i+1]
#     first = (a_0 > mx_111) + (a_1 > mx_111) >= 1
#     second = (abs(a_0) % 10 == 7) + (abs(a_1) % 10 == 7) >= 1
#     if first and second:
#         c += 1
#         mn = min(mn, a_0 + a_1)
# print(c, mn) # 147 10849
# 18 ------------------------------------------------------------

# 19-21 ------------------------------------------------------------
# def win(s0, s1, round):
#     if s0 + s1 == 0: return (round % 2) == 0
#     if round == 0: return 0
#     nextWin = []
#     for i in range(1, 5):
#         nextWin.append(win(s0-i, s1, round-1))
#     for i in range(1, 5):
#         nextWin.append(win(s0, s1-i, round-1))
#     return any(nextWin) if (round-1) % 2 == 0 else any(nextWin)
# print('19) ', [s for s in range(15, 100) if win(15, s, 2)])
# # print('20) ', [s for s in range(15, 300) if win(15, s, 3) and not win(15, s, 1)])
# print('21) ', [s for s in range(16, 50) if win(15, s, 2) and win(15, s ,4)])
# Какая-то хуйня
# 22 ------------------------------------------------------------

# 23 ------------------------------------------------------------
# def f(start, end):
#     if end < start or start == 8: return 0
#     if end == start: return 1
#     return f(start+2, end) + f(start*3, end)
# print(f(2, 50) * f(50, 60))
# 24 ------------------------------------------------------------
# s = open('24_66.txt').readline()
# s = s.replace('KOT', '*')
# print('*' * 75 in s)
# 25 ------------------------------------------------------------
# def delit(a) :
#     res = []
#     i = 2
#     while i * i < a + 1 :
#         if a % i == 0 :
#             res.append(i)
#         while a % i == 0 :
#             a //= i
#         i += 1
#     if a != 1 :
#         res.append(a)
#     return res
# def F(n):
#     prost_mn = delit(n)
#     return sum(prost_mn) // len(prost_mn)
# arr = []
# for i in range(650000, 700000):
#     if F(i) % 37 == 23: arr.append((i, F(i)))
# print(arr)
# 26 ------------------------------------------------------------
# Очередная поебень от Джобса
# 27 ------------------------------------------------------------
# f = open('27-B_1258.txt')
# n = int(f.readline())
# s = [(0,0,0)]
# for i in range(n):
#     a, b = map(int, f.readline().split())
#     new_sum = [(min(a, b), max(a, b), a + b)]
#     if a % 2 != 0:
#         for mn, mx, ms in s:
#             new_sum += [(mn + min(a, b), mx + max(a, b), ms + a + b)]
#         s += new_sum
#         s = list({(mn%2, mx%2): (mn, mx, ms) for mn, mx, ms in sorted(s)}.values())
# maxx  = -10**20
# for mn, mx, ms in s:
#     if mn % 2 == 0 and mx % 2 != 0:
#         maxx = max(maxx, ms)
# print(maxx) # 44067 301651117