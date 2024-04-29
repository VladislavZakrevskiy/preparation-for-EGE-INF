# 2 --------------------------------------------------------------------------
# print('x y z w F')
# for x in range(2):
#     for y in range(2):
#         for z in range(2):
#             for w in range(2):
#                 F = ((x <= y) or (z <= w)) and (not (x <= w))
#                 arr = [x, y, z, w]
#                 if not F and arr[0] == 1 and arr[1] == 0 and arr[2] == 1:
#                     print(x, y, z, w, int(F))
# for x in range(2):
#     for y in range(2):
#         for z in range(2):
#             for w in range(2):
#                 F = ((x <= y) or (z <= w)) and (not (x <= w))
#                 arr = [x, y, z, w]
#                 if F and arr[0] == 1 and arr[3] == 1:
#                     print(x, y, z, w, int(F))
#                 if F and arr[2] == 1 and arr[3] == 0:
#                     print(x, y, z, w, int(F))
# 5 --------------------------------------------------------------------------
# def convert_to (N, base=3):
#     s = ''
#     while N > 0:
#         s = str(N%base) + s
#         N //= base
#     return s
# def f(N):
#     ost = N % 4
#     N_3 = convert_to(N)
#     if ost == 0:
#         N_3 += N_3[-1] + N_3[-2] + N_3[-3]
#     if ost != 0:
#         ost_4 = ost * 4
#         ost_3 = convert_to(ost_4)
#         N_3 += ost_3
#     return int(N_3, 3)
# for N in range(9, 1000):
#     if f(N) < 127: print(f(N))
# 8 --------------------------------------------------------------------------
# from itertools import *
# c = 0
# for el in permutations('014689ACEFG',r=6):
#     s = ''.join(el)
#     if el[0] in '468ACEG': c += 1
# print(c) # 211680
# 12 --------------------------------------------------------------------------
# def f(s):
#     while ('52' in s) or ('222' in s) or ('122' in s):
#         if '52' in s: s = s.replace('52','11',1)
#         if '222' in s: s = s.replace('222','15',1)
#         if '122' in s: s = s.replace('122','21',1)
#     return s
# def summa_cifr(s):
#     summa = 0
#     for num in s: summa += int(num)
#     return summa
# def is_quadrat(x):
#     sqrt = x ** 0.5
#     return sqrt % 1 == 0
# for i in range(4, 1000):
#     s = '5' + '2' * i
#     if is_quadrat(summa_cifr(f(s))): print(i)
# 13 --------------------------------------------------------------------------
# from itertools import *
# print(bin(255)[2:].zfill(8), bin(255)[2:].zfill(8), bin(252)[2:].zfill(8), bin(0)[2:].zfill(8), 'mask')
# print(bin(172)[2:].zfill(8), bin(118)[2:].zfill(8), bin(1)[2:].zfill(8), bin(255)[2:].zfill(8), 'ip')
# c = 0
# for el in product('01', repeat=10):
#     if el.count('1') == 2 or el.count('1') == 4 or el.count('1') == 8: c+=1
# print(c)
# 14 --------------------------------------------------------------------------
# def convert_to(x, base=17):
#     s = ''
#     cifri = '0123456789ABCDEFG'
#     while x > 0:
#         s = str(cifri[x%base]) + s
#         x //= base
#     return s
# a = 5*3**1917 + 6*2**1878 + 7*3**1870 - 1991
# k = [0]*17
# res = convert_to(a)
# for el in res:
#     k[int(el, 17)] += 1
# print(k)
# 15 --------------------------------------------------------------------------
# for A in range(-10000, 10000):
#     for x in range(1, 1000):
#         F = (x&A != 0) or ((x&52 == 0) and (x&14 == 0))
#         if not F: break
#     else: print(A)
# 16 --------------------------------------------------------------------------
# def f(x):
#     if x == 2501: return 3128751
#     if x == 2001: return 2003001
#     if x == 1501: return 1127251
#     if x == 1101: return 606651
#     if x == 901: return 406351
#     if x < 3: return 1
#     if x > 2: return 2*x - 1 + f(x-2)
# print(f(3033))
# 17 --------------------------------------------------------------------------
# def convert_to(x, base=6):
#     s = ''
#     cifri = '0123456789ABCDEFG'
#     while x > 0:
#         s = str(cifri[x%base]) + s
#         x //= base
#     return s
#
# f = open('17_10126.txt')
# a = [int(x) for x in f]
# mx_23 = 99987 # max(x for x in a if len(convert_to(x)) >= 2 and convert_to(x)[-1] == '3' and convert_to(x)[-2] == '2')
# c = 0
# mx = 0
# for i in range(len(a) - 3):
#     a_0 = a[i]
#     a_1 = a[i+1]
#     a_2 = a[i+2]
#     cond1 = (1000 <= abs(a_0) <= 9999) + (1000 <= abs(a_1) <= 9999) + (1000 <= abs(a_2) <= 9999) == 1
#     cond2 = (a_0  + a_1 + a_2) % mx_23 == 0
#     if cond2 and cond1:
#         c += 1
#         mx = max(mx, a_0 + a_1 + a_2)
# print(c, mx)
# 19-21 --------------------------------------------------------------------------
# def win(s, round):
#     if s >= 248: return round%2 == 0
#     if round == 0: return 0
#     nextWin = [win(s+1, round-1), win(s+2, round-1), win(s*3, round-1)]
#     return any(nextWin) if (round-1)%2 == 0 else all(nextWin)
#
# print('19) ', [s for s in range(1, 248) if not win(s, 1) and win(s, 2)])
# print('20) ', [s for s in range(1, 248) if not win(s, 1) and win(s, 3)])
# print('21) ', [s for s in range(1, 248) if not win(s, 2) and win(s, 4)])
# 23 --------------------------------------------------------------------------
# def f(start, end):
#     if start > end or start == 13: return 0
#     if start == end: return 1
#     return f(start+1,end) + f(start+5, end) + f(start*2, end)
# print(f(7, 25))
# 24 --------------------------------------------------------------------------
# s = open('24_10131.txt').readline()
# k = 0
# m = [10**20]*len(s)
# mx = 0
# for el in 'QWERTYUIOPSDFGHJKLZXCVNM':
#     s = s.replace(el, '0')
# for i in range(len(s)):
#     if s[i] == 'A': k += 1
#     if s[i] == 'B': k -= 1
#     if k == 0: mx = max(mx, i + 1)
#     mx = max(mx, i - m[k])
#
#     m[k] = min(i, m[k])
# print(mx)
# 25 --------------------------------------------------------------------------
# from fnmatch import *
# for i in range(0, 10**9, 1024):
#     if fnmatch(str(i), '3?5?21*4?') and i % 1024 == 0:
#         print(i, i // 1024)
# 26 --------------------------------------------------------------------------
# f = open('26_10072.txt')
# n = int(f.readline())
# a = [int(x) for x in f]
# a.sort()
# c = 0
# max_sum = 0
# for i_mx in range(len(a)-1, -1, -1):
#     mx = a[i_mx]
#     for j_1 in range(0, len(a)):
#         a_0 = a[j_1]
#         for j_2 in range(0, len(a)):
#             a_1 = a[j_2]
#             if mx < a_0 + a_1:
#                 c += 1
#                 max_sum = max(a_0, a_1, mx)
#             else: break
# print(c, max_sum)
# 27 --------------------------------------------------------------------------
# f = open('27B_10134.txt')
# k = int(f.readline())
# n = int(f.readline())
# a = [int(x) for x in f]
# mx = -10**20
# mx_back = (10**20, -10**20)
# mx_back_proizv = (10**20, -10**20)
#
#
# for i in range(2*k, n):
#     mx_back = (min(mx_back[0], a[i-2*k]), max(mx_back[1], a[i-2*k]))
#     mx_back_proizv = (min(mx_back_proizv[0], mx_back[0]*a[i-k], mx_back[1]*a[i-k]), max(mx_back_proizv[1], mx_back[1]*a[i-k],  mx_back[0]*a[i-k]))
#     mx = max(mx, mx_back_proizv[0]*a[i],  mx_back_proizv[1]*a[i])
#
# print(mx % (10**9 + 7))


