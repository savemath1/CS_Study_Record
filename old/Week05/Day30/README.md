```

## Day30

* 혼자 공부하는 파이썬 196p~197p

딕셔너리의 items()함수와 반복문 조합하기

enumerate() 함수와 반복문을 조합해서 for i,value in enumerate(리스트) 형태로 반복문을
작성할 수 있었던 것처럼 딕셔너리는 items() 함수와 함께 사용하면 키와 값을 조합해서
쉽세 반복문을 작성 할 수 있다.

직접 해보는 손코딩

딕셔너리의 items() 함수와 반복문

# 변수를 선언합니다.
example_dictionary = {
    "키A": "값A",
    "키B": "값B",
    "키C": "값C",
}

# 딕셔너리의 items() 함수 결과 출력하기

print("# 딕셔너리의 items() 함수")
print("items():", example_dictionary.items())
print()

# for 반복문과 items() 함수와 조합해서 사용하기
print("# 딕셔너리의 items() 함수와 반복문 조합하기")

for key, element in example_dictionary.items():
    print("dictionary[{}] = {}".format(key, element))

실행결과
# 딕셔너리의 items() 함수
items(): dict_items([('키A', '값A'), ('키B', '값B'), ('키C', '값C')])

딕셔너리의 items() 함수와 반복문 조합하기
dictionary[키A] = 값A
dictionary[키B] = 값B
dictionary[키C] = 값C

```