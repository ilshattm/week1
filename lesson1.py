#fest = "Hello"
#print(fest)
# is_hot = False
# is_cold = False
# if is_hot:
#     print("It's a hot day")
#     print("Drink plenty of water")
# elif is_cold:
#     print("It's a cold day")
#     print("Wear warm clothes")
# else:
#     print("It's a lovely day")
#
# print("Enjoy your day")
# def get_result(genre: str, time: int, cost: int):
#     if genre == 'comedy' or genre == 'horror' or genre == 'detective':
#         if time > 20:
#             if cost < 501:
#                print(f"You have a ticket at {time} and cost is {cost}")
#         else:
#            if cost < 301:
#                print(f"You have a ticket at {time} and cost is {cost}")
#     else:
#         print(f"You have other genre than  {genre} ")
#
#
# get_result('horror', 15, 300)

# for x in range(4):
#     for y in range(3):
#         print(f'({x}, {y})')
# numbers = [2, 2, 2, 2, 5]
# for i in numbers:
#     chart = ''
#     for j in range(i):
#         chart += 'x'
#     print(chart)
# names = ['John', 'Bob', 'Ilsh', "Mary", "Henry", "Gerd"]
# names[0] = "Jon"
# print(names[2:])
# print(names)
# names = [46, 26, 798, 345, 875, 748, 738, 374, 746]
# max_num = 0
# for i in names:
#     if max_num < i:
#         max_num = i
# names[0] = "Jon"
# print(names[2:])
# print(max_num)
numbers = [46, 26, 798, 345, 875, 748, 738, 374, 746]
# numbers.append(20)
numbers.insert(0, 234)
print(numbers)