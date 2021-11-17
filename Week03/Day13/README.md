## Day13

* 혼자 공부하는 파이썬 92p~99p

문자열 뒤에 마침표(.)를 입력해 보면 자동 완성 기능으로 다양한 것들이 나온다.
이것들은 모두 문자열이 가지고 있는 자체적인 기능이다.

문자열의 format()함수
숫자를 문자열로 변환한다.
>>>string_a = "{}".format(10)
>>>print(string_a)
>>>print(type(string_a))

실행결과
10
<class 'str'>

>>>format_a = "{}만 원".format(5000)
>>>format_b = "파이썬 열공하여 첫 연봉 {}만 원 만들기".format(5000)
>>>format_c = "{} {} {}".format(3000, 4000, 5000)
>>>format_d = "{} {} {}".format(1, "문자열", True)

>>>print(format_a)
>>>print(format_b)
>>>print(format_c)
>>>print(format_d)

실행결과
5000만 원
파이썬 열공하여 첫 연봉 5000만 원 만들기
3000 4000 5000
1 문자열 True

에러 예외
>>>"{}" "{}".format(1, 2, 3, 4, 5)
'1 2'

>>>"{} {} {}".format(1, 2)
에러 발생

(매개변수가 {}보다 많으면 {}개수만큼 적용되고 나머지 매개변수는 버려진다.
그러나 {}가 매개변수보다 많으면 에러가 발생한다.)

format()함수의 다양한 기능

1.정수 출력의 다양한 형태

>>># 조합하기
>>>output_h = "{:+d}".format(52)    #기호를 뒤로 밀기:양수
>>>output_i = "{:+5d}".format(-52)  #기호를 뒤로 밀기:음수
>>>output_j = "{:=+5d}".format(52)  #기호를 앞으로 밀기:양수
>>>output_k = "{:=+5d}".format(-52) #기호를 앞으로 밀기:음수
>>>output_l = "{:+05d}".format(52)  #0으로 채우기:양수
>>>output_m = "{:+05}".format(-52)  #0으로 채우기:음수

>>>print("# 조합하기")
>>>print(output_h)
>>>print(output_i)
>>>print(output_j)
>>>print(output_k)
>>>print(output_l)
>>>print(output_m)

실행결과
#조합하기
  +52
  -52
+  52
-  52
+0052
-0052

2.부동 소수점 출력의 다양한 형태

 float자료형 기본
>>>output_a = "{:f}".format(52.273)
>>>output_b = "{:15f}".format(52.273)
>>>output_c = "{:+15f}".format(52.273)
>>>output_d = '{;=015}".format(52.273)

>>>print(output_a)
>>>print(output_b)
>>>print(output_c)
>>>print(output_d)

실행결과
52.273000
      52.273000
     +52.273000
+0000052.273000

 소수점 아래 자릿수 지정하기
>>>output_a = "{:15.3f}".format(52.273)
>>>output_b = "{:15.2f}".format(52.273)
>>>output_c = "{:15.1f}".format(52.273)

>>>print(output_a)
>>>print(output_b)
>>>print(output_c)

실행결과
        52.273
         52.27
          52.3  (※자동으로 반올림 된다.)

 의미없는 소수점 제거하기
>>>output_a = 52.0
>>>output_b = "{:g}".format(output_a)
>>>print(output_a)
>>>print(output_b)

실행결과
52.0
52