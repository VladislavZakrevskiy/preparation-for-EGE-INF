# f = open('27A_2719.txt')
# n = int(f.readline())
# k1 = k0 = 0
#
# for i in range(n):
#     x = int(f.readline())
#     if x % 2 == 0: k0 += 1
#     else: k1 += 1
# print(k1*(k1-1)//2 + k0*(k0-1)//2) #2459 24995121

# -------------------------------------------------------

# f = open('27B_2720.txt')
# n = int(f.readline())
# k7 = k = 0
#
# for i in range(n):
#     x = int(f.readline())
#     if x % 7 == 0: k7 += 1
#     else: k += 1
# print(k7*k + k7*(k7-1)//2) # 1209 13831740

# -------------------------------------------

# f = open('27B_2721.txt')
# n = int(f.readline())
# k65 = k13 = k5 = k = 0
#
# for i in range(n):
#     x = int(f.readline())
#     if x % 65 == 0: k65 += 1
#     elif x % 13 == 0: k13 += 1
#     elif x % 5 == 0: k5 += 1
#     else: k += 1
# print(k65*(n - k65) + k65*(k65-1)//2 + k13*k5) # 168 2503584

# ------------------------------------------------

# f = open('27B_2722.txt')
# n = int(f.readline())
# k5_0 = k5_1 = k_1 = k_0 = 0
# for i in range(n):
#     x = int(f.readline())
#     if x % 5 == 0 and x % 2 == 0: k5_0 += 1
#     if x % 5 != 0 and x % 2 != 0: k_1 += 1
#     if x % 5 == 0 and x % 2 != 0: k5_1 += 1
#     if x % 5 != 0 and x % 2 == 0: k_0 += 1
# print(k5_0 * k_1 + k5_1 * k_0 + k5_0 * k5_1) # 1056 8863690

# ----------------------------------------------

# f = open('27B_2723.txt')
# n = int(f.readline())
# c = 0
# for i in range(n):
#     x = int(f.readline())
#     if x % 19 == 0: c += 1
# print(c*(c-1)*(c-2)//6) # 4 25808936

# -------------------------------------------------

# f = open('27B_2724.txt')
# n = int(f.readline())
# k = [0]*131
#
# for i in range(n):
#     x = int(f.readline())
#     k[x%131] += 1
# count = k[0]*(k[0]-1)//2
# for i in range(1, 66):
#     count += k[i]*k[131-i]
# print(count) # 31 381543

# ----------------------------------------
#
# f = open('27B_2725.txt')
# n = int(f.readline())
# k = [0]*69
# for i in range(n):
#     x = int(f.readline())
#     k[x%69] += 1
# count = 0
# for i in range(69):
#     count += k[i]*(k[i]-1)//2
# print(count) # 61 725088

# -------------------------------------------

# f = open('27B_2733.txt')
# n = int(f.readline())
# a = [0]*80
# b = [0]*80
# for i in range(n):
#     x = int(f.readline())
#     if x > 50000: a[x%80] += 1
#     else: b[x%80] += 1
# count = a[0]*(a[0]-1)//2 + a[40]*(a[40]-1)//2 + a[40]*b[40] + a[0]*b[0]
# for i in range(1, 40):
#     count += a[i]*b[80-i] + b[i]*a[80-i] + a[i]*a[80-i]
# print(count) # 48 465486

# -------------------------------------------

# f = open('27B_2737.txt')
# n = int(f.readline())
# k = [0]*2001
#
# for i in range(n):
#     x = int(f.readline())
#     if x > 2000 or x < 0: continue
#     k[x] += 1
# c = k[1000] * (k[1000]-1)//2
# for i in range(1000):
#     c += k[i] * k[2000-i]
# print(c) # 1 4040

# --------------------------------------------------

# f = open('27B_2726.txt')
# n = int(f.readline())
# a_0 = []
# a_1 = []
#
# for i in range(n):
#     x = int(f.readline())
#     if x % 2 == 0: a_0 += [x]
#     else: a_1 += [x]
# a_0.sort()
# a_1.sort()
#
# print(a_0[-1] + a_1[-1]) # 73319 133981

# -------------------------------------------------------

# f = open('27A_2727.txt')
# n = int(f.readline())
# k = []
# k31 = []
#
# for i in range(n):
#     x = int(f.readline())
#     if x % 31 == 0: k31 += [x]
#     else: k += [x]
# k31.sort()
# k.sort()
#
# print(min(k31[0] * k31[1], k[0] * k31[0])) # 21831874 3472

