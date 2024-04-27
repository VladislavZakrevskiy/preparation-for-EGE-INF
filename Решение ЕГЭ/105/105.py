# 2 --------------------------------------------------------------------------
# print('x y w z F')
# for x in range(2):
#     for y in range(2):
#         for z in range(2):
#             for w in range(2):
#                 F = y and (x or z) or (not (y or z)) or w
#                 if not F: print(x, y, w, z, int(F))
# 5 --------------------------------------------------------------------------
# def f(n):
#     n_2 = bin(n)[2:]
#     if n % 2 == 0:
#         l_0 = n_2[-2]
#         l_1 = n_2[-1]
#         n_2 += l_0 + l_1
#     else:
#         n_2 = '1' + n_2 + '0'
#     return int(n_2, 2)
#
# for n in range(2, 1000):
#     if f(n) < 100:
#         print(n)
# 8 --------------------------------------------------------------------------
# from itertools import product
# c = 0
#
# for word in product('012345678', repeat=5):
#     if word[0] == '0': continue
#     rydom = word[0] != word[1]\
#     or word[1] != word[2]\
#     or word[2] != word[3]\
#     or word[3] != word[4]\
#
#     if word.count('5') == 1 and rydom:
#         c += 1
# print(c)
# 12 --------------------------------------------------------------------------
# def f(s):
#     while '333' in s or '555' in s:
#         if '555' in s:
#             s = s.replace('555', '3', 1)
#         else:
#             s = s.replace('333', '5', 1)
#     return s
# max_s = -367278932
# for i in range(4, 10000):
#     s = '3' + '5' * i
#     res = f(s)
#     three = res.count('3') * 3
#     five = res.count('5') * 5
#     summa = three + five
#     max_s = max(max_s, summa)
# print(max_s)
# 13 --------------------------------------------------------------------------
# print(bin(255)[2:].zfill(8), bin(255)[2:].zfill(8), bin(255)[2:].zfill(8), bin(240)[2:].zfill(8))
# print(bin(192)[2:].zfill(8), bin(168)[2:].zfill(8), bin(32)[2:].zfill(8), bin(48)[2:].zfill(8))
# 14 --------------------------------------------------------------------------
# s = 2 * 729**333 + 2*243**334 - 81**335 + 2*27**336 - 2*9**337 - 338
# c = 0
# for i in str(s):
#     if i != '0': c += 1
# print(c)
# 15 --------------------------------------------------------------------------
# for A in range(1, 1000):
#     for x in range(1, 1000):
#         F = (x&A == 0) or (not (x&37 == 0)) or (not (x&12 == 0))
#         if not F: break
#     else: print(A)
# 16 --------------------------------------------------------------------------
# бумажка какашка
# 17 --------------------------------------------------------------------------
# f = open('17_12249.txt')
# a = [int(x) for x in f]
# max_3 = 99683
#
# c = 0
# max_s = -34156783
#
# for i in range(len(a)-2):
#     a_0 = a[i]
#     a_1 = a[i+1]
#     a_2 = a[i+2]
#     first = ( (abs(a_0) % 10 == 3) + (abs(a_1) % 10 == 3) + (abs(a_2) % 10 == 3)) >= 1
#     second = (a_0 + a_1 + a_2) <= max_3
#     if first and second:
#         c += 1
#         max_s = max(max_s, a_0 + a_1 + a_2)
# print(c, max_s)
# 19-21 --------------------------------------------------------------------------
# def win(s, m):
#     if s >= 301: return m % 2 == 0
#     if m == 0: return 0
#     nextWin = [
#         win(s + 3, m - 1),
#         win(s * 5, m - 1)
#     ]
#     return any(nextWin) if (m - 1) % 2 == 0 else all(nextWin)
# print('19)', [s for s in range(1, 301) if not win(s, 1) and win(s, 2)])
# print('20)', [s for s in range(1, 301) if not win(s, 1) and win(s, 3)])
# print('21)', [s for s in range(1, 301) if not win(s, 2) and win(s, 4)])
# 23 --------------------------------------------------------------------------
# def f(s, e):
#     if s == e: return 1
#     if s > e or s == 16: return 0
#     return f(s + 1, e) + f(s + 3, e) + f(s ** 2, e)
# print(f(3, 20) * f(20, 26))
# 24 --------------------------------------------------------------------------
# s = list(open('24_12254.txt').readline())
# c = 0
# max_c = 0
#
# for i in range(0, len(s)-2, 3):
#     a_0 = s[i]
#     a_1 = s[i+1]
#     a_2 = s[i+2]
#     if a_0 == 'R' and a_1 == 'S' and a_2 == 'Q':
#         c += 1
#         max_c = max(max_c, c)
#     else: c = 0
# print(max_c)
# print('RSQ'*17)
# 25 --------------------------------------------------------------------------
# from fnmatch import fnmatch
# for i in range(0, 10**12, 98591):
#     if fnmatch(str(i), '12?3*456??9'):
#         print(i, i // 98591)
# 26 --------------------------------------------------------------------------
# f = open('26_12256.txt')
# s, n = map(int, f.readline().split())
# a = [int(x) for x in f]
# a.sort()
#
# kuzov = []
# gruz_kuzov = 0
# for num in a:
#     if gruz_kuzov + num <= s:
#         kuzov.append(num)
#         gruz_kuzov += num
#     else: break
# print(kuzov)
# print(a)
# print(len(kuzov), max(kuzov))
# 27 --------------------------------------------------------------------------
