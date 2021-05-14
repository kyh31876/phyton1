# for variables in 변수할당가능한 자료:
#   문장1
#   문장2

for i in "테스트123":
    print(i) #문자 하나씩 받아와서 차례대로 반복출력 
l =['test',1,2,3] #4개의 요소를 가지고 있음 
for i in l:
    print(i)

tp1=(1,2,3)
for i in tp1:
    print(i)

tp2=[(1,2),(2,3),(4,5)]
for i in tp2:
    print(i)

    

# 구간의 범위를 알려준다 
for i in range(3): #0부터 3전까지 반복해준다 
    print(i)


for i in range(1,6):
    print(i)

for i in range(1,6,2): #1부터 6까지 2씩 증가 
    print(i)

for i in range(10): #0부터 9까지 수가 반복해 실행 
    print("Hello!")


for i in range(3): #i가 0,1,2 로 차례대로 반복 
    print(100) # i=0 100,200 i=1 100,200 i=2 100,200
    print(200)
print(300)


#도형 그리기 
import turtle as t 
for i in range(3):#triangle
    t.forward(100)
    t.left(120)

for i in range(4):#square
    t.forward(100)
    t.left(90)

#원그리기 
t.circle(50)

#구구단 3단 
for i in range(1,10): 
    third = ("3*%d = %d" %(i,3*i)) 
    print(third, end=",") #줄바꿈 없이 출력 


#구구단 2단부터 9단까지 
for i in range(2,10):
    for j in range(1,10):
        print(i*j,end=" ")
    print("\n") #반복 구문이끝났을떄 줄바꾸기 




# while 조건문: 
#   조건문이 참인경우 문장1


#for문 : 1.특정회수만큼 반복실행 
#       2.자료를 순서대로 할당 
#       3. for 변수 in  변수할당가능한 자료
#while문 :1.특정 조건을 만족하는 동안 반복 실행 
#        2.True/False로 논리적 검사를 진행   
#        3.while 조건문:

num =1 #먼저 변수를 정하기  print:1
while num < 5: #5보다 작을 동안 실행  
    print(num) 
    num =num+1 #변수를 업데이트 

#break문 
num =1
while num < 5: 
    print(num) 
    break #나오자마자 나간다.
    num =num+1 


#continue 
num =1 
while num < 5: 
    print(num) 
    num =num+1 
    continue #continue 뒤에껀 실행을 안시킨다. 
    num = num+10000


#출석확인 
num=0 
while num<10:
    num = num+1
    print("%d번 학생 출석 확인" %num)

for num in range(11):
    print("%d번 학생 출석 확인 " %num)


#if 문 
    #if 조건문1:
        #조건문 1이 참인경우 문장1 
        #조건문 1이 참인경우 문장2
    #elif: #조건문2:
        #조건문1이거짓 조건문2가 참인경우

    #else: #조건문1과 조건문2가 거짓일떄 실행되는 문장

#어떤값이 -5를 가질때 val이란 변수가 양수인지 음수인지 판정코드
val=-5
if val>0:
    print("양수")
elif val <0:   
    print("음수")
else: 
    print("0")


#모든 자료형은 불 자료형으로 변환 가능하다. 
#숫자형: 참(0이 아닌숫자) / 거짓(0인경우) 
#문자열: 참(1개 이상의 문자가 있는경우)/ 거짓(문자가 없는경우""")
#리스트,튜플,딕셔너리: 참(1개 이상의 값이 있는경우) / 거짓(값이 없는경우 )



#3천원있으면 버스, 3천원이 없으면 걸어가는 경우
money = True

if money:
    print("let take a bus")
else: 
    print("go on a walk")

a=10

if a>10:
    print(100)
else:
    print(200)

print(Data)

Data = ['name','address','email','FAX'] #원하는 뱐수가 있는지 사용할떄는 in 을이용할수 있다. 
if 'phone' in Data:
    print("call")
elif "email" in Data:
    print("send a Email")
else:
    print("visit")


# and / or 

# A and B : A 와 B 모두 참이여야 참이된다. 

# A or B : A또는 B 둘중 하나만 참이여도 참이된다. 

a=10
b=8

if a >=10 and b>= 8:
    print("AAA")
else: 
    pritn("BBB")