# ------------------------------------------------------

# f = open('27B_2728.txt')
# n = int(f.readline())
# k23_1 = []
# k23_0 = []
# k_1 = []
# k_0 = []
#
# for i in range(n):
#     x = int(f.readline())
#     if x % 23 == 0 and x % 2 == 0: k23_0 += [x]
#     if x % 23 == 0 and x % 2 != 0: k23_1 += [x]
#     if x % 23 != 0 and x % 2 == 0: k_0 += [x]
#     if x % 23 != 0 and x % 2 != 0: k_1 += [x]
#
# k23_0.sort()
# k23_1.sort()
# k_0.sort()
# k_1.sort()
#
# a = k23_0[-2:] + k23_1[-2:] + k_1[-2:] + k_0[-2:]
# m = 0
# for i in range(len(a)):
#     for j in range(i+1, len(a)):
#         if (a[i] % 23 == 0) + (a[j] % 23 == 0) >= 1 and (a[i] + a[j]) % 2 == 0:
#             m = max(m, a[i] + a[j])
# print(m) # 65406 133892

# -----------------------------------------------------------

# f = open('27B_2729.txt')
# n = int(f.readline())
# k = [ [] for i in range(11)]
#
# for i in range(n):
#     x = int(f.readline())
#     k[x%11] += [x]
# a = []
#
# for i in range(11):
#     k[i].sort()
#     a += k[i][:3]
# m = 1000000000000000000000000000000000000
#
# for i in range(len(a)):
#     for j in range(i+1, len(a)):
#         for k in range(j+1, len(a)):
#             if (a[i] + a[j] + a[k]) % 11 == 0:
#                 m = min(m, a[i] + a[j] + a[k])
#
# print(m) # 17424 88

# ------------------------------------------------------------

# f = open('27B_2730.txt')
# n = int(f.readline())
# k12 = []
# k3 = []
# k4 = []
# k = []
#
# for i in range(n):
#     x = int(f.readline())
#     if x % 12 == 0: k12 += [x]
#     elif x % 3 == 0: k3 += [x]
#     elif x % 4 == 0: k4 += [x]
#     else: k += [x]
#
# k12.sort()
# k3.sort()
# k4.sort()
# k.sort()
#
# a = k12[-4:] + k3[-4:] + k4[-4:] + k[-4:]
# len_a = len(a)
# m = 0
# for i in range(len_a):
#     for j in range(i+1, len_a):
#         for k in range(j+1, len_a):
#             for l in range(k+1, len_a):
#                 if (a[i] * a[j] * a[k] * a[l]) % 12 == 0:
#                     m = max(m , a[i] + a[j] + a[k] + a[l])
# print(m) # 144001 267927

# ---------------------------------------------------------

# f = open('27B_2732.txt')
# n = int(f.readline())
# k = [ [] for i in range(80)]
# for i in range(n):
#     x = int(f.readline())
#     k[x%80] += [x]
# a = []
# for i in range(80):
#     k[i].sort()
#     a += k[i][-2:]
#     a += k[i][:2]
#
# m = 0
# for i in range(len(a)):
#     for j in range(i+1, len(a)):
#         if (a[i] - a[j]) % 80 == 0:
#             m = max(m, a[i] - a[j])
#
# print(m) # 85440 99920

# -----------------------------------------------------

# f = open('27B_2734.txt')
# n = int(f.readline())
# k = [0]*46
#
# for i in range(n):
#     x = int(f.readline())
#     sum_dig = sum(int(x) for x in str(x))
#     k[sum_dig] += 1
# print(max(k), k.index(max(k))) # 10 621

# ------------------------------------------

# f = open('27A_2736.txt')
# n = int(f.readline())
# k = [0]*10
# for i in range(n):
#     x = int(f.readline())
#     k[int(str(x)[0])] += 1
# print(min(k[1:])) # 7 1064

# ---------------------------------------------

# f = open('27B_2738.txt')
# n = int(f.readline())
# k = [0] * 10
# for i in range(n):
#     x = int(f.readline())
#     for num in str(x):
#         k[int(num)] += 1
# print(min(k)) # 37 3863

# ------------------------------------------------

