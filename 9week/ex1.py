## 상관 분석 => 관계성
##           관계 정도 계산 
#            1. 공분산 이용
# 1. 방향성  -------> 공분산 값이 +이면 정방향 -이면 역방향
# 2. 관계 강도                                          **** 공분산을 가지고는 관계 강도를 계산 불가 ---> 상관 계수 사용(비례값)    -1<(강도)<1

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

w = pd.read_csv('ch5-1.csv')
print(w, end='\n\n')
print(w.head(10), end='\n\n')

w_n = w.iloc[:, 1:5]   # 전체 행에 1~4열
print(w_n, end='\n\n')
w_cor = w_n.corr(method = 'pearson')   ## 상관행렬 만들기
print(w_cor, end='\n\n')

sns.pairplot(w_n)      #### 산점도 만들기

plt.figure(figsize= (10,7))
sns.heatmap(w_cor, annot=True, cmap='Blues')    #####  상관행렬도 만들기
plt.show()