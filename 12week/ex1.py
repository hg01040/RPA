import pandas as pd
from sklearn.model_selection import train_test_split


w = pd.read_csv("ch5-1.csv")
x_data = w.iloc[:, 2:5].values  # (독립) 
y_data = w.iloc[:, 1].values   # (종속)병아리의 무게

x_train, x_test, y_train, y_test = train_test_split(x_data, y_data, test_size=0.2) 

###  test_size=0.2 --> 테스트사이즈를 20퍼센트 사용 

from sklearn.neural_network import MLPRegressor
model_mlp = MLPRegressor().fit(x_train, y_train) ## MLPRegressor 인공지능 학습 모델 fit 함수로 학습
y_pred_mlp = model_mlp.predict(x_test)

df_x_test = pd.DataFrame(x_test, columns=['egg_weight','movement','food'])
df_y_pred = pd.DataFrame(y_pred_mlp, columns=['predict'])
df_y_test = pd.DataFrame(y_test , columns=['real'])
df = pd.concat([df_x_test, df_y_test, df_y_pred], axis=1)
print(df, end='\n\n')

from sklearn.metrics import r2_score
R2 = r2_score(y_test, y_pred_mlp)
print("R2 = ", R2, end='\n\n')