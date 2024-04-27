# 2 --------------------------------------------------------------------------
# print('w x y z F')
# for x in range(2):
#     for y in range(2):
#         for z in range(2):
#             for w in range(2):
#                 F = (not (x == (w and (not z)))) and (y == (x and (not w)))
#                 if F:
#                     print(w, x, y, z, int(F))
# 5 --------------------------------------------------------------------------
# def f(n):
#     bin_n = bin(n)[2:]
#     bin_arr = list(bin_n)
#     if bin_n.count('1') % 2 == 0:
#         bin_arr[0] = '1'
#         bin_arr[1] = '1'
#         bin_arr += ['0']
#     else:
#         bin_arr[0] = '1'
#         bin_arr[1] = '0'
#         bin_arr += ['1']
#     return int(''.join(bin_arr), 2)
# max_n = -1000000
# for i in range(2, 50):
#     max_n = max(max_n, f(i))
# print(max_n)
# 8 --------------------------------------------------------------------------
# from itertools import permutations
# sogl = ['С', 'В', 'Т']
# glas = ['О', 'Е', 'Ь']
# def is_correct(word):
#     for i in range(len(word)-1):
#         l_0 = word[i]
#         l_1 = word[i+1]
#         if (l_0 in sogl and l_1 in sogl) or (l_0 in glas and l_1 in glas):
#             return False
#     return True
# c = 0
# for perm in permutations('СОВЕСТЬ', r=7):
#     if is_correct(perm):
#         c += 1
# print(c)
# 12 --------------------------------------------------------------------------
# def f(s):
#     while '25' in s or '355' in s or '555' in s:
#         if '25' in s:
#             s = s.replace('25', '5', 1)
#         if '355' in s:
#             s = s.replace('355', '52', 1)
#         if '555' in s:
#             s = s.replace('555', '3', 1)
#     return s
# for i in range(4, 1000):
#     s = '2' + '5'*i
#     if f(s).count('3') == 3:
#         print(i)
#         break
# 13 --------------------------------------------------------------------------
# print(bin(255)[2:].zfill(8), bin(255)[2:].zfill(8), bin(255)[2:].zfill(8), bin(224)[2:].zfill(8))
# print(bin(246)[2:].zfill(8), bin(81)[2:].zfill(8), bin(65)[2:].zfill(8), bin(0)[2:].zfill(8))
# 14 --------------------------------------------------------------------------
# def convert_5(n):
#     str_n = ''
#     while n > 0:
#         str_n += str(n % 5)
#         n //= 5
#     return str_n[::-1]
#
# max_xy = -1000000
# for x in range(1000):
#     for y in range(1000):
#         num = 5**50 + 5**30 - 5**x - y - 5**y - x
#         num_5 = convert_5(num)
#         if num_5.count('0') == 10:
#             max_xy = max(max_xy, x*y)
# print(max_xy)
# 16 --------------------------------------------------------------------------
# for A in range(1000):
#     for x in range(90,101):
#         F = (not (x&79 == 0)) and ((x&31 == 0) <= (not (x&A == 0)))
#         if not F: break
#     else: print(A)
# 17 --------------------------------------------------------------------------
# from functools import lru_cache
# @lru_cache(maxsize=None)
# def f(n):
#     if n < 5: return 4
#     if n > 4: return 4*f(n-4)
# print(f(4444)/f(4400))
# 17 --------------------------------------------------------------------------
# f = open('17_12450.txt')
# a = [int(x) for x in f]
# min_52 = 52
# c = 0
# max_s = -213424352678
# for i in range(len(a)-2):
#     a_0 = a[i]
#     a_1 = a[i+1]
#     a_2 = a[i+2]
#     if ((a_0 % 113) + (a_1 % 113) + (a_2 % 113)) == min_52:
#         c += 1
#         max_s = max(max_s, a_0 + a_1 + a_2)
# print(c, max_s)
# 19-21 --------------------------------------------------------------------------
# def win(s1,s2,m):
#     if s1*s2 >= 777: return m % 2 == 0
#     if m == 0: return 0
#     nextWin = [
#         win(s1+3,s2,m-1),
#         win(s1*2,s2, m-1),
#         win(s1, s2+3, m-1),
#         win(s1, s2*2, m-1),
#     ]
#     return any(nextWin) if (m-1) % 2 == 0 else all(nextWin)
# print('19)', [s for s in range(1, 111) if win(7, s, 2)]) # 28
# print('20)', [s for s in range(1, 111) if not win(7, s, 1) and win(7, s, 3)])
# print('21)', [s for s in range(1, 111) if not win(7, s, 2) and win(7, s, 4)])
# 23 --------------------------------------------------------------------------
# def f(s, e, A):
#     if A >= 3: return 0
#     if s == e: return 1
#     if s + 4 > e: return 0
#     return f(s-2, e, A + 1) + f(s*2, e, A) + f(s*3, e, A)
# print(f(6,48, 0))
# 24 --------------------------------------------------------------------------
# s = open('24_12410.txt').readline()
# list_s = list(s)
# narysh = 0
# i_nar = [0 for i in range(len(list_s))]
# max_len = -10
# print(len(list_s))
# for i in range(len(list_s)-1):
#     l_0 = list_s[i]
#     l_1 = list_s[i+1]
#     if l_0 > l_1:
#         narysh += 1
#         i_nar[i] = i
#     if narysh > 100000:
#         i_nar[i] = i
#     if narysh >= 100_000:
#         max_len = max(max_len, i - i_nar[i - 100_000] + 1)
# print(max_len)
# 25 --------------------------------------------------------------------------
# def dels(n):
#     delits = []
#     for i in range(1, int(n ** 0.5)+1):
#         if n % i == 0: delits += [i, n //i]
#     return delits
#
# from fnmatch import fnmatch
# for i in range(0, 10**10, 7777):
#     if fnmatch(str(i), '12*567?') and i % 2 == 0:
#         print(i , i//7777)
# 26 --------------------------------------------------------------------------

# 27 --------------------------------------------------------------------------
