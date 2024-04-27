# 2 --------------------------------------------------------------------------
# print('w z y x F')
# for x in range(2):
#     for y in range(2):
#         for z in range(2):
#             for w in range(2):
#                 F = (x or (not y)) and (not (x == z)) and w
#                 if F: print(w, z, y, x, F)
# 5 --------------------------------------------------------------------------
# def f(n):
#     n_2 = bin(n)[2:]
#     ost_2 = n_2.count('1') % 2
#     n_2 += str(ost_2)
#     ost_2 = n_2.count('1') % 2
#     n_2 += str(ost_2)
#     return int(n_2, 2)
# min_f = 35451762
# for n in range(10000):
#     if f(n) > 60:
#         min_f = min(min_f, f(n))
# print(min_f)
# 8 --------------------------------------------------------------------------
# from itertools import product
# c = 0
#
# for word in product('ВЗГЛЯД', repeat=4):
#     if word.count('З') == 1 or word.count('З') == 2:
#         c += 1
# print(c)
# 12 --------------------------------------------------------------------------
# def f(s):
#     while '>1' in s or '>2' in s or '>3' in s:
#         if '>1' in s:
#             s = s.replace('>1', '22>', 1)
#         if '>2' in s:
#             s = s.replace('>2', '222>', 1)
#         if '>3' in s:
#             s = s.replace('>3', '1>', 1)
#     return s
# res = f('>' +  '2' * 12 + '3' * 30 + '1' * 11)
# one = res.count('1')
# two = res.count('2') * 2
# three = res.count('3') * 3
# print(one + two + three)
# 13 --------------------------------------------------------------------------
# print(bin(255)[2:].zfill(8), bin(255)[2:].zfill(8), bin(255)[2:].zfill(8), bin(240)[2:].zfill(8))
# print(bin(192)[2:].zfill(8), bin(168)[2:].zfill(8), bin(64)[2:].zfill(8), bin(176)[2:].zfill(8))
# print((bin(192)[2:].zfill(8) + bin(168)[2:].zfill(8) + bin(64)[2:].zfill(8) + bin(176)[2:].zfill(8)).count('1'))
# 14 --------------------------------------------------------------------------
# def convert_4 (n):
#     s = ''
#     while n > 0:
#         s += str(n % 4)
#         n //= 4
#     return s[::-1]
# s = 16**820 - 2**761 + 14
# print(convert_4(s).count('0'))
# 15 --------------------------------------------------------------------------
# for A in range(1000):
#     for x in range(1000):
#         F = ((x & A) != 0) <= ((x & 17 == 0 and x & 5 == 0) <= x & 3 != 0)
#         if not F: break
#     else: print(A)
# 16 --------------------------------------------------------------------------
# def f(n):
#     if n <= 2: return 1
#     return f(n-1) + 2*f(n-2)
# print(f(17))
# 17 --------------------------------------------------------------------------
# f = open('17_2388.txt')
# a = [int(x) for x in f]
# c = 0
# max_s = -32416789
# for i in range(len(a)-1):
#     a_0 = a[i]
#     a_1 = a[i+1]
#     if (a_0 % 5 == 0 and a_0 % 5 == 0) and (a_1 % 3 != 0 and a_1 % 3 != 0):
#         c += 1
#         if a_0 + a_1 > 0: max_s = max(max_s, a_0 + a_1)
# print(c, max_s)
# 19-21 --------------------------------------------------------------------------
# def win(s, m):
#     if s >= 50 and s <= 119: return m % 2 == 0
#     if s >=5 and s >= 119: return (m - 1) % 2 == 0
#     if m == 0: return 0
#     nextWin = [
#         win(s + 2, m - 1),
#         win(s * 3, m - 1)
#     ]
#     return any(nextWin) if (m-1) % 2 == 0 else all(nextWin)
# print('19)', [s for s in range(1, 50) if win(s, 2)])
# print('20)', [s for s in range(1, 50) if not win(s, 1) and win(s, 3)])
# print('21)', [s for s in range(1, 50) if not win(s, 2) and win(s, 4)])
# 23 --------------------------------------------------------------------------
# def f(s, e):
#     if s > e: return 0
#     if s == e: return 1
#     return f(s + 1, e) + f(s + 2, e) + f(s * 2, e)
# print(f(4, 9) * f(9, 12) * f(12, 15))
# 24 --------------------------------------------------------------------------
# s = open('24_2393.txt').readline()
# c = m = 1
# for i in range(len(s)-1):
#     if int(s[i]) <= int(s[i+1]):
#         c += 1
#         m = max(m, c)
#     else:
#         c = 1
# print(m)
# 25 --------------------------------------------------------------------------
# def simpleDividers(n):
#    answer = []
#    d = 2
#    while d * d <= n:
#        if n % d == 0:
#            answer.append(d)
#            n //= d
#        else:
#            d += 1
#    if n > 1:
#        answer.append(n)
#    return list(set(answer))
# for i in range(670_000, 1_000_000):
#     div = simpleDividers(i)
#     if sum(div) % 10 == 5:
#         print(i, sum(div))
# 26 --------------------------------------------------------------------------

# 27 --------------------------------------------------------------------------
