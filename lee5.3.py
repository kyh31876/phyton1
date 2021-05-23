#dictionary Type 
# word - 뜻 key- value {key : value}... value 에 list 형태를 묶어서 사용할수있다. 

#indexing []
a=[1,2,3]
# a[key] 

#data type {'var1':[1,2,3,4...],'var2':[1,2,3,4...]} :Dataframe

##모듈 불러오기
#import 모듈명(pandas)
#import 모듈명 or pd
#from 모듈명 import 모듈명(함수명)

#dataframe 으로 변경 
#pandas.dataframe(Dict data(2차원 배열자료), columns=[열이름],index=[index name])




#data frame 변환 

from os import P_PID
import pandas as pd 
dict_data={'c0':[1,2,3],'c1':[4,5,6],'c2':[7,8,9],'c3':[10,11,12],'c4':[13,14,15]}

df=pd.DataFrame(dict_data)

print(type(df))
print('\n')
print(df)

import pandas as pd 
df=pd.DataFrame([[15,'남','덕영중'],[17,'여','수리중']],index=['준서','예은'],columns=['나이','성별','학교'])
print(df)


#column index/row 이름 변경 

#행 index 변경: DataFrameobject.index= 새로운 행 인덱스 배열 
#열 이름 변경: DataFreamobject.columns=새로운 이름배열 




# rename()이용 
#행 인덱스 변경 : DataFrameobject.rename(index={기존 인덱스:새인덱스})
#열 이름 변경 : DataFrameobject.rename(columns={기존이름:새이름})

import pandas as pd
df=pd.DataFrame([[15,'남','덕영중'],[17,'여','수리중']],index=['준서','예은'],columns=['나이','성별','학교'])
#[[list1],[list2]]
df.rename(index={'준서':'학생1','예은':'학생2'},inplace=True) #바꾼값을 저장
df.rename(columns={'나이':'연령','성별':'남녀','학교':'소속'},inplace=True)
print(df)


#row/column 삭제   변수명 띄어쓰기 가능한 사용하지말것
#행삭제: DataFrameobject.drop(행 index or 배열,axis=0)
#열삭제: DataFrameobject.drop(열 이름 or 배열,axis=1)

import pandas as pd 
exam_data={'수학':[90,80,70],'영어':[98,89,95],'음악':[85,95,100],'체육':[100,90,90]}
df=pd.DataFrame(exam_data,index=['서준','우현','인아'])
print(df)
print('\n') # 한줄 띄우기

df2=df[:] #복사해서 다른곳에 붙여넣기 
df2.drop('우현',inplace=True)
print(df2)

df3=df[:]
df3.drop(['우현','인아'],axis=0,inplace=True)
print(df3)


df4=df[:]
df4.drop('수학',axis=1,inplace=True)
print(df4)

df5=df[:]
df5.drop(['영어','음악'],axis=1,inplace=True)
print(df5)


##행/열/element 선택

#행선택 
    #loc #인덱스 이름 : 개채명.loc['인덱스이름']
    #iloc #정수형 인덱스 : 개체명.iloc[위치번호]

#비연속 범위 지정 
    #[['a','c']]


#열선택 

    #DataFrameObject["열이름"] or DataFrameObject.열이름 ; 열 1개 선택
    #DataFrameObject[[열1,열2,..,열n]]; 열 n 개 선택 


#element 선택 
    #인덱스 이름: DataFrameObject.loc[행인덱스, 열이름]
    #정수 위치 인덱스: DataFrameObject.iloc[행번호, 열번호]

#행/열/원소 선택 
import pandas as pd 

exam_data={'수학':[90,80,70],'영어':[98,89,95],'음악':[85,95,100],'체육':[100,90,90]}
df=pd.DataFrame(exam_data,index=['서준','우현','인아'])

#행선택 


df.loc[['서준','우현']]; df.iloc[[0,2]] #서준과 우현을 선택 
df.loc['서준':'우현']; df.iloc[0:2] 
df.loc['서준']; df.iloc[0] 

