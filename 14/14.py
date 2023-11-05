# print(bin(8**1341 - 4**1342 + 2**1343 - 1344).count('1'))

# print(bin(8**152 + 4**915 - 2**778 - 4**71 - 2**31 - 30).count('0') - 1)

# print(hex(2**379 + 2**378 + 2**377)[2])

# s = (2*343**123 + 2401)*(3*343**137 - 2401)
# num7 = ''
# while s > 0:
#     num7 += str(s%7)
#     s //= 7
# print(num7.count('6'), num7)

# s = 4*625**1920 + 4*125**1930 - 4*25**1940 - 3*5**1950 - 1960
# num5 = ''
# while s:
#     num5 += str(s % 5)
#     s //= 5
# print(num5.count('0'), num5)

# s = 103 * 7**103 - 5*7**57 + 98
# num7 = ''
# while s:
#     num7 += str(s%7)
#     s //= 7
# sum = 0
# for i in num7:
#     sum += int(i)
# print(sum)

# for x in range(1000):
#     s = 27**7 - 3**11 + 36 - x
#     sum = 0
#     while s:
#         sum += s % 3
#         s //= 3
#
#     if sum == 22:
#         print(x)

# for x in range(10000):
#     s = 5**2026 + 7*5**1013 + 107 - x
#     num6 = ''
#     while s:
#         num6 += str(s % 6)
#         s //= 6
#     if num6.count('5') - num6.count('0') == 28:
#         print(x)

# s = 1755
#
# def convert_by (num, base):
#     num_base = ''
#     while num:
#         num_base += str(num % base)
#         num //= base
#     return  num_base[::-1]
#
# print(2, convert_by(s, 2))
# print(3, convert_by(s, 3))
# print(4, convert_by(s, 4))
# print(5, convert_by(s, 5))
# print(6, convert_by(s, 6))
# print(7, convert_by(s, 7))
# print(8, convert_by(s, 8))
# print(9, convert_by(s, 9))
# print(10, convert_by(s, 10))

# ответ: 15

# for x in '0123456789abcde':
#     if (int(f'82{x}19', 15) - int(f'6{x}073', 15)) % 11 == 0:
#         print(x, (int(f'82{x}19', 15) - int(f'6{x}073', 15)) // 11)

# for x in range(44):
#     f1 = 44**3 + x*44**2 + 2*44 + 3
#     f2 = 3*44**3 + 2*44**2 + x*44 + 1
#     d = f1 + f2
#     if d % 42 == 0:
#         print(x, d // 42)

for p in range(100):
    for x in range(p):
        for y in range(p):
            f1 = p**3 + x*p**2 + 7*p + 7
            f2 = x*p**3 + x*p**2 + 7*p + 7
            s = y*p**3 + y*p + y
            if (f1 + f2) == s:
                print(p, y*p**3 + x*p**2 + y*p + x)