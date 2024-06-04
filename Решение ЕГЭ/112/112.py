# 2 --------------------------------------------------------------------------
# for x in range(2):
#     for y in range(2):
#         for z in range(2):
#             for w in range(2):
#                 F = (((not x) and w) <= y) and (y <= (z and (not y)))
#                 if F: print(z, y, x, w, int(F))
# 5 --------------------------------------------------------------------------
# def f(n):
#     arr_num = sorted(map(int, list(str(n))))
#     min_num = min(arr_num)
#     max_num = max(arr_num)
#     chet_nums = list(filter(lambda num: num % 2 == 0, arr_num))
#
#     first = (max_num + min_num)**2
#     second = 1
#     for num in chet_nums: second *= num
#
#     if first > second: return int(f'{first}{second}')
#     return int(f'{second}{first}')
# print(f(22229))
# for n in range(10_000, 100_000):
#     if f(n) == 12116: print(n)
# 8 --------------------------------------------------------------------------
# from itertools import product
# c = 0
# for word in product(sorted('АЛГОРИТМ'), repeat=6):
#     s = ''.join(word)
#     if s.count('Л') <= 1 and s[0] != 'Р' and s[-1] not in 'ЛГРТМ':
#         c += 1
# print(c)
# 12 --------------------------------------------------------------------------
# def f(s):
#     while '73' in s or '3333' in s or '1133' in s:
#         if '73' in s:
#             s = s.replace('73', '11', 1)
#         if '3333' in s:
#             s = s.replace('3333', '7', 1)
#         if '1133' in s:
#             s = s.replace('1133', '37', 1)
#     return s
# for i in range(4, 10_000):
#     s = '7' + '3' * i
#     res = f(s)
#     one = res.count('1')
#     three = res.count('3') * 3
#     seven = res.count('7') * 7
#     summ = one+three+seven
#
#     if summ == 128: print(i)
# 13 --------------------------------------------------------------------------
# print(bin(153)[2:].zfill(8), bin(202)[2:].zfill(8), bin(16)[2:].zfill(8), bin(32)[2:].zfill(8))
# print(bin(153)[2:].zfill(8), bin(202)[2:].zfill(8), bin(16)[2:].zfill(8), bin(37)[2:].zfill(8))
# print(int('11111111', 2) + int('11111',2))
# 14 --------------------------------------------------------------------------
# for i in range(16, 37):
#     s = int('17496', i) + int('91F83', i) + int('D9543', i)
#     if s % 12 == 0:
#         print(i, s // 12)
# 15 --------------------------------------------------------------------------
# for A in range(1000):
#     is_good_x = True
#     for x in range(1000):
#         for y in range(1000):
#             F = (x<7) or (y >= 3*x + A - 20) or (x >= 34) or (y < 121)
#             if not F:
#                 is_good_x = False
#                 break
#         if not is_good_x: break
#     if is_good_x: print(A)
# 16 --------------------------------------------------------------------------
# на бумажке легче
# 17 --------------------------------------------------------------------------
# f = open('17 (4).txt')
# a = [int(x) for x in f]
# s_111 = 39000
# c = 0
# min_s = 4651798037
# def del_naib (n):
#     naib = max(map(int, list(str(abs(n)))))
#     return abs(n) % naib == 0
#
# for i in range(len(a)-2):
#     a_0 = a[i]
#     a_1 = a[i+1]
#     a_2 = a[i+2]
#
#     first = (del_naib(a_0) + del_naib(a_1) + del_naib(a_2)) >= 1
#     second = (a_0 * a_1 * a_2) >= s_111
#     if first and second:
#         c += 1
#         min_s = min(min_s, a_0 * a_1 * a_2)
# print(c, min_s)
# 19-21 --------------------------------------------------------------------------
# def win (s, m):
#     if s <= 221: return m % 2 == 0
#     if m == 0: return 0
#
#     nextWin = [
#         win(s - 2, m - 1),
#         win(s - 3, m - 1),
#         win(s - 4, m - 1),
#         win(s - 5, m - 1),
#         win(s // 2, m - 1),
#     ]
#
#     return any(nextWin) if (m - 1) % 2 == 0 else all(nextWin)
# print('19)', [s for s in range(222, 10000) if not win (s, 1) and win(s, 2)])
# print('20)', [s for s in range(222, 10000) if not win (s, 1) and win(s, 3)])
# print('21)', [s for s in range(222, 10000) if not win (s, 2) and win(s, 4)])
# 23 --------------------------------------------------------------------------
# def f(s, e):
#     if s > e or s == 21: return 0
#     if s == e: return 1
#     return f(s + 2, e) + f(s + 3, e) + f(s * 2, e)
# print(f(7, 14)*f(14, 32))
# 24 --------------------------------------------------------------------------
from fnmatch import fnmatch
nechet = '[1,3,5,7,9]'
for i in range(0, 10**10, 2024):
    if fnmatch(str(i), f'71{nechet}{nechet}{nechet}39?28'):
        print(i, i // 2024)

# 25 --------------------------------------------------------------------------

# 26 --------------------------------------------------------------------------

# 27 --------------------------------------------------------------------------


