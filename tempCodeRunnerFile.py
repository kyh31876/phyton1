nation =[]
while TRUE:
    name=input("국가를 입력 (종료:exit):")
    if name == "exit":
        break
    if name in nation:
        print("중복된 국가가 존재합니다")
        print("다시입력 하세요 ")
        continue
    nation.append(name)
print("국가 :", nation)
