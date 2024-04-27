# 2 --------------------------------------------------------------------------
# for x in range(2):
#     for y in range(2):
#         for z in range(2):
#             for w in range(2):
#                 F = (x and (not z)) or (y == z) or (not w)
#                 if not F: print(w,y,z,x,int(F))
# 5 --------------------------------------------------------------------------
# def convert_3(n):
#     s = ''
#     while n > 0:
#         s += str(n % 3)
#         n //= 3
#     return s[::-1]
# def f(n):
#     n_3 = convert_3(n)
#     if n % 3 == 0:
#         pre_last =  n_3[-2]
#         last = n_3[-1]
#         n_3 += pre_last + last
#     else:
#         n_5 = convert_3((n % 3) * 5)
#         n_3 += n_5
#     return int(n_3, 3)
# max_i = -367687294
# for i in range(3, 10000):
#     if f(i) <= 242:
#         max_i = max(max_i, f(i))
# print(max_i)
# 8 --------------------------------------------------------------------------
# from itertools import product
# c = 0
# n = 0
# for word in product(sorted('ПРОГУЛКА'), repeat=5):
#     c += 1
#     s = ''.join(word)
#     if c % 2 == 0 and s[0] != 'Г' and s.count('Л') <= 2: n += 1
# print(n)
# 12 --------------------------------------------------------------------------
# def f(s):
#     while '72' in s or '522' in s or '2222' in s:
#         if '72' in s:
#             s = s.replace('72','22', 1)
#         if '522' in s:
#             s = s.replace('522','25', 1)
#         if '2222' in s:
#             s = s.replace('2222', '5', 1)
#     return s
# for i in range(4, 10_000):
#     s = '5' + i * '2'
#     res = f(s)
#     two = res.count('2') * 2
#     five = res.count('5') * 5
#     seven = res.count('7') * 7
#     summa = two + five + seven
#     if summa == 63:
#         print(i, res)
#         break
# 13 --------------------------------------------------------------------------
# print(bin(255)[2:].zfill(8), bin(255)[2:].zfill(8), bin(255)[2:].zfill(8), bin(192)[2:].zfill(8))
# print(bin(222)[2:].zfill(8), bin(63)[2:].zfill(8), bin(131)[2:].zfill(8), bin(128)[2:].zfill(8))
# from itertools import product
# c = 0
# for num in product('01', repeat=6):
#     if num.count('1') == 4: c += 1
# print(c)
# 14 --------------------------------------------------------------------------
# for x in '0123456789ABCDEFGHI':
#     s = int(f'5{x}642535', 19) + int(f'78{x}11114', 19) + int(f'9334{x}39', 19)
#     if s % 18 == 0: print(x, s // 18)
# 15 --------------------------------------------------------------------------
# B = list(range(24, 91))
# C = list(range(47, 116))
# A = []
# for x in range(-1000, 1000):
#     F = (x in C) <= ((not (x in A) and (x in B)) <= (not (x in C)))
#     if not F: A += [x]
# print(A)
# 16 --------------------------------------------------------------------------
# print(2019 + 2018)
# 17 --------------------------------------------------------------------------
# f = open('17 (2).txt')
# a = [int(x) for x in f]
# min_3 = -9963
# c = 0
# max_s = -4657682909
# for i in range(len(a)-2):
#     a_0 = a[i]
#     a_1 = a[i+1]
#     a_2 = a[i+2]
#     summa = a_0 + a_1 + a_2
#     first = ((abs(a_0) % 10 == 3) + (abs(a_1) % 10 == 3) + (abs(a_2) % 10 == 3)) <= 2
#     second = summa >= min_3
#     if first and second:
#         c += 1
#         max_s = max(max_s, summa)
# print(c, max_s)
# 19-21 --------------------------------------------------------------------------
# def win(s, m):
#     if s >= 65: return m % 2 == 0
#     if m == 0: return 0
#     nextWin = [
#         win(s + 1, m - 1),
#         win(s + 2, m - 1),
#         win(s * 3, m - 1),
#     ]
#     return any(nextWin) if (m - 1) % 2 == 0 else all(nextWin)
# print('19)', [s for s in range(1, 65) if not win(s, 1) and win(s, 2)])
# print('20)', [s for s in range(1, 65) if not win(s, 1) and win(s, 3)])
# print('21)', [s for s in range(1, 65) if not win(s, 2) and win(s, 4)])
# 23 --------------------------------------------------------------------------
# def f(s, e):
#     if s > e or s == 15: return 0
#     if s == e: return 1
#     return f(s+1, e) + f(s+2, e) + f(s*2, e)
# print(f(3, 9) * f(9, 17))
# 24 --------------------------------------------------------------------------
# s = open('24 (2).txt').readline()
# print(len(s))
# s = s.split('Y')
# max_s = -74287939
# c = 0
# y = 0
# arr = [0] * len(s)
# for i in range(len(s)):
#     len_s = len(s[i])
#     y += 1
#     c += len_s
#     arr[i] = len_s
#     max_s = max(max_s, c)
#
#     if y == 150:
#         y -= 1
#         c -= arr[i - 150]
# print(max_s + 150)
# 25 --------------------------------------------------------------------------
# from fnmatch import fnmatch
# for i in range(0, 10**8, 323):
#     if fnmatch(str(i), '2*8?6?13'):
#         print(i, i // 323)
# 26 --------------------------------------------------------------------------
# f = open('26 (1).txt')
# n = int(f.readline())
# data = []
# for s in f:
#     s, e = map(int, s.split())
#     data += [[e, s]]
# data.sort()
# is_free = 0
# c = []
#
# for e, s in data:
#     if len(c) == 12 and s >= is_free:
#         print(s, e)
#         continue
#     if s >= is_free:
#         c += [[s, e]]
#         is_free = e
# print(len(c), c)
# 27 --------------------------------------------------------------------------
# f = open('27-B.txt')
# k = int(f.readline())
# n = int(f.readline())
# mx = max_back = max_p_back = -3526768793631
# a = [int(x) for x in f]
# for i in range(2*k, n):
#     max_back = max(max_back, a[i - 2*k])
#     max_p_back = max(max_p_back, max_back + a[i-k])
#     mx = max(mx, max_p_back + a[i])
# print(mx)