# f = open ('27B_2731.txt')
# n = int(f.readline())
# x12 = []
# ym = 0
#
# for i in range(n):
#     x, y = map(int, f.readline().split())
#     if y == 0: x12 += [x]
#     ym = max(ym, abs(y))
# print((max(x12) - min(x12)) * ym // 2) # 5684 38600

# --------------------------------------------------------------

# f = open('27B_2735.txt')
# n = int(f.readline())
# ox = 0
# oy = 0
# notxy = 0
# 
# for i in range(n):
#     x, y = map(int, f.readline().split())
#     if y == 0: ox += 1
#     if x == 0: oy += 1
#     if x != 0 and y != 0: notxy += 1
# print(ox*oy*notxy) # 846 7518420

# -------------------------------------------------------------

# f = open('Динамические решения/27A_2720.txt')
# n = int(f.readline())
# k = k7 = 0
# c = 0
# for i in range(n):
#     x = int(f.readline())
#     if x % 7 == 0: c += k
#     else: c += k7
#
#     k += 1
#     if x % 7 == 0: k7 += 1
# print(c) # 1209 13831740

# ----------------------------------------------------------

# f = open('Динамические решения/27A_2721.txt')
# n = int(f.readline())
# k = k65 = k13 = k5 = 0
# c = 0
# for i in range(n):
#     x = int(f.readline())
#     if x % 65 == 0: c += k
#     elif x % 13 == 0: c += k5
#     elif x % 5 == 0: c += k13
#     else: c += k65
#
#     if x % 65 == 0: k65 += 1
#     if x % 13 == 0: k13 += 1
#     if x % 5 == 0: k5 += 1
#     k += 1
# print(c) # 168 2503584

# ---------------------------------------------------------

# f = open('Динамические решения/27B_2722.txt')
# n = int(f.readline())
# k5_0 = k5_1 = k_1 = k_0 = 0
# c = 0
# for i in range(n):
#     x = int(f.readline())
#     if x % 5 == 0 and x % 2 == 0: c += k_1 + k5_1
#     if x % 5 == 0 and x % 2 != 0: c += k5_0 + k_0
#     if x % 5 != 0 and x % 2 == 0: c += k5_1
#     if x % 5 != 0 and x % 2 != 0: c += k5_0
#
#     if x % 5 == 0 and x % 2 == 0: k5_0 += 1
#     if x % 5 == 0 and x % 2 != 0: k5_1 += 1
#     if x % 5 != 0 and x % 2 == 0: k_0 += 1
#     if x % 5 != 0 and x % 2 != 0: k_1 += 1
# print(c) # 1056 8863690

# ---------------------------------------------------------

# f = open('Динамические решения/27B_2724.txt')
# n = int(f.readline())
# k = [0]*131
# c = 0
# for i in range(n):
#     x = int(f.readline())
#
#     ost = 0 if x % 131 == 0 else 131 - x%131
#     c += k[ost]
#
#     k[x%131] += 1
# print(c) # 31 381543

# ---------------------------------------------------

# f = open('Динамические решения/27B_2733.txt')
# n = int(f.readline())
# k = [[0]*80 for i in range(2)]
# c = 0
# for i in range(n):
#     x = int(f.readline())
# 
#     ost = 0 if x % 80 == 0 else 80 - x % 80
#     koef = 0 if x > 50000 else k[0][ost]
#     c += k[x > 50000][ost] + koef
# 
#     k[x > 50000][x % 80] += 1
# print(c) # 48 465486

# --------------------------------------

# f = open('Динамические решения/27A_2726.txt')
# n = int(f.readline())
# m = -10**20
# k = [-10**20]*3
#
# for i in range(n):
#     x = int(f.readline())
#     ost = 0 if x % 3 == 0 else 3-x%3
#     m = max(m, x + k[ost])
#
#     k[x%3] = max(x, k[x%3])
# print(m, k ) # 72384 133947

# --------------------------------------------------------------

# f = open('Подпоследовательности/27A_2900.txt')
# n = int(f.readline())
# s = 0
# k = [10**20] * 1000
# ms = 0
#
# for i in range(n):
#     x = int(f.readline())
#     s += x
#     if s % 1000 == 0: ms = max(ms, s)
#     s1 = s - k[s%1000]
#     ms = max(ms, s1)
#
#     k[s%1000] = min(k[s%1000], s)
# print(ms) # 259000 49763000

# --------------------------------------------------

