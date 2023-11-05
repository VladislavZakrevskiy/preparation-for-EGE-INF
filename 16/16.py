# def f(n):
#     if n < 10:
#         return n
#     if n >= 10:
#         return n%10 + 8*f(n//10)
# print(f(10**30))

# def f (n):
#     if n == 30:
#         return -88
#     if n == 40:
#         return -626
#     if n < 3:
#         return 2
#     if n > 2 and n % 2 == 0:
#         return 2*f(n-2) - f(n-1) + 2
#     if n > 2 and n % 2 != 0:
#         return 2*f(n-1) + f(n-2) - 2

# print(f(45))

def f(n):
    if n == 1500:
        return 1125750
    if n == 1000:
        return 500500
    if n == 800:
        return 320400
    if n == 700:
        return 245350
    if n == 600:
        return 180300
    if n == 500:
        return 125250
    if n == 1:
        return 1
    if n > 1:
        return n + f(n-1)

f2023 = 2047276
cnt = 0
for n in range(1, 101):
    if (f2023 // f(n)) % 2 == 0:
        cnt += 1
        print(n)
print (cnt)