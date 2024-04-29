# 2 --------------------------------------------------------------------------
# print('x y z w F')
# for x in range(2):
#     for y in range(2):
#         for z in range(2):
#             for w in range(2):
#                 F = ((not x) <= (not y)) and (not (w <= (x == z)))
#                 if F:
#                     print(x, y, z, w, int(F))
# 5 --------------------------------------------------------------------------
# def convert_3(n):
#     s = ''
#     while n > 0:
#         s += str(n % 3)
#         n //= 3
#     s = list(s)
#     s.reverse()
#     return ''.join(s)
#
# def f(n):
#     is_odd = (n % 2 == 0)
#     ost_3 = n % 3
#     n_3 = convert_3(n)
#     splitted_n3 = list(n_3)
#     if is_odd:
#         for i in range(len(splitted_n3)):
#             if splitted_n3[i] == '1': splitted_n3[i] = '2'
#         a_1 = splitted_n3[-1]
#         a_2 = splitted_n3[-2]
#         splitted_n3 += [a_2, a_1]
#     if not is_odd:
#         splitted_n3 += [str(ost_3), str(ost_3)]
#     return int(''.join(splitted_n3), 3)
# for n in range(10, 10000):
#     if f(n) <= 1165:
#         print(n)
# 8 --------------------------------------------------------------------------
# from itertools import product
# odd_nums = ['1', '3', '5', '7', '9', 'B', 'D', 'F']
# c = 0
# for num in product('0123456789ABCDEFG', repeat=5):
#     cond = False
#     for i in range(len(num)):
#         if num[i] == '1' and ((num[i-1] not in odd_nums and i >= 1) or i < 1) and ((num[i+1] not in odd_nums and i <= 4) or i > 4):
#             cond = True
#     if num[0] != '0' and num.count('1') <= 2 and cond:
#         c += 1
# 12 --------------------------------------------------------------------------
# def f(s):
#     while '25' in s or '355' in s or '5555' in s:
#         if '25' in s:
#             s = s.replace('25', '33', 1)
#         if '355' in s:
#             s = s.replace('355', '52', 1)
#         if '5555' in s:
#             s = s.replace('5555', '2', 1)
#     return s
# max_2 = -10000
# for n in range(3, 2001):
#     s = '2' + '5' * n
#     max_2 = max(max_2, f(s).count('2'))
# print(max_2)
# 13 --------------------------------------------------------------------------
# print(bin(154)[2:].zfill(8), bin(127)[2:].zfill(8), bin(192)[2:].zfill(8), bin(130)[2:].zfill(8))
# print(bin(255)[2:].zfill(8), bin(255)[2:].zfill(8), bin(255)[2:].zfill(8), bin(192)[2:].zfill(8))
# 14 --------------------------------------------------------------------------
# for x in '0123456789ABCDEFGHIJ':
#     is_y_good = True
#     for y in '0123456789ABCDEFGHIJ':
#         if (int(f'5{y}4{x}{y}4HJ4', 20) + int(f'4{y}6B{y}{x}1', 20)) % 15 != 0:
#             is_y_good = False
#             break
#     if is_y_good: print(x)
# print((int(f'584H84HJ4', 20) + int(f'486B8H1', 20)))
# 15 --------------------------------------------------------------------------
# for A in range(10000):
#     is_x_good = True
#     for x in range(1, 1000):
#         for y in range(1, 1000):
#             F = (not (2*x < 2*A + 3*y)) or (y < 5) or (y >= 18) or (x < 87)
#             if not F:
#                 is_x_good = False
#                 break
#         if not is_x_good: break
#     if is_x_good: print(A)
# 16 --------------------------------------------------------------------------
# def f(n):
#     if n >= 4938: return n + 6
#     return n * f(n + 5)
# print(f(4928) - f(4935))
# 17 --------------------------------------------------------------------------
# f = open('17_11625.txt')
# a = [int(x) for x in f]
# max_3 = -2**100
# for num in a:
#     if str(num)[-1] == '3':
#         max_3 = max(max_3, num)
# c = 0
# s = 0
# for i in range(len(a)-2):
#     a_0 = a[i]
#     a_1 = a[i+1]
#     a_2 = a[i+2]
#     first = ((a_0 % 2 == 1) + (a_1 % 2 == 1) + (a_2 % 2 == 1)) == 1
#     second = (a_0 + a_1 + a_2) >= max_3
#     if first and second:
#         c += 1
#         s += (a_0 + a_1 + a_2)
# print(c, s)
# 19-21 --------------------------------------------------------------------------
# def win (num_stones, step):
#     if num_stones >= 458: return step % 2 == 0
#     if step == 0: return 0
#     nextWin = [win(num_stones+1, step-1), win(num_stones*5, step-1), win(num_stones+3, step-1)]
#     return any(nextWin) if (step-1) % 2 == 0 else all(nextWin)
# print('19) ', [s for s in range(1,458) if win(s, 2)])
# print('20) ', [s for s in range(1,458) if not win(s, 1) and win(s,3)])
# print('21) ', [s for s in range(1,458) if not win(s, 2) and win(s, 4)])
# 23 --------------------------------------------------------------------------
# def f(start, end):
#     if start < end: return 0
#     if start == end: return 1
#     return f(start - 2, end) + f(start - 5, end) + f(start // 3, end)
# print(f(32, 15)*f(15,13)*f(13,9))
# 24 --------------------------------------------------------------------------
# s = open('24_11630.txt').readline()
# for i in range(11, 1, -1):
#     s = s.replace('+'*i, 'SPLIT')
# s = s.split('SPLIT')
# s.sort(key=len)
# for i in range(-1, -len(s), -1):
#     if '+' in s[i]:
#         print(len(s[i]))
#         break
# print(len('34937+7549431185692+56634161885+445893921784+37658262676371+31339528944718+64828528+7937393738842+37886+5329367+2929+73+7577344195+61179687+92878773413+1246599172'))
# 25 --------------------------------------------------------------------------
# from fnmatch import fnmatch
# for num in range(0, 10**11, 466963):
#     if fnmatch(str(num), '?9?38*6?') and num % 2 == 0:
#         print(num, num // 466963)
# 26 --------------------------------------------------------------------------
# f = open('26_11632.txt')
# n, m = map(int, f.readline().split())
# a = [int(x) for x in f]
# gruzes = []
# contes = []
# for i in range(n):
#     gruzes += [a[i]]
# for i in range(n, n + m):
#     contes += [a[i]]
# gruzes.sort(reverse=True)
# contes.sort(reverse=True)
# max_gruz = -2**100
# c = 0
# for i in range(n):
#     gruz = gruzes[i]
#     for j in range(m):
#         cont = contes[j]
#         if gruz <= cont:
#             gruzes[i] = 1000000000000
#             contes[j] = -1000000000000
#             max_gruz = max(max_gruz, gruz)
#             c += 1
#             break
# print(c, max_gruz)
# 27 --------------------------------------------------------------------------
f = open('27_A_11633.txt')
k = int(f.readline())
n = int(f.readline())
a = [int(x) for x in f]
mn = min_back_1 = min_back_2 = 2000000000
for i in range(2*k, n):
    min_back_1 = min(min_back_1, a[i-2*k])
    min_back_2 = min(min_back_2, min_back_1 + a[i-k])
    mn = min(mn, min_back_2 + a[i])
print(mn)
