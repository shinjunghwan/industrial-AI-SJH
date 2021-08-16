class Rectangle:
  def __init__(self, side=0):
    self.side = side
  
  def getArea(self):
    return self.side * self.side

def printAreas(r,n):
  while n >= 1:
    print(r.side, "\t", r.getArea())
    r.side = r.side + 1
    n = n - 1

myRect = Rectangle()
count = 5
printAreas(myRect, count)
print("사각형의 변= ", myRect.side)
print("반복횟수 = ", count)
