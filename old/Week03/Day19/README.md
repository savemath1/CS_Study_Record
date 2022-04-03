```


## Day19

* 혼자 공부하는 파이썬 154p~159p

리스트 내부에 있는지 확인하기 : in/not in 연산자

값 in 리스트

in

>>>list_a = [273, 32, 103, 57, 52]
>>>273 in list_a
True
>>>99 in list_a
False
>>>100 in list_a
False
>>>52 in list_a
True

not in

>>>list_a = [273, 32, 103, 57,52]
>>>273 not in list_a
False
>>>99 not in list_a
True
>>>100 not in list_a
True
>>>52 not in list_a
False
>>>not 273 in list_a
False

(마지막처럼 in 연산자를 사용하고 전체를 not으로 감싸는 방법도 있지만, not in 연산자를 사용하는것이 훨씬 읽기 쉽다.)

for 반복문

print("출력")
print("출력")
print("출력")
print("출력")
print("출력")

복사하고 붙여넣기 해서 코드를 반복시킬수 있지만 반복량이 많아지면 이렇게 할수 없어진다.

for i in range(100):
    print("출력")

for 반복문 : 리스트와 함께 사용하기

for 반복자 in 반복할 수 있는 것:
    코드

# 리스트를 선언합니다.
array = [273, 32, 103, 57, 52]

# 리스트에 반복문을 적용합니다.
for element in array:
    # 출력합니다.
    print(element)

실행 결과
273
32
103
57
52

for 반복문은 문자열을 함께 사용할 수도 있다.

for character in "안녕하세요"
    print("-", character)


```