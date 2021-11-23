```

## Day28

* 혼자 공부하는 파이썬 190p~194p

문자열, 리스트, 딕셔너리와 관련된 기본 함수

지금까지 내용은 모든 프로그래밍 언어에서 대부분 유효한 내용이다.
하지만 반복문과 관련된 파이썬만의 기능들도 있다. 이 기능 들을 살펴보자.

리스트에 적용할 수 있는 기본 함수: min(), max(), sum()
리스트 뒤집기: reversed()
현재 인덱스가 몇 번째인지 확인하기: enumerate()
딕셔너리로 쉽게 반복문 작성하기: items()
리스트 안에 for문 사용하기: 리스트 내포

리스트에 적용할 수 있는 기본 함수: min(), max(), sum()

min(): 리스트 내부에서 최솟값을 찾는다.
max(): 리스트 내부에서 최댓값을 찾는다.
sum(): 리스트 내부에서 값을 모두 더한다.

>>>numbers = [103, 52, 273, 32, 77]
>>>min(numbers)
32
>>>max(numbers)
273
>>>sum(numbers)
537

이렇게도 가능
>>>min(103, 52, 273)
52
>>>max(103, 52, 273)
273

reversed()함수로 리스트 뒤집기

# 리스트를 선언하고 뒤집습니다.
list_a = [1, 2, 3, 4, 5]
list_reversed = reversed(list_a)

# 출력합니다.
print("# reversed() 함수")
print("reversed([1, 2, 3, 4, 5])):", list_reversed)
print("list(reversed([1, 2, 3, 4, 5])):", list(list_reversed))
print()

# 반복문을 적용해 봅니다.
print("# reversed() 함수와 반복문")
print("for i in reversed([1, 2, 3, 4, 5]):")
for i in reversed(list_a):
    print("-", i)

실행결과
# reversed() 함수
reversed([1, 2, 3, 4, 5]): <list_reverseiterator object at 0x031F21D0>
list(reversed([1, 2, 3, 4, 5])): [5, 4, 3, 2, 1]

# reversed() 함수와 반복문
for i in reversed([1, 2, 3, 4, 5]):
- 5
- 4
- 3
- 2
- 1

확장 슬라이싱
[::-1]

>>> numbers = [1, 2, 3, 4, 5]
>>> numbers
[1, 2, 3, 4, 5]
>>> numbers[::-1]
[5, 4, 3, 2, 1]

비파괴적 코드이므로 원본 numbers에는 영향이 없다. 이는 문자열에도 적용 가능

>>> "안녕하세요"[::-1]
'요세하녕안'

```