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


#row/column 삭제 
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
#loc #인덱스 이름 

#iloc #정수형 인덱스 

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
df.loc['서준']; df.iloc[0]
df.loc[['서준','우현']]; df.iloc[[0,2]] #서준과 우현을 선택 
df.loc['서준':'우현']; df.iloc[0:2] 


#열선택 
df['수학'] ; df.영어
df[['음악','체육']]; df[['수학']]


#원소 선택
df.loc['서준','음악']; df.loc[0,2]  # 서준 row 음악 column
df.loc['서준',['음악','체육']]; df.iloc[0,[2,3]]  #서준 row 음악,체육 columns 
df.loc['서준','음악':'체육']; df.iloc[0,2:]

df.loc[['서준','우현'],['음악','체육']]; df.iloc[[0,1],[2,3]] #서준 우현 row 음악, 체육 column
df.loc['서준':'우현','음악':'체육']; df.iloc[0:2,2:]