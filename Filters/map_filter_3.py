#Add 5 marks to passed students (≥40)
marks = [35, 42, 28, 50, 60]
result= list(map(lambda x: x+5 , filter(lambda x: x>40 , marks)))
print(result)