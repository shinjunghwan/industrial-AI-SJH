import math

def calCircle(r) :
  area = math.pi * r * r
  circum = 2 * math.pi * r
  return (area, circum)

radius = float(input("원의 반지름을 입력하시오: "))
(a,c) = calCircle(radius)
b = '안녕하세요'
print(str(b)+". 원의 넓이는 "+str(a)+"이고 원의 둘레는"+str(c)+"이다.")
