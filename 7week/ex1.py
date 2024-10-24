import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('2024_seoul_data.csv', encoding='utf-8')
df2 = df.fillna(method='ffill')  # 결측치를 위에 있는 데이터로 채워넣어라
df2.info()

df2.rename(columns={'최저기온':'min_temp'}, inplace=True)# 데이터 프레임 상에서 이름 바꾸기 
df2.rename(columns={'평균기온':'avg_temp'}, inplace=True)
df2.rename(columns={'최고기온':'max_temp'}, inplace=True)
df2.head(3)

plt.rc('font', family='Malgun Gothic')
plt.rcParams['axes.unicode_minus'] = False

plt.title('서울시 2024년도 여름 기온 변화')
plt.plot(range(1,len(df2)+1), df2['max_temp'], label='최고기온', c='r') # range 함수로 1부터 전체 데이터까지 다 불러옴
plt.plot(range(1,len(df2)+1), df2['avg_temp'], label='평균기온', c='y')
plt.plot(range(1,len(df2)+1), df2['min_temp'], label='최저기온', c='b')
plt.xlabel('일')
plt.ylabel('기온')
plt.legend() # 범례표시 시키기 
plt.show() # 화면 출력