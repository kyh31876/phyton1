#선그래프 
from matplotlib import font_manager, rc
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

