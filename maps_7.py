#Extract last digit of each number
numbers = [123, 456, 789]
result=list(map(lambda x: x%10 , numbers))
print(result)