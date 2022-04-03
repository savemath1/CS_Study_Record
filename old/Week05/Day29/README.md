```

## Day29

* 혼자 공부하는 파이썬 194p~196p

enumerate() 함수와 반복문 조합하기

현재 인덱스가 몇 번째 인지 확인하기.

예시)
example_list = ["요소A", "요소B", "요소C"]

0번째 요소는 요소A입니다.
1번째 요소는 요소B입니다.
2번째 요소는 요소C입니다.

이런결과를 출력하려면...

방법(1)
example_list = ["요소A", "요소B", "요소C"]
i = 0
for item in example_list:
 print("{}번째 요소는 {}입니다.".format(i, item))
 i += 1

방법 (2)
example_list = ["요소A", "요소B", "요소C"]
for i in range(len(example_list)):
    print("{}번째 요소는 {}입니다.".format(i, example_list[i]))

직접해보는 손코딩-enumerate() 함수와 리스트

# 변수를 선언합니다.
example_list = ["요소A", "요소B", "요소C"]

# 그냥 출력합니다.
print("# 단순 출력")
print(example_list)
print()

# enumerate() 함수를 적용해 출력합니다.
print("# enumerate() 함수 적용 출력")
print(enumerate(example_list))
print()

# list() 함수로 강제 변환해 출력합니다.
print("# list() 함수로 강제 변환 출력")
print(list(enumerate(example_list)))
print()

# for 반복문과 enumerate() 함수 조합해서 사용하기
print(" 반복문과 조합하기")
for i, value in enumerate(example_list):
    print("{}번째 요소는 {}입니다."format(i,value))

실행결과

# 단순 출력
['요소A', '요소B', '요소C']

# enumerate() 함수 적용 출력
<enumerate object at 0x02A43CB0>

# list() 함수로 강제 변환 출력
[(0, '요소A'), (1, '요소B'), (2, '요소C')]

# 반복문과 조합하기
0번째 요소는 요소A입니다.
1번째 요소는 요소B입니다.
2번째 요소는 요소C입니다.

```