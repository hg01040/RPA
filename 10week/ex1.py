## 상관분석 -- 관계성 => "ㅇㅇㅇ과 xxx 간 관계"
## 회귀분석 -- 인과성 => "ㅇㅇㅇ가 xxx에 미치는 영향"
# 둘의 공통점 : 선형이다.
# 회귀분석은 독립변수(원인)이 종속변수(결과)에 영향을 미치는지 알아보는 법
# 회귀분석은 직선방정식 y=ax+b : 선형회귀모델
# 모델 생성 절차 1. 알고리즘 입력 2.데이터 학습 3. 예측 값 확인 4. 검증


import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.formula.api as smf  # 라이브러리 불러오기

w = pd.read_csv('ch5-1.csv')   # 데이터 읽기 밑 선별
w_n = w.iloc[:, 1:5]

model_lm = smf.ols(formula= 'weight ~ egg_weight' , data = w_n) # => 회귀모델 셋팅 // smf.ols = 결과, 원인 값 지정 // data = 데이터 불렁오기 // *** 순서가 결과값 ~~ 원인값
result_lm = model_lm.fit() ## fit는 모델학습 시작
result_lm.summary()        ## 결과 확인

print(result_lm.summary())

### R-squared 값 == 모델의 신뢰성 0.7이상이면 높은거
### Prob (F-staistic) 값 == 모델 데이터 통계값 1.32e-16 = e -16승 ///  0.05이하면 유의미하다
### coef   egg_weight == 결과에 미치는 영향력    /// intercept는 상수다 
### P>|t|  0.000 === 상관계수 통계값 0.05이하면 유의미하다


plt.figure(figsize= (10,7))
plt.scatter(w.egg_weight, w.weight, alpha=.5) ## 독립변수 종속변수 산점도 그리기 
plt.plot(w.egg_weight, w.egg_weight*2.3371 - 14.5475, color = 'red') ## 회귀방정식을 직선으로 그리기
plt.text(66, 132, 'weight - 2.3371egg_weight - 14.5475', fontsize = 12) 
plt.title('Scatter Plot')
plt.xlabel('egg_weight')
plt.ylabel('weight')
plt.show()