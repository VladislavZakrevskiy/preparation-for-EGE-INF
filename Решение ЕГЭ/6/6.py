# 2 --------------------------------------------------------------------------
##print('z y w x F')
##for x in range(2):
##    for y in range(2):
##        for z in range(2):
##            for w in range(2):
##                F = (x <= y) or (not(w <= z))
##                if not F: print(z,y,w,F)
# 5 --------------------------------------------------------------------------
##def convert_to(x, base=3):
##    s = ''
##    alfabet = '0123456789ABDE'
##    while x > 0:
##        s = str(alfabet[x%base]) + s
##        x //= base
##    return s
##
##def f(x):
##    ost = x % 3
##    x_3 = convert_to(x)
##    if ost == 0:
##        x_3 += x_3[-2] + x_3[-1]
##    else:
##        ost_3 = convert_to(ost*5)
##        x_3 += ost_3
##    return int(x_3,3)
##for x in range(1, 100):
##    if f(x) > 133:
##        print(f(x))
##        break
# 8 --------------------------------------------------------------------------
##from itertools import *
##c = 0
##for el in permutations('КАЛИЙ',r=5):
##    s = ''.join(el)
##    if el[0] != 'О' and 'ИА' not in s: c += 1
##print(c)
# 12 --------------------------------------------------------------------------
##def f(s):
##    while '33' in s or '11' in s or '22' in s:
##        if '33' in s:
##            s = s.replace('33', '12', 1)
##        if '11' in s:
##            s = s.replace('11', '32', 1)
##        if '22' in s:
##            s = s.replace('22', '31', 1)
##    return s
##def sum_c(s):
##    summa = 0
##    for i in s: summa += int(i)
##    return summa
##print(sum_c(f(34*'2'+30*'3'+38*'1')))
# 13 --------------------------------------------------------------------------
##print(bin(142)[2:].zfill(8), bin(198)[2:].zfill(8), bin(113)[2:].zfill(8), bin(106)[2:].zfill(8), 'ip')
##print(bin(142)[2:].zfill(8), bin(198)[2:].zfill(8), bin(112)[2:].zfill(8), bin(0)[2:].zfill(8), 'web')
# 14 --------------------------------------------------------------------------
##def convert_to(x, base=3):
##    s = ''
##    alfabet = '0123456789ABDE'
##    while x > 0:
##        s = str(alfabet[x%base]) + s
##        x //= base
##    return s
##print(oct(64**30+2**300-4).count('7'))
# 15 --------------------------------------------------------------------------
##for A in range(1000):
##    is_good = True
##    for x in range(1000):
##        if not is_good: break
##        for y in range(1000):
##            F = (2*y + x != 70) or (x < y) or (A < x)
##            if not F:
##                is_good = False
##                break
##    else: print(A)
# 16 --------------------------------------------------------------------------
##from functools import *
##@lru_cache(None)
##def f(n):
##    if n < -100000: return 1
##    if n > 10: return f(n-1) + 3*f(n-3) + 2
##    return -f(n-1)
##for i in range(-100_000, 21):
##    f(i)
##print(f(20))
# 17 --------------------------------------------------------------------------
##f = open('17_2398.txt')
##a = [int(x) for x in f]
##c = 0
##mx = 0
##for i in range(len(a)-2):
##    a_0 = a[i]
##    a_1 = a[i+1]
##    a_2 = a[i+2]
##    if a_0 < 0 and a_2 < 0 and a_1 > 0 and abs(a_1)%10 == 9:
##        c += 1
##        mx = max(mx, a_0 + a_1 + a_2)
##print(c, mx)
# 19-21 --------------------------------------------------------------------------
##def win(s1,s2,round):
##    if s1+s2 >=131: return round%2 == 0
##    if round == 0: return 0
##    nextWin = [win(s1+2,s2,round-1), win(s1*2,s2,round-1),
##               win(s1,s2+2,round-1), win(s1,s2*2,round-1), ]
##    return any(nextWin) if (round-1)%2 == 0 else all(nextWin)
##print('19) ', [s for s in range(1,123) if win(11, s, 2)]) # 30
##print('20) ', [s for s in range(1,123) if not win(11, s, 1) and win(11, s, 3)]) # 54 57
##print('21) ', [s for s in range(1,123) if not win(11, s, 2) and win(11, s, 4)]) # 52
# 23 --------------------------------------------------------------------------
##def f(start, end):
##    if start > end: return 0
##    if start == end: return 1
##    s = f(start+1, end) + f(start+2, end)+ f(start*2, end)
##    
##    return s
##print(f(2,12))
##from itertools import *
##c = []
##for el in product('123', repeat=10):
##    s = 2
##    arr = []
##    for comand in el:
##        arr.append(comand)
##        if s > 12: break
##        if comand == '1':
##            s += 1
##            if s == 12 and arr.count('3') <= 2:
##               c.append(''.join(arr))  
##        if comand == '2':
##            s += 2
##            if s == 12 and arr.count('3') <= 2:
##                c.append(''.join(arr))
##        if comand == '3':
##            s *= 2
##            if s == 12 and arr.count('3') <= 2:
##                c.append(''.join(arr))
##print(set(c))
# 24 --------------------------------------------------------------------------
##s = open('24_2500.txt').readline()
##c = 0
##for let in 'QWERTYUIOPASDFGHJKLZXCVBNM':
##    c += s.count('G' + let + 'ME')
##print(c)
# 25 --------------------------------------------------------------------------
##from fnmatch import *
##def sum_c(s):
##    s = str(s)
##    summa = 0
##    for i in s: summa += int(i)
##    return summa
##for i in range(2023, 10**9, 2023):
##    if fnmatch(str(i), '20*23') and sum_c(i) % 7 == 0 and sum_c(i) < 20:
##        print(i) 
# 26 --------------------------------------------------------------------------
##f = open('26_788.txt')
##d, e, n = map(int, f.readline().split())
##for_disk_d = []
##for_disk_e = []
##for i in range(n):
##    x = int(f.readline())
##    if x > 500: for_disk_d.append(x)
##    else: for_disk_e.append(x)
##a = for_disk_e + for_disk_d
##for_disk_d.sort()
##for_disk_e.sort()
##a.sort()
##sum_d = 0
##sum_e = 0
##c = 0
##for el in for_disk_d:
##    if sum_d + el <= d:
##        sum_d += el
##        c += 1
##        print(el, sum_d)
##for el in for_disk_e:
##    if sum_e + el <= e:
##        sum_e += el
##        c += 1
##        print(el)
##print(a)
# 27 --------------------------------------------------------------------------
f = open ('27-B_2582.txt')
n, k = map(int, f.readline().split())
k_3 = 0
s = 0
m = [10**20]*n
mx = 0

for i in range(n):
    x = int(f.readline())
    s += x
    if x < 0 and abs(x) % 10 == 3: k_3 += 1
    if k_3 == k: mx = max(mx, s)
    mx = max(mx, s - m[k_3 - k])
    
    m[k_3] = min(m[k_3], s)
print(mx)
