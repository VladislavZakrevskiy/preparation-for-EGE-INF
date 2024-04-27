# 2 --------------------------------------------------------------------------
# print('x w z y F')
# for x in range(2):
#     for y in range(2):
#         for z in range(2):
#             for w in range(2):
#                 F = (not (x <= (not (z <= w)))) and ((not z) <= ((not w) == y))
#                 if not F and (x + y + z + w) >= 3:
#                     print(x, w, z, y, int(F))
#                 if F and ((x == 0) + (y == 0) + (z == 0) + (w == 0)) >= 2:
#                     print(x, w, z, y, int(F))
# 5 --------------------------------------------------------------------------
# def f(n):
#     str_n = list(str(n))
#     num_list = [
#         int(str_n[0])*int(str_n[1]),
#         int(str_n[1]) * int(str_n[2]),
#     ]
#     num_list.sort()
#     return int(f'{num_list[0]}{num_list[1]}')
#
# for n in range(100, 1000):
#     if f(n) == 621:
#         print(n)
# 8 --------------------------------------------------------------------------

# 12 --------------------------------------------------------------------------
# def f(s):
#     while '52' in s or '2222' in s or '1122' in s:
#         if '52' in s:
#             s = s.replace('52','11')
#         if '2222' in s:
#             s = s.replace('2222','5')
#         if '1122' in s:
#             s = s.replace('1122', '25')
#     return s
# for i in range(4, 10000):
#     s = '5' + '2'*i
#     res = f(s)
#     one = res.count('1')
#     two = res.count('2')*2
#     five = res.count('5')*5
#     if one + two + five == 64: print(i)
# 13 --------------------------------------------------------------------------
# print(bin(142)[2:].zfill(8), bin(68)[2:].zfill(8), bin(56)[2:].zfill(8), bin(0)[2:].zfill(8), )
# print(bin(255)[2:].zfill(8), bin(255)[2:].zfill(8), bin(255)[2:].zfill(8), bin(240)[2:].zfill(8), )
# 14 --------------------------------------------------------------------------
# for x in '0123456789AB':
#     s = int(f'9A87{x}21', 12) + int(f'2{x}68', 14) - int(f'1{x}2F4', 16)
#     if s % 3 == 0:
#         print(s//3)
# 15 --------------------------------------------------------------------------
# B = list(range(70, 80 + 1))
# def DEL(n, m):
#     return n % m == 0
#
# for A in range(1, 1000):
#     for x in range(1, 10000):
#         F = DEL(x, 12) and (x in B) and not DEL(x, A)
#         if F: break
#     else: print(A)
# 16 --------------------------------------------------------------------------
# from functools import lru_cache
# c = 0
# @lru_cache(maxsize=None)
# def g(n):
#     if n < 10: return n
#     if n >= 10: return g(n-2) + 1
#
# @lru_cache(maxsize=None)
# def f(n): return g(n-1)
#
# for x in range(1, 100+1):
#     if (f(x) ** 0.5) % 1 == 0:
#         c += 1
#         print(x, f(x))
# print('c=', c)
# 17 --------------------------------------------------------------------------
# f = open('17_11887.txt')
# a = [int(x) for x in f]
# max_68 = 95968
# c = 0
# max_s = -222222222222222222222222222
# for i in range(len(a)-3):
#     a_0 = a[i]
#     a_1 = a[i+1]
#     a_2 = a[i+2]
#     a_3 = a[i+3]
#     s = (len(str(abs(a_0))) == 2) + (len(str(abs(a_1))) == 2) + (len(str(abs(a_2))) == 2) + (len(str(abs(a_3))) == 2)
#     if (s == 1 or s == 4) and (a_0 + a_1 + a_2 + a_3 >= max_68):
#         c += 1
#         max_s = max(max_s, a_0 + a_1 + a_2 + a_3)
# print(c, max_s)
# 19-21 --------------------------------------------------------------------------
# Руки
# 23 --------------------------------------------------------------------------
# from functools import lru_cache
# @lru_cache(maxsize=None)
# def f(s, e):
#     if s == e: return 1
#     if s > e or s == 100: return 0
#     sum = 0
#     if s <= 10: sum += f(s ** 2, e)
#     if s % 10 != 0: sum += f(s + (s%10), e)
#     if s % 68 != 0: sum += f(s + (s%68), e)
#     return sum
# # 96
# print(f(2, 68)* f(68, 680))
# 24 --------------------------------------------------------------------------
# s = open('24_11892.txt').readline()
# s = s.split('Y')
# min_s = 10000000000000000000
# min_str = ''
# for stroka in s:
#     if stroka.count('X') >= 500:
#         if min_s > len(stroka):
#             min_s = len(stroka)
#             min_str = stroka
# print(min_s, min_str)
# 25 --------------------------------------------------------------------------
# def is_nechet(n):
#     str_n = str(n)
#     for i in str_n:
#         if int(i) % 2 == 0:
#             return False
#     return True
# arr = []
# for A in range(0,9,2):
#     for B in range(1000):
#         if is_nechet(B):
#             s = int(f'1{A}2157{B}4')
#             if s % 133 == 0 :
#                 arr += [[s, s//133]]
# arr.sort(key=lambda x: x[0])
# for i in arr:
#     print(i[0], i[1])
# 26 --------------------------------------------------------------------------

# 27 --------------------------------------------------------------------------