#열선택 
df['수학'] ;df.수학 #수학선택 
df[['음악','체육']]; df[['수학']] #수학 , 음악 선택 


#원소 선택
df.loc['서준','음악']; df.loc[0,2]  # 서준 row 음악 column ; 서준의 음악 점수
df.loc['서준',['음악','체육']]; df.iloc[0,[2,3]]  #서준 row 음악,체육 columns  서준의 음악 체육 점수 
df.loc['서준','음악':'체육']; df.iloc[0,2:] 

df.loc[['서준','우현'],['음악','체육']]; df.iloc[[0,1],[2,3]] #서준 우현 row 음악, 체육 column 서준 우현의 음악 체육 점수 
df.loc['서준':'우현','음악':'체육']; df.iloc[0:2,2:]


#행/열 추가 
#행 추가 : DataFrameObject.loc["새로운 행 이름"] = 데이터 값 

# 열 추가 :DataFrameObject['추가하는 열이름] =데이터 값

# 원소값 변경: DataFrameObject.[행,열]= 새로운 값 

# 행,열 위치 변경 :DataFrameObject.transpose()


import pandas as pd 

exam_data = {'이름':['서준','우현','인아'],
'수학':[90,80,70],'영어':[98,89,70],
'음악':[85,98,100],'체육':[100,90,90]}
df = pd.DataFrame(exam_data, index=['서준','우현','인아'])

# row 추가 
df.loc[3]=0  #3번쨰 위치에 0 추가 
df.loc[4]=0
df.loc[4]=['동규',90,80,70,60] #4번째에 동규주고 90~60 값제공
df.loc['행5']=df.loc[3] #행5라는 새로운 행에 3번째 값을 붙여넣기

# column 추가 
df.국어= 80 #국어라는 변수를 붙이고 80을 넣는다

#행,열 바꾸기 
df.T

#원소 추가 
df.iloc[[0:1],[0:3]]=90 #서준과 우현의 수학 


#특정열을 행 인덱스로 설정 : DataFrame객체.set_index(열이름)

#행 인덱스 재배열: DataFrame객체.reindex(새로운인텍스.배열 )

#행 인덱스 초기화 :DataFrame객체.rest_index()

#행 인덱스를 기준으로 데이터프레임 정렬: DataFrame객체.sort_index(by='변수명',acending=True)

#특정열의 데이터값을 기준으로 데이터프레임 정렬 :DataFrame객체.sort_value(by='변수명')


exam_data = {'이름':['서준','우현','인아'],
'수학':[90,80,70],'영어':[98,89,70],
'음악':[85,98,100],'체육':[100,90,90]}
df=pd.DataFrame(exam_data)

df.set_index(['이름'])
dict_data={'c0':[1,2,3],'c1':[4,5,6],'c2':[7,8,9],'c3':[10,11,12].'c4':[13,14,15]}
df=pd.DataFrame(dict_data,index['r0','r1','r2'],fill_value='지정값')

#행인덱스 재배열 
df.reindex(new_index,,fill_value='지정값')
#행 인덱스 초기화 
df.reset_index()
#행 인덱스 기준 정려 
df.
#특정 열 데이터값 기준정렬 


#DataFrame 형태: 2차원배열 
#Series 형태: 1차원 



#외부파일 읽어오기 
# pandas.read_format("address")

import pandas as pd 

#csv 파일 불러오기 
tb=pd.read_csv('/Users/yuhyun/Downloads/read_csv_sample.csv')

#excel파일 불러오기 
pd.read_xlsx('/Users/yuhyun/Downloads/남북한발전전력량.xlsx',header=None)
print(data)


#html불러오기 
tables=pd.read_html("/Users/yuhyun/Downloads/sample.html")

print(len(tables))

for i in range(len(tables)):
    print(tables[i])
    print('\n')



        #header = 0 (0번쨰줄을 변수명 .) 1(첫번쨰 줄을 변수명 )  N(변수명이 없다)
        #encoding = 'CP949'          


#내보내기
#pandas.object.to_format("address")

#csv로 내보내기 

import pandas as pd 

