# arr = [1, 2, -4, 56, 8, 89, 77, 23, 4, 22]
# max = arr[0]
# sum = 0
# for i in arr:
#     if max < i:
#         max = i
#     sum += i
# print(max, sum)

arr = [10, 65, 100, 30, 95]
average = 0
for i in range(len(arr)):
    average = average + arr[i]
average = average / len(arr)
print(average)



#
def solution(arr, k):
    answer = 0
    temp =[]
    for a in arr:
        for b in a:
            temp.append(b)
    temp.sort()
    answer = temp[k-1]
    return answer

print(solution([[3,5,6,9],[11,7,1,4],[0,14,12,8]],4))

# def money(price, money):
#     answer = 0
#     total = 0
#     for i in price:
#         total += i
#     answer = money - total
#     return answer
#
# print(money([2100,3200,2100,800], 10000))
# print(money([1000,2000,3000,500], 7000))

# def findmin(data):
#     total = 0
#     for i in data:
#         total += i
#     cnt = 0
#     avg = total // len(data)
#     for i in data:
#         if i < avg:
#             cnt += 1
#     return cnt
#
# print(findmin([1,2,3,4,5,6,7,8,9,10]))

def find(scores):
    grade = [0 for i in range(5)]
    for i in scores:
        if i >= 85:
            grade[0] += 1
        elif i >= 70:
            grade[1] += 1
        elif i >= 55:
            grade[2] += 1
        elif i >= 40:
            grade[3] += 1
        else:
            grade[4] += 1

print(find([43,15,73,82,56,29,93]))

