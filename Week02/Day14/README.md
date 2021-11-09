'''
## Day14

* 혼자 공부하는 파이썬 99p~105p

대소문자 바꾸기 : upper() 와 lower()

upper()함수는 문자열의 알파벳을 대문자로, l0wer()함수는 문자열의 알파벳을 소문자로 출력해준다.

>>>a = "Hello Python Programming...!"
>>>a.upper()
'HELLO PYTHON PROGRAMMING...!'
>>>a.lower()
'hello python programming...!'
    ※함수를 쓰면 문자열이 바뀔것이라생각하는데 절대 ㄴㄴ 원본은 그대로 유지.

문자열 양 옆의 공백 제거하기 : strip()

strip() : 문자열 양옆의 공백을 제거한다.
lstrip() : 문자열 왼쪽의 공백을 제거한다.
rstrip() : 문자열 오른쪽의 공백을 제거한다.

문자열의 구성 파악하기 : is땡땡()

isalnum() : 문자열이 알파벳 또는 숫자로만 구성되어 있는지 확인합니다.
isalpha() : 문자열이 알파벳으로만 구성되어 있는지 확인합니다.
isidentifier() : 문자열이 식별자로 사용할 수 있는 것인지 확인합니다.
isdecimal() : 문자열이 정수 형태인지 확인합니다.
isdigit() : 문자열이 숫자로 인식될 수 있는 것인지 확인합니다.
isspace() : 문자열이 공백으로만 구성되어 있는지 확인합니다.
islower() : 문자열이 소문자로만 구성되어 있는지 확인합니다.
isupper() : 문자열이 대문자로만 구성되어 있는지 확인합니다.

출력은 True(맞다) False(아니다)로 나오는데 이를 불(boollean)이라 부른다.

>>>print("TrainA10".isalnum())
True
>>>print("10".isdigit())
True

문자열 찾기 : find() 와 rfind()

문자열 내부에 특정 문자가 어디에 위치하였는지 확인할 때 쓰인다.

find() : 왼쪽부터 찾아서 처음등장하는 위치를 찾는다.
rfind() : 오른쪽부터 찾아서 처음 등장하는 위치를 찾습니다.

>>>output_a = "안녕안녕하세요".find("안녕")
>>>print(output_a)
0

>>>output_b = "안녕안녕하세요".rfind("안녕")
>>>print(output_b)
2

문자열과 in 연산자
>>>print("안녕" in "안녕하세요")
True

>>>print("잘자" in "안녕하세요")
False

문자열 자르기 : split()

문자열을 특정한 문자로 자를때는 split() 함수를 사용한다. 다음과 같은 예제에서는
split 함수 괄호 안의 문자열인 공백(띄어쓰기)을 기준으로 자른것이다.

>>>a = "10 20 30 40 50".split(" ")
>>>print(a)
['10', '20', '30', '40', '50']

format() : 숫자와 문자열을 다양한 형태로 출력할 수 있다.
upper()와 lower() : 문자열의 알파벳을 대문자 혹은 소문자로 변경.
strip() : 문자열 양 옆의 공백을 제거.
find() : 문자열 내부에 특정 문자가 어디에 위치하는지 찾을때 사용.
in연산자 : 문자열 내부에 어떤 문자열이 있는지 확인할 때 사용.
split() : 문자열을 특정한 문자로 자를 때 사용.

틀린문제

a = input("> 1번째 숫자: ")
b = input("> 2번째 숫자: ")
print()

print("{} + {} = {}".format(a, b, int(a), int(b))
'''
