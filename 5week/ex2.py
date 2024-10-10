import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.font_manager as font_manager

def addtext(x,y):
    for i in range(len(x)):
        plt.text(i,y[i]+0.5,y[i], ha = 'center')
        
hat = pd.read_csv('singer_youtube.csv') # hat 변수에 데이터셋 입력
print(hat.head(), end="\n\n") # 위에서 부터 5개 데이터 확인

font_path = "malgun.ttf"
font_name = font_manager.FontProperties(fname=font_path).get_name()
plt.rc('font', family=font_name)

plt.figure(figsize=(15, 10))
plt.bar(hat['name'], hat['youtube count'], # (첫번째 hat = 부화장 / 두번째 hat 병아리 수) = 부화장 별로 병아리 수 **hat처리 부분이 가장 중요함**
    color = ('red','orange','yellow','green','blue','navy','purple'))
plt.title('name')
plt.xlabel('hatchery')
plt.ylabel('chick count')

addtext(hat['name'], hat['youtube count'])

plt.show()