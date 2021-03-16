

divmod(a,b); #a나누기 b 의 몫과 나머지르 계산
pow(x, y); # a 의 b승

fullsec1 = int(input(divmod(100, 60))); #전체 초단위 분으로 변경 


fullsec= int(input("5234"))
hour = (fullsec // 60) // 60
minute =(fullsec // 60) % 60
seconds = fullsec % 60
print("$d초는" %fullsec, end="")
print("%d시 %d분 %d초 입니다" %(hour ,minute, seconds)) # %d int값가져오기  d: int f: real s: string. 

money =int(input("7890 : "))
500w = money // 500
money= money % 500
100w = money // 100
money = money % 100 
50w = money // 50 
money = money % 50 
10w = money //10 
money = money % 10
print("500원 %d개, 100원 %d개, 50 원 %d개, 10원 %d개" %(500w, 100w ,50w, 10w))

eval("") #문자형 expression 을 str타입으로 바꿈