data = {'name':["Jerry",'Riah','Paul']
'algol':['A','A+','B'],
'basic':['C','B','B+'],
'c++':['B+','C','C+']
}

pd= pd.DataFrame(data)
df.set_index('name',inplace=True)
print(df)
pd.tb.to_csv('/Users/yuhyun/sample.csv')



#excel 내보내기: pandas.EXcelWriter('address') 
#to_excel(ExcelWriter Object,sheet="sheetname")
import pandas as pd 
data1= {'name': ['Jerry','Riah','Paul'],'algol':['A','A+','B'],
'basic':['C','B','B+'],'C++':['B+','C','C+']}

data2= {'c0':[1,2,3],'c1':[4,5,6],'c2':[7,8,9],'c3':[10,11,12],'c4':[13,14,15]}

df1=pd.DataFrame(data1)
df1.set_index('name',inplace=True)


df2= pd.DataFrame(data2)
df2.set_index('c0',inplace=True)

writer= pd.ExcelWriter('/Users/yuhyun/Downloads/df_excelwriter.xlsx')
df1.to_excel(writer,sheet_name="sheet1")
df2.to_excel(writer,sheet_name="sheet2")
writer.save()



tal=pd.read_csv('/Users/yuhyun/Downloads/auto-mpg.csv',header=None,names=['mpg','cylinders','displacement','horsepower','weight','acceleration',
'model_year','origin','name']) #변수명이 없을때
tal.columns=['mpg','cylinders','displacement','horsepower','weight','acceleration',
'model_year','origin','name'] #변수명 주기 


#앞부분 미리보기 : DataFreamObject.head(n)
#뒤부분 미리보기 : DataFreamObject.tail(n)

# 데이터 프레임의 크기 확인 : DataFreamObject.shape()

#데이터프레임의 기본정보 출력 : DataFreamObject.info() 

#데이터프레임의 기술 통계 요약 : DataFreamObject.describe()

#열데이터 개수확인 :DataFreamObject.count()
tal.count() #유효한 값만반환 


#열 데이터 eigen value 개수 :DataFreamObject["열이름"].value_counts()
#option dropna=Ture (NAN제외)
tal.count[].value_counts()

#평균값 
tal.mean() #계산결과를 series object 로 반환 
tal['mpg'].mean()
#중간값 
tal.meaian
tal['mpg'],median()

#최대값 
tal.mean()
tal['mpg'].man()
#최소값 
tal.min()
tal['mpg'].min()

#표준편차 
tal.min()
tal['mpg'].std()

#상관계수
tal.corr()
tal[['mpg','origin']].corr() #적어도 2개 이상으로 구성되어야함 

tal.head(4)

#graph
#선그래프:DataFreamObject.plot()

#막대 그래프 DataFreamObject.plot(kind='bar')

#히스토그램 DataFreamObject.plot(kind='hist)

#산점도 DataFreamObject.(x,y,kind='scateer')
            #header = 0 (0번쨰줄을 변수명 .) 1(첫번쨰 줄을 변수명 )  N(변수명이 없다)
            #encoding = 'CP949'          
# #내보내기  # pandas.to_format("address")


import pandas as pd 
df=pd.read_excel("/Users/yuhyun/Downloads/남북한발전전력량.xlsx")  

df_ns=df.iloc[[0,5],3:] #행에는 0번쨰 5번쨰자료를 열에는 3번째부터 끝까지 
df_ns.index=['south','north'] #인덱스 네이밍 

df_ns.columns=df_ns.columns.map(int) #열이름을 정수형으로 맵변환 
print(df_ns.head())

df_ns.plot()

tdf_ns=df_ns.T #transpose 시키기 
print(tdf_ns.head())

df.plot(x='weight',y='mpg',kind=scatter()) #산점도그리기 
df[['mpg','weight']].plot(kind='box') #mpg와 weight로 box형태로 그리기 

 #누락데이터 개수확인: info()  value_count()
 
 #누락데이터 여부확인 : isnull() ;결측이면 TRUE  notnulll();  결측이면  false

 
