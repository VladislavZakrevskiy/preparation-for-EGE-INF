# 2 --------------------------------------------------------------------------
# print('y x w z F')
# for x in range(2):
#     for y in range(2):
#         for z in range(2):
#             for w in range(2):
#                 F = (x or (not y)) and (not (x == z))
#                 if F: print(y, x, w, z, int(F))
# 5 --------------------------------------------------------------------------
# def f(x):
#     ost = x % 3
#     s = ''
#     while x > 0:
#         s = str(x%6) + s
#         x //= 6
#     if ost == 0:
#         s = s + s[0] + s[1]
#     if ost != 0:
#         ost_10 = 10*ost
#         ost_s = ''
#         while ost_10 > 0:
#             ost_s = str(ost_10 % 6) + ost_s
#             ost_10 //= 6
#         s = s + ost_s
#     return int(s, 6)
# for N in range(6, 100):
#     if f(N) > 680:
#         print(f(N))
# 8 --------------------------------------------------------------------------
# from itertools import *
# c = 0
# for el in product('ЕКМОПРТЬ', repeat=5):
#     c += 1
#     s = ''.join(el)
#     if c % 2 != 0 and el[0]!= 'Ь'  and el.count('К') == 2:
#         print(el, c)
# 12 --------------------------------------------------------------------------
# def f(s):
#     while '12' in s or '322' in s or '222' in s:
#         if '12' in s: s = s.replace('12', '2', 1)
#         if '322' in s: s = s.replace('322', '21', 1)
#         if '222' in s: s = s.replace('222', '3', 1)
#     return s
# mx = 0
# for i in range(4, 1000):
#     s = '1' + '2'*i
#     print(f(s))
#     mx = max(mx, len(f(s)))
# print(mx)
# 13 --------------------------------------------------------------------------
# print(bin(255)[2:].zfill(8), bin(255)[2:].zfill(8), bin(255)[2:].zfill(8), bin(240)[2:].zfill(8), 'mask')
# print(bin(192)[2:].zfill(8), bin(168)[2:].zfill(8), bin(32)[2:].zfill(8), bin(160)[2:].zfill(8), 'web')
# from itertools import product
# c = 0
# for el in product('01', repeat=4):
#     if el.count('0') >= 2: c += 1
# print(c)
# 14 --------------------------------------------------------------------------
# def f(x):
#     a = 5*150**4 + 150**3 + x*150**2 + 2*150 + 9
#     b = x*150**3 + 2*150 + 3
#     return  a + b
# for x in range(150):
#     if f(x) % 149 == 0: print(f(x)//149)
# 15 --------------------------------------------------------------------------
# def TREYG(n, m, k):
#     return max(n, m, k) < n + m + k - max(n,m,k)
# def MAX(a, b):
#     if a > b: return a
#     if a <= b: return b
# for A in range(1, 1000):
#     for x in range(1, 1000):
#         F = not ((TREYG(x, 11, 18) == (not (MAX(x, 5) > 68 ))) and TREYG(x, A, 5))
#         if not F: break
#     else: print(A)
# 16 --------------------------------------------------------------------------
# def F(n):
#     if n == 151: return 264721893124
#     if n == 150: return 57080822040
#     if n == 121: return 652455454
#     if n == 120: return -246928274
#     if n == 101: return -2964234
#     if n == 100: return -17860138
#     if n == 71: return -194396
#     if n == 70: return -139656
#     if n == 51: return -8276
#     if n == 50: return -4048
#     if n == 41: return -1538
#     if n == 40: return -626
#     if n == 30: return -88
#     if n == 20: return -10
#     if n < 3: return 2
#     if n % 2 == 0 and n > 2: return 2*F(n-2) - F(n-1) + 2
#     if n % 2 != 0 and n > 2: return 2*F(n-1) + F(n-2) - 2
# print(F(170))
# 17 --------------------------------------------------------------------------
# f = open('17_10719.txt')
# a = [int(x) for x in f]
# c = 0
# mx = 0
# for i in range(len(a)-3):
#     a_0 = a[i]
#     a_1 = a[i+3]
#     cond = (abs(a_0)%100 == 13) + (abs(a_1)%100 == 13) == 1
#     if cond:
#         c += 1
#         mx = max(mx, a_0 + a_1)
# print(c, mx)
# 19-21 --------------------------------------------------------------------------
# def win(s, round):
#     if s >= 30: return round%3 == 0
#     if round == 0: return 0
#     nextWin = [win (s+1, round-1), win(s*2, round-1)]
#     return any(nextWin) if round % 3 != 0 else all(nextWin)
# print('19) ', [s for s in range(1, 30) if win(s, 3)])
# print('20) ', [s for s in range(1, 30) if not win(s, 2) and not win(s, 5) and win(s, 8)])
# print('21) ', [s for s in range(1, 30) if win(s, 1)])
# 23 --------------------------------------------------------------------------
# def f(start, end):
#     if start > end: return 0
#     if start == end: return 1
#     return f(start+2, end) + f(start**2, end) + f(start**3, end)
# print(f(10, 1000))
# 24 --------------------------------------------------------------------------
# s = open('24_10724 (2).txt').readline()
# for let in '123456789ABCDE':
#     s = s.replace(let, '*')
# mx = 0
# c = 0
# for i in range(len(s)):
#     if s[i] == '*':
#         c += 1
#         mx = max(mx, c)
#         continue
#     if s[i] == '0':
#         if s[i-1] == '*':
#             c += 1
#             mx = max(mx, c)
#             continue
#         else:
#             c = 0
#             mx = max(mx, c)
#             continue
#     if s[i] != '*':
#         c = 0
#         mx = max(mx, c)
#     mx = max(mx, c)
# print(mx)
# 25 --------------------------------------------------------------------------
# from fnmatch import *
# def dels(x):
#     arr = []
#     for i in range(1, x+1):
#         if x % i == 0:
#             arr.append(i)
#     return arr
# for N in range(65000, 800000):
#     if fnmatch(str(N), '6*97*5?') and len([s for s in dels(N) if s%2 == 0]) >= 4:
#         print(N, sum([s for s in dels(N) if s%2 == 0]))
# 26 --------------------------------------------------------------------------
# f = open('26_11566.txt')
# n = int(f.readline())
# a = []
# b = [0]*44650
# for i in range(n):
#     start, end = map(int, f.readline().split())
#     a.append([start, end])
# a.sort()
# for i in range(len(a)):
#     start, end = a[i]
#     b[start] += 1
#     b[end] -= 1
#
# k = 0
# d = 0
# c = 0
# mx = 0
# for i in range(len(b)):
#     k += b[i]
#     if k > 0:
#         c += 1
#         d += 1
#     else: d = 0
#     mx = max(mx, d)
# print(c, mx)
# 27 --------------------------------------------------------------------------
# f = [-10, 0, 2, 3, -1] #open('27-B_11567.txt')
# n = 5 #int(f.readline())
# c = 0
# m = [0]*n
# k = 0
# for i in range(n):
#     x = f[i]
#     if x > 0: k += 1
#     if x < 0: k -= 1
#     if k == 0: c += 1
#     c += m[k]
#
#     m[k] += 1
# print(c) # 21661 13385023015
# a = [int(x) for x in f]
# for i in range(n):
#     k = 0
#     for j in range(i, n):
#         if a[j] > 0: k += 1
#         if a[j] < 0: k -= 1
#         if k == 0: c += 1
# print(c) # 21661