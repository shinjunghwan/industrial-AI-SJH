sum = 0
limit = int(input("어디까지 계산할까요? "))
for i in range(1, limit+1) : #1,2,3,4
  sum += i
print("합계 : ", sum)
