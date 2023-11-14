# file = open('26-111.txt')
# K = int(file.readline())
# N = int(file.readline())
# a = []
#
# for i in range(N):
#     st, end = map(int, file.readline().split())
#     a.append([st, end])
#
# a.sort()
# cameras = [0]*K
#
# last = 0
# count = 0
# for i in range(N):
#     st, end = a[i]
#     for j in range(K):
#         if cameras[j] < st:
#             cameras[j] = end
#             last = j + 1
#             count += 1
#             break
# print(count, last)

# --------------------------------------------------------

# file = open('26-119.txt')
# N, L, M = map(int, file.readline().split())
# 
# a = []
# 
# for i in range(N):
#     start, time, type = file.readline().split()
#     a.append([int(start), int(time), type])
# 
# a.sort()
# 
# l = [0]*L
# m = [0]*M
# 
# not_park = 0
# m_park = 0
# 
# for i in range(N):
#     start, time, type = a[i]
#     if type == 'A':
#         is_park = False
#         for j in range(L):
#             if l[j] <= start:
#                 l[j] = start + time
#                 is_park = True
#                 break
#         for k in range(M):
#             if m[k] <= start and not is_park:
#                 m[k] =  start + time
#                 is_park = True
#                 break
#         if not is_park:
#             not_park += 1
#     else:
#         is_m_park = False
#         for y in range(M):
#             if m[y] <= start:
#                 m[y] =  start + time
#                 m_park += 1
#                 is_m_park = True
#                 break
#         if not is_m_park:
#             not_park += 1

# print(m_park, not_park)

# -----------------------------------------------------

# file = open('26-112.txt')
# N, M = map(int, file.readline().split())
# a = []
#
# for i in range(M):
#     start, time = map(int, file.readline().split())
#     a.append([start, time])
# a.sort(key=lambda x: x[0])
# b = [0]*N
# b_nums = [0]*N
# last = []
#
# for i in range(M):
#     start, time = a[i]
#     for j in range(N):
#         if b[j] <= start:
#             if start <= 1440:
#                 b[j] = start + time
#             b_nums[j] += 1
#             last = [b[j], time]
#             break
#     else:
#         next_free_bank = min(b)
#         for j in range(N):
#             if b[j] == next_free_bank:
#                 if b[j] <= 1440:
#                     b_nums[j] += 1
#                     last = b[j]
#                 b[j] += time
#                 break
#
# print(max(b_nums), last)

# --------------------------------------------------------

# file = open('26-125.txt')
# D, P = map(int, file.readline().split())
#
# a = []
#
# for i in range(D):
#     start, mana = map(int, file.readline().split())
#     if mana > 1:
#         a.append([start, mana // 2])
#
# a.sort()
#
# k = [0]*P
# count = 0
# d_max = 0
# for i in range(len(a)):
#     start, time = a[i]
#     for j in range(P):
#         if k[j] <= start:
#             k[j] = start + time if k[j] == 0 else start + time + 2
#             if k[j] > 1440:
#                 time -= k[j] - 1440
#             count += time
#             d_max = max(d_max, time)
#             break
# print(count, d_max)

# -------------------------------------------------

# from math import *
#
# f = open('26-122.txt')
# K, N = map(int, f.readline().split())
# a = []
#
# for i in range(N):
#     start, end = map(int, f.readline().split())
#     a.append([start, end])
#
# a.sort()
#
# d = [0]*(100 * K)
# max_len = 0
# d_last = 0
#
# for i in range(N):
#     start, end = a[i]
#     for j in range(100*K):
#         if d[j] < start:
#             d[j] = end
#             d_last = len([x for x in d if x > start])
#             break
# d = [x for x in d if x != 0]
# print(ceil(len(d) / K), d_last)

# -----------------------------------------------------

# f = open('26-124.txt')
# K, M, N = map(int, f.readline().split())
# a = []
#
# for i in range(N):
#     a.append(int(f.readline()))
# a.sort(reverse=1)
#
# stadion = [M]*K
# count = 0
# for i in range(N):
#     zayvka = a[i]
#     for j in range(K):
#         if stadion[j] >= zayvka:
#             stadion[j] -= zayvka
#             count += 1
#             break
# print(count, sum(stadion))

# -----------------------------------------------

# f = open('26-75.txt')
# N = int(f.readline())
#
# a = [0]*1_000_000
#
# for i in range(N):
#     st, end = map(int, f.readline().split())
#     a[st] += 1
#     a[end] -= 1
# k = 0
# k_max = 0
# count_1 = 0
# for i in range(1_000_000):
#     k += a[i]
#     if k >= 1:
#         count_1 += 1
#     k_max = max(k_max, k)
# print(k_max, count_1)

