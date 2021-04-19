names =[] 
name_str = input("다섯명 이름 입력 :") 
name_str.split()


rmv=input("삭제할 이름입력 :")
if rmv in names:
    names.remove(rmv)
    print("%s가작세되었습니다." %rmv)
else: 
    print("%s가 존재하지 않습니다." %rmv)
