# def f(N):
#     is_4et = (N % 2 == 0)
#     R = ''
#     str3 = ''
#     while N:
#         str3 += str(N%3)
#         N //=3
#     str3 = str3[::-1]
#     # print(str3)
#     if is_4et:
#         R = f'1{str3}00'
#     if not is_4et:
#         sum = 0
#         for l in str3:
#             sum += int(l)
#         str3sum = ''
#         while sum:
#             str3sum += str(sum%3)
#             sum //= 3
#         str3sum = str3sum[::-1]
#         R = f'{str3}{str3sum}'
#     return R
#
#
# for N in range(1000):
#     if int(f(N), 3) > 168:
#         print(N)
#         break

# def to_6 (N):
#     str6 = ''
#     while N:
#         str6 += str(N%6)
#         N //= 6
#     return str6[::-1]
#
# def f(N):
#     is_thodd = (N % 3 == 0)
#     R = ''
#     str6 = to_6(N)
#     if is_thodd:
#         R = f'{str6[0]}{str6[1]}{str6}'
#     else:
#         ostatok = (N % 3) * 10
#         str_ost6 = to_6(ostatok)
#         R = f'{str6}{str_ost6}'
#     return R
#
# for N in range(6, 1000):
#     if int(f(N), 6) > 680:
#         print(int(f(N), 6))
#         break


def to_3 (N):
    str3 = ''
    while N:
        str3 += str(N%3)
        N //= 3
    return str3[::-1]

def f(N):
    str3 = to_3(N)
    ind_0 = str3.count('0')
    ind_1 = str3.count('1')
    ind_2 = str3.count('2')
    odd = ind_0 + ind_2
    R = ''

    if odd > ind_1:
        R = f'22{str3}'
    else:
        R = f'11{str3}'

    return R

arr = []
for N in range(11, 1001):
    if int(f(N), 3) > 100:
        arr.append(int(f(N), 3))
print(min(arr))