import seaborn as sns 
df= sns.load_dataset('titanic')
 
nan_deck=df['deck'].value_counts(dropna=True)
 
print(nan_deck)
df['deck'].isnull() #특정변수에대해 결측여부 확인 
print(df.head().isnull())
print(df.head().notnull())

print(df.shape())
print(df.dtypes())
print(df.head().isnull().sum(axis=0))


#object.dropna(axis=행/열), thresh= NAN 개수:조건에 맞는 행/열 제거) 변수를 제거 
#object.dropna(subset=행/열 이름, how= 'any'; 하나의 NaN 이 있을떄 삭제 , all; 모두 NaN일떄 삭제 ) 변수안의 데이터를 제거 

df_thresh= df.dropna(axis=1, thresh=500)
df_thresh.info()
print(df_thresh.columns)

df_age=df.dropna(subset=['age'], how='any',axis=0)

print(len(df_age))


#누락데이터 대체 : object.fillna(대체값, inplace=True/False); 대체값으로 NaN을 대체
# object.fillna(method="ffill",inplace=True/Fasle); NaN바로 앞으값으로Nan 값을 대체 


#age값의 평균값을 age에 대체 
df=sns.load_dataset('titanic')
mean_age=df['age'].mean(axis=0)
df['age'].fillna(mean_age,inplace=True)
print(df['age'].head(10))


#embark_town 825부터 830 까지 결측값을 최빈값으로 대체 
df=sns.load_dataset('titanic')
print(df['embark_town'][825:830])
most_freq=df['embark_town'].value_counts(dropna=True).idxmax()
print(most_freq)
df['embark_town'].fillna(most_freq,inplace=True)
print(df['embark_town'][825:830])


df['embark_town'].fillna(method='ffill',inplace=True)

#중복데이터 여부 확인 
#duplicates() #중복되는 행이면 true 반환 , 처음나오는 행에 대해서는 false반환
#object.drop_duplicates() #전체 데이터셋을 기준으로 중복된행제거 


#object.drop_duplicates(subset=기준열); 선택된 열을 기준으로 중복된행을 제거 

import pandas as pd

df=pd.DataFrame({'c1':['a','a','b','a','b'],
                 'c2':[1,1,1,2,2],
                 'c3':[1,1,2,2,2]})

df2=df.drop_duplicates()
df3=df.drop_duplicates(subset=['c2','c3'])


start, end = 1,41
  
# iterating each number in list
for num in range(start, end + 1):
      
    # checking condition
    if num % 2 == 0:
        print(num, end = ",")

#자료변환 
#Object.dtypes; 자료형확인 
#Object.unique(); 열의 고유값 확인 
#Object.astype('변경할 자료명') ; 선택한 자료형으로  변환 


#구간분할 
    #Object.cut(x=데이터 배열, bins=경계값 리스트, label=bin 이름, include_lowest=True/False)
    # cut option : lowest =True 첫경계값 포함 False(첫 경계값미포함 ) 


#더미변수; Object.get_dummies(범주형)

#열순서 바꾸기 Object[재구성한 열이름의 리스트]



#데이터 프레임 연결 : Object.concat(데이터 프레임의 리스트, ignore_index=True/False
# axis=0/1,join='outer'/'inner')
#options : axis=0 (행연결) 1(열연결), join='outer' (합집합으로 연결)
#'inner'(교집합으로 연결 )

#대이터 프레임 병합:merge()
#pandas.merge(df_lect,df_right, how='outer'/'inner', on=기준변수, how='left'/'right',left_on=,right_on=)
#options how=join='outer' (합집합으로 연결) 'inner'(교집합으로 연결 )
#on=변수명(기준이 되는 변수, None일경우 공통의 모든열 기준), how='left'(왼쪽의 데이터프레임 
#키에속하는 데이터값기준으로 병합) 'right'(오른쪽 기준으로 병합)
#left_on=변수명(좌우 다른 키를 줄경우 왼쪽데이터프레임 키 ) right_on=변수명(좌우다른 키를 
# 줄경우 오른쪽 데이터 프레임키)

