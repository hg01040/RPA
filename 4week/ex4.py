def sumfunc(num):
    sum = 0
    for j in range(1,num+1):
        sum=sum+j
    return sum
num = int(input("1이상의 정수를 입력하세요"))
sum = sumfunc(num)
if sum <= 1:
    print("잘못입력하셨습니다")
else:
    print(f"1~{num}까지 정수의 합은 {sum}입니다.")
