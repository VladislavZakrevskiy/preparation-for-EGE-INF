# 2 --------------------------------------------------------------------------
# for x in range(2):
#     for y in range(2):
#         for z in range(2):
#             for w in range(2):
#                 F = (z <= y) and (not w) and x
#                 if F: print(x,y,z,w, int(F))
# 5 --------------------------------------------------------------------------
# def f(n):
#     n_2 = bin(n)[2:]
#     sum_n = n_2.count('1')
#     arr = list(n_2)
#     if sum_n % 2 == 0:
#         arr[0] = '1'
#         arr[1] = '0'
#         arr += ['0']
#     else:
#         arr = ['1'] + arr
#         arr[-1] = '0'
#         arr[-2] = '1'
#     return int(''.join(arr), 2)
# for x in range(2, 1000):
#     if f(x) < 224: print(x)
# 8 --------------------------------------------------------------------------
# from itertools import product
# c = 0
# i = 0
# for word in product('ЕЛНОСЦ',repeat=6):
#     i += 1
#     s = ''.join(word)
#     if i % 2 == 0:
#         if s[0] not in 'ЕО' and s.count('Ц') == 2:
#             c += 1
# print(c)
# 12 --------------------------------------------------------------------------
# def f(s):
#     while '25' in s or '355' in s or '555' in s:
#         if '25' in s:
#             s = s.replace('25', '5', 1)
#         if '355' in s:
#             s = s.replace('355', '522', 1)
#         if '555' in s:
#             s = s.replace('555', '3', 1)
#     return s
# for i in range(4, 500):
#     s = '2' + '5' * i
#     if f(s).count('2') == 8:
#         print(i)
# 13 --------------------------------------------------------------------------
# print(bin(255)[2:].zfill(8), bin(255)[2:].zfill(8), bin(255)[2:].zfill(8), bin(192)[2:].zfill(8))
# print(bin(192)[2:].zfill(8), bin(168)[2:].zfill(8), bin(32)[2:].zfill(8), bin(64)[2:].zfill(8))
# print('11000000 10101000 00100000 01000101')
# 14 --------------------------------------------------------------------------
# def to_7 (n):
#     s = ''
#     while n > 0:
#         s += str(n%7)
#         n //= 7
#     return s[::-1]
# n = 5 * 343**2031 + 4 * 49**2142 - 3 * 7**111 + 7**222
# s = 0
# for x in range(7):
#     s += to_7(n).count(f'{x}') * x
# print(s)
# 15 --------------------------------------------------------------------------
# for A in range(1, 1000):
#     for x in range(1, 10000):
#         F = (x & 47 == 0) or ( (x&13 == 0) <= (not (x&A == 0)) )
#         if not F: break
#     else: print(A)
# 16 --------------------------------------------------------------------------
# print(2*1092 + 8 + 2*1096 + 8 + 2*1100 + 8)
# 17 --------------------------------------------------------------------------
# f = open('17 (3).txt')
# a = [int(x) for x in f]
# min_double = 1033
# c = 0
# max_s = -3541567898093
#
# def f(n):
#     return abs(n) >= 100 and abs(n) < 1000
#
# for i in range(len(a)-2):
#     a_0 = a[i]
#     a_1 = a[i+1]
#     a_2 = a[i+2]
#
#     first = (f(a_0) + f(a_1) + f(a_2)) == 3
#     second = (a_0 + a_1 + a_2) > min_double
#
#     if first and second:
#         c += 1
#         max_s = max(max_s, a_0 + a_1 + a_2)
# print(c, max_s)
# 19-21 --------------------------------------------------------------------------
# def win(s, m):
#     if s >= 172: return m%2 == 0
#     if m == 0: return 0
#
#     nextWin = [
#         win(s + 1, m - 1),
#         win(s + 2, m - 1),
#         win(s + 3, m - 1),
#         win(s * 2, m - 1),
#     ]
#
#     return any(nextWin) if (m - 1) % 2 == 0 else all(nextWin)
# print('19)', [s for s in range(1, 172) if not win(s, 1) and win(s, 2)])
# print('20)', [s for s in range(1, 172) if not win(s, 1) and win(s, 3)])
# print('21)', [s for s in range(1, 172) if not win(s, 2) and win(s, 4)])
# 23 --------------------------------------------------------------------------
# from itertools import product
# def f(s):
#     n = 3
#     for i in range(len(s)):
#         if s[i] == '1':
#             n += 1
#         if s[i] == '2':
#             n *= 2
#     return n
# a = []
# for comand in product('12', repeat=1):
#     a += [f(''.join(comand))]
# for comand in product('12', repeat=2):
#     a += [f(''.join(comand))]
# for comand in product('12', repeat=3):
#     a += [f(''.join(comand))]
# for comand in product('12', repeat=4):
#     a += [f(''.join(comand))]
# for comand in product('12', repeat=5):
#     a += [f(''.join(comand))]
# a.sort()
# print(set(a))
# 24 --------------------------------------------------------------------------
# s = open('24 (4).txt').readline()
# for l in 'AEIOUY':
#     s = s.replace(l, '0')
# for l in 'QWRTPSDFGHJKLZXCVBNM':
#     s = s.replace(l, '1')
# print(len(max(s.split('01'), key=len)) + 2)
# 25 --------------------------------------------------------------------------
from math import *
def find_divisors(n):
    divisors = []
    for i in range(2, int(sqrt(n))+1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n // i)
    return divisors
def find_sr (n):
    divisors = find_divisors(n)
    if len(divisors) == 0: return [0, 0, 0]
    return [sum(divisors), len(divisors), floor(sum(divisors) / len(divisors))]
c = 0
for i in range(700_000, 0, -1):
    summ, length, M = find_sr(i)
    if M % 1000 == 313 and c < 8:
        c += 1
        print(i, M)

# 26 --------------------------------------------------------------------------

# 27 --------------------------------------------------------------------------


