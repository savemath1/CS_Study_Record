```

## Day23

* 혼자 공부하는 파이썬 126p~137p (첫번째 복습)

03-2 if~else와 elif구문

if조건문은 뒤에 else 구문을 붙여서 사용할 수 있다. 이처럼 if 구문 뒤에 else 구문을 붙인 것을 'if else 조건문'이라고 부른다. 그럼 어떠한 경우에 사용하는 조건문인지 알아보자.

# 입력을 받습니다.
number = input("정ㅅ 입력> ")
number = int(number)

# 짝수 조건
if number % 2 == 0:
    print("짝수입니다")

# 홀수 조건
if number % 2 == 1:
    print("홀수입니다")

이처럼 if를 두번쓰는 것은 낭비다.
그러므로 아래와 같이 한다.

# 입력을 받습니다.
number = input("정수 입력> ")
number = int(number)

# 조건문을 사용합니다.
if number %2- 2 == 0:
    # 조건이 참일 때, 즉 짝수 조건
    print("짝수입니다")
else:
    # 조건이 거짓일 때, 즉 홀수 조건
    print("홀수입니다")

요로케 한다.

형태
if 조건:
    조건이 참일 때 실행할 문장
else:
    조건이 거짓일 때 실행할 문장

그런데 딱 두가지만으로 구분되지 않는 것도 있다. 예를 들어 계절 이나 요일이다.
따라서 세 개 이상의 조건을 연결해서 사용하는 방법이 필요하다. 그것이 바로
'elif구문' 이다.

형태
if 조건A:
    조건A가 참일 때 실행할 문장
elif 조건B:
    조건B가 참일 때 실행할 문장
elif 조건C:
    조건C가 참일 때 실행할 문장
...
else:
    모든 조건이 거짓일 때 문장

예시를 함 보면...

# 변수를 선언합니다.
score = float(input("학점 입력> "))

# 조건문을 적용합니다.
if score == 4.5:
    print("신")
elif 4.2 <= score:
    print("교수님의 사랑")
elif 3.5 <= score:
    print("현 체재의 수호자")
elif 2.8 <= score:
    print("일반인")
elif 2.3 <= score:
    print("일탈을 꿈꾸는 소시민")
elif 1.75 <= score:
    print("오락 문화의 선구자")
elif 1.0 <= score:
    print("불가촉천민")
elif 0.5 <= score:
    print("자벌레")
elif 0 < score:
    print("플랑크톤")
else:
    print("시대를 앞서가는 혁명의 씨앗")

실행결과
학점 입력> 3.2
일반인

요런거다.

False로 변환 되는 값 : None, 숫자 0과0.0, 빈 컨테이너(빈 문자열, 빈 바이트열, 빈 리스트, 빈 튜플, 빈 딕셔너리 등)

이외에는 모두 True로 변환 되므로 위에 언급한 세가지만 기억하자.

pass 키워드

형태

if zero == 0:
    빈줄 삽입
else:
    빈줄 삽입

pass키워드 사용 형태

# 입력을 받습니다.
 number = input("정수 입력> ")
 number = int(number)

# 조건문 사용
if number > 0:
    # 양수일 때: 아직 미구현 상태입니다.
    pass
else:
    # 음수일 때: 아직 미구현 상태입니다.
    pass

```