# ----------------------------------------------------------------

# f = open('26-76.txt')
# L, N = map(int, f.readline().split())
# a = [0]*(10**9)
#
# for i in range(N):
#     start, end = map(int, f.readline().split())
#     a[start] += 1
#     a[end] -= 1
#
# k = 0
# sum_0 = 0
# max_0 = 0
# d_0 = 0
# for i in a:
#     if i == 0:
#         sum_0 += 1
#         d_0 += 1
#         max_0 = max(max_0, d_0)
# print(sum_0, max_0)

# ---------------------------------------------------------------

# f = open('26_11484.txt')
# N = int(f.readline())
# a = []
#
# for i in range(N):
#     start, end = map(int, f.readline().split())
#     a.append([start, end])
#
# a.sort(key=lambda x: x[1])
# ans = []
# gr = 0
# for i in a:
#     start, end = i
#     if start >= gr:
#         gr = end
#         ans.append([start, end])

# print(len(ans), ans[0][1])

# ---------------------------------------------------------

# f = open('26_10726.txt')
# N = int(f.readline())
# a = [0]*44641
#
# for i in range(N):
#     start, end = map(int, f.readline().split())
#     a[start] += 1
#     a[end] -= 1
# count = 0
# count_max = 0
# d = 0
# k = 0
# for el in a:
#     k += el
#     if k > 0:
#         count += 1
#         d += 1
#         count_max = max(d, count_max)
#     if k == 0:
#         d = 0
# print(count, count_max)

# --------------------------------------------------------------

# f = open('26_10107.txt')
# N = int(f.readline())
# a = []
# for i in range(N):
#     start, end = map(int, f.readline().split())
#     a.append([start, end])
# a.sort(key=lambda x: x[1])
#
# gr = a[0][1]
# ans = [a[0]]
# # max_pereryv = 0
#
# for el in a:
#     start, end = el
#     if start >= gr:
#         # max_pereryv = max(max_pereryv, start - gr)
#         gr = end
#         ans.append(el)
# print(len(ans), ans[-1][0] - ans[-2][1])

# --------------------------------------------------------------

# f = open('26_9847.txt')
# N = int(f.readline())
# a = [0]*10001
#
# for i in range(N):
#     start, end = map(int, f.readline().split())
#     a[start] += 1
#     a[end] -= 1
#
# k = 0
# d_max = 0
# count_maxes = 0
# is_first = True
#
# for i in a:
#     k += i
#     if k > d_max:
#         d_max = k
#         count_maxes = 1
#     if k == d_max and is_first:
#         count_maxes += 1
#         is_first = False
#     if k != d_max:
#         is_first = True
# print(count_maxes, d_max)

# -----------------------------------------------------------

# f = open('26_9793.txt')
# N = int(f.readline())
# a = []
# all_nums = []
# for i in range(N):
#     shlif, okrash = map(int, f.readline().split())
#     a.append([shlif, okrash])
#     all_nums.append([shlif, i+1, 0])
#     all_nums.append([okrash, i+1, 1])
#
# all_nums.sort()
# ans = [0]*N
# were_indexes = []
# index_start = 0
# index_end = -1
# last = 0
#
# for el in all_nums:
#     num, index, type = el
#     if type == 0 and index not in were_indexes:
#         ans[index_start] = index
#         were_indexes.append(index)
#         index_start += 1
#         last = index
#     if type == 1 and index not in were_indexes:
#         ans[index_end] = index
#         were_indexes.append(index)
#         index_end -= 1
#
# print(last, ans.index(last))

# ---------------------------------------------------------

# f = open('26_9756.txt')
# N = int(f.readline())
# a = []
# for i in range(N):
#     start, end = map(int, f.readline().split())
#     a.append([start, end])
# a.sort(key = lambda x: x[1])
# print()
# gr = 0
# ans = []
#
# for i in range(N):
#     start, end = a[i]
#     if start >= gr:
#         gr = end
#         ans.append([start, end])
# print(len(ans), [x for x in a if x[1] > 1028 and x[0] > 991])

# -----------------------------------------------------------------

# f = open('26_9711.txt')
# M, N = map(int, f.readline().split())
# a = []
#
# for i in range(N):
#     start, time, num_start, num_finish = map(int, f.readline().split())
#     a.append([start, time, num_start, num_finish])
#
# samokati = [0]*M
# max_sam = 0
# samokati_finish_max = [0]*M
#
# for el in a:
#     start, time, num_start, num_finish = el
#     end = start + time
#     for j in range(M):
#         if samokati[j] < start:
#             samokati[j] = end
#             samokati_finish_max[j] += 1
#             break
#
#
# print(max_sam, max(samokati_finish_max))

# ------------------------------------------------------------

