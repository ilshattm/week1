# price_home = 1000000
# good_credit = False
# if good_credit:
#     down_payment = price_home * 0.1
# else:
#     down_payment = price_home * 0.2
# print(f"Down payment ${down_payment}")
#has_high_income = False
# has_good_credit = True
# has_creminal_record = False
# if has_good_credit and not has_creminal_record:
#     print("Eligible for loan")
# temperature = 36
# if temperature > 30:
#     print("It's a hot day")
# else:
#     print("It's a not hot day")
# --------------------------------------------
# name = input("write your name: ")
# name_count = len(name)
# if name_count < 3:
#     print("Your name must be at 3 characters")
# elif name_count > 50:
#     print("Your name can be  a maximum of 50 characters")
# else:
#     print("Your name look good")
# ----------------------------------------
# convrter kg to lbs or lbs to kg
# weight = input("Weight: ")
# weight = float(weight)
# defind = input("(L)bs or K(g): ")
# q = ord(defind)
# if q == 75:
#     weight = int(weight / 0.45)
#     print("Weight in Lbs: ",weight)
# elif q == 76:
#     weight = int(weight * 0.45)
#     print("Weight in Kg: ", weight)
# i = 1
# p = False
# while i < 4:
#     g = int(input("Guess "))
#     if g == 9 and p == False:
#         print("You win")
#         p = True
#         i = 4
#
#
#     else:
#         i += 1
#
#
# if p == False:
#     print("Wrong")
# else:
#     pass

#######################################
# command = input(">")
# i = 0
# j = 0
# while command != "quit":
#
#     if command == "help":
#         print("start -  to start  the car ")
#         print("stop -  to stop  the car ")
#         print("quit -  to exist ")
#     elif command == "start":
#         if i == 0:
#             print("Car started ... Ready to go!")
#             i +=1
#         else:
#             print("Car was started ...")
#     elif command == "stop":
#         if i == 0:
#             print("Car stoped.")
#             i += 1
#         else:
#             print("Car was stoped ...")
#
#     else:
#         print("I dont understand that ...")
#     command = input(">")

##############################################
# price = [10, 20, 30]
# aver = 0
# for i in price:
#     aver = aver + i
#
# print(aver)

def buy_car(model: str, year: int, usage: int, color: str, owner: int, price: float, left_wheel: bool):
    model_upper = model.upper()
    color_upper = color.upper()
    return (
        model_upper in ['LEXUS', 'TOYOTA']
        and year > 2003 and color_upper in ['WHITE', 'GREY']
        and owner < 3 and left_wheel == True
        and usage < 150001 and price < 10001
        or (
        model_upper in ['LEXUS', 'TOYOTA'] and year > 2003 and color_upper in ['WHITE', 'GREY']
        and owner < 3 and left_wheel == True and usage > 199999 and price < 8001
         )


    )

p = buy_car('toyota', 2014, 10000, 'grey', 2, 500.9, True)
print(p)