# f = open('Подпоследовательности/27B_2901.txt')
# n = int(f.readline())
# s = 0
# k = [0] * 666
# c = 0
#
# for i in range(n):
#     x = int(f.readline())
#     s += x
#     if s % 666 == 0: c += 1
#     c += k[s%666]
#
#     k[s%666] += 1
# print(c) # 5 75150

# ------------------------------------------------------

# f = open('Подпоследовательности/27B_2902.txt')
# n = int(f.readline())
# k = [0] * 11
# k5 = 0
# count = 0
#
# for i in range(n):
#     x = int(f.readline())
#     if x % 5 == 0: k5 += 1
#     if k5 % 11 == 0: count += 1
#     count += k[k5 % 11]
#
#     k[k5%11] += 1
# print(count) # 588 4557520

# ------------------------------------------------

# f = open('Подпоследовательности/27A_2256.txt')
# n = int(f.readline())
# m = [10**20] * 3
# k = 0
# ms = 0
# s = 0
#
# for i in range(n):
#     x = int(f.readline())
#     s += x
#     if x % 5 == 0: k += 1
#     if k % 3 == 0: ms = max(ms, s)
#     s1 = s - m[k%3]
#     ms = max(ms, s1)
#
#     m[k%3] = min(m[k%3], s)
# print(ms) # 66453 69995639

# ----------------------------------------------------------

# f = open('Подпоследовательности/27B_1877.txt')
# n = int(f.readline())
# ms = 0
# ml = 0
# s = 0
# m = [10**20]*89
# l = [0]*89
# for i in range(n):
#     x = int(f.readline())
#     s += x
#     if s % 69 == 0 and s > ms: ms, ml = s, i+1
#
#     s1 = s - m[s % 69]
#     l1 = (i + 1) - l[s % 69]
#
#     if s1 > ms or (s1 == ms and l1 < ml): ms, ml = s1, l1
#     if s < m[s%69]: m[s%69], l[s%69] = s, i+1
# print(ml) # 14 99989

# ----------------------------------------------------

# f = open('Подпоследовательности/27B_2904.txt')
# n = int(f.readline())
# ms = 10**20
# ml = 0
# s = 0
# m = [-10**20]*2077
# l = [0]*2077
# for i in range(n):
#     x = int(f.readline())
#     s += x
#     if s % 2077 == 0 and s < ms: ms, ml = s, i+1
#
#     s1 = s - m[s % 2077]
#     l1 = (i + 1) - l[s % 2077]
#
#     if s1 < ms or (s1 == ms and l1 > ml): ms, ml = s1, l1
#     if s > m[s % 2077]: m[s % 2077], l[s % 2077] = s, i+1
# print(ml) # 28 8208

# -------------------------------------------------------

# f = open('Подпоследовательности/27B_2907.txt')
# n = int(f.readline())
# k, s, ms = 0, 0, 0
# m = [10**20] * 30
#
# for i in range(n):
#     x = int(f.readline())
#     s += x
#     if x > 0 and x % 2 == 0: k += 1
#     if k % 30 == 0: ms = max(ms, s)
#     s1 = s - m[k%30]
#     ms = max(ms, s1)
#
#     m[k%30] = min(s, m[k%30])
# print(ms) # 21365 286527

# --------------------------------------------------

# f = open('Подпоследовательности/27B_2363.txt')
# n = int(f.readline())
# q = []
# s = 0
# c = 0
# m = [0]*117
#
# for i in range(5-1):
#     x = int(f.readline())
#     s += x
#     q.append(s)
#
# for i in range(n-4):
#     x = int(f.readline())
#     s += x
#     if s % 117 == 0: c += 1
#     c += m[s%117]
#
#     m[q[0]%117] += 1
#     q.pop(0)
#     q.append(s)
# print(c) # 34 42729434

# ----------------------------------------------------------------

# f = open('Подпоследовательности/27B_2908.txt')
# n = int(f.readline())
# q = []
# s = 0
# ms = -10**20
# m = [10**20]*7
# k7 = 0
# for i in range(7-1):
#     x = int(f.readline())
#     s += x
#     if x > 0 and x % 7 == 0: k7 += 1
#     q.append([s, k7])
#
# for i in range(n-6):
#     x = int(f.readline())
#     s += x
#     if x % 7 == 0 and x > 0: k7 += 1
#     if k7 % 7 == 0: ms = max(ms, s)
#     s1 = s - m[k7%7]
#     ms = max(s1, ms)
#
#     s0, k0 = q[0]
#     m[k0%7] = min(m[k0 % 7], s0)
#     q.pop(0)
#     q.append([s, k7])
# print(ms) # 48451 290112

