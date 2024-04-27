# 2 --------------------------------------------------------------------------
# print('x y z w F')
# for x in range(2):
#     for y in range(2):
#         for z in range(2):
#             for w in range(2):
#                 F = (x or (not y)) and (not (y == z)) and (not w)
#                 if F: print(x, z, y ,w, int(F))
# 5 --------------------------------------------------------------------------
# def convert_3 (n):
#     s = ''
#     while n > 0:
#         s += str(n % 3)
#         n //= 3
#     return s[::-1]
# def f(n):
#     n_3 = convert_3(n)
#     if n % 3 == 0:
#         pre_last = n_3[-2]
#         last = n_3[-1]
#         n_3 += pre_last + last
#     else:
#         n_5 = convert_3((n % 3) * 5)
#         n_3 += n_5
#     return int(n_3, 3)
# min_s = 2173918301
# for i in range(3, 100):
#     if f(i) > 133:
#         min_s = min(min_s, f(i))
# print(min_s)
# 8 --------------------------------------------------------------------------
# from itertools import product
# c = 0
# for num in product('0123456789', repeat=6):
#     s = ''.join(num)
#     if s[0] != '0' and int(s) % 5 == 0:
#         s_set = set(s)
#         if len(s) == len(s_set):
#             for n in '02468': s = s.replace(n, 'ч')
#             for n in '13579': s = s.replace(n, 'н')
#             if 'чч' not in s and 'нн' not in s:
#                 c += 1
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
# max_s = -6138131313
# max_str = ''
# for i in range(4, 10_000):
#     s = '1' + '9' * i
#     res = f(s)
#     one = res.count('1')
#     four = res.count('4') * 4
#     nine = res.count('9') * 9
#     summa = one + four + nine
#     if max_s < summa:
#         max_s = summa
#         max_str = res
# print(max_s, max_str)
# 13 --------------------------------------------------------------------------
# print(bin(255)[2:].zfill(8), bin(255)[2:].zfill(8), bin(255)[2:].zfill(8), bin(192)[2:].zfill(8))
# print(bin(192)[2:].zfill(8), bin(168)[2:].zfill(8), bin(32)[2:].zfill(8), bin(128)[2:].zfill(8))
# from itertools import product
# c = 0
# for i in product('01', repeat=6):
#     if i.count('1') == 1 or i.count('1') == 3 or i.count('1') == 5: c += 1
# print(c)
# 14 --------------------------------------------------------------------------
# for x in '1234567':
#     n = int(f'{x}1{x}', 16) + int(f'{x}3{x}3', 8)
#     print(n, x)
# 15 --------------------------------------------------------------------------
# def NOD(n, m, k):
#     min_a = min(n, m)
#     max_k = -63187913
#     for i in range(1, min_a + 1):
#         if n % i == 0 and m % i == 0: max_k = max(max_k, i)
#     return max_k == k
# c = 0
# for A in range(1, 1000 + 1):
#     for x in range(1, 1000):
#         F = NOD(A, 420, 2) or ((not NOD(A, x, 12)) <= (not (NOD(110, x, 11))))
#         if not F: break
#     else: c += 1
# print(c)
# 16 --------------------------------------------------------------------------
# print(2021 + 2022 + 2020)
# 17 --------------------------------------------------------------------------
# f = open('17 (1).txt')
# a = [int(x) for x in f]
# max_121 = 20121
# c = 0
# max_s = -6783981131
#
# def chet_4 (n):
#     return len(str(abs(n))) == 4 and abs(n) % 2 == 0
#
# for i in range(len(a)-2):
#     a_0 = a[i]
#     a_1 = a[i+1]
#     a_2 = a[i+2]
#     summa = a_0 + a_1 + a_2
#     first = (chet_4(a_0) + chet_4(a_1) + chet_4(a_2)) <= 1
#     second = (summa <= max_121)
#     if first and second:
#         c += 1
#         max_s = max(max_s, summa)
# print(c, max_s)
# 19-21 --------------------------------------------------------------------------
# def win(s1,s2,s3, m):
#     if (s1 + s2 + s3) >= 25 or s1 >= 20 or s2 >= 20 or s3 >= 20: return m % 2 == 0
#     if m == 0: return 0
#     nextWin = [
#         win(s1*2, s2, s3, m - 1),
#         win(s1, s2*2, s3, m - 1),
#         win(s1, s2, s3*2, m - 1),
#         win(s1+2, s2+2, s3+2, m - 1)
#     ]
#     return any(nextWin) if (m-1) % 2 == 0 else all(nextWin)
# print('19)', [s for s in range(1, 20) if not win(2,3,s,1) and win(2,3,s,2)])
# print('19)', [s for s in range(1, 20) if not win(2,3,s,1) and win(2,3,s,3)])
# print('19)', [s for s in range(1, 20) if not win(2,3,s,2) and win(2,3,s,4)])
# 23 --------------------------------------------------------------------------
# def f(s,e):
#     if e > s: return 0
#     if s == e: return 1
#     return f(s-1,e) + f(s // 2, e)
# print(f(30, 12)*f(12, 1))
# 24 --------------------------------------------------------------------------
# s = open('24 (1).txt').readline()
# s = s.replace('NPO', '1').replace('PNO', '1').replace('N', ' ').replace('P', ' ').replace('O', ' ').split()
# print(len(max(s, key=len)))
# 25 --------------------------------------------------------------------------
# from fnmatch import fnmatch
# c = 0
# for i in range(0, 680_000, 8):
#     if fnmatch(str(i), '1*2*'):
#         print(i)
#         c += 1
# print(c)
# 26 --------------------------------------------------------------------------

# 27 --------------------------------------------------------------------------

