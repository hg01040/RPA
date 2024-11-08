import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.font_manager as font_manager

def addtext(x,y):
    for i in range(len(x)):
        plt.text(i,y[i]+0.5,y[i], ha = 'center')
        
hat = pd.read_csv('ch4-1.csv') # hat 변수에 데이터셋 입력
print(hat.head(), end="\n\n") # 위에서 부터 5개 데이터 확인

font_path = "malgun.ttf"
font_name = font_manager.FontProperties(fname=font_path).get_name()
plt.rc('font', family=font_name)

plt.figure(figsize=(15, 10))
plt.bar(hat['hatchery'], hat['chick'], # (첫번째 hat = 부화장 / 두번째 hat 병아리 수) = 부화장 별로 병아리 수 **hat처리 부분이 가장 중요함**
    color = ('red','orange','yellow','green','blue','navy','purple'))
plt.title('hatchery statistics')
plt.xlabel('hatchery')
plt.ylabel('chick count')

addtext(hat['hatchery'], hat['chick'])

plt.show()

print("########################################### 파이차트를 그리기 위해 비율 계산")

import seaborn as sns
pct = hat['chick']/hat['chick'].sum()
col7 = sns.color_palette('Pastel2', 7)

# 파이차트 그리기
plt.figure(figsize=(10, 10))
plt.pie(pct, labels = hat['hatchery'], autopct='%.1f%%', colors=col7, counterclock= False) # pct는 데이터가 먼저 나온다
plt.show()

print("########################################################################### 라인 차트 그리기 ")
plt.figure(figsize=(10, 7))
plt.plot(hat.hatchery, hat.chick, marker='*', color='y', linestyle='--',linewidth=4) # 첫번째 구분 두번째 데이터가 온다 /// hat['chick']랑 hat.chick 같은 것으로 허용 hat['hatchery']랑 hat.hatchery도 동일
plt.title('부화장별 병아리 부화현황')
plt.xlabel('부화장')
plt.ylabel('부화마릿수')
plt.grid(True)
plt.legend(['부화마릿수'], fontsize=10, loc='best')
plt.show()


# bar - plt.bar (구분, 데이터 ...)
# pie - plt.pie(비율데이터 ......)
# Line - Line.plot(구분, 데이터 ...)