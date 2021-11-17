```

## Day21

* 혼자 공부하는 파이썬 163p~168p

딕셔너리 요소에 접근하기

# 딕셔너리를 선언합니다.
dictionary = {
    "name": "7D 건조 망고",
    "type": "당절임",
    "ingredient": ["망고", "설탕", "메타중아황산나트륨", "치자황색소"],
    "origin": "필리핀"
}

#출력합니다.
print("name:", dictionary["name"])
print("type:", dictionary["type"])
print("ingredient:", dictionary["ingredient"])
print("origin:" , dictionary["origin"])
print()

# 값을 변경합니다.
dictionary["name"] = "8D 건조 망고"
print("name:", dictionary["name"])

실행결과
name: 7D 건조 망고
type: 당절임
ingredient: ['망고', '설탕', '메타중아황산나트륨', '치자황색소']
origin: 필리핀

name: 8D 건조 망고


>>> dictionary["ingredent"]
['망고', '설탕', '메타종아황산나트륨', '치자황색소']
>>> dictionary["dictionary"][1]
'설탕'

딕셔너리의 문자열 키와 관련된 실수

>>> dict_key = {
    name: "7D 건조 망고",
    type: "당절임"
}
--->이러면 NameError가 발생한다. name이라는 이름이 정의되지 않았다는 것이다.
    type은 type()이라는 함수가 있어서 오류가 나지 않는다.

>>> name = "이름"
>>> dict_key = {
    name: "7D 건조 망고",
    type: "당절임"
}
>>> dict_key
{'이름': '7D 건조 망고', <class 'type'>: '당절임'}

딕셔너리에 값 추가하기/제거하기

딕셔너리[새로운 키] = 새로운 값

del dictionary로 제거도 가능

딕셔너리 요소 추가하기

# 딕셔너리를 선언합니다.
dictionary  = {}

# 요소 추가 전에 내용을 출력해 봅니다.
print("요소 추가 이전:", dictionary)

# 딕셔너리에 요소를 추가합니다.
dictionary["name"] = "새로운 이름"
dictionary["head"] = "새로운 정신"
dictionary["body"] = "새로운 몸"

# 출력합니다.
print("요소 추가 이후:", dictionary)

실행결과
요소 추가 이전: {}
요소 추가 이후: {'name' : '새로운 이름', 'head': '새로운 정신', 'body': '새로운 몸'}

딕셔너리 요소 제거하기

# 딕셔너리를 선언 합니다.
dictionary = {
    "name": "7D 건조 망고",
    "type": "당절임"
}

# 요소 제거 전에 내용을 출력해 봅니다.
print("요소 제거 이전:", dictionary)

# 딕셔너리의 요소를 제거합니다.
del dictionary["name"]
del dictionary["type"]

# 요소 제거 후에 내용을 출력해 봅니다.
print("요소 제거 이후:", dictionary)

실행결과
요소 제거 이전: {'name': '7D 건조 망고', 'type': '당절임}
요소 제거 이후: {}

KeyError
리스트의 길이를 넘은 인덱스에 접근하면 IndexError가 발생했었는데, 딕셔너리도 존재하지
않는 키에 접근하면 마찬가지로 KeyError가 발생한다.

>>> dictionary = {}
>>> dictionary["key"]
요러면 에러 발생

값을 제거할때도 존재하지 않는 키에 접근하면 에러발생
>>>del dictionary["key"]
오류발생
KeyError: 'key'

딕셔너리 내부에 키가 있는지 확인하기
리스트 때 처럼 똑같이 딕셔너리도 'in 키워드'를 사용한다.

# 딕셔너리를 선언합니다.
dictionary = {
    "name": "7D 건조 망고",
    "type": "당절임",
    "ingredient": ["망고", "설탕", "메타중아황산나트륨", "치자황색소"],
    "origin": "필리핀"
}

# 사용자로부터 입력을 받습니다.
key = input("> 접근하고자 하는 키: ")

# 출력합니다.
if key in dictionary:
    pirnt(dictionary[key])
else:
    print("존재하지 않는 키에 접근하고 있습니다.")

실행결과
> 접근하고자 하는 키: name
7D 건조 망고
> 접근하고자 하는 키: ㅇ ㅂ ㅇ
존재하지 않는 키에 접근하고 있습니다.

```