# 2 --------------------------------------------------------------------------
# print('w x y z F')
# for x in range(2):
#     for y in range(2):
#         for z in range(2):
#             for w in range(2):
#                 F = ((x and (not y)) <= (z and w)) and ((y <= z) or (w <= x))
#                 if not F:
#                     print(y, z, w, x, int(F))
# 5 --------------------------------------------------------------------------
# alf = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B']
# def convert_12(n):
#     s = ''
#     while n > 0:
#         s += alf[n % 12]
#         n //= 12
#     return s[::-1]
# def f(n):
#     ost_4 = n % 4
#     n_12 = convert_12(n)
#     if ost_4 == 0:
#         n_12 = '2' + n_12 + '64'
#     else:
#         max_n = -12313
#         list_n_12 = list(n_12)
#         for num in list_n_12:
#             max_n = max(max_n, int(num, 12))
#         max_n = alf[max_n]
#         n_12 += max_n
#     return int(n_12, 12)
# min_r = 382848029424
# for i in range(10000):
#     if f(i) > 1799:
#         min_r = min(min_r, f(i))
# print(min_r)
# 8 --------------------------------------------------------------------------
# from itertools import product
# def is_correct(word):
#     if word[0] == '0':
#         return False
#
#     if word[-1] == '7' and word[-2] in ['1', '3', '5', '7']:
#         return False
#
#     if word[0] == '7' and word[1] in ['1', '3', '5', '7']:
#         return False
#
#     if (word.count('0') + word.count('2') + word.count('4') + word.count('6')) != 2:
#         return False
#     for i in range(len(word)-2):
#         a_0 = word[i]
#         a_1 = word[i+1]
#         a_2 = word[i+2]
#         if a_1 == '7' and (a_0 in ['1', '3', '5', '7'] or a_2 in ['1', '3', '5', '7']):
#             return False
#     return True
# c = 0
# for word in product('01234567', repeat=7):
#     if is_correct(word):
#         c += 1
# print(c)
# 12 --------------------------------------------------------------------------
# def f(s):
#     while '57' in s or '877' in s or '777' in s:
#         if '57' in s:
#             s = s.replace('57', '7', 1)
#         if '877' in s:
#             s = s.replace('877', '75', 1)
#         if '777' in s:
#             s = s.replace('777', '8', 1)
#     return s
# max_s = -113131
# for i in range(4, 10000):
#     s = '5' + '7'*i
#     res = f(s)
#     five = res.count('5')*5
#     seven = res.count('7')*7
#     eight = res.count('8')*8
#     max_s = max(max_s, five + seven + eight)
# print(max_s)
# 13 --------------------------------------------------------------------------
# print(bin(255)[2:].zfill(8), bin(255)[2:].zfill(8), bin(255)[2:].zfill(8), bin(192)[2:].zfill(8))
# print(bin(207)[2:].zfill(8), bin(0)[2:].zfill(8), bin(0)[2:].zfill(8), bin(167)[2:].zfill(8))
# 14 --------------------------------------------------------------------------
# for x in '0123456789ABCDEFGHIJ':
#     s = int(f'931{x}964', 32) + int(f'4{x}51{x}1', 32) + int(f'2861{x}637', 32)
#     if s % 31 == 0:
#         print(x, s//31)
# 15 --------------------------------------------------------------------------
# for A in range(1,1000):
#     is_good = True
#     for x in range(1,1000):
#         for y in range(1,1000):
#             F = ((x**2 + y**2) > 1024 - x) or (y < -2*x + A)
#             if not F:
#                 is_good = False
#                 break
#         if not is_good:
#             break
#     if is_good:
#         print(A)
# 16 --------------------------------------------------------------------------
# from functools import lru_cache
# @lru_cache(maxsize=None)
# def f(n):
#     if n < 10: return n
#     return g(f(n - 1) % 10) + f(g(n % 10) - 1) - f(n-3)
# @lru_cache(maxsize=None)
# def g(n):
#     if n < 10: return -n
#     return f(g(n - 1) % 10) + g(f(n - 1) - 1) + g(n-2)
# for i in range(1112):
#     f(i)
#     g(i)
# print(f(1111) + g(1111))
# 17 --------------------------------------------------------------------------
# f = open('17_11838.txt')
# a = [int(x) for x in f]
# max_50 = 67050
# def is_5znach(n):
#     return 10_000 <= abs(n) and abs(n) <= 100_000
# c = 0
# max_s = -247842949882
# for i in range(len(a)-2):
#     a_0 = a[i]
#     a_1 = a[i+1]
#     a_2 = a[i+2]
#     first = (a_0 != a_1) and (a_1 != a_2) and (a_2 != a_0)
#     second = is_5znach(a_0) and is_5znach(a_1) and is_5znach(a_2)
#     third = ((a_0 + a_1 + a_2) <= max_50)
#     if first and second and third:
#         c += 1
#         max_s = max(max_s, a_0 + a_1 + a_2)
# print(c, max_s)
# 19-21 --------------------------------------------------------------------------
# def win(s1, s2, m):
#     if s1 + s2 >= 375: return m % 2 == 0
#     if m == 0: return 0
#     nextWin = [
#         win(s1 + 3, s2, m - 1),
#         win(s1 * 2, s2, m - 1),
#         win(s1, s2 + 3, m - 1),
#         win(s1, s2 * 2, m - 1),
#     ]
#     return any(nextWin) if (m - 1) % 2 == 0 else all(nextWin)
# print('19)', [s for s in range(1, 348) if win(27, s, 2)]) # 87
# print('19)', [s for s in range(1, 348) if not win(27, s, 1) and win(27, s, 3)])
# print('19)', [s for s in range(1, 348) if not win(27, s, 2) and win(27, s, 4)])
# 23 --------------------------------------------------------------------------
# def f(s, e):
#     if s == e: return 1
#     if s < e or s == 20: return 0
#     return f(s-2, e) + f(s-3, e) + f(s%5, e)
# print(f(41, 10)*f(10, 5))
# 24 --------------------------------------------------------------------------
# s = open('24_11813.txt').readline().strip()
# k = max_k = 1
#
# for i in range(len(s) - 1):
#     if (s[i] in 'EYUIOA') != (s[i+1] not in 'EYUIOA'):
#         k += 1
#         max_k = max(max_k, k)
#     else:
#         k = 1
# print(max_k)
# 25 --------------------------------------------------------------------------
# from itertools import product
# arr = []
# for x in range(10):
#     for y in product('0123456789', repeat=3):
#         num = int(f'21{''.join(y)}68{x}79')
#         if num % 1777 == 0:
#             arr += [[num, num // 1777]]
# arr.sort(key=lambda x: x[0])
# for i in arr:
#     print(i[0], i[1])
# 26 --------------------------------------------------------------------------

# 27 --------------------------------------------------------------------------
