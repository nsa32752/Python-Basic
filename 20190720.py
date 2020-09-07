# test = ['one','two','three']
# for i in test:
#     print(i)
#
#
marks = [90, 25, 67, 45, 80]
number = 0
for mark in marks:
    number = number +1
    if mark >= 60:
        print(str(number) + "번 학생은 합격입니다.")
    else:
        print(str(number) + "번 학생은 불합격입니다.")

        
for x in range(11,1,-1):
    print(x)

# fruits = ['apple', 'banana', 'melon', 'grape', 'orange']
# for x in fruits:
#     if len(x) >= 6:
#         continue
#     print(x)
#
# print(list(range(10)))

# for i in range(2, 10):
#     for j in range(1, 10):
#         print(str(i), "x", str(j), "=", i*j)

# num = 1
# while num != 0:
#     num = int(input("입력 : "))
#     if num != 0:
#         print("0이 아닙니다. 다시 입력해주세요.")

# coffee = 10
# money = 300
# while money:
#     print("돈을 받았으니 커피를 줍니다.")
#     coffee = coffee -1
#     print("남은 커피의 양은 %d개입니다." % coffee)
#     if coffee == 0:
#         print("커피가 다 떨어졌습니다. 판매를 중지합니다.")
#         break

# num = 1
# sum = 0
# while num <= 1000:
#     if num % 3 == 0:
#         sum += num
#     num += 1
# print(sum)

# A = [70, 60, 55, 75, 95, 90, 80, 80, 85, 100]
# sum = 0
# for x in A:
#     sum += x
# print(sum / 10)

# numlist = [3, 29, 38, 12, 57, 74, 40, 85, 61]
# index = 1
# minimum = 0
# minindex = 0
# for x in numlist:
#     if x > minimum:
#         minimum = x
#         minindex = index
#     index += 1
# print(minimum, minindex)
#
# def fillwith_(sentence):
#     new_sentence = ''
#     for char in sentence:
#         if char == ' ':
#             char = '_'
#         new_sentence += char
#     return new_sentence
#
# print(fillwith_('아름다운 가을 단풍 구경하러 산으로 갑시다.'))