# ----------------------------------------------------------

# f = open('Сдвиги/27A_6318.txt')
# n, m = map(int, f.readline().split())
# a = []
# for i in range(n):
#     k = int(f.readline())
#     a.append(k)
#
# s = mx = sum(a[:2*m + 1])
# for i in range(m+1, n - m):
#     s = s - a[i - m - 1] + a[i + m]
#     mx = max(s, mx)
# print(mx) # 81162 641474

# ---------------------------------------------

# f = open('Сдвиги/27B_6320.txt')
# n, m = map(int, f.readline().split())
# a = []
#
# for i in range(n):
#     k = int(f.readline())
#     a.append(k)
# a = a*2
#
# s = mx = sum(a[:2*m+1])
# for i in range(m+1, n*2 - m):
#     s = s - a[i-m-1] + a[i+m]
#     mx = max(mx, s)
# print(mx) # 91573 1782723

# --------------------------------------------------

# f = open('Сдвиги/27B_4116.txt')
# n, mk = map(int, f.readline().split())
# mx = 0
# a = [int(x) for x in f]
# s = a[0]
# start = end = 0
#
# while s + a[end+1] <= mk:
#     s += a[end+1]
#     end += 1
#
# mx = end - start + 1
#
# while end != n-1:
#     s -= a[start]
#     while end != n-1 and s + a[end+1] <= mk:
#         s += a[end+1]
#         end += 1
#     start += 1
#
#     mx = max(mx, end - start + 1)
# print(mx) # 38 14918

# --------------------------------------------------

# f = open('Сдвиги/27A_6321.txt')
# n, v, m = map(int, f.readline().split())
# a = []
# for i in range(n):
#     km, k = map(int, f.readline().split())
#     c = k // v if k % v == 0 else k // v + 1
#     a.append([km, c])
# a.sort()
# b = [0] * (a[-1][0] + 1)
#
# for el in a:
#     km, c = el
#     b[km] = c
# s = mx = sum(b[:2*m+1])
#
# for i in range(m+1, a[-1][0] + 1-m):
#     s = s - b[i-m-1] + b[i+m]
#     if b[i] > 0: mx = max(mx, s)
# print(mx) # 2504 3346

# -------------------------------------------------

# f = open('Сдвиги/27B_4630.txt')
# n, k_par, m = map(int, f.readline().split())
# a = []
# for i in range(n):
#     km, k = map(int, f.readline().split())
#     km = km % k_par
#     c = k // 9 if k % 9 == 0 else k // 9 + 1
#     a.append([km, c])
#
# b = [0]*k_par
# for el in a:
#     km, c = el
#     b[km] = c
#
# b = b*2
# s = mx = sum(b[:2*m+1])
# for i in range(m+1, k_par + m):
#     s = s - b[i - m - 1] + b[i+m]
#     if b[i] > 0: mx = max(mx, s)
# print(mx) # 409 95850

# ------------------------------------------------

# f = open('Сдвиги/27B_5644.txt')
# n = int(f.readline())
# a = [int(x) for x in f]
# sm = sum(a)
# s = 0
# b = []
# for i in range(n):
#     s += a[i]
#     b.append(s)
# 
# s = 0
# for i in range(n):
#     s += a[i] * i
# 
# mx = s
# for i in range(1, n):
#     s = s + b[i-1] - (sm - b[i-1])
#     mx = max(mx, s)
# print(mx) # 849014 44029481068414

# ----------------------------------------------

# f = open('Сдвиги/27B_6323.txt')
# n, m = map(int, f.readline().split())
# a = []
# sm = 0
# for i in range(n):
#     km, k = map(int, f.readline().split())
#     c = k // m if k % m == 0 else k // m + 1
#     sm += c
#     a.append([km, c, sm])
# s = 0
# for i in range(n):
#     s += (a[i][0] - a[0][0]) * a[i][1]
# mx = s
# d_price = 0
#
# for i in range(1, n):
#     d_price += a[i-1][1]
#     r = a[i][0] - a[i-1][0]
#     s = s + r*d_price - r*(sm - d_price)
#     mx = min(mx, s)
# print(mx) # 71028 2999492166115

# ---------------------------------------------------

