# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
numbe0 = 10, 20, 30 """Packing"""
number1, number2 = 100, 200"""(Unpacking)"""
"""// 연산자 : 나눈 몫
– % 연산자 (modulus) : 나눈 나머지
– ** 지수승 : a**b → a의 b승"""
a,b= 1,2;
x,y=3,4;
divmod(a,b); """나누기 b 의 몫과 나머지르 계산"""
pow(x, y); """a 의 b승d"""

fullsec = int(input("5264: "))
hour = (fullsec // 60) // 60
minute = (fullsec // 60) % 60
seconds = fullsec % 60
print("%d초는" %fullsec, end=" ")
print("%d시간 %d분 %d초 입니다" %(hour, minute, seconds))


money = int(input("84756 : "))
m500 = money // 500
money %= 500
m100 = money // 100
money %= 100
m50 = money // 50
money %= 50
m10 = money // 10
money %= 10
print("500원 %d개, 100원 %d개, 50원 %d개, 10원 %d개" %(m500, m100,
m50, m10))


eval(“문자열”)

expression = input("일반 수식을 그대로 입력 : ") # 일반 수식을 문자열로 입력 받아 그대로 연산하기
answer = eval(expression)
print("결과 : %.2f" %answer)

theory= 90; practice= 85
decision = theory >= 90 and practice >=90
print(decision)

""" 흐름제어, 조건문(if,else), 반복문(for), 4칸 띄우기 (코드블록)tab, space;
"""

"""== 같은지 여부 !=다른지 여부비교 >,>=,< ,<= 두값의 크기를 비교  """
if  num1 > num2: """ 조건이 참일때 수행"""


age= int(input("15:")) #조건만족 할때 

if age >=14 :
    print("child")
print ("they are chindren")



number=int(input("27:")) # even odd 판별
if number%2  == 0: 
    print("even number")
print ("odd number")

price = float(input("20:"))#float 실수로 변환 가결 할인 행사에 다른 상품구입 가격 구하기
if price >= 10:
     discount = price * 0.2
else: 
    discount = price *0.1
final_price = price - discount 
print("최종가격 : %.2f만원" %final_price ) #뒤에있는 값을 앞으로 가져와 출력  f는 실수값 가져올때  d는 정수값 s 는 문자 