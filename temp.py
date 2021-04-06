# -*- coding: utf-8 -*-
"""
Spyder Editor
This is a temporary script file.
"""
numbe0 = 10, 20, 30 #Packing
number1, number2 = 100, 200 #(Unpacking)
# % 연산자 (modulus) : 나눈 나머지
# // 연산자 : 나눈 몫
# ** 지수승 : a**b → a의 b승
a,b= 1,2;
x,y=3,4;
divmod(a,b); #나누기 b 의 몫과 나머지르 계산
pow(x, y); #a 의 b승d

fullsec = int(input("5264: ")) #왼쪽이 함수 오른쪽이 넣는값
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


# eval(“”) 

expression = input("일반 수식을 그대로 입력 : ") # 일반 수식을 문자열로 입력 받아 그대로 연산하기
answer = eval(expression)
print("결과 : %.2f" %answer)

theory= 90; practice= 85
decision = theory >= 90 and practice >=90
print(decision)

# 흐름제어, 조건문(if,else), 반복문(for), 4칸 띄우기 (코드블록)tab, space;


# == 같은지 여부 !=다른지 여부비교 >,>=,< ,<= 두값의 크기를 비교  
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

hours =float(input("9:")) #근무시간 7시간이넘을 경우 ,넘은시간에 대해 시간당 임금을  50%추가
pay = 8000

if hours >7:
    salary = pay * hours
    salary = salary + (pay *(hours-7))* 0.5
else:
    salary =pay*hours
    print(" 임금: %.2f원" %salary)
    

# end(&) or(|) 
    
score =int(input(":"))    #  학점출력 코드
if 90 <= score <= 100:
    print("A")
elif 80 <= score <90:
    print("B")
elif 70 <= score <= 80:
    print("C")
    else print("F")
    
month = int(input("4:")) # 달의 일수 구하기 

if month == 2:
    print("28일")
elif month == 4 or month ==6 or month ==9 or month == 11:
    print("30일")
else: print("31일")

#0 ~ 24시간 중 하나를 입력받아 인사하기 
nowtime = int(input("지금 시간은 (0-24): "))
if nowtime > 12: 
    hour1 = nowtime/2 
print ("현재시간 %d 시간 입니다." %(hour1))






# 미터단위 를 피트단위로 변환 
d_ft = int(input("피트입 : "))
d_meter = d_ft * 3.28
print("피트는 %d미터 입니다. ." %(d_meter))

d_mt = int(input("미터 입력 : "))
d_feet = d_mt * 0.3048
print("미터는 %d 피트 입니다." %(d_feet))
print("The distance in miles is %.2f miles." % d_miles)

#사칙연산 계산하기 


print("1.+, 2.-, 3.*, 4./")

menu = int(input("메뉴선택 : "))
num1 = input("First Number:\n")

operator = input("Operator (+, -, *, /):\n")
num2 = input("Second Number:\n")

num1 = float(num1)
num2 = float(num2)

out = None

if operator == "+":
    out =  num1 + num2
elif operator == "-":
    out = num1 - num2
elif operator == "*":
    out = num1 * num2
elif operator == "/":
    out = num1 / num2
print("Answer: " + str(out))
    
#while 문의 조건식이 참인 동안 코드블록문장을 계속반복, 거짓이면 while  문을 빠져나감.

count = 1# 특정횟수만큼 반복
while count <= 10:
    print("hello python")
    count +=1
    
count = 1 #무한루프 ,조건이 무조건 참
while Ture:  #참임
    print("hello phthon")
    if count == 10: #조건빠져나오기
        break #if 문에걸린 브레이크
    count +=1
    
    
    #1부터 10까지 합구하기 
total = 0
count = 1 
while count <= 10:
    total += count  #일반항 
    count += 1 # count = count + 1, 반복 
print("합 :", total)


# 키보드로 입력한 수를 차례로 누적하여 합구하기 
total =0 
while True:
    number = input(int("수를 입력 (0: 종료):")) #값입력 
     if number == 0: 
        break
    total += number 
print ("수" , total)
    

#학생 10명의 점수로 합격 불합격자수 구하기
passes= 0; failure = 0 
count = 1 
while count <= 10: 
    score = int(input("학생 점수를 입력 :"))
    if  score >= 80: 
        passes += 1
    else: 
        failure += 1
        
print(" 합격 : %d,  불합격 : %d" %(passes, failure ))


# while 문에서  else 문  사용이 가능함 

count = 1
while count <= 5:
    if count == 3:  
        break
    print ("python", count)
    count += 1
else: 
    print ("감사합니다.")
    
count = 1
while count <= 5: 
    print ("python", count)
    count += 1 
else: #모든 반복을 다 수행 했을 경우  else 수행 
    print("감사합니다.")


# BMI 측정하기 
 
while True: #계속반복
    print("비만도 판정")
    height = float(input("신장(m)은 ?":))
    weight = float(input("체중(Kg)은 ?":))
    BMI = weight/pow(height,2)
    if BMI < 18.5:
        print("마름")
    elif 18.5 <= BMI < 25:
        print("표준")
else:
    print("비만")
대답= input("계속?") #대답
    if 대답 == "n" :
        break
