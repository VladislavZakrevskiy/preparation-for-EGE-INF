# def gameOver (num_stones):
#     return num_stones >= 342
#
# def win (num_stones, step):
#     if gameOver(num_stones): return step % 2 == 0
#     if step == 0: return 0
#     nextWin = [win(num_stones+2, step-1), win(num_stones*5, step-1)]
#     return any(nextWin) if (step-1) % 2 == 0 else all(nextWin) # в 19 all -> any

# for x in range(11, 326): # 14
#     if win(x, 2):
#         print(x)

# for x in range(11, 326): # 65 66
#     if win(x, 3) and not win(x, 1):
#         print(x)

# for x in range(11, 326): # 63 64 67 68
#     if win(x, 4) or win(x, 2):
#         print(x)

# def f(s1, s2, m):
#     if s1 + s2 <= 20: return m % 2 == 0
#     if m == 0: return 0
#     nextWin = [
#                f(s1-1, s2, m-1),
#                f((s1+1)//2, s2,  m-1),
#                f(s1, (s2+1)//2, m-1),
#                f(s1, s2 - 1, m-1)
#                ]
#     return any(nextWin) if (m-1)%2==0 else all(nextWin)
#
# print('19) ', [s for s in range(11, 300) if f(10, s, 2)])
# print('20) ', [s for s in range(11, 300) if f(10, s, 3) and not f(10, s, 1)])
# print('21) ', [s for s in range(11, 300) if not f(10, s, 2) and f(10, s ,4)])

# def f(a,b,m):
#     if a==b: return m%2==0
#     if m == 0: return 0
#     h = []
#     if a < b: h = [f(a+1, b, m-1), f(a+3, b, m-1)]
#     else: h = [f(a, b+1, m-1), f(a, b+3, m-1)]
#     return any(h) if (m-1)%2 == 0 else all(h)
#
# def f2(a,b,m):
#     if a==b: return m%2==0
#     if m == 0: return 0
#     h = []
#     if a < b: h = [f(a+1, b, m-1), f(a+3, b, m-1)]
#     else: h = [f(a, b+1, m-1), f(a, b+3, m-1)]
#     return any(h) if (m-1)%2 == 0 else any(h)
#
# print('19)', [s for s in range(1, 24) if f(13, s, 2)])
# print('20)', [s for s in range(1, 24) if not f(13, s, 1) and  f(13, s, 3)])
# print('21)', [s for s in range(1, 24) if not f(13, s, 2) and f(13, s, 4) and f2(13, s, 2)])

# def f(s, m):
#     if s >= 281: return m%2 == 0
#     if m == 0: return 0
#     nextWin = [f(s+4, m-1), f(s*2, m-1)]
#     return any(nextWin) if (m-1)%2 == 0 else all(nextWin)
#
# print('19) ', [s for s in range(1, 281) if f(s, 2)]) # 137
# print('20) ', [s for s in range(1, 281) if not f(s, 1) and f(s, 3)]) # 69, 70, 133, 134, 135, 136
# print('21) ', [s for s in range(1, 281) if not f(s, 2) and f(s, 4)]) # 129

# def f(s1, s2, m):
#     if 107 <= s1 + s2 <= 170: return m%2 == 0
#     if s1 + s2 > 170: return  m%2 != 0
#     if m == 0: return 0
#     nextWin = [
#         f(s1 + 4, s2, m - 1),
#         f(s1 * 2, s2, m - 1),
#         f(s1, s2 + 4, m - 1),
#         f(s1, s2 * 2, m - 1),
#     ]
#     return any(nextWin) if (m-1)%2 == 0 else all(nextWin)
#
# print('19) ', [s for s in range(1,101) if f(5, s, 2)]) # 26
# print('20.1) ', [s for s in range(1,101) if not f(5, s, 2) and f(5, s, 3)])
# print('20.2) ', [s for s in range(1,101) if f(5, s, 3)]) # 51, 25
# print('21) ', [s for s in range(1,101) if (f(5, s, 2) or f(5, s, 4)) and not f(5, s, 2)]) # 43, 44

# def f(s, m):
#     if s >= 100: return m%2 != 0
#     if m == 0: return 0
#     nextWin = [
#         f(s+2, m-1),
#         f(s+4, m-1),
#         # f(s*2, m-1)
#     ]
#     return any(nextWin) if (m-1)%2 == 0 else all(nextWin)
#
# print('19) ', [s for s in range(1, 100) if f(s, 1)]) # 94
# print('20) ', [s for s in range(1, 100) if f(s, 5) and f(s, 3) and f(s,1)]) # 94
# print('21) ', [s for s in range(1, 100) if not f(s, 1) and f(s, 3)]) # 94
