# 2 --------------------------------------------------------------------------
# print('x y z F')
# for x in range(2):
#     for y in range(2):
#         for z in range(2):
#             F = ((not z) and x) or (x and y)
#             print(x, y, z, F)
# z y x
# 5 --------------------------------------------------------------------------
# def make_R(N):
#     is_kr_3 = N % 3 == 0
#     bin_N = bin(N)[2:]
#     if is_kr_3:
#         R = ''
#         for l in bin_N:
#             if l == '0': R += '11'
#             else: R += '1'
#         return int(R, 2)
#     else:
#         R = ''
#         for l in bin_N:
#             if l == '1': R += '10'
#             else: R += '0'
#         return int(R, 2)
# max_R = 0
# for i in range(10000):
#     R = make_R(i)
#     if R < 161: max_R = max(R, max_R)
# print(max_R)
# 8 --------------------------------------------------------------------------
# import itertools
# n = 0
# for l in itertools.permutations('ПРОСТО', 6):
#     is_good = True
#     for i in range(1, 5):
#         if l[i-1] == l[i] or l[i+1] == l[i]:
#             is_good = False
#     if is_good:
#         print(l)
#         n += 1
# print(n)
# 12 --------------------------------------------------------------------------
# def f(s):
#     while '52' in s or '2222' in s or '1122' in s:
#         if '52' in s:
#             s = s.replace('52', '11', 1)
#         if '2222' in s:
#             s = s.replace('2222', '5', 1)
#         if '1122' in s:
#             s = s.replace('1122', '25', 1)
#     return s
# for i in range(4, 10000):
#     s = '5' + '2' * i
#     R = f(s)
#     five = R.count('5')
#     two = R.count('2')
#     one = R.count('1')
#     print (five * 5 + two * 2 + one, i, R)
#     if str(five * 5 + two * 2 + one)[-1] == '7':
#         print(i)
#         break
# 13 --------------------------------------------------------------------------
# print(bin(136)[2:].zfill(8), bin(36)[2:].zfill(8), bin(240)[2:].zfill(8), bin(16)[2:].zfill(8), 'ip')
# print(bin(255)[2:].zfill(8), bin(255)[2:].zfill(8), bin(255)[2:].zfill(8), bin(248)[2:].zfill(8), 'mask')
# 14 --------------------------------------------------------------------------
# N = 3 * 3125**9 + 2 * 625**8 - 4 * 625**7 + 3 * 125**6 - 2 * 25**5 - 2024
# def convert_to(number, base, upper=False):
#     digits = '0123456789abcdefghijklmnopqrstuvwxyz'
#     if base > len(digits): return None
#     result = ''
#     while number > 0:
#         result = digits[number % base] + result
#         number //= base
#     return result.upper() if upper else result
# print(convert_to(N, 25).count('0'))
# 15 --------------------------------------------------------------------------
# P = [2,4,6,8,10,12,14,16,18,20]
# Q = [3,6,9,12,15,18,21,24,27,30]
# A = [x for x in range(10000)]
#
# def f(x):
#     return ((x in A) <= (x in P)) and ((not (x in Q)) <= (not (x in A)))
#
# for x in range(10000):
#     if not f(x):
#         A.remove(x)
# print(A)
# 16 --------------------------------------------------------------------------
# def F(n):
#     if n == 1: return 1
#     if n > 1: return n * F(n-1)
# print(2023*2024)
# 17 --------------------------------------------------------------------------
# f = open('17_12926.txt')
# a = [int(x) for x in f]
# A = -2**100
# max_xx = -2**100
# for i in range(len(a)-3):
#     l_0 = a[i]
#     l_1 = a[i+1]
#     l_2 = a[i+2]
#     l_3 = a[i+3]
#     if str(l_0)[-1] == str(l_1)[-1] and str(l_1)[-1] == str(l_2)[-1] and str(l_2)[-1] == str(l_3)[-1]:
#         A = max(A, l_0 + l_1 + l_2 + l_3)
#     if (abs(l_0) < 100 and abs(l_0) > 9):
#         max_xx = max(max_xx, l_0)
#     if  abs(l_3) < 100 and abs(l_3) > 9:
#         max_xx = max(max_xx, l_3)
# min_s = 2**100
# n = 0
# for i in range(len(a) - 4):
#     l_0 = a[i]
#     l_1 = a[i + 1]
#     l_2 = a[i + 2]
#     l_3 = a[i + 3]
#     l_4 = a[i + 4]
#     first = ((l_0 < A) + (l_1 < A) + (l_2 < A) + (l_3 < A) + (l_4 < A) == 1)
#     s = l_0 + l_1 + l_2 + l_3 + l_4
#     second = (s % max_xx == 0)
#     if first and second:
#         n += 1
#         min_s = min(min_s, s)
# print(n, min_s)
# 19-21 --------------------------------------------------------------------------
# def win (num_stones, step):
#     if num_stones > 20: return step % 2 == 0
#     if step == 0: return 0
#     nextWin = [win(num_stones+1, step-1), win(num_stones*2, step-1)]
#     return any(nextWin) if (step-1) % 2 == 0 else all(nextWin)
# print('19) ', [s for s in range(1, 21) if not win(s, 1) and win(s, 3)])
# print('20) ', [s for s in range(1, 21) if not win(s, 2) and win(s, 4)])
# print('21) ', [s for s in range(1, 21) if not win(s, 1) and not win(s, 3) and win(s, 5)])
# 23 --------------------------------------------------------------------------
# def f(start, end):
#     if start > end or start == 11 or start == 12: return 0
#     if start == end: return 1
#     return f(start+1, end) + f(start*2, end) + f(start**2, end)
# print(f(2, 10)*f(10, 40))
# 24 --------------------------------------------------------------------------
# s = open('24_12931.txt').readline()
# s = s.replace('VWXYZ', "*")
# c = 0
# max_c = 0
# for l in s:
#     if l == '*':
#         c += 1
#         max_c = max(max_c, c)
#     else: c = 0
# print (max_c)
# 25 --------------------------------------------------------------------------
# from fnmatch import fnmatch
# for i in range(10):
#     for j in range(10**7):
#         if int(f'1{i}2{j}4') % 2024 == 0 and int(f'1{i}2{j}4') ** 0.5 % 1 == 0:
#             print(int(f'1{i}2{j}4'), int(f'1{i}2{j}4') / 2024)
# 26 --------------------------------------------------------------------------

# 27 --------------------------------------------------------------------------


