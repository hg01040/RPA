import pandas as pd

col_names = ['과목번호', '과목명', '강의실', '시간수']
list1 = list([['C1', '인공지능개론', 'R1', 3],
              ['C2', '웃음치료', 'R2', 2],
              ['C3', '경영학', 'R3', 3],
              ['C4', '3D디자인', 'R4', 4],
              ['C5', '스포츠경영', 'R5', 2],
              ['C6', '예술의 세계', 'R6', 1],
])

df = pd.DataFrame(list1, columns=col_names)
print(df)

data = {
    '과목번호' : ['C1', 'C2', 'C3', 'C4', 'C5', 'C6'],
    '과목명' : ['인공지능개론', '웃음치료', '경영학', '3D디자인', '스포츠경영', '예술의세계'],
    '강의실' : ['R1', 'R2', 'R3', 'R4', 'R2', 'R3'],
    '시간수' : [3, 2, 3, 4, 2, 1]
}

df = pd.DataFrame(data)
print(df, end='\n\n')

sr_name = df['과목명']
print(sr_name, end='\n\n')

sr_no = df.loc[2]
print(sr_no, end='\n\n')

cell_name = df.loc[2]['과목명']
print(cell_name)

df.to_csv('file.csv', index=False) # to_csv 는 데이터 프레임을 csv 파일로 변환해서 만들어줌


print("#############################################")

df['담당교수'] = ['홍길동', '김철수', '이영희', '박영수', '최영희', '김영수']
print(df, end='\n\n')

df.loc[6] = ['C7', '통계학', 'R7', 3, '이철수']
print(df, end='\n\n')

df1 = df.drop(['강의실'], axis=1)
print(df1, end='\n\n')

df2 = df.drop([5], axis=0)
print(df2, end='\n\n')

print("###########################################################################################")

#범위찾기
#행찾기
print(df.loc[0:2], end='\n\n') # 이 경우에는 0~2까지 나옴(숫자가 아니라 행의 이름으로 찾는 방식이기 때문에 0,1,2까지 출력)
print(df.iloc[0:2], end='\n\n') # iloc이어야 0~1까지 나옴(행의 숫자로 찾는 방식이기 때문에 0,1까지만 출력)

#열 찾기
# print(df[['과목명', '담당교수']], end='\n\n')
print(df.loc[:, '강의실': '담당교수'], end='\n\n')