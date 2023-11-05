# Исполнитель преобразует число на экране.
# У исполнителя есть три команды, которые обозначены латинскими буквами:
# A. Прибавить 1
# B. Прибавить 3
# C. Умножить на 3
# Программа для исполнителя – это последовательность команд.
# Сколько существует программ,
# для которых при исходном числе 3 результатом является число 31,
# при этом траектория вычислений содержит одновременно и число 9, и число 27?
# Траектория вычислений программы –
# это последовательность результатов выполнения всех команд программы.
# Например, для программы CBA при исходном числе 7 траектория будет состоять из чисел 21, 24, 25.

# def f(start, end):
#     if start > end:
#         return 0
#     elif start == end:
#         return 1
#     return f(start + 1, end) + f(start + 3, end) + f(start * 3, end)
# print(f(3,9) * f(9,27) * f(27, 31))

# Чисто проверка на дауна

# Исполнитель преобразует число на экране. У исполнителя есть три команды, которые обозначены латинскими буквами:
# А. Вычесть 1
# В. Вычесть 3
# С. Найти целую часть от деления на 2
# Программа для исполнителя — это последовательность команд.
# Сколько существует программ,
# для которых при исходном числе 19 результатом является число 3, п
# ри этом траектория вычислений не содержит числа 7 и содержит 10?
# Траектория вычислений программы — это последовательность результатов выполнения всех команд программы.
# Например, для программы СВА при исходном числе 13 траектория будет состоять из чисел 6, 3, 2.

# def f(start, end):
#     if start < end or start == 7:
#         return 0
#     if start == end:
#         return 1
#     if start > end:
#         return f(start - 1, end) + f(start - 3, end) + f(start // 2, end)
#
#
# print(f(19, 10) * f(10, 3))

popast = 21
ne_popast = 15

def f (start, end):
    if start > end or start == ne_popast:
        return 0
    if start == end:
        return 1
    return f(start+1, end) + f(start+2, end) + f(start*3, end)
# print(f(6, popast) * f(popast, 25))
print(1320+1380)