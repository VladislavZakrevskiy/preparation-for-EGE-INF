# 2 --------------------------------------------------------------------------
# print('x w z y')
# for x in range(2):
#     for y in range(2):
#         for z in range(2):
#             for w in range(2):
#                 F = (x and (not y)) or (y == z) or (not w)
#                 if not F:
#                     print(x, w, z, y)
# 5 --------------------------------------------------------------------------
# def f(n):
#     str_n = str(n)
#     a = []
#     for i in range(len(str_n)-1):
#         a.append(int(str_n[i]+str_n[i+1]))
#     mx = max(a)
#     mn = min(a)
#     return mx + mn
# for N in range(10, 10000):
#     if f(N) == 137:
#         print(N)
#         break
# 8 --------------------------------------------------------------------------
# def val_6 (x):
#     str_x = str(x)
#     a = set(str_x)
#     is_odin = len(a) == len(str_x)
#     next_must = int(str_x[0]) % 2
#     for i in range(len(str_x)):
#         el = str_x[i]
#         if int(el) % 2 == 0 and next_must == 0: next_must = 1
#         elif int(el) % 2 != 0 and next_must == 1: next_must = 0
#         else:
#             next_must = 2
#             break
#     if (next_must == 1 or next_must == 0) and is_odin:
#         return True
#     return False
#
# def val_4(x):
#     str_x = str(x)
#     is_good = True
#     for i in range(len(str_x)-1):
#         if str_x[i] == str_x[i+1]:
#             is_good = False
#             break
#     return  is_good
#
# c_6 = 0
# for N in range(100_000, 1_000_000):
#     if val_6(N): c_6 += 1
# c_4 = 0
# for N in range(1_000, 10_000):
#     if val_4(N): c_4 += 1
# print(c_6, c_4, c_6-c_4)
# 12 --------------------------------------------------------------------------
# def f(s):
#     while '>1' in s or '>3' in s or '>2' in s:
#         if '>1' in s:
#             s = s.replace('>1', '1>')
#         if '>3' in s:
#             s = s.replace('>3', '>2')
#         if '>2' in s:
#             s = s.replace('>2', '>1')
#     return s
# def is_prost(x):
#     sqrt_x = int(x ** 0.5)
#     is_pr = True
#     for i in range(2, sqrt_x + 1):
#         if x % i == 0: is_pr = False
#     return is_pr
# for n in range(10):
#     s = '>' + '1'*16 + '2'*n + '3' * 16
#     f_num = f(s)[:-1]
#     summa = len(f_num)
#     if is_prost(summa):
#         print(n)
#         break
# 13 --------------------------------------------------------------------------
# print('********', '********', '********', '********', 'mask')
# print(bin(175)[2:].zfill(8), bin(122)[2:].zfill(8), bin(80)[2:].zfill(8), bin(13)[2:].zfill(8), 'ip')
# print(bin(175)[2:].zfill(8), bin(122)[2:].zfill(8), bin(80)[2:].zfill(8), bin(0)[2:].zfill(8), 'web')

# 14 --------------------------------------------------------------------------
# for p in range(1, 50):
#     for x in range(p):
#         for y in range(p):
#             F = ( (3*p + 2) * (p + 4) ) == (x*p**2 + y*p + 2 )
#             if F: print((y*p + x))
# 15 --------------------------------------------------------------------------
# P = list(range(35, 56))
# Q = list(range(45, 66))
# A = []
# for x in range(-1000, 1000):
#     first = (x in P) <= (x in A)
#     second = (x not in A) <= (x not in Q)
#     if not (first and second): A.append(x)
# print(A, len(A))
# 16 --------------------------------------------------------------------------
# def F(n):
#     if n >= 2073: return n + 3
#     return n + F(n+2) - F(n+3)
# print(F(2070) + F(2069))
# 17 --------------------------------------------------------------------------
# c = 0
# mn = 10**20
# f = open('17_2008.txt')
# a = [int(x) for x in f]
# for el in a:
#     if el > 100 and int(str(el)[-2]) <= 4 and int(str(el)[-3]) in range(3,8):
#         c += 1
#         mn = min(mn, el)
# print(c, mn)
# 19-21 --------------------------------------------------------------------------
# def win(s, step):
#     if s >= 129: return step % 2 == 0
#     if step == 0: return 0
#     nextWin = [win(s + 1, step-1), win(s * 2, step - 1)]
#     return any(nextWin) if (step-1)%2 == 0 else all(nextWin)
#
# print('19) ', [s for s in range(1,129) if win(s, 2) and not win(s,1)])
# print('20) ', [s for s in range(1,129) if win(s, 3) and not win(s,1)])
# print('21) ', [s for s in range(1,129) if win(s, 4) and not win(s,2)])
# 23 --------------------------------------------------------------------------
# def f(start, end):
#     if start >= end: return 0
#     if start == end: return 1
#     return f(start+1, end) + f(start*2, end)
# A = list(range(2, 200))
# for e in range(2, 200):
#     if f(1, e) <= 5:
#         A.append(e)
# print(A)
# 24 --------------------------------------------------------------------------
# s = open('24_1873.txt').readline()
# s = s.replace('PR', ' ').replace('RP', ' ')
# print(max(map(len, s.split())) + 2 )

# 25 --------------------------------------------------------------------------
# def netriv_deliteli(x):
#     sqrt_x = x//2
#     prost = []
#     for i in range(2, sqrt_x+1):
#         if x % i == 0 and i % 2 != 0: prost.append(i)
#     return prost[::-1] if len(prost) >= 6 else 0
# def D(N):
#     delit = netriv_deliteli(N)
#     if delit == 0: return 0
#     return delit[5]
# arr = [[200000000, 5], [200000003, 7], [200000004, 3], [200000005, 5], [200000008, 13]]
# n = 0
# for i in range(200_000_001 + n, 200_000_010 + n):
#     print(i)
#     if len(arr) == 5: break
#     if D(i) > 0: arr.append([i, D(i)])
# print(arr)
# 26 --------------------------------------------------------------------------
f = open('26_5383.txt')
n, s = map(int, f.readline().split())
prior_1 = []
prior_0 = []
for i in range(n):
    lists, obyz = map(int, f.readline().split())
    if obyz == 1: prior_1.append(lists+10)
    if obyz == 0: prior_0.append(lists+10)
prior_0.sort()
prior_1.sort()
summa = 0
c = 0
for i in range(len(prior_1)):
    summa += prior_1[i]
    if summa > s: break
    c += 1
for i in range(len(prior_0)):
    summa += prior_0[i]
    print(prior_0[i], c)
    if summa > s: break
    c += 1

print(summa, s, c)
# 27 --------------------------------------------------------------------------


