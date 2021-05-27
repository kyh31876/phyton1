#선그래프 
from matplotlib import font_manager, rc
import matplotlib
font_apth = "/Users/yuhyun/Library/Fonts" 
font_name=font_manager.Fontproperties(fname=font_path).get_name()
rc('font',family=font_name)


#x축, y축 자료 지정: matplotlib.pyplot.plot(x축데이터).y축데이터
#maker=, makersize=,marketfaceolor=,color=,linewidth=, label=)
#그래프 스타일 지정: matplotlib.pyplot.style..use("스타일 이름")



#데이터 전처리
import pandas as pd 
import matplotlib.pyplot as plt 

from matplotlib import font_manager, rc
font_path = "" 
font_name=font_manager.FontProperties(fname=font_path).get_name()
rc('font',family=font_name)

df= pd.read_excel('/Users/yuhyun/Downloads/시도별 전출입 인구수.xlsx',fillna=0,header=0) 

df= df.fillna(method='ffill')#결측치가 있으면 앞자료를복사해 붙여오기 

mask=(df['전출지별']=='서울특별시') & (df['전입자별']!='서울특별시') 
df_seoul=df[mask]
df_seoul=df_seoul.drop(['전출지별'],axis=1) #전출지별 열에따라 모두날리기 
df_seoul.rename({'전입지별':'전입지'},axis=1,inplace=True) #열의자료에서 전입지별을 전입지로 바꾸곡 저장 
df_seoul.set_index('전입지',inplace=True) #전입지를 행인덱스로 지정후 저장 
sr_one=df_seoul.loc['경기도'] #행이름이 경기도인 자료만 가져와서 sr_one에 저장 


#선그래프그리기
plt.style.use('ggplot')
plt.figure(figsize=(14,5)) #그림크기 지성 가로 14 세로는 5 
plt.xticks(size=10, rotation='vertical') # 수직으로 축회전 사이즈 14에서 10으로 사이즈 변환 
plt.plot(sr_one.index, sr_one.values,marker='o',markersize=10) # sr_one의 인덱스를 x축 , sr_one의 value를 y축으로  마커는 o 

plt.title('서울 -> 경기 인구이동',size=30) #제목설정 
plt.xlabel('기간',size=20) 
plt.ylabel('이동인구수',size=20)
plt.legend(labels=['서울 ->경기'],loc='best',fontsize=15) #범례나타내기 위치는 최적위치, 폰트사이즈는 15

plt.show() #출력하라 

#그래프 겹치기 : 회면 분할후 여러개 만들기 
#axe Object : 그림객체 
###
fig = matplotlib.pyplot.figure(figsize=('행크기','열크기'))
ax1= fig.add_subplot('분할 행개수', '분할 열개수', '순서')
ax2=fig.add_subplot('분할 행개수', '분할 열개수', '순서')

ax1.plot(data)
ax2.plot(data)

ax1.legent(loc=)
ax1.set_title(,size=)
ax1.set_xlabe(,size=)
ax1.set_ylabel(,size=)
ax1.set_xticklabels(,rotation=)
ax1.tick_params(axis=,labelsize=)


# 
matplotlib.pyplotl,show()
plt.style.use('ggplot')

fig=plt.figure(figsize=(10,10))
ax1= fig.add_subplot(2,1,1)
ax2=fig.add_subplot(2,1,2)

ax1.plot(sr_one,marker='o',markersize=10) 
ax2.plot(sr_one,marker='o',markerfacecolor='green',markersize=10,
color='olive',linewidth=2,label='서울 -> 경기') #빨간색점이 초록색점로 바뀜, 선색깔이 올리브, 선두께가 2로 
ax2.legend(loc='best') #범레를 최적의 위치에 넣는다.

ax1.set_ylim(50000,800000) #시작지점, 끝지점 지정  
ax2.set_ylim(50000,800000)

