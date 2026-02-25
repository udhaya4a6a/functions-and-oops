## Filter with a lambda function and multiple conditions
numbers=[1,2,3,4,5,6,7,8,9]
even_and_greater_than_five=list(filter(lambda x: x%2==0 and x>5 , numbers))
print(even_and_greater_than_five)