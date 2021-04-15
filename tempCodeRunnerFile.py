total = 0
while True:
    number = int(input("수를 입력(0: 종료):")) #값입력 
    if number == 0: 
        break
    total += number 
print ("합:"  total)
