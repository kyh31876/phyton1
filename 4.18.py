# "+" 연산은 문자열 연결
# "*" 연산은 문자열 반속
# "\" 연산은 현재 라인과 다음라인을 연결 \



# in keyword: data 내부의 요소의 존재를 확인 

# not in keyword 요소가 내부에 포함되지않음을 확인 


# data 형의 변환 
#int()# 문자열 형태의 숫자를 정수형으로 변환 

#float(): 문자열 형태의 숫자나정수를 실수로 변환 

#str() : 숫자데이터를 문자열로


#임의의 문자열을 입력받아 문자와 숫자의 개수 구하기
nchar =0; ndigit=0; nother=0;
massage= input("문자열 입력:")

for letter in message:
    if 'A' <= letter <= 'Z' or 'a' <= letter <= 'z':
        nchar += 1 
    elif '0' <= letter <= '9':
        ndigit +=1
    else:
        nother +=1

print("문자:%d개" %nchar)
print("숫자:%d개" %ndigit)
print("기타:$d개" %nother )


#문자열의 중간에 있는 문자를 출력하기

word = input("문자열을 입력:")
length =len(word)

if length % 2==1:
    letter=word[length//2]
    print("중간글자: %s" %letter)
else:
    letter1=word[(length//2)-1]
    letter2=word[(length//2)]
    print("중간글자: %s" %(letter1+letter2))

#입력된 문자를 거꾸로 읽기 
message=input("문자를 입력하세요:")
print(message[::-1])


#slicing 
## 인덱스 범위 내에서 순차 자료의 일부를 추출하는 것
##슬라이싱의 결과에서 마지막 인덱스 요소는 포함되지 않음
##결과는 원래의 자료형과 같으며 , 문자열은 새로운 객체로 인식

#stingObject[start:end:step]
#str_obj: 문자열 object 이름 
#start: 시작index 
#end: 마지막index 


