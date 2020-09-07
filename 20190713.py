# def find(string):
#     if 'a' in string:
#         return True
#     elif 'e' in string:
#         return True
#     elif 'i' in string:
#         return True
#     elif 'o' in string:
#         return True
#     elif 'u' in string:
#         return True
#     else:
#         return False
#
# string = 'crwth'
# print(find(string))
# string2 = 'apple'
# print(find(string2))
#
#
# def findbig(A, B):
#     if A > B:
#         print("A is big")
#     elif A < B:
#         print("B is big")
#     else:
#         print("A equals B")
#
# print(findbig(10, 3))
# print(findbig(5,14))
# print(findbig(6,6))

# def score(sco):
#     if 90 <= sco <= 100:
#         print("A")
#     elif 80 <= sco < 90:
#         print("B")
#     elif 70 <= sco < 80:
#         print("C")
#     elif 60 <= sco < 70:
#         print("D")
#     else:
#         print("F")
#
# score(14)
# score(97)
# score(75)
#
# def finds(year):
#     if (year % 4 == 0) and((year % 100 != 0) or ( year % 400 == 0)):
#         print("윤년입니다.")
#     else:
#         print("윤년이 아닙니다.")

with open("basic.txt", "w") as file:
    file.write("Hello Python Programming")
    file.write("Let's do it")
    file.write("Bye")
    file.close()

with open("basic.txt", "r") as file:
    contents = file.read()
    print(contents)
    file.close()

with open("basic.txt", "r") as file:
    for x in file:
        print(x)
    file.close()







