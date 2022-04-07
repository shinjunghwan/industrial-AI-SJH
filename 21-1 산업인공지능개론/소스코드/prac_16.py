def callByReference(list):
  list[0] = 99

values = [0,1,2,3,4,5]
print(values)
callByReference(values)
print(values)
