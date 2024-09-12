a=123
b=15.556

print(a, "and", b, sep='@', end='\n\n')

print("a:{0} b:{1}".format(a, b)) # 함수
print(f"a:{a} b:{b}")             # 키워드

print(f"a:{a:05d} b:{b:2f}") 
print("a:%05d b:%.2f" % (a, b)) # 연산자 %d는 정수형태 / %f는 실수형태