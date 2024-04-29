# 2 --------------------------------------------------------------------------
# print('x y z w F')
# for x in range(2):
#     for y in range(2):
#         for z in range(2):
#             for w in range(2):
#                 F = (not (x <= (z > w))) and (z > (w != y))
#                 if not F and (x+y+z+w) >= 3: print(x,y,z,w,int(F))
# 5 --------------------------------------------------------------------------
# def f(x):
#     str_x = str(x)
#     a_0 = int(str_x[0])
#     a_1 = int(str_x[1])
#     a_2 = int(str_x[2])
#     a = a_0 * a_1
#     b = a_1 * a_2
#     if a > b: return int(str(b) + str(a))
#     return int(str(a) + str(b))
#
# for N in range(100, 1000):
#     if f(N) == 621: print(N)

# 8 --------------------------------------------------------------------------
# from itertools import *
# c = 0
# for el in product('01', repeat=5):
#     c += 1
# for el in product('01', repeat=6):
#     c += 1
# print(c)
# 12 --------------------------------------------------------------------------
# def f(s):
#     while ('52' in s) or ('2222' in s) or ('1122' in s):
#         if '52' in s: s = s.replace('52', '11')
#         if '2222' in s: s = s.replace('2222', '5')
#         if '1122' in s: s = s.replace('1122', '25')
#     return s
# def sum_cifr(s):
#     summa = 0
#     for num in s: summa += int(num)
#     return summa
# for i in range(4, 10000):
#     s = '5' + '2'*i
#     res = f(s)
#     if sum_cifr(res) == 64:
#         print(i)
# 13 --------------------------------------------------------------------------
# print(bin(255)[2:].zfill(8), bin(255)[2:].zfill(8), bin(255)[2:].zfill(8), bin(240)[2:].zfill(8), 'mask')
# print(bin(142)[2:].zfill(8), bin(68)[2:].zfill(8), bin(56)[2:].zfill(8), bin(0)[2:].zfill(8), 'web')
# 14 --------------------------------------------------------------------------
# for x in range(12):
#     a = 9*12**6 + 10*12**5 + 8*12**4 + 7*12**3 + x*12**2 + 2*12 + 1
#     b = 2*14**3 + x*14**2 + 6*14 + 8
#     c = 16**4 + x*16**3 + 2*16**2 + 15*16 + 4
#     if (a+b-c) % 3 == 0: print(x, (a+b-c)//3)
# 15 --------------------------------------------------------------------------
# def DEL(n,m): return n%m == 0
# B = list(range(70, 81))
#
# for A in range(1, 1000):
#     for x in range(1, 1000):
#         F = DEL(x, 12) and (x in B) and (not DEL(x, A))
#         if F: break
#     else: print(A)
# 16 --------------------------------------------------------------------------
# def f(n): return g(n-1)
# def g(n):
#     if n < 10: return n
#     if n >= 10: return g(n-2) + 1
# def is_quadrat(x):
#     sqrt = x ** 0.5
#     return sqrt % 1 == 0
# c = 0
# for n in range(1, 101):
#     res = f(n)
#     if is_quadrat(res): c += 1
# print(c)
# 17 --------------------------------------------------------------------------
# f = open('17_11887.txt')
# a = [int(x) for x in f]
# mx_68 = max(x for x in a if abs(x) % 100 == 68)
# def is_2zna4(x): return abs(x) >= 10 and abs(x) <= 99
#
# c = 0
# mx = -10**20
#
# for i in range(len(a) - 4):
#     a_0 = a[i]
#     a_1 = a[i+1]
#     a_2 = a[i+2]
#     a_3 = a[i+3]
#     first = is_2zna4(a_0) + is_2zna4(a_1) + is_2zna4(a_2) + is_2zna4(a_3) == 1
#     second = is_2zna4(a_0) + is_2zna4(a_1) + is_2zna4(a_2) + is_2zna4(a_3) == 4
#     cond1 = first or second
#     cond2 = a_0 + a_1 + a_2 + a_3 >= mx_68
#     if cond1 and cond2:
#         c+= 1
#         mx = max(mx, a_0 + a_1 + a_2 + a_3)
# print(c, mx)
# 19-21 --------------------------------------------------------------------------
# def real_letters(arr):
#     biggest_word = max(arr, key=len)
#     res = []
#     for a in range(len(biggest_word)): res.append([])
#     for i in range(len(arr)):
#         word = arr[i]
#         for j in range(len(word)):
#             res[j].append(word[j])
#     for i in range(len(res)): res[i] = list(set(res[i]))
#     return res
# print(' '.join([str(x) for x in map(len, real_letters(['ворона', 'волк', 'волна', 'морис', 'морковь', 'моряна']))]))
# print(' '.join(['В' if x%2 == 1  else 'П' for x in range(7)]))
# 23 --------------------------------------------------------------------------
# def f(start, end):
#     if start == 300: return 124
#     if start == 330: return 23916
#     if start == 350: return 4381
#     # if start == 400: return 124
#     if start == 500: return 43
#     if start > end or start == 100 : return 0
#     if start == end: return 1
#     s = f(start**2, end)
#     if start % 10 != 0: s += f(start + start%10, end)
#     if start % 68 != 0: s += f(start + start%68, end)
#     return s
# print(f(310, 680)) # 4799789947424
# 24 ---------- ----------------------------------------------------------------
# s = open('24_11892.txt').readline()
# print(s.count('X'))
# s = s.replace('Y', ' ').split()
# a = [x for x in s if x.count('X') >= 500]
# print(len(min(a, key=len)), min(a, key=len).count('X'))
# 25 --------------------------------------------------------------------------
# from itertools import *
# for A in '02468':
#     for B in product('13579', repeat=1):
#         b_str = ''.join(B)
#         s = int(f'1{A}2157{b_str}4')
#         if s % 133 == 0 and s <= 10**10: print(s, s // 133)
# 1021575394 7681018
# 1421575554 10688538
# 1821575714 13696058
# a = [[122157574 ,918478], [1021575394 ,7681018],[1421575554 ,10688538], [1821575714 ,13696058]]
# a.sort()
# print(a)
# 26 --------------------------------------------------------------------------
# f = open('26_11894.txt')
# n, k = map(int, f.readline().split())
# now_skill = k
# a = []
# for i in range(n):
#     level, skill = map(int, f.readline().split())
#     a.append([level, skill])
# a.sort()
# c = 0
# for level, skill in a:
#     if level < now_skill:
#         c += 1
#         now_skill += skill
# print(c, now_skill)
# 27 --------------------------------------------------------------------------
# f = open('27-B_11895.txt')
# n, t, k = map(int, f.readline().split())
# a = []
# for i in range(n):
#     pokupka, prodazha = map(int, f.readline().split())
#     a.append([pokupka, prodazha])
# min_back = 10**20
# mx_razn = 0
# for i in range(t, n):
#     min_back = min(min_back, a[i-t][0])
#     mx_razn = max(mx_razn, (k // min_back) * (a[i][1] - min_back))
# print(mx_razn) # 19860 9999910000