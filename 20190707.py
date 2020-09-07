##1
def solution(sentence):
    str = ''
    for c in sentence:
        if c != '.' and c != ' ':
            str += c
    size = len(str)
    for i in range(size // 2):
        if str[i] != str[size - 1 - i]:
            return False
    return True


sentence1 = "never odd or even."
ret1 = solution(sentence1)
print("solution 함수의 반환 값은", ret1, "입니다.")

sentence2 = "palindrome"
ret2 = solution(sentence2)

# [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret2, "입니다.")

##2-1
for x in range(5):
    for i in range(4-x):
        print(" ", end='')
    for j in range(2*x+1):
        print("*", end='')
    print()

##3
string1 = "!edoc doog a tahW\n"
string2 = ""
for x in string1:
    string2 = x + string2
print(string2)
