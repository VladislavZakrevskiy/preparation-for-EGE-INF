# 2 --------------------------------------------------------------------------
# print('w z x y F')
# for x in range(2):
#     for y in range(2):
#         for z in range(2):
#             for w in range(2):
#                 F = (x <= y) and z and (not w)
#                 if F:
#                     print(w, z, x, y, int(F))
# 5 --------------------------------------------------------------------------
# def convert_3(n):
#     s = ''
#     while n > 0:
#         s += str(n % 3)
#         n //= 3
#     return s[::-1]
# def f(n):
#     n_3 = convert_3(n)
#     list_n_3 = list(n_3)
#     one = n_3.count('1')
#     two = n_3.count('2') * 2
#     sum = one+two
#     ost_4 = sum % 4
#     if ost_4 == 0:
#         list_n_3 = ['1'] + list_n_3
#         list_n_3[-2] = ''
#         list_n_3[-1] = ''
#     else:
#         ost_4_3 = convert_3(ost_4 * 3)
#         list_n_3 = list_n_3 + [ost_4_3]
#     return int(''.join(list_n_3), 3)
#
# min_n = 131414
# for i in range(4, 1000):
#     if f(i) > 353:
#         min_n = min(f(i), min_n)
# print(min_n)
# 8 --------------------------------------------------------------------------
# from itertools import product
# c = 1
# n = 0
# for word in product('АГИЛМОРФ', repeat=5):
#     if c % 2 == 0 and word[0] != 'Л' and word[1] != 'М' and word.count('И') <= 2:
#         n += 1
#     c += 1
# print(n)
# 12 --------------------------------------------------------------------------
# def f(s):
#     while '23' in s or '5333' in s or '33333' in s:
#         if '23' in s:
#             s = s.replace('23', '3', 1)
#         if '5333' in s:
#             s = s.replace('5333', '32', 1)
#         if '33333' in s:
#             s = s.replace('33333', '55', 1)
#     return s
#
# min_s = 34567828765
# for i in range(4, 2000):
#     s = '3'*i + '5'
#     res = f(s)
#     two = res.count('2') * 2
#     three = res.count('3') * 3
#     five = res.count('5') * 5
#     sum = two + three + five
#     min_s = min(min_s, sum)
# print(min_s)
# 13 --------------------------------------------------------------------------
# print(bin(255)[2:].zfill(8), bin(255)[2:].zfill(8), bin(255)[2:].zfill(8), bin(240)[2:].zfill(8))
# print(bin(192)[2:].zfill(8), bin(168)[2:].zfill(8), bin(31)[2:].zfill(8), bin(80)[2:].zfill(8))
# 14 --------------------------------------------------------------------------
# for x in '0123456789ABCDEFGHIJKLMNP':
#     s = int(f'27{x}98876', 26) + int(f'26{x}51', 26) + int(f'15{x}47', 26) + int(f'62{x}5', 26)
#     if s % 25 == 0:
#         print(x, s // 25)
# 15 --------------------------------------------------------------------------
# B = list(range(120,130+1))
# def DEL(n, m): return n % m == 0
#
# for A in range(1, 1000):
#     for x in range(1, 10000):
#         F = ((x in B) <= (not DEL(x, 7))) or (A > 2*x)
#         if not F: break
#     else: print(A)
# 16 --------------------------------------------------------------------------
# бумажка какашка
# 17 --------------------------------------------------------------------------
# f = open('17_11236.txt')
# a = [int(x) for x in f]
# max_2z = 97
# kv_max_2z = 9409
# max_4z_1 = 9621
#
# c = 0
# max_s = -642783
#
# for i in range(len(a) - 2):
#     a_0 = a[i]
#     a_1 = a[i+1]
#     a_2 = a[i+2]
#     first = ((a_0 > kv_max_2z) + (a_1 > kv_max_2z) + (a_2 > kv_max_2z)) == 2
#     second = abs(a_0)*abs(a_1)*abs(a_2) % max_4z_1 == 0
#     if first and second:
#         c += 1
#         max_s = max(max_s, abs(a_0) + abs(a_1) + abs(a_2))
# print(c, max_s)
# 19-21 --------------------------------------------------------------------------
# def win(s1,s2,m):
#     if s1 + s2 >= 464: return m % 2 == 0
#     if m == 0: return 0
#     nextWin = [
#         win(s1 + 2, s2, m - 1),
#         win(s1 * 3, s2, m - 1),
#         win(s1, s2 + 2, m - 1),
#         win(s1, s2 * 3, m - 1),
#     ]
#     return any(nextWin) if (m - 1) % 2 == 0 else all(nextWin)
# print('19)', [s for s in range(1, 451) if not win(13, s, 1) and win(13, s, 2)])
# print('20)', [s for s in range(1, 451) if not win(13, s, 1) and win(13, s, 3)])
# print('21)', [s for s in range(1, 451) if not win(13, s, 2) and win(13, s, 4)])
# 23 --------------------------------------------------------------------------
# def f(s, e, last):
#     if s > e: return 0
#     if s == e: return 1
#     sum = f(s + 2, e, 1) + f(s * 3, e, 3)
#     if last != 2: sum += f(s ** 2, e, 2)
#     return sum
# print(f(2, 64, 0))
# 24 --------------------------------------------------------------------------
# s = open('24_11241.txt').readline()
# for let in 'ABCD':
#     s = s.replace(let, '*')
# s = s.split('*')
# print(len(max(s, key=len)))
# 25 --------------------------------------------------------------------------
# from fnmatch import fnmatch
# for i in range(0, 10**10, 2919):
#     if fnmatch(str(i), '9*253?74'):
#         print(i, i // 2919)
# 26 --------------------------------------------------------------------------

# 27 --------------------------------------------------------------------------
