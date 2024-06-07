# 2 --------------------------------------------------------------------------
# for x in range(2):
#     for y in range(2):
#         for z in range(2):
#             for w in range(2):
#                 F = (not (x <= z)) or (y == w) or y
#                 if not F: print(z, x,y, w, int(F))
# 5 --------------------------------------------------------------------------
# def f(n):
#     n_2 = bin(n)[2:]
#     if n % 2 == 0:
#         n_2 = '10' + n_2
#     if n % 2 != 0:
#         n_2 = '1' + n_2 + '01'
#     return int(n_2, 2)
#
# for N in range(1000):
#     if f(N) > 516:
#         print(N)
#         break
# 8 --------------------------------------------------------------------------
# from itertools import product
# c = 0
# for word in product('АПРСУ', repeat=5):
#     c += 1
#     s = ''.join(word)
#     if s.count('У') <= 1 and 'АА' not in s: print(s, c)
# 12 --------------------------------------------------------------------------
# def f(s):
#     while '1111' in s or '8888' in s:
#         if '1111' in s:
#             s = s.replace('1111', '8', 1)
#         else:
#             s = s.replace('8888', '11', 1)
#     return s
# print(f('8' * 82))
# 13 --------------------------------------------------------------------------
# from itertools import product
# print(bin(255)[2:].zfill(8), bin(255)[2:].zfill(8), bin(255)[2:].zfill(8), bin(248)[2:].zfill(8), )
# print(bin(122)[2:].zfill(8), bin(159)[2:].zfill(8), bin(136)[2:].zfill(8), bin(144)[2:].zfill(8), )
# for num in product('01', repeat=3):
#     if num.count('1') != 1: print(num)
# 14 --------------------------------------------------------------------------
# def to_A (n):
#     s = ''
#     alf = '0123456789AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA'
#     while n > 0:
#         s += str(alf[n % 27])
#         n //= 27
#     return s[::-1]
# n = 2 * 729**2014 + 2 * 243**2016 - 2 * 81**2018 + 2 * 27**2020 - 2 * 9**2022 - 2024
# print(to_A(n).count('A'))
# 15 --------------------------------------------------------------------------
# def DEL (n,m): return n % m == 0
# for A in range(1, 1000):
#     for x in range(1, 1000):
#         F = (not DEL(x, A)) <= (DEL(x, 14) <= (not DEL(x, 4)))
#         if not F: break
#     else: print(A)
# 16 --------------------------------------------------------------------------
# print(2023**2)
# 17 --------------------------------------------------------------------------
# f = open('17_16328.txt')
# a = [int(x) for x in f]
# min_19 = 114
#
# c = max_s = 0
#
# for i in range(len(a)-1):
#     a_0 = a[i]
#     a_1 = a[i+1]
#
#     if ((a_0 % min_19 == 0) + (a_1 % min_19 == 0)) >= 1:
#         c += 1
#         max_s = max(max_s, a_0 + a_1)
# print(c, max_s)
# 19-21 --------------------------------------------------------------------------

# 23 --------------------------------------------------------------------------
# s = open('24_16333.txt').readline()
# s = s.replace('Q', 'b')
# s = s.replace('R', 'b')
# s = s.replace('W', 'b')
#
# s = s.replace('1', 'c')
# s = s.replace('2', 'c')
# s = s.replace('4', 'c')
# print(s)
#
# s = s.split('cc')
# a = []
# for i in range(len(s)):
#     for n in s[i].split('bb'): a += [n]
# print(len('cbcbcbcbcbcbcbcb'))
# 24 --------------------------------------------------------------------------

# 25 --------------------------------------------------------------------------

# 26 --------------------------------------------------------------------------
f = open('26_16335.txt')
N = int(f.readline())
a = [int(x) for x in f]

a.sort()
a = a[::-1]
b = [a[0]]

for i in range(len(a)):
    if b[-1] - a[i] >= 4:
        b += [a[i]]
print(len(b), b[-1])
# 27 --------------------------------------------------------------------------
f = open('27_A_16336.txt')
N = int(f.readline())
a = [int(x) for x in f]
sm = sum(a)
a = a*2
s = 0

for i in range(N):
    s += min(i, N-i)*a[i]

mn = s
cheaper = sum(a[1:N//2+1])
for i in range(1, N):
    s = s - cheaper + (sm - cheaper)
    mn = min(mn, s)
    cheaper = cheaper - a[i] + a[N//2 + i]
print(mn)





