# 2 --------------------------------------------------------------------------
# print('x y z w F')
# for x in range(2):
#     for y in range(2):
#         for z in range(2):
#             for w in range(2):
#                 F = (x or y) or (not (y == z)) and (not w)
#                 if F and x + y + z + w >= 1:
#                     print(x,y,z,w,int(F))
# 5 --------------------------------------------------------------------------
# def f(n):
#     bin_n = bin(n)[2:]
#     splitted_bin_n = list(bin_n)
#     sum = 0
#     for num in bin_n:
#         sum += int(num)
#     if (sum % 2 == 0):
#         splitted_bin_n += ['0']
#         splitted_bin_n[0] = '1'
#         splitted_bin_n[1] = '0'
#     else:
#         splitted_bin_n += ['1']
#         splitted_bin_n[0] = '1'
#         splitted_bin_n[1] = '1'
#     return int(''.join(splitted_bin_n), 2)
#
# for n in range(10000):
#     if f(n) < 35:
#         print(n)
# 8 --------------------------------------------------------------------------
# import itertools
# i = 0
# c = 0
# for word in itertools.product('АИНПТЦЯ', repeat=6):
#     i+=1
#     if i % 2 == 0 and word[0] == 'Н' and word.count('Я') == 2:
#         c+= 1
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
# for n in range(4, 10000):
#     s = '3' + n * '5'
#     r = f(s)
#     if len(r) == r.count('5'):
#         print(n)
#         break
# 13 --------------------------------------------------------------------------
# print(bin(192)[2:].zfill(8), bin(168)[2:].zfill(8), bin(32)[2:].zfill(8), bin(48)[2:].zfill(8))
# print(bin(255)[2:].zfill(8), bin(255)[2:].zfill(8), bin(255)[2:].zfill(8), bin(240)[2:].zfill(8))
# 14 --------------------------------------------------------------------------
# for x in range(22):
#     first = (22**7 * 9)+(22**6 * 8)+(22**5 * x)+(22**4 * 7)+(22**3 * 9)+(22**2 * 6)+(22 * 4) + 1
#     second = (22**4 * 3)+(22**3 * 2)+(22**2 * x) + 22 + 4
#     third = (22**3 * 7)+(22**2 * 3)+(22 * x) + 4
#     if (first + second + third) % 21 == 0:
#         print(x, (first + second + third) / 21)
# maxi = []
# for x in "0123456789ABCDEFGHIJKL":
#     x1 = '98' + str(x) + '79641'
#     x2 = '36' + str(x) + '14'
#     x3 = '73' + str(x) + '4'
#     res = int(x1, 22) + int(x2, 22) + int(x3, 22)
#     if res % 21 == 0:
#         res = res / 21
#         maxi.append(res)
# print(max(maxi))
# 15 --------------------------------------------------------------------------
# for A in range(10000):
#     is_x_corr = True
#     for x in range(1, 1000):
#         for y in range(1, 1000):
#             F = (99 != y + 2*x) or (A < x) or (A < y)
#             if not F:
#                 is_x_corr = False
#                 break
#         if not is_x_corr: break
#     if is_x_corr: print(A)
# 16 --------------------------------------------------------------------------
# def f(n):
#     if n >= 2025: return n
#     return n + f(n + 2)
# print(f(2022) - f(2023))
# 17 --------------------------------------------------------------------------
# f = open('17.txt')
# a = [int(x) for x in f]
# max_221 = -100_100
# for num in a:
#     if num > 99 and str(num)[-1] == '1' and str(num)[-2] == '2' and str(num)[-3] == '2':
#         max_221 = max(max_221, num)
#
# min_sum = 2*100
# c = 0
# for i in range(len(a)-2):
#     a_0 = a[i]
#     a_1 = a[i+1]
#     a_2 = a[i+2]
#     first = ((abs(a_0) > 9 and int(str(a_0)[-2]) % 2 == 1) \
#             + (abs(a_1) > 9 and int(str(a_1)[-2]) % 2 == 1) \
#             + (abs(a_2) > 9 and int(str(a_2)[-2]) % 2 == 1)) == 2
#     second = ((abs(a_0) > 9 and abs(a_0) < 100) \
#              + (abs(a_1) > 9 and abs(a_1) < 100) \
#              + (abs(a_2) > 9 and abs(a_2) < 100)) <= 2
#     third = (a_0 + a_1 + a_2) > max_221
#     if first and second and third:
#         c += 1
#         min_sum = min(min_sum, (a_0 + a_1 + a_2))
# print(c, min_sum)
# 19-21 --------------------------------------------------------------------------

# 23 --------------------------------------------------------------------------

# 24 --------------------------------------------------------------------------

# 25 --------------------------------------------------------------------------

# 26 --------------------------------------------------------------------------

# 27 --------------------------------------------------------------------------