ax1.set_xticklabels(sr_one.index,rotation=75) #라벨의 이름 지정후 75도 기울임 
ax2.set_sticklabels(sr_one.index,rotation=75)

plt.show()

#그래프 겹치기: 한화면에 여러개 그리기 
#fig=matlpotlib.pyplot(figsize=(행크기, 열크기))
#ax=fig_add_subplot(1,1,순서) ;하나만 
#ax.plot(data1)
#ax.plot(data2)

#ax.legend(loc=)
#ax.set_title(,size=)
#ax.set_xlabel(,size=)
#ax.set_ylabel(,size=)
#ax.set_xticklabels(,rotation=)
#ax.tick_params(axis=,labelsiez=)


#회귀선이 있는 산점도 
#seaborn.regplot(x= x축 변수, y = y축변수, data=데이터, ax=axe obejct , fit_reg= True/ False )


import matplotlib.pyplot as plt
import seaborn as sns

titanic = sns.load_dataset('titanic')

sns.set_style('darkgrid')
fig=plt.figure(figsize=(15,5))
ax1=fig.add_subplot(1,2,1) # 1행 2열의 첫번째 위치 
ax2=fig.add_subplot(1,2,2)

sns.regplot(x='age', y='fare', data=titanic, ax=ax1)
sns.regplot(x='age', y='fare', data=titanic, ax=ax2, fig_reg=False)
plt.show()

#displot()
#seaborn.displot(변수,hist=True/False, ,kde=True/False, fig
# ax=axe Object, color=)

import matplotlib.pyplot as plt
import seaborn as sns

titanic = sns.load_dataset('titanic')
sns.set_style('darkgrid')

fig=plt.figure(figsize=(15,5))
ax1=fig.add_subplot(1,3,1)
ax2=fig.add_subplot(1,3,2)
ax3=fig.add_subplot(1,3,3)

sns.displot(titanic['fare'], ax=ax1)
sns.displot(titanic['fare'], hist=True, ax=ax2)
sns.displot(titanic['fare'],kde=False, ax=ax3)

ax1.set_title('titanic fare-hist.kde')
ax2.set_title('titanic fare-kde')
ax3.set_title('titanic fare-hist')

plt.show()


#stat.ttest_1samp()함수의 활용 
#from scipy.stats import ttest_1samp
#from scipy.stats import shapiro
#shapiro(data) #정규성 검정 
#stats.ttest_1samp(data, popmean=검정값) #ttest_1samp option; popmean=검정하고자 하는 모평균의 값


import pandas as pd 
from scipy import stats 
data=pd.DataFrame({'v1':[35,40,12,15,21,14,46,10,28,48,16,30,
                         32,48,31,22,12,39,19,25]})


from scipy.stats import shapiro #평균 차이 검증 
shapiro(data)

from scipy.stats import ttest_1samp
print("one_sample 평균)",data['v1'].mean())
result1=stats.ttest_1samp(data,popmean=25)
print("result 결과) statistic: %.3f, pvalue:%.3f"%result1)

#stat.test_ind() 독립표본에의한 두모평균의 비교 
#from scipy import stats 
#from scipy.stat import ttest_ind
#stat.levene(data1,data2)
#stats.test_ind(data1,data2,equal_var=True ) #equal_var; 같은분산주기  

from sklearn import datasets 
dataset= datasets.load_iris() 
data=dataset.data

import pandas as pd 
a=pd.DataFrame(data)
data1=a.iloc[0:51,0];data2=a.iloc[51:101,0]

from scipy import stats 
from scipy.stats import shapiro 
shapiro(data1)
shapiro(data2)
stats.levene(data1,data2) #등분산검정

from scipy.stats import ttest_ind
print("one_sample 평균1)", data1.mean())
print("one_sample 평균2)", data2.mean())
print("one_sample 표준편차1)", data1.std())
print("one_sample 표준편차2)", data2.std())
reslut=stats.ttest_ind(data1,data2)
print("t검정통계량: %.5f, p값:%.5f"%result )
