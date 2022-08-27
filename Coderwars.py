# """ больше нудя считаем кол-во , а меньше суммируем. если ноль то пусто"""


# def count_positives_sum_negatives(input):
#     if not input:
#         return []
#     count_ = 0
#     sum_ = 0
#     for element in input:
#         if element > 0:
#             count_ += 1
#         elif element < 0:
#             sum_ += element
#     return [count_, sum_]
#
#
# res = count_positives_sum_negatives([0, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14, -15])
# print(res)
#
# #**************************************************************
# """четное нечетное"""


# def even_or_odd(number):
#     return 'Odd' if number % 2 else 'Even'
#
#
# x = even_or_odd(24)
# y = even_or_odd(13)
# z = even_or_odd(21)
# t = even_or_odd(126)
# print(x, y, t, z)
#
# #***************************************************************************
# """ увеличиваем массив  в 2 раза """
# def maps(a):
#     y = []
#     for i in a:
#         y.append(i * 2)
#     return y
#
#
# x = maps([1, 2, 3, 4])
# print(x)

#*******************************************************************************

# """ перевернуть слово"""
#
#
# def solution(string):
#
#     # res = "".join(reversed(string))
#     """ ИЛИ """
#     res = string[::-1]
#     return res
#
#
# res = solution("world")
# res_2 = solution("word")
#
# print(res)
# print(res_2)

#*******************************************************************
# """Hello,{name} how are you doing today? Вивод строки"""
#
#
# def greet(name):
#
#     return f'Hello, {name} how are you doing today?'
#
#
# nam = greet("Zlata")
# nam_2 = greet("Klim")
# print(nam, '\n',nam_2)
#*****************************************************************************

# """
# min in masiv
# """
# def find_smallest_int(arr):
#     for item in arr:
#         return min(arr)
#
#
# res = find_smallest_int([1, -2, 27, 96, 2])
# print(res)

# def digitize(n):
#     return list(map(int, str(n)))[::-1]
#
#
# x = digitize(125635448)
# print(x)

# def merge_arrays(arr1, arr2):
#
#     new = set((set(arr1) - set(arr2)))
#     res = list(new) + arr2
#     res.sort()
#     return res
#
#
# x = merge_arrays([-1, 7, 3, 4], [-1, 5, 3, 4])
#
# print(x)
#
#
# def merge_arrays(arr1, arr2):
#
#     return sorted(set(arr1 + arr2))
#
#
# x = merge_arrays([-1, 7, 3, 4], [-1, 5, 3, 4])
# print(x)


# def last(lst):
#     if not lst:
#         return None
#     return lst[-1]
#
#
# res =last([1,2,3,4])
# print(res)

# def closest_multiple_10(i):
#     return round(i , -1)
#
#
# x = closest_multiple_10(14)
# print(x)

def ordered_count(inp):
    w = []
    return w.count(inp)


x = ordered_count("abracadabra")


print(x)



developer1 = {'Name': 'Zlata', 'City': 'LA', 'Skill': 'Python', 'Rate': 600, 'Phone': '+380631234573'}
developer2 = {'Name': 'Peter', 'City': 'Kyiv', 'Skill': 'Python', 'Rate': 1800, 'Phone': '+380631234567'}
developer3 = {'Name': 'Vlad', 'City': 'Kyiv', 'Skill': 'Python', 'Rate': 1300, 'Phone': '+380631234570'}
developer4 = {'Name': 'Ivan', 'City': 'Kyiv', 'Skill': 'Python', 'Rate': 2800, 'Phone': '+380631234572'}
developer5 = {'Name': 'Alex', 'City': 'Lviv', 'Skill': 'Python', 'Rate': 4800, 'Phone': '+380631234574'}

devs = [developer1, developer2, developer3, developer4, developer5]


def get_rate_stat(developers):
    rates = []
    stat = {"mean": None, "min": None, "max": None, "item_number": 0}
    for developer in developers:
        rate = developer['Rate']
        rates.append(rate)

    stat.update(
        {"mean": sum(rates) / len(rates),
         "min": min(rates),
         "max": max(rates),
         "item_number": len(rates)
         }
                )

    return stat