#불자료형 (bool )
#참/거짓형 나태내는 논리연산 
# 0:거짓 1:참 
#False, True 대문자로써야된다

a=True 
print(a)

a=False
print(a)

print(type(a))

#str : 문자형 
#int : 정수형 
#float : 실수형(소수)

#비교연산자를 이용한 참/거짓 판단 
print(1==1) # 변수명 =정보, 왼족정보 == 오른쪽정보 

print(1<5) #비교연산자 왼쪽편을 기준으로 한다. 

print(2 in [1,2,3])
print(1<=5)
print(1>=5)
print(1==5) #왼쪽이랑 등호오른쪽이 다르냐

#모든 자료형은 참/거짓으로 판단가능
#숫자형(정수,실수): 참(0)이 아닌 숫자가 있을 경우  
#               거짓(0인경우)

#문자형 : 참(1개이상의 문자가 있을경우) 
#              거짓 (문자가 없는경우 "")
#리스트,튜플,딕셔너리 : 참(1개이상의 값이 있을경우)
#                거짓(값이없는경우 , [],{},()

#bool()함수를 이용하여 참/거짓을 판단 가능 

print(bool(0))
print(bool(123))

print(bool(""))
print(bool("abc"))

print(bool([1,2,3]))

# 집합자료형 (set): 집합에 관련된것을 쉽게처리하기 위해 만든 자료혈

s1 =set([1,2,3]) #set함수를 이용해 만든 set 자료형
print(type(s1))

#{key:function}: 딕셔너리 자료형
# {} 이용하여 집합자료형 생성가능 

s2={1,2,3}
print(type(s2))

s3=set("Hello")
print(type(s3))
print(s3)
# 집합자료형의 특징: 1 . 중복을 허용하지 않는다.
#               2. 순서가 없다.
#리스트,튜플 자료형 순서가 있기 때문에 인덱싱 사용가능 
#딕셔너리, 집합은 순서가 없기 때문에 인덱싱이 사용불가능하다. 

#집합은 중복을 제거하기 위한 필터역할로 종종 사용 
lists2=list(s2) #list 함수를 이용해 집합을 list 로 변환 
print(lists2[1])


s1=set([1,2,3,4,5,6])
s2=set([4,5,6,7,8,9])

print(s1,s2)

#교집합 
print(s1 & s2)
print(s1.intersection(s2))

#합집합
print(s1 | s2)
print(s1.union(s2))


#차집합 
print(s1-s2) #s1을 기준으로 s2와 다른값
print(s1.difference()s2)



#집합 자료형 관련 함수
s1=set([1,2,4])
s1.add(3) # 값을 하나 추가 
print(s1)

s1.update([5,6,7]) #값을 여러개 추가 
s1.remove(7) # 값을제거 
print(s1)