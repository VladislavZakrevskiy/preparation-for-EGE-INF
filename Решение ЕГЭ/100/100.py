# 2 --------------------------------------------------------------------------
# print('y w z x F')
# for x in range(2):
#     for y in range(2):
#         for z in range(2):
#             for w in range(2):
#                 F = ((x < y) == w) or ((not y) and z)
#                 if not F:
#                     print(y,w,z,x, int(F))
# 5 --------------------------------------------------------------------------
# def convert_to_5(n, isRev):
#     s = ''
#     while n > 0:
#         s += str(n%5)
#         n //= 5
#     if isRev:
#         return ''.join(reversed(s))
#     return s
# def f(n):
#     n_5 = convert_to_5(n, True)
#     rev_n_5 = convert_to_5(n, False)
#     return abs(int(n_5, 5) - int(rev_n_5, 5))
# for n in range(5, 10000):
#     if f(n) == 100:
#         print(n)
#         break
# 8 --------------------------------------------------------------------------
# from itertools import product
# prost = ['2','3','5','7','B']
# c = 0
# for num in product('0123456789AB', repeat=8):
#     first = ((num[0] in prost)
#     + (num[1] in prost)
#     + (num[2] in prost)
#     + (num[3] in prost)
#     + (num[4] in prost)
#     + (num[5] in prost)
#     + (num[6] in prost)
#     + (num[7] in prost)) >= 2
#     second = ((int(num[0], 12) % 2) != (int(num[1], 12) % 2))
#     if first and second:
#         c += 1
# print(c)
# 12 --------------------------------------------------------------------------
# какая-то хуйня полная я в ахуе
# 13 --------------------------------------------------------------------------
# print(bin(164)[2:].zfill(8), bin(59)[2:].zfill(8), bin(151)[2:].zfill(8), bin(82)[2:].zfill(8), )
# print(bin(255)[2:].zfill(8), bin(255)[2:].zfill(8), bin(0)[2:].zfill(8), bin(0)[2:].zfill(8), )
# print(367 - (int('10100100', 2) + int('00111011', 2) + int('10010000',2) + int('0', 2)))
# 14 --------------------------------------------------------------------------
# max_s = -22222222222222
# del_s = 0
# for x in ['A', 'B', 'C', 'D']:
#     arr_y = []
#     if x == 'A':
#         arr_y = ['9']
#     if x == 'B':
#         arr_y = ['9', 'A']
#     if x == 'C':
#         arr_y = ['9', 'A', 'B']
#     if x == 'D':
#         arr_y = ['9', 'A', 'B', 'C']
#
#     for y in arr_y:
#         s = int(f'7{x}37{y}', 14) + int(f'9{y}63', int(x, 16)) - int(f'15148', int(y, 16))
#         if s > max_s:
#             max_s = s
#             del_s = s // (int(x, 16) + int(y, 16))
# print(max_s, del_s)
# 15 --------------------------------------------------------------------------
# def DEL(n,m):
#     return (n % m == 0)
# B = list(range(31, 68+1))
# for A in range(1, 1000):
#     for x in range(1, 10000):
#         F = (DEL(x, A) and (x in B)) <= (x&58 == 0)
#         if not F: break
#     else: print(A)
# 16 --------------------------------------------------------------------------
# from functools import lru_cache
#
# @lru_cache(None)
# def f(n):
#     if n < 3: return n
#     if n > 2: return (2*n -1) * (f(n-1) + f(n-2))
# for i in range(70):
#     f(i)
# print(f(69) % (10**9 + 7))
# 17 --------------------------------------------------------------------------
# import math
#
# f = open('17_9969.txt')
# a = [int(x) for x in f]
# max_razl = -10234
# c = 0
# pks = 0
# for i in range(0, len(a)-2):
#     a_0 = a[i]
#     a_1 = a[i+1]
#     a_2 = a[i+2]
#     sqrt_a_0 = math.sqrt(a_0 if a_0 >= 0 else 0.01)
#     sqrt_a_1 = math.sqrt(a_1 if a_1 >= 0 else 0.01)
#     sqrt_a_2 = math.sqrt(a_2 if a_2 >= 0 else 0.01)
#     first = ((sqrt_a_0 % 1 == 0) + (sqrt_a_1 % 1 == 0) + (sqrt_a_2 % 1 == 0)) == 1
#     second = False
#     pk = 0
#     if sqrt_a_0 % 1 == 0:
#         second = ((a_1 + a_2) >= max_razl)
#         pk = sqrt_a_0
#     if sqrt_a_1 % 1 == 0:
#         second = ((a_0 + a_2) >= max_razl)
#         pk = sqrt_a_1
#     if sqrt_a_2 % 1 == 0:
#         second = ((a_1 + a_0) >= max_razl)
#         pk = sqrt_a_2
#     if first and second:
#         c += 1
#         pks += pk
# print(c, pks)
# 19-21 --------------------------------------------------------------------------
from functools import lru_cache
@lru_cache(maxsize=None)
def win(stones1, stones2, step):
    if stones1 + stones2 >= 192: return step % 2 == 0
    if step == 0: return 0
    nextWin = [
        win(stones1+3, stones2, step-1),
        win(stones1+5, stones2, step-1),
        win(stones1+7, stones2, step-1),
        win(stones1*2, stones2, step-1) if stones1*2 + stones2 <= 256 else None,
        win(stones1, stones2+3, step-1),
        win(stones1, stones2+5, step-1),
        win(stones1, stones2+7, step-1),
        win(stones1, stones2*2, step-1) if stones2*2 + stones1 <= 256 else None,
    ]
    return any(nextWin) if (step-1)%2 == 0 else all(nextWin)
s19 = []
for k1 in range(0, 257):
    for k2 in range(0, 257 - k1):
        if win(k1, k2, 2):
            s19.append(k1+k2)
s19.sort()
print('19)', s19)
print('20)', [s for s in range(1, 159) if not win(16, s, 2) and not win(16, s, 4) and win(16, s, 6)])
s21 = []
for m in range(2, 101, 2):
    for k1 in range(1, 165):
        if win(27, k1, m):
            s21.append(k1)
print('21)', len(s21))
# 23 --------------------------------------------------------------------------

# 24 --------------------------------------------------------------------------

# 25 --------------------------------------------------------------------------

# 26 --------------------------------------------------------------------------

# 27 --------------------------------------------------------------------------


