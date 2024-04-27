# 2 --------------------------------------------------------------------------
# print('x z y w F')
# for x in range(2):
#     for y in range(2):
#         for z in range(2):
#             for w in range(2):
#                 F = (x or (not y)) and (not (y == z)) and (not w)
#                 if F: print(x, z, y, w, int(F))
# 5 --------------------------------------------------------------------------
# def convert_3 (n):
#     s = ''
#     while n > 0:
#         s += str(n % 3)
#         n //= 3
#     return s[::-1]
# def f(n):
#     ost_3 = n % 3
#     n_3 = convert_3(n)
#     if ost_3 == 0:
#         last_0 = n_3[-2]
#         last_1 = n_3[-1]
#         n_3 += last_0 + last_1
#     if ost_3 != 0:
#         n_3 += convert_3(ost_3 * 5)
#     return int(n_3, 3)
# min_res = 64278739
# for i in range(3, 100000):
#     res = f(i)
#     if res > 133:
#         min_res = min(min_res, res)
# print(min_res)
# 8 --------------------------------------------------------------------------
# from itertools import *
# c = 0
# for word in product('0123456789', repeat=6):
#     num = ''.join(word)
#     if num[0] != '0' and len(set(num)) == len(num) and int(num) % 5 == 0:
#         for i in '02468': num = num.replace(str(i), 'r')
#         for i in '13579': num = num.replace(str(i), 'f')
#         if 'rr' not in num and 'ff' not in num: c += 1
# print(c)
# 12 --------------------------------------------------------------------------
# def f(s):
#     while '19' in s or '49' in s or '999' in s:
#         if '19' in s:
#             s = s.replace('19', '9', 1)
#         if '49' in s:
#             s = s.replace('49', '91', 1)
#         if '999' in s:
#             s = s.replace('999', '4', 1)
#     return s
# max_s = -3627893
# for i in range(4, 10000):
#     s = '1' + '9'*i
#     res = f(s)
#     summa = sum(map(int, res))
#     max_s = max(summa, max_s)
# print(max_s)
# 13 --------------------------------------------------------------------------
# print(bin(255)[2:].zfill(8), bin(255)[2:].zfill(8), bin(255)[2:].zfill(8), bin(192)[2:].zfill(8))
# print(bin(192)[2:].zfill(8), bin(168)[2:].zfill(8), bin(32)[2:].zfill(8), bin(128)[2:].zfill(8))
# c = 0
# from itertools import product
# for i in product('10', repeat=6):
#     s = ''.join(i)
#     count = s.count('1')
#     if count == 3 or count == 1 or count == 5:
#         print(s)
#         c += 1
# print(c)
# 14 --------------------------------------------------------------------------
# for x in '1234567':
#     res = int(f'{x}1{x}', 16) + int(f'{x}3{x}3', 8)
#     print(x, res)
# 15 --------------------------------------------------------------------------
# def dels(n):
#     ans = []
#     for i in range(1, int(n**0.5)+1):
#         if n % i == 0:
#             ans += [i, n // i]
#     return sorted(list(set(ans)))
# def NOD (n, m, k):
#     dels_m = dels(m)
#     max_del = -381393
#     for i in dels_m:
#         if n % i == 0:
#             max_del = max(max_del, i)
#     return max_del == k
# ans = []
# for A in range(1, 1001):
#     for x in range(1, 1001):
#         F = NOD(A, 420, 2) or ((not NOD(A, x, 12)) <= (not NOD(110, x, 11)))
#         if not F: break
#     else: ans.append(A)
# print(len(ans))
# 16 --------------------------------------------------------------------------
# бумажка какашка
# 17 --------------------------------------------------------------------------
# f = open('17.txt')
# a = [int(x) for x in f]
# max_121 = 20121
# def cond(n):
#     first = abs(n) % 2 == 0
#     second = len(str(abs(n))) == 4
#     return first and second
# c = 0
# max_s = -3728322
#
# for i in range(len(a) - 2):
#     a_0 = a[i]
#     a_1 = a[i+1]
#     a_2 = a[i+2]
#     first = (cond(a_0) + cond(a_1) + cond(a_2)) <= 1
#     second = (a_0 + a_1 + a_2) <= max_121
#     if first and second:
#         c += 1
#         max_s = max(max_s, a_0 + a_1 + a_2)
# print(c, max_s)
# 19-21 --------------------------------------------------------------------------
# def win(s1, s2, s3, m):
#     if s1 >= 20 or s2 >= 20 or s3 >= 20 or s1 + s2 + s3 >= 25: return m % 2 == 0
#     if m == 0: return 0
#     nextWin = [
#         win(s1 + 2, s2 + 2, s3 + 2, m - 1),
#         win(s1 * 2, s2, s3, m - 1),
#         win(s1, s2 * 2, s3, m - 1),
#         win(s1, s2, s3 * 2, m - 1)
#     ]
#     return any(nextWin) if (m - 1) % 2 == 0 else all(nextWin)
# print('19)', [s for s in range(1, 20) if not win(2, 3, s, 1) and win(2, 3, s, 2)])
# print('20)', [s for s in range(1, 20) if not win(2, 3, s, 1) and win(2, 3, s, 3)])
# print('21)', [s for s in range(1, 20) if not win(2, 3, s, 2) and win(2, 3, s, 4)])
# 23 --------------------------------------------------------------------------
# def f(s, e):
#     if s < e: return 0
#     if s == e: return 1
#     return f(s - 1, e) + f(s // 2, e)
# print(f(30, 12)*f(12,1))
# 24 --------------------------------------------------------------------------
# s = open('24.txt').readline()
# s = s.replace('NPO', '1')
# s = s.replace('PNO', '1')
# s = s.replace('P', '0')
# s = s.replace('O', '0')
# s = s.replace('N', '0')
# s = s.split('0')
# print(len(max(s, key=len)))
# 25 --------------------------------------------------------------------------
# from fnmatch import fnmatch
# c = 0
# for i in range(0, 680_000, 8):
#     if fnmatch(str(i), '1*2*'): c += 1
# print(c)
# 26 --------------------------------------------------------------------------
# какая-то хуйня
# 27 --------------------------------------------------------------------------
f = open('27_A.txt')
N = int(f.readline())
a = [int(x) for x in f]
s = ''
def deltaPosl(s):
    summa = 0
    for i in range(0, len(s) - 1):
        summa += s[i + 1] - s[i]
    return summa
max_delta = -36178313113
for i in range(N):
    for j in range(i, N):
        arr = [a[x] for x in range(i, j + 1)]
        if deltaPosl(arr) > max_delta:
            max_delta = deltaPosl(arr)
            s = arr
print(max_delta, s) #9939

