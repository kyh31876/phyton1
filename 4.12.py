#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 12 16:08:48 2021

@author: tetsuyaariake
"""


#리스트는 그값의 생성 삭제 수정이 가능, 튜플은 그값을 수정할수 없음 

#string (" ",' ',""" """,''' ''')
# "안쪽내용에 작은 따옴표가 필요할떄"
# ' 안쪽내용에 큰 따옴표가 필요할떄' 

t1 = ('a' ,'b' , ('c', 'd'))

print("he siad")
print("AAAAAA \n BBBBBB") #한줄 띄우기 
print("AAAAAA BBBBBB") 
print("""AAAAAAA
      BBBBBBBB""")

# 
#escape code : 프로그레밍을 할떄 사용할수있도록 미리 정의해둔 문자조합
# \n : 줄바꿈
# \t : 문자열사이 간격 탭으로 조정 
# \\ : 문자열에 \ 그대로 입력하고 싶을떄 
# \' : 문자열에 '를 그대로 입력하고 싶을떄 
# \" : 문자열에 "를 그대로 입력하고 싶을떄 

a="my"
b="name"
c = "is"
d = "ASW"
print(a+b+c+d)
len(a)

#문자열의 인덱싱과 슬라이싱 
a="apple"

print(a[:3])


#문자열 나누기 
a = "20200412Sunny"
print(a[1:4])

data= a[:8] 
weather = a[8:]
print(data)
print(weather)

#문자열 일부 수정 
a= "panana"

c= "b" + a[1:]
print(c)

#문자열의 format 
tem =20 
print("Today`s temperature is %d degree celsius" %tem)#tem이라는 변수의 값이 %d에들어간다

wea='sunnuy'
print("Today`s temperature is %s degree celsius" %wea)

tem =20 
wea='sunnuy'

print("Today`s temperature is %d %s degree celsius" %(tem, wea))

# %s 문자열 받아오기 
# %d 정수형 받아오기
# %.nf 실수 n 자리까지 받아오기 
# %o 8진수 
# %x 16진수 


#특수한 문자의 갯수 세기 
a= "apple"
print(a)
print(a.count('p'))
print(a.count('k'))

#문자의 위치1 
a="Gundamm"
print(a.find("G")) #index number
print(a.find("m")) #여러개있더라도 가장먼저나오는 인덱스 알려줌 
print(a.find("j")) #없는 문자는 -1로 반환 


#문자의 위치2 
print(a.index("G"))
print(a.index("m"))
print(a.index("j")) #없는문자를 출력하면 오류발생 

# a-b-c-d
print('-'.join('abcd')) #abcd 사이에 - 이 들어간다 

print('&'.join(['a','b','c','d']))

#소문자 -> 대문자 
a= "apple"
print(a)
print(a.upper()) #대문자로 변환됨 
print(a.lower()) #소문자로 변환 

#문자열의 공백 삭제방법
#문자열의 왼쪽의 공백 (lstrip)

#문자열의 오른쪽의 공백 (rstrip)

#문자열의 왼쪽과 오른쪽의 모두 공백을 삭제 (strip)


a="My name is AAA"
print(a.strip())


#문자열바꾸기 (replace)
a="My name is AAA" 
print(a.replace('name','phone number')) #name을 phone number로 바꾸겟다


#문자열 나누기 (split)
print(a.split()) #빈칸으로 나누기

a='a*b*c*d'
print(a.split('*'))