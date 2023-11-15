# a = [int(x) for x in open('17_11481.txt')]
# a_8 = [x for x in a if str(x)[0] == '8']
# max_8 = max(a_8)
#
# ans = []
# for i in range(len(a)-2):
#     a_0 = abs(a[i])
#     a_1 = abs(a[i+1])
#     a_2 = abs(a[i+2])
#
#     na4alo_6 = (str(a_0)[0] == '6' and str(a_1)[0] != '6' and str(a_2)[0] != '6') \
#                or (str(a_0)[0] != '6' and str(a_1)[0] == '6' and str(a_2)[0] != '6') \
#                or (str(a_0)[0] != '6' and str(a_1)[0] != '6' and str(a_2)[0] == '6') \
#                or (str(a_0)[0] != '6' and str(a_1)[0] != '6' and str(a_2)[0] != '6')
#     sum_troyka = sum([a[i], a[i+1], a[i+2]])
#     if na4alo_6 and sum_troyka >= max_8:
#        ans.append(sum_troyka)
# print(len(ans), min(ans))

# --------------------------------------------------------

# a = [int(x) for x in open('17_10771.txt')]
#
# def is_prost (x):
#     if x < 2: return False
#     sqrt = int(x ** 0.5) + 1
#     for i in range(2, sqrt):
#         if x % i == 0:
#             return False
#     return True
#
# ans = []
# for i in range(len(a)-2):
#     if ('3' in (str(a[i]) ) and ('3' in str(a[i+1]) ) and ( '3' in str(a[i+2]))) and is_prost(a[i] + a[i+1] + a[i+2]):
#        ans.append(a[i] + a[i+1] + a[i+2])
# print(len(ans), min(ans))

# -------------------------------------------------

# a = [int(x) for x in open('17_10719.txt')]
# ans = []
# def is_kon_13 (str_n):
#     if len(str_n) < 2: return False
#     return str_n[-1] == '3' and str_n[-2] == '1'
#
# for i in range(len(a)-3):
#     str_0 = str(a[i])
#     str_1 = str(a[i+3])
#     if (is_kon_13(str_0) and not is_kon_13(str_1)) or ( not is_kon_13(str_0) and  is_kon_13(str_1)):
#         ans.append(a[i] + a[i+3])
# print(len(ans), max(ans))

# ----------------------------------------------------

# a = [int(x) for x in open('17_10100.txt')]
# a_kon_13 = [x for x in a if str(x)[-1] == '3' and str(x)[-2] == '1']
# max_kon_13 = max(a_kon_13)
# def is_3zna4(x):
#     return x >= 100 and x <= 999
# ans = []
# for i in range(len(a)-2):
#     a_0 = a[i]
#     a_1 = a[i+1]
#     a_2 = a[i+2]
#     if ((is_3zna4(a_0) and is_3zna4(a_1) and not is_3zna4(a_2)) or \
#         (is_3zna4(a_0) and not is_3zna4(a_1) and is_3zna4(a_2)) or \
#         (not is_3zna4(a_0) and is_3zna4(a_1) and is_3zna4(a_2))) and (a[i] + a[i+1] + a[i+2]) <= max_kon_13:
#         ans.append(a[i] + a[i+1] + a[i+2])
# print(len(ans), max(ans))

# ----------------------------------------------------

# a = [int(x) for x in open('17_9840.txt')]
# def is_4zna4 (x):
#     return x >= 1000 and x <= 9999
#
# a_kon_39 = [x for x in a if is_4zna4(x) and str(x)[-1] == '9' and str(x)[-2] == '3']
# max_kon_39 = max(a_kon_39)
#
# ans = []
# for i in range(len(a)-1):
#     a_0 = a[i]
#     a_1 = a[i+1]
#     if ((is_4zna4(a_0) and not is_4zna4(a_1)) or (not is_4zna4(a_0) and is_4zna4(a_1))) and abs(a_0 + a_1) <= max_kon_39 :
#         ans.append(a_0 + a_1)
# print(len(ans), max(ans))

# ------------------------------------------------------

# a = [int(x) for x in open('17_9786.txt')]
# m = max(x for x in a if abs(x) % 100 == 25)
#
# ans = []
# for i in range(len(a)-2):
#     if (1000 <= a[i] <= 9999) + (1000 <= a[i+1] <= 9999) + (1000 <= a[i+2] <= 9999) <= 2 \
#             and a[i] + a[i+1] + a[i+2] <= m:
#         ans.append(a[i] + a[i+1] + a[i+2])
# print(len(ans), max(ans))

# ------------------------------------------------------

# a = [int(x) for x in open('17_9748.txt')]
# m = max(x for x in a if abs(x) % 100 == 15)
# ans = []
# for i in range(len(a)-2):
#     if (1000 <= a[i] <= 9999) + (1000 <= a[i+1] <= 9999) + (1000 <= a[i+2] <= 9999) == 1 and \
#         a[i] + a[i+1] + a[i+2] >= m:
#         ans.append(a[i] + a[i+1] + a[i+2])
# print(len(ans), max(ans))

# ----------------------------------------------------

# a = [int(x) for x in open('17_9704.txt')]
# m = 0
# for i in range(len(a)-1):
#     if (10 <= a[i] <= 99) + (10 <= a[i+1] <= 99) == 1:
#         m = max(m, a[i] + a[i+1])
# print(len([x for x in a if x >= m]), min(x for x in a if x >= m))

# -----------------------------------------------------

# a = [int(x) for x in open('17_9547.txt')]
# m_11 = min(x for x in a if 100 <= x <= 999 and abs(x) % 100 == 11)
# ans = []
# for i in range(len(a)-1):
#     if (100 <= a[i] <= 999) + (100 <= a[i+1] <= 999) == 1 and \
#         abs(a[i] - a[i+1]) % m_11 == 0:
#         ans.append(a[i] + a[i+1])
#
# print (len(ans), max(ans))

# --------------------------------------------------------------

# a = [int(x) for x in open('17_9070.txt')]
# m = min(x for x in a if 100<=x<=999 and str(x).count('0') <= 1 and str(x).count('1') <= 1 and str(x).count('2') <= 1 and str(x).count('3') <= 1 and str(x).count('4') <= 1 and str(x).count('5') <= 1 and str(x).count('6') <= 1 and str(x).count('7') <= 1 and str(x).count('8') <= 1 and str(x).count('9') <= 1)
#
# ans = []
# for i in range(1, len(a)//2 + 1):
#     a_0 = a[i-1]
#     a_1 = a[-i]
#     if (a_0 * a_1) % m == 0:
#        ans.append(a_0+a_1)
#
# print(len(ans), min(ans))