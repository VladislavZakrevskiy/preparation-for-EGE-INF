# 2 --------------------------------------------------------------------------
# for x in range(2):
#     for y in range(2):
#         for z in range(2):
#             F = (x==y) or ((z or y) <= x)
#             if not F: print(x, y, z)
# 5 --------------------------------------------------------------------------
# def f(n):
#     s_odd = 0
#     s_even = 0
#     str_n = str(n)
#     for i in range(len(str_n)):
#         if i % 2 == 0: s_even += int(str_n[i])
#         else: s_odd += int(str_n[i])
#     arr = [s_odd, s_even]
#     arr.sort()
#     arr = map(lambda x: str(x), arr)
#     return int(''.join(arr))
#
# for i in range(10_000, 100_000):
#     if f(i) == 621:
#         print(i)
#         break
# 7 --------------------------------------------------------------------------
# S = 1000 * 800
# max_s = 800 * 2**13
# print(S * 8 / 2**13)
# 8 --------------------------------------------------------------------------
# from itertools import product
# c = 0
# for word in product('АДМТ', repeat=5):
#     c += 1
#     if c == 330:
#         print(word)
#         break
# 12 --------------------------------------------------------------------------
# def f(s):
#     while '22' in s:
#         if '224' in s:
#             s = s.replace('224', '9', 1)
#         else: s = s.replace('22', '5', 1)
#     return s
# print(f('2'*8 + '224'*6))
# 13 --------------------------------------------------------------------------
# print(bin(192)[2:].zfill(8), bin(138)[2:].zfill(8), bin(245)[2:].zfill(8), bin(125)[2:].zfill(8))
# print(bin(255)[2:].zfill(8), bin(255)[2:].zfill(8), bin(240)[2:].zfill(8), bin(0)[2:].zfill(8))
# print(int('11110000', 2))
# 14 --------------------------------------------------------------------------
# def convert_6(n):
#     s = ''
#     while n > 0:
#         s += str(n % 6)
#         n //= 6
#     return s[::-1]
# print(convert_6(36**7 + 6**30 - 12).count('5'))
# 15 --------------------------------------------------------------------------
# for A in range(1000):
#     is_x_good = True
#     for x in range(1000):
#         for y in range(1000):
#             F = (x + 2*y > 16) or (x + y <= A)
#             if not F:
#                 is_x_good = False
#                 break
#         if not is_x_good: break
#     if is_x_good: print(A)
# 16 --------------------------------------------------------------------------
# def f(n):
#     if n == 1: return 1
#     if n == 2: return 2
#     return 3*f(n-1) - f(n-2)
# print(f(8))
# 17 --------------------------------------------------------------------------
# f = open('17_2024-0a7fd6d6-50b1-4904-ac02-bd03198ddc2d.txt')
# print(f.readline())
# a = [3150] + [int(x) for x in f]
# print(a)
# c = 0
# max_s = -728793692
#
# for i in range(len(a)-1):
#     a_0 = a[i]
#     a_1 = a[i+1]
#     first = ((a_0 % 4 == 0) + (a_1 % 4 == 0)) >= 1
#     second = (a_0 + a_1) % 7 == 0
#     if first and second:
#         c += 1
#         max_s = max(max_s, a_0 + a_1)
# print(c, max_s)
# 19-21 --------------------------------------------------------------------------
# def win(s, m):
#     if s >= 41: return m % 2 == 0
#     if m == 0: return 0
#     nextWin = [
#         win(s + 2, m - 1),
#         win(s + 3, m - 1),
#         win(s * 2, m - 1),
#     ]
#     return any(nextWin) if (m-1) % 2 == 0 else all(nextWin)
# print('19)', [s for s in range(1, 41) if win(s, 2)])
# print('19)', [s for s in range(1, 41) if not win(s, 1) and win(s, 3)])
# print('19)', [s for s in range(1, 41) if not win(s, 2) and win(s, 4)])
# 23 --------------------------------------------------------------------------
# def f(s, e):
#     if s > e: return 0
#     if s == e: return 1
#     return f(s + 1, e) + f(s + 4, e) + f(s * 2, e)
# print(f(1, 10) * f(10, 24))
# 24 --------------------------------------------------------------------------
# s = open('24_2024-9fa13bf9-1fd0-4076-aa0e-7ed119cb2796.txt').readline()
# print(len(s))
# c = max_c = 2
# for i in range(2, len(s)):
#     if int(s[i-2]) + int(s[i-1]) < int(s[i]):
#         c += 1
#         max_c = max(max_c, c)
#     else:
#         count = 3
# print(max_c)
# 25 --------------------------------------------------------------------------
# from fnmatch import fnmatch
# for i in range(0, 10**7, 2024):
#     if fnmatch(str(i), '2?3*96'):
#         print(i, i // 2024)
# 26 --------------------------------------------------------------------------
# f = open('26_2024-6620c40d-3dc3-4f03-928e-d029ea280057.txt')
# a, b = f.readline().split()
# d = []
# s = 0
# count = 0
# for i in f:
#     if 210 <= int(i) <= 220:
#         s += int(i)
#         count += 1
#     else:
#         d.append(int(i))
# d.sort()
# d2 = []
# i = 0
# while sum(d2) + d[i] <= int(b) - s:
#     count += 1
#     d2.append(d[i])
#     i += 1
# k = len(d) - 1
# while i > 0:
#     while k >= 0:
#         if sum(d2) - d2[i-1] + d[k] <= int(b) - s and d[k] != 0:
#             d2[i-1] = d[k]
#             d[k] = 0
#             i -= 1
#             break
#         else:
#             k -= 1
# s += sum(d2)
# print(count, s)
# 27 --------------------------------------------------------------------------
f = open('27_b_2024-0dbbe2b9-e968-440f-9012-76b645b510bf.txt')
n = int(f.readline())
summ = 0
raznica3 = []
for i in range(n):
    a, b = f.readline().split()
    a = int(a)
    b = int(b)
    summ = summ + max(a, b)
    r1 = max(a, b) - min(a, b)
    if r1 % 3 != 0:
     raznica3.append(r1)
raznica3 = sorted(raznica3)
if summ % 3 == 0:
    print(summ)
else:
    i = 0
    k = 0
    while summ % 3 != 0:
        i = i + 1
        if summ % 3 != 0:
            summ = summ - raznica3[i]
            if summ % 3 == 0:
                print(summ)
                break
            else:
                summ = summ + raznica3[i]
                i = i + 1
        if k < 1:
            summ = summ - raznica3[0] - raznica3[1]
            if summ % 3 == 0:
                print(summ)
                k = k + 1
                break
            else:
                summ = summ + raznica3[0] + raznica3[1]
                k = k + 1
