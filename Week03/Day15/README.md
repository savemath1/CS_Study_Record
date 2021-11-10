```

## Day15

* 혼자 공부하는 파이썬 108p~125p

'불'
숫자와 문자열은 만드는 형태에 따라 무한에 가까운 종류를 만들수 있었다.
하지만 불은 오직 True Flase 이 값만 가질수 있다.

>>>Print(True)
True
>>>print(False)
False

비교 연산자
== 같다
!= 다르다
< 작다
> 크다
<= 작거나 같다
>= 크거나 같다

>>>print(10 == 100)
False
>>>print(10 != 100)
True
>>>print(10 < 100)
True
>>>print(10 > 100)
False
>>>print(10 <= 100)
True
>>>print(10 >= 100)
False

문자열도 비교연산자 가능
(사전 순서)
>>>print("가방" == "가방")
True
>>>print("가방" != "하마")
True
>>>print("가방" < "하마")
True
>>>print("가방" > "하마")
False

>>> x = 25
>>> print(10 < x < 30)
True
>>> print(40 < x < 60)
False

불 연산하기 : 논리 연산자

not
and
or

if 조건문
(if의 조건문 뒤에는 반드시 콜론(:)을 붙여줘야 한다.
 if다음 문장은 4칸 들여쓰기 후 입력.->탭1=띄어쓰기4)

 if 불 값이 나오는 표현식:
    볼 값이 참일 때 실행할 문장
    불 값이 참일 때 실행할 문장

#입력을 받습니다.
number = input("정수 입력> ")
number = int(number)

#짝수 조건
if number % 2 == 0:
    print("짝수입니다")

#홀수 조건
if number % 2 == 1:
    print("홀수입니다")

예제 문제

a = float(input("> 1번째 숫자: "))
b = float(input("> 2번째 숫자: "))
print()

if a > b:
    print("처음 입력했던 {}가 {}보다 더 큽니다.".format(a,b))
if a < b:
    print("두 번째로 입력했던 {}가 {}보다 더 큽니다.".format(b,a))

실행결과
> 1번째 숫자 : 100
> 2번째 숫자 : 10

처음 입력했던 100.0가 10.0보다 더 큽니다

```