import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.formula.api as smf  

## ------------y = 실제값 / x \\--예측값  // -y -`평균`

w = pd.read_csv('ch5-1.csv')   # 데이터 프레임으로 만들기
w_n = w.iloc[:, 1:5]           # 행은 끝까지 열은 1~4까지

model_lm = smf.ols(formula= 'weight ~ food' , data = w_n) # => 회귀모델 셋팅 // smf.ols = 결과, 원인 값 지정 // data = 데이터 불렁오기 // *** 순서가 결과값 ~~ 원인값
result_lm = model_lm.fit() ## fit는 모델학습 시작
result_lm.summary()        ## 결과 확인

print(result_lm.summary())

from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
import numpy as np

predicted_value = result_lm.predict()  # result 모델에서 예측

mse = mean_squared_error(w_n['weight'], predicted_value)    # weight 는 실제값 // predicted_value 는 예측값 을 넣어서 비교
mae = mean_absolute_error(w_n['weight'], predicted_value)   # weight 는 실제값 // predicted_value 는 예측값 을 넣어서 비교
rmse = np.sqrt(mse)                                       # MSE에 루트를 씌워서 비교
r_squared = r2_score(w_n['weight'], predicted_value)      # weight 는 실제값 // predicted_value 는 예측값 을 넣어서 비교

print("Mean Squared Error (MSE):", mse)
print("Mean Absolute Error (MAE):", mae)
print("Root Mean Squared Error (RMSE):", rmse)
print("R-squared:", r_